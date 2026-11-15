"""BRA-16 — Humanlike Hundred Acre Item 3 (croquis person, not boxes).

Body: MakeHuman CC0 base (apply import rot → Z-up 1.82 m adult male proportions).
Clothes: body-face shells + solidify (character-artist), PH mustard/grey, leather boots.
Hair: short wavy light-brown mesh locks (croquis).
Lookdev: Clawd recipe — PH box-project, 36 mm DOF, AgX MHC, honest light.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import bmesh
from mathutils import Matrix, Vector, Quaternion

OUT = Path("/Users/jongarcia/Documents/Development/platforms/blender-skills/demos/out")
ASSETS = OUT / "assets"
MH = ASSETS / "mh_base.obj"
BALLOON = ASSETS / "balloon_graphic.png"
BLEND = OUT / "SM_HundredAcre_Item3_Human.blend"
RENDER = OUT / "hundred-acre-item3-human.png"

KEEP = {
    "knitted_fleece",
    "poly_wool_herringbone",
    "cotton_jersey",
    "denim_fabric",
    "grey_plaster_02",
    "concrete_floor_01",
}
TARGET_H = 1.82


def ov():
    for w in bpy.context.window_manager.windows:
        for a in w.screen.areas:
            if a.type != "VIEW_3D":
                continue
            for r in a.regions:
                if r.type == "WINDOW":
                    return {
                        "window": w,
                        "screen": w.screen,
                        "area": a,
                        "region": r,
                        "scene": bpy.context.scene,
                        "view_layer": bpy.context.view_layer,
                    }
    return None


def run(fn):
    o = ov()
    if not o:
        return fn()
    with bpy.context.temp_override(**o):
        return fn()


def clear():
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    for col in list(bpy.data.collections):
        if col != bpy.context.scene.collection:
            try:
                bpy.data.collections.remove(col)
            except Exception:
                pass
    for block in (bpy.data.meshes, bpy.data.cameras, bpy.data.lights, bpy.data.worlds, bpy.data.armatures):
        for item in list(block):
            try:
                block.remove(item)
            except Exception:
                pass
    for m in list(bpy.data.materials):
        if m.name not in KEEP:
            bpy.data.materials.remove(m)


def ensure_col(name, parent=None):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(c)
    return c


def link(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)


def act(obj):
    bpy.context.view_layer.objects.active = obj
    for o in bpy.context.view_layer.objects:
        o.select_set(o == obj)


def assign(obj, mat):
    if not mat:
        return
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def force_box_project(mat, blend=0.25, scale=1.0, kill_displacement=False):
    if not mat or not mat.node_tree:
        return
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    texcoord = next((n for n in nodes if n.type == "TEX_COORD"), None) or nodes.new("ShaderNodeTexCoord")
    mapping = next((n for n in nodes if n.type == "MAPPING"), None) or nodes.new("ShaderNodeMapping")
    mapping.inputs["Scale"].default_value = (scale, scale, scale)
    for l in list(mapping.inputs["Vector"].links):
        links.remove(l)
    links.new(texcoord.outputs["Object"], mapping.inputs["Vector"])
    for n in nodes:
        if n.type != "TEX_IMAGE":
            continue
        n.projection = "BOX"
        n.projection_blend = blend
        for l in list(n.inputs["Vector"].links):
            links.remove(l)
        links.new(mapping.outputs["Vector"], n.inputs["Vector"])
    if kill_displacement:
        for n in list(nodes):
            if n.type == "DISPLACEMENT":
                for l in list(n.outputs[0].links):
                    links.remove(l)
                nodes.remove(n)
        out = next((n for n in nodes if n.type == "OUTPUT_MATERIAL"), None)
        if out:
            for l in list(out.inputs["Displacement"].links):
                links.remove(l)


def tint_ph(src, new_name, tint, strength=0.75, box_scale=1.6):
    src_m = bpy.data.materials.get(src)
    if not src_m:
        raise RuntimeError("missing " + src)
    m = src_m.copy()
    m.name = new_name
    force_box_project(m, 0.25, box_scale, kill_displacement=True)
    nt = m.node_tree
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    base = bsdf.inputs["Base Color"]
    fr = None
    if base.links:
        prev = base.links[0]
        fr = prev.from_socket
        nt.links.remove(prev)
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs["Factor"].default_value = strength
    mix.inputs["B"].default_value = (*tint, 1.0)
    if fr:
        nt.links.new(fr, mix.inputs["A"])
    else:
        mix.inputs["A"].default_value = (0.7, 0.7, 0.7, 1)
    try:
        nt.links.new(mix.outputs["Result"], bsdf.inputs["Base Color"])
    except Exception:
        nt.links.new(mix.outputs[0], bsdf.inputs["Base Color"])
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.18
        bsdf.inputs["Coat Roughness"].default_value = 0.35
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.5
    return m


def mat_skin():
    m = bpy.data.materials.new("MAT_Skin_Human")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.84, 0.68, 0.56, 1)
    bsdf.inputs["Roughness"].default_value = 0.48
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.2
        if "Subsurface Radius" in bsdf.inputs:
            bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.2, 0.1)
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 500
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.035
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.06
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def mat_eye():
    m = bpy.data.materials.new("MAT_Eye_Human")
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.15, 0.22, 0.32, 1)
    bsdf.inputs["Roughness"].default_value = 0.06
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 1.0
        bsdf.inputs["Coat Roughness"].default_value = 0.03
    return m


def mat_hair():
    m = bpy.data.materials.new("MAT_Hair_Wavy")
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    # light brown / croquis
    bsdf.inputs["Base Color"].default_value = (0.42, 0.28, 0.16, 1)
    bsdf.inputs["Roughness"].default_value = 0.38
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.25
        bsdf.inputs["Coat Roughness"].default_value = 0.25
    return m


def mat_leather():
    m = bpy.data.materials.new("MAT_Boot_Leather")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.22, 0.11, 0.06, 1)
    bsdf.inputs["Roughness"].default_value = 0.48
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.25
        bsdf.inputs["Coat Roughness"].default_value = 0.3
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 80
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.25
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def import_body(col):
    """Import MakeHuman CC0 body only (skip joint helpers), Z-up 1.82 m, face camera (-Y)."""
    if not MH.exists():
        raise RuntimeError("missing " + str(MH))
    before = set(bpy.data.objects)

    def _imp():
        # Split OBJ groups so joint-* / helper-* don't pollute the human mesh
        try:
            bpy.ops.wm.obj_import(filepath=str(MH), use_split_groups=True)
        except TypeError:
            bpy.ops.wm.obj_import(filepath=str(MH))

    run(_imp)
    imported = [o for o in bpy.data.objects if o not in before]
    body = None
    for o in imported:
        n = o.name.lower()
        if n == "body" or n.startswith("body"):
            body = o
            break
    if body is None:
        # Fallback: largest mesh by vertex count
        meshes = [o for o in imported if o.type == "MESH"]
        body = max(meshes, key=lambda o: len(o.data.vertices))
    for o in imported:
        if o != body:
            bpy.data.objects.remove(o, do_unlink=True)
    body.name = "SM_Char_Item3_Body"
    link(body, col)
    act(body)
    run(lambda: bpy.ops.object.transform_apply(location=True, rotation=True, scale=True))
    zs = [v.co.z for v in body.data.vertices]
    h = max(zs) - min(zs)
    s = TARGET_H / h
    body.scale = (s, s, s)
    run(lambda: bpy.ops.object.transform_apply(location=False, rotation=False, scale=True))
    # feet on ground, center XY
    zs = [v.co.z for v in body.data.vertices]
    xs = [v.co.x for v in body.data.vertices]
    ys = [v.co.y for v in body.data.vertices]
    dz = -min(zs)
    cx = (min(xs) + max(xs)) * 0.5
    cy = (min(ys) + max(ys)) * 0.5
    for v in body.data.vertices:
        v.co.z += dz
        v.co.x -= cx
        v.co.y -= cy
    # After OBJ apply: skull bulk is +Y, nose tip is -Y → face camera from -Y
    for p in body.data.polygons:
        p.use_smooth = True
    act(body)
    run(lambda: bpy.ops.object.shade_smooth())
    print("BODY dim", tuple(round(d, 3) for d in body.dimensions), "z", round(min(v.co.z for v in body.data.vertices), 3), round(max(v.co.z for v in body.data.vertices), 3))
    head = [v.co for v in body.data.vertices if v.co.z > 1.55]
    if head:
        print("head y", round(min(v.y for v in head), 3), round(max(v.y for v in head), 3), "(face=min Y)")
    return body


def male_proportions(body):
    """Push androgynous MH base toward adult male croquis (shoulders, flat chest, narrow hips)."""
    me = body.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table()
    zmin = min(v.co.z for v in bm.verts)
    zmax = max(v.co.z for v in bm.verts)
    h = zmax - zmin or 1.0

    def t(z):
        return (z - zmin) / h

    for v in bm.verts:
        u = t(v.co.z)
        x, y = v.co.x, v.co.y
        # broader shoulders / lats
        if 0.58 < u < 0.80:
            w = 1.0 + 0.18 * math.sin((u - 0.58) / 0.22 * math.pi)
            v.co.x *= w
        # flatten chest / reduce breast volume (pull +Y and -Y toward center on chest)
        if 0.58 < u < 0.72 and abs(x) < 0.14:
            v.co.y *= 0.88
            if y < 0:  # front
                v.co.y *= 0.92
        # much narrower waist + hips (croquis male, not pear)
        if 0.40 < u < 0.58:
            v.co.x *= 0.88
            v.co.y *= 0.90
        if 0.42 < u < 0.52:
            v.co.x *= 0.92
        # male jaw
        if 0.82 < u < 0.91 and abs(x) < 0.08:
            v.co.y -= 0.012 * (1.0 - abs(x) / 0.08)
            if u < 0.87:
                v.co.z -= 0.003
        # thigh volume slight
        if 0.18 < u < 0.40:
            v.co.x *= 1.04
    bmesh.ops.smooth_vert(bm, verts=bm.verts, factor=0.2, use_axis_x=True, use_axis_y=True, use_axis_z=True)
    bm.to_mesh(me)
    bm.free()
    me.update()


def hide_body_under_clothes(body):
    """Remove torso/leg skin under garments so knit/wool read clean (keep head/hands/feet)."""
    me = body.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    kill = []
    for f in bm.faces:
        c = f.calc_center_median()
        # keep head+neck
        if c.z > 1.48:
            continue
        # keep hands (outer T-pose)
        if c.z > 1.15 and abs(c.x) > 0.42:
            continue
        # keep feet soles region for boot contact cue — actually hide, boots cover
        if c.z < 0.08 and abs(c.x) > 0.05:
            continue
        # delete mid body under clothes
        if 0.08 < c.z < 1.50:
            kill.append(f)
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bm.to_mesh(me)
    bm.free()
    me.update()


def a_pose_arms(body):
    """Drop MakeHuman T-pose arms to fashion A-pose (hands near hips/pockets)."""
    me = body.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table()
    for sx in (1.0, -1.0):
        pivot = Vector((0.16 * sx, 0.0, 1.45))
        # Tight arm pick — avoid dragging half the torso (was causing paper-fan mesh)
        arm_verts = [
            v
            for v in bm.verts
            if v.co.x * sx > 0.18 and 0.95 < v.co.z < 1.52 and abs(v.co.y) < 0.18
        ]
        if not arm_verts:
            print("no arm verts", sx)
            continue
        # L (+X): +Y rot drops arm; R (-X): -Y rot drops arm
        q_drop = Quaternion(Vector((0, 1, 0)), math.radians(82 if sx > 0 else -82))
        q_fwd = Quaternion(Vector((1, 0, 0)), math.radians(-18))
        for v in arm_verts:
            offset = v.co - pivot
            v.co = pivot + q_fwd @ (q_drop @ offset)
        print("A-pose side", sx, "n", len(arm_verts))
    bm.to_mesh(me)
    bm.free()
    me.update()


def shell_from_body(body, name, z0, z1, col, mat, solidify=0.012, inflate=0.007, x_abs_min=None):
    """Duplicate body faces in Z band → inflate → solidify. Local Z-up assumed."""
    mesh = body.data.copy()
    obj = bpy.data.objects.new(name, mesh)
    link(obj, col)
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.faces.ensure_lookup_table()
    kill = []
    for f in bm.faces:
        c = f.calc_center_median()
        if c.z < z0 or c.z > z1:
            kill.append(f)
            continue
        if x_abs_min is not None and abs(c.x) < x_abs_min and c.z < 0.5:
            # optional: used for boots side split
            pass
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * inflate
    bm.to_mesh(mesh)
    bm.free()
    sol = obj.modifiers.new("Thick", "SOLIDIFY")
    sol.thickness = solidify
    sol.offset = 1.0
    act(obj)
    run(lambda: bpy.ops.object.modifier_apply(modifier="Thick") if obj.modifiers.get("Thick") else None)
    assign(obj, mat)
    for p in obj.data.polygons:
        p.use_smooth = True
    return obj


def make_boots(body, col, mat):
    boots = []
    for side, sx in (("L", 1.0), ("R", -1.0)):
        mesh = body.data.copy()
        obj = bpy.data.objects.new(f"SM_Char_Item3_Boot_{side}", mesh)
        link(obj, col)
        bm = bmesh.new()
        bm.from_mesh(mesh)
        kill = []
        for f in bm.faces:
            c = f.calc_center_median()
            if c.z > 0.22 or c.x * sx < 0.02:
                kill.append(f)
        bmesh.ops.delete(bm, geom=kill, context="FACES")
        bm.normal_update()
        for v in bm.verts:
            v.co += v.normal * 0.008
            if v.co.z < 0.05:
                v.co.z = max(0.002, v.co.z * 0.4)
                v.co.y -= 0.015  # toe toward camera (-Y already face)
            v.co.x += 0.008 * sx
        bm.to_mesh(mesh)
        bm.free()
        sol = obj.modifiers.new("Thick", "SOLIDIFY")
        sol.thickness = 0.01
        act(obj)
        run(lambda o=obj: bpy.ops.object.modifier_apply(modifier="Thick") if o.modifiers.get("Thick") else None)
        assign(obj, mat)
        for p in obj.data.polygons:
            p.use_smooth = True
        boots.append(obj)
    return boots


def add_eyes(body, col, mat):
    # Face = min Y (nose tip)
    head = [v.co for v in body.data.vertices if v.co.z > 1.55]
    if not head:
        return []
    cz = sum(v.z for v in head) / len(head)
    y_face = min(v.y for v in head)
    eyes = []
    for sx in (0.032, -0.032):
        mesh = bpy.data.meshes.new("Eye")
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=20, v_segments=12, radius=0.011)
        bm.to_mesh(mesh)
        bm.free()
        e = bpy.data.objects.new("SM_Eye", mesh)
        e.location = (sx, y_face - 0.004, cz + 0.008)
        link(e, col)
        assign(e, mat)
        for p in e.data.polygons:
            p.use_smooth = True
        eyes.append(e)
    return eyes


def add_wavy_hair(body, col, mat):
    """Short wavy light-brown locks as smooth mesh strips on scalp — croquis read."""
    scalp_verts = [v.co.copy() for v in body.data.vertices if v.co.z > 1.58 and v.co.y > -0.05]
    if len(scalp_verts) < 10:
        scalp_verts = [v.co.copy() for v in body.data.vertices if v.co.z > 1.55]
    # Cap
    mesh = bpy.data.meshes.new("HairCap")
    bm = bmesh.new()
    # convex-ish scalp shell from top faces of body
    body_bm = bmesh.new()
    body_bm.from_mesh(body.data)
    body_bm.faces.ensure_lookup_table()
    # extract top faces
    kill_keep = []
    for f in body_bm.faces:
        c = f.calc_center_median()
        if c.z > 1.58 and f.normal.z > 0.2:
            kill_keep.append(f)
    # duplicate into new mesh via copy
    body_bm.free()

    # Build hair from body top shell
    cap = body.data.copy()
    cap_obj = bpy.data.objects.new("SM_Char_Item3_HairCap", cap)
    link(cap_obj, col)
    bm = bmesh.new()
    bm.from_mesh(cap)
    kill = [
        f for f in bm.faces
        if f.calc_center_median().z < 1.60
        or f.normal.z < 0.25
        or abs(f.calc_center_median().x) > 0.14
    ]
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * 0.01
        v.co.z += 0.008
        # keep hair close to skull — avoid giant helmet
        v.co.x *= 0.92
        v.co.y *= 0.92
    bm.to_mesh(cap)
    bm.free()
    assign(cap_obj, mat)
    for p in cap_obj.data.polygons:
        p.use_smooth = True
    sol = cap_obj.modifiers.new("Thick", "SOLIDIFY")
    sol.thickness = 0.006
    act(cap_obj)
    run(lambda: bpy.ops.object.modifier_apply(modifier="Thick") if cap_obj.modifiers.get("Thick") else None)

    # Wavy locks — elongated icospheres / tapered cubes along scalp front/sides
    locks = []
    # Face −Y — bangs on −Y; volume on skull +Y
    anchors = [
        (0.00, -0.08, 1.72, 0.09, 0.04, 0.06),
        (0.05, -0.07, 1.70, 0.06, 0.035, 0.07),
        (-0.05, -0.07, 1.70, 0.06, 0.035, 0.07),
        (0.09, -0.02, 1.69, 0.05, 0.04, 0.08),
        (-0.09, -0.02, 1.69, 0.05, 0.04, 0.08),
        (0.05, 0.04, 1.74, 0.05, 0.05, 0.045),
        (-0.05, 0.04, 1.74, 0.05, 0.05, 0.045),
        (0.00, 0.07, 1.75, 0.07, 0.05, 0.04),
    ]
    for i, (x, y, z, sx, sy, sz) in enumerate(anchors):
        mesh = bpy.data.meshes.new(f"Lock{i}")
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=12, v_segments=8, radius=1.0)
        for v in bm.verts:
            v.co.x *= sx
            v.co.y *= sy
            v.co.z *= sz
            # wave displace
            v.co.x += 0.01 * math.sin(v.co.z * 40 + i)
            v.co.y += 0.008 * math.cos(v.co.z * 35 + i * 0.7)
        bm.to_mesh(mesh)
        bm.free()
        o = bpy.data.objects.new(f"SM_HairLock_{i}", mesh)
        o.location = (x, y, z)
        link(o, col)
        assign(o, mat)
        for p in o.data.polygons:
            p.use_smooth = True
        locks.append(o)
    return cap_obj, locks


def add_balloon(col, y_front):
    if not BALLOON.exists():
        return None
    mesh = bpy.data.meshes.new("Balloon")
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.085)
    uv = bm.loops.layers.uv.new()
    for face in bm.faces:
        for loop in face.loops:
            co = loop.vert.co
            loop[uv].uv = ((co.x + 0.085) / 0.17, (co.y + 0.085) / 0.17)
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("SM_BalloonDecal", mesh)
    # Face −Y: decal on chest toward camera
    obj.location = (0.0, y_front - 0.02, 1.30)
    obj.rotation_euler = (math.radians(90), 0, 0)
    obj.scale = (1.0, 1.35, 1.0)
    link(obj, col)
    m = bpy.data.materials.new("MAT_Balloon_Decal")
    m.use_nodes = True
    m.blend_method = "BLEND"
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.5
    tex = n.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(str(BALLOON))
    tex.extension = "CLIP"
    tc = n.new("ShaderNodeTexCoord")
    l.new(tc.outputs["UV"], tex.inputs["Vector"])
    l.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    if "Alpha" in bsdf.inputs:
        l.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    assign(obj, m)
    return obj


def setup_studio():
    cd = bpy.data.cameras.new("CAM_Item3_Human")
    cd.sensor_width = 36.0
    cd.lens = 55.0
    cd.dof.use_dof = True
    cd.dof.aperture_fstop = 4.5
    cd.clip_start = 0.05
    cd.clip_end = 400
    cam = bpy.data.objects.new("CAM_Item3_Human", cd)
    bpy.context.scene.collection.objects.link(cam)
    # Face −Y — camera on −Y looking toward origin
    cam.location = (0.55, -3.4, 0.95)
    focus = Vector((0.0, 0.0, 1.05))
    cam.rotation_euler = (focus - cam.location).to_track_quat("-Z", "Y").to_euler()
    cd.dof.focus_distance = (cam.location - focus).length
    bpy.context.scene.camera = cam

    key = bpy.data.lights.new("LGT_Key", type="AREA")
    key.energy = 240
    key.size = 3.0
    key.color = (1.0, 0.97, 0.93)
    ko = bpy.data.objects.new("LGT_Key", key)
    bpy.context.scene.collection.objects.link(ko)
    ko.location = (2.2, -2.0, 2.6)
    ko.rotation_euler = (math.radians(-48), math.radians(20), 0)

    fill = bpy.data.lights.new("LGT_Fill", type="AREA")
    fill.energy = 90
    fill.size = 5.0
    fill.color = (0.75, 0.80, 0.92)
    fo = bpy.data.objects.new("LGT_Fill", fill)
    bpy.context.scene.collection.objects.link(fo)
    fo.location = (-2.4, -1.0, 1.7)

    rim = bpy.data.lights.new("LGT_Rim", type="AREA")
    rim.energy = 110
    rim.size = 2.0
    ro = bpy.data.objects.new("LGT_Rim", rim)
    bpy.context.scene.collection.objects.link(ro)
    ro.location = (-0.2, 2.4, 2.2)

    world = bpy.data.worlds.new("World_Studio")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.58, 0.60, 0.64, 1)
    bg.inputs["Strength"].default_value = 0.28

    def grid(name, size, loc, rot=None):
        mesh = bpy.data.meshes.new(name + "_Mesh")
        bm = bmesh.new()
        bmesh.ops.create_grid(bm, x_segments=8, y_segments=8, size=size * 0.5)
        bm.to_mesh(mesh)
        bm.free()
        obj = bpy.data.objects.new(name, mesh)
        obj.location = loc
        if rot:
            obj.rotation_euler = rot
        bpy.context.scene.collection.objects.link(obj)
        return obj

    g = grid("SM_Ground", 10, (0, 0, 0))
    # Backdrop behind character (+Y)
    b = grid("SM_Backdrop", 10, (0, 2.8, 2.2), (math.radians(90), 0, 0))
    force_box_project(bpy.data.materials.get("concrete_floor_01"), 0.25, 0.35)
    force_box_project(bpy.data.materials.get("grey_plaster_02"), 0.25, 0.4)
    assign(g, bpy.data.materials.get("concrete_floor_01"))
    assign(b, bpy.data.materials.get("grey_plaster_02"))


def setup_render(samples=160):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.render.resolution_x = 1200
    sc.render.resolution_y = 1800
    sc.render.resolution_percentage = 100
    cy = sc.cycles
    cy.samples = samples
    cy.use_adaptive_sampling = True
    cy.adaptive_threshold = 0.02
    cy.use_denoising = True
    try:
        cy.denoiser = "OPENIMAGEDENOISE"
        cy.denoising_input_passes = "RGB_ALBEDO_NORMAL"
        cy.denoising_prefilter = "ACCURATE"
    except Exception:
        pass
    cy.max_bounces = 7
    cy.diffuse_bounces = 4
    cy.glossy_bounces = 4
    cy.transmission_bounces = 6
    cy.transparent_max_bounces = 12
    cy.sample_clamp_indirect = 6.0
    cy.sample_clamp_direct = 0.0
    cy.caustics_reflective = False
    cy.caustics_refractive = False
    cy.blur_glossy = 0.6
    cy.filter_width = 1.5
    sc.render.use_persistent_data = True
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Medium High Contrast"
    sc.view_settings.exposure = 0.0
    sc.render.filepath = str(RENDER)
    sc.render.image_settings.file_format = "PNG"
    prefs = bpy.context.preferences.addons.get("cycles")
    if prefs is not None:
        try:
            prefs.preferences.compute_device_type = "METAL"
            for d in prefs.preferences.devices:
                d.use = True
        except Exception:
            pass


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    clear()
    root = ensure_col("COL_Item3_Human")
    body_c = ensure_col("COL_Body", root)
    cloth_c = ensure_col("COL_Cloth", root)
    hair_c = ensure_col("COL_Hair", root)

    body = import_body(body_c)
    male_proportions(body)
    # Keep T-pose topology intact — prior A-pose vertex rotates shredded the silhouette.
    # Croquis arm-down is a follow-up pose pass; BRA-16 priority is human likeness.
    skin = mat_skin()
    assign(body, skin)
    # Smooth human read
    sub = body.modifiers.new("Subdiv", "SUBSURF")
    sub.levels = 1
    sub.render_levels = 2
    add_eyes(body, body_c, mat_eye())

    sweater_mat = tint_ph("knitted_fleece", "MAT_Knit_Mustard", (0.78, 0.52, 0.16), 0.82, 1.7)
    pants_mat = tint_ph("poly_wool_herringbone", "MAT_Wool_Grey", (0.32, 0.32, 0.35), 0.72, 1.3)
    leather = mat_leather()

    sweater = shell_from_body(body, "SM_Char_Item3_Cloth_Sweater", 0.88, 1.50, cloth_c, sweater_mat, 0.014, 0.008)
    # Trim sweater past mid-forearm so T-pose hands stay skin
    bm = bmesh.new()
    bm.from_mesh(sweater.data)
    kill = [f for f in bm.faces if abs(f.calc_center_median().x) > 0.48]
    if kill:
        bmesh.ops.delete(bm, geom=kill, context="FACES")
        bm.to_mesh(sweater.data)
    bm.free()
    pants = shell_from_body(body, "SM_Char_Item3_Cloth_Pants", 0.05, 0.96, cloth_c, pants_mat, 0.012, 0.007)
    make_boots(body, cloth_c, leather)

    y_front = min(v.co.y for v in body.data.vertices if 1.1 < v.co.z < 1.4)
    add_balloon(cloth_c, y_front)
    add_wavy_hair(body, hair_c, mat_hair())
    hide_body_under_clothes(body)

    setup_studio()
    setup_render(160)
    run(lambda: bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)))
    print("SAVED", BLEND)
    run(lambda: bpy.ops.render.render(write_still=True))
    print("RENDERED", RENDER, RENDER.exists(), RENDER.stat().st_size if RENDER.exists() else 0)


main()

"""BRA-12 Item 3 — Clawd photoreal recipe at adult fashion scale.

Canon: bra-13-clawd-artifact-canon.md / hundred-acre-claude-artifact.md
  Real metres · 36 mm sensor · DOF · Poly Haven box-project blend 0.25
  Bevel every edge · one honest light · cooler/darker backdrop · AgX MHC
  64–176 samples · OIDN albedo+normal · clamp indirect 6 · max bounce 7

Subject: Hundred Acre Softness Item 3
  Mustard crew sweater + red balloon graphic, grey trousers, brown boots.
  Built Clawd-style from measured bevelled boxes/cylinders — not blockout flats.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import bmesh
from mathutils import Matrix, Vector

OUT = Path("/Users/jongarcia/Documents/Development/platforms/blender-skills/demos/out")
ASSETS = OUT / "assets"
BLEND = OUT / "SM_HundredAcre_Item3_Realistic.blend"
RENDER = OUT / "hundred-acre-item3-realistic.png"
BALLOON = ASSETS / "balloon_graphic.png"

KEEP = {
    "knitted_fleece",
    "poly_wool_herringbone",
    "cotton_jersey",
    "denim_fabric",
    "grey_plaster_02",
    "concrete_floor_01",
}


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
    for block in (bpy.data.meshes, bpy.data.cameras, bpy.data.lights, bpy.data.worlds, bpy.data.metaballs):
        for item in list(block):
            block.remove(item)
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


def apply_mods(obj):
    act(obj)

    def _():
        for m in list(obj.modifiers):
            try:
                bpy.ops.object.modifier_apply(modifier=m.name)
            except Exception as e:
                print("mod", m.name, e)

    run(_)


def shade(obj):
    for p in obj.data.polygons:
        p.use_smooth = True


def assign(obj, mat):
    if not mat:
        return
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


def clawd_finish(obj, bevel_w=0.003, subdiv=2, apply=True):
    """Clawd: bevel every edge + subdiv so edges catch light."""
    b = obj.modifiers.new("Bevel", "BEVEL")
    b.width = bevel_w
    b.segments = 3
    b.limit_method = "ANGLE"
    b.angle_limit = math.radians(30)
    b.affect = "EDGES"
    s = obj.modifiers.new("Subdivision", "SUBSURF")
    s.levels = subdiv
    s.render_levels = max(subdiv, 2)
    shade(obj)
    if apply:
        apply_mods(obj)
        shade(obj)


def box(name, size, loc, col, rot=None):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    sx, sy, sz = size
    for v in bm.verts:
        v.co.x *= sx
        v.co.y *= sy
        v.co.z *= sz
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    if rot:
        obj.rotation_euler = rot
    link(obj, col)
    return obj


def cyl(name, radius, depth, loc, col, rot=None, verts=32):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_cone(
        bm,
        cap_ends=True,
        cap_tris=False,
        segments=verts,
        radius1=radius,
        radius2=radius,
        depth=depth,
    )
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    if rot:
        obj.rotation_euler = rot
    link(obj, col)
    return obj


def join_objects(name, objs, col):
    """Merge parts in world space. Do not trust matrix_world on fresh objects — use LocRotScale."""
    if not objs:
        return None
    bm = bmesh.new()
    for o in objs:
        # Fresh objects can report identity matrix_world until depsgraph update;
        # LocRotScale from explicit transforms is reliable for Clawd multi-box joins.
        mat = Matrix.LocRotScale(o.location, o.rotation_euler.to_quaternion(), o.scale)
        temp = bmesh.new()
        temp.from_mesh(o.data)
        temp.transform(mat)
        temp.verts.ensure_lookup_table()
        bmesh.ops.recalc_face_normals(temp, faces=temp.faces)
        verts_map = {}
        for v in temp.verts:
            verts_map[v.index] = bm.verts.new(v.co)
        bm.verts.ensure_lookup_table()
        for f in temp.faces:
            try:
                bm.faces.new([verts_map[v.index] for v in f.verts])
            except Exception:
                pass
        temp.free()
        bpy.data.objects.remove(o, do_unlink=True)
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    link(obj, col)
    bm2 = bmesh.new()
    bm2.from_mesh(mesh)
    bmesh.ops.remove_doubles(bm2, verts=bm2.verts, dist=0.0015)
    bm2.to_mesh(mesh)
    bm2.free()
    return obj


def force_box_project(mat, blend=0.25, scale=1.0, kill_displacement=False):
    """Clawd: Poly Haven maps box-projected in object space, blend 0.25."""
    if not mat or not mat.node_tree:
        return
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    texcoord = next((n for n in nodes if n.type == "TEX_COORD"), None)
    if not texcoord:
        texcoord = nodes.new("ShaderNodeTexCoord")
    mapping = next((n for n in nodes if n.type == "MAPPING"), None)
    if not mapping:
        mapping = nodes.new("ShaderNodeMapping")
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
        # PH fabric displacement + subdiv = fringe spikes; keep albedo/rough/normal only
        for n in list(nodes):
            if n.type == "DISPLACEMENT":
                for l in list(n.outputs[0].links):
                    links.remove(l)
                nodes.remove(n)
        out = next((n for n in nodes if n.type == "OUTPUT_MATERIAL"), None)
        if out and out.inputs["Displacement"].links:
            for l in list(out.inputs["Displacement"].links):
                links.remove(l)
        try:
            mat.cycles.displacement_method = "BUMP"
        except Exception:
            try:
                mat.displacement_method = "BUMP"
            except Exception:
                pass


def tint_ph(src, new_name, tint, strength=0.75, box_scale=1.4):
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
        bsdf.inputs["Coat Weight"].default_value = 0.22
        bsdf.inputs["Coat Roughness"].default_value = 0.32
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.55
        if "Sheen Roughness" in bsdf.inputs:
            bsdf.inputs["Sheen Roughness"].default_value = 0.35
    return m


def mat_balloon_decal():
    """Standalone chest decal — more reliable than projecting onto joined sweater UVs."""
    m = bpy.data.materials.new("MAT_Balloon_Decal")
    m.use_nodes = True
    m.blend_method = "BLEND"
    try:
        m.shadow_method = "NONE"
    except Exception:
        pass
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.55
    if "Alpha" in bsdf.inputs:
        bsdf.inputs["Alpha"].default_value = 1.0
    tex = n.new("ShaderNodeTexImage")
    if BALLOON.exists():
        tex.image = bpy.data.images.load(str(BALLOON))
    tex.extension = "CLIP"
    tc = n.new("ShaderNodeTexCoord")
    l.new(tc.outputs["UV"], tex.inputs["Vector"])
    l.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    if "Alpha" in bsdf.inputs:
        l.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def add_balloon_decal(col):
    if not BALLOON.exists():
        print("balloon missing", BALLOON)
        return None
    mesh = bpy.data.meshes.new("SM_BalloonDecal_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.11)
    # UV unwrap simple quad
    uv_layer = bm.loops.layers.uv.new()
    for face in bm.faces:
        for loop in face.loops:
            co = loop.vert.co
            loop[uv_layer].uv = ((co.x + 0.11) / 0.22, (co.y + 0.11) / 0.22)
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("SM_BalloonDecal", mesh)
    # Chest front of mustard sweater (~mid torso)
    obj.location = (0.0, -0.155, 1.28)
    obj.rotation_euler = (math.radians(90), 0, 0)
    obj.scale = (1.0, 1.35, 1.0)
    link(obj, col)
    assign(obj, mat_balloon_decal())
    return obj


def mat_skin():
    m = bpy.data.materials.new("MAT_Skin_Realistic")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.82, 0.64, 0.50, 1)
    bsdf.inputs["Roughness"].default_value = 0.48
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.18
        if "Subsurface Radius" in bsdf.inputs:
            bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.2, 0.1)
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 900
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.03
    if "Distance" in bump.inputs:
        bump.inputs["Distance"].default_value = 0.0002
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.08
        bsdf.inputs["Coat Roughness"].default_value = 0.3
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def mat_leather():
    m = bpy.data.materials.new("MAT_Leather_Boot")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    # Clawd paint recipe adapted to leather
    bsdf.inputs["Base Color"].default_value = (0.22, 0.12, 0.06, 1)
    bsdf.inputs["Roughness"].default_value = 0.48
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.25
        bsdf.inputs["Coat Roughness"].default_value = 0.3
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 120
    noise.inputs["Detail"].default_value = 14
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.28
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def mat_hair():
    m = bpy.data.materials.new("MAT_Hair")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.20, 0.12, 0.07, 1)
    bsdf.inputs["Roughness"].default_value = 0.38
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.28
        bsdf.inputs["Coat Roughness"].default_value = 0.22
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 400
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.12
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def build_figure(root):
    body_c = ensure_col("COL_Body", root)
    cloth_c = ensure_col("COL_Cloth", root)
    hair_c = ensure_col("COL_Hair", root)

    skin = mat_skin()
    hair_mat = mat_hair()
    leather = mat_leather()
    sweater_mat = tint_ph("knitted_fleece", "MAT_Knit_Mustard_PH", (0.78, 0.52, 0.16), 0.82, 1.6)
    pants_mat = tint_ph("poly_wool_herringbone", "MAT_Wool_Grey_PH", (0.30, 0.30, 0.33), 0.72, 1.2)

    # Adult male ~1.82 m — Clawd measured multi-part craft
    # Head
    head = box("SM_Head", (0.17, 0.20, 0.22), (0.0, 0.0, 1.70), body_c)
    neck = cyl("SM_Neck", 0.055, 0.09, (0.0, 0.0, 1.545), body_c)
    jaw = box("SM_Jaw", (0.14, 0.12, 0.06), (0.0, -0.02, 1.60), body_c)
    nose = box("SM_Nose", (0.025, 0.04, 0.028), (0.0, -0.11, 1.68), body_c)
    for sx, side in ((0.09, "L"), (-0.09, "R")):
        box(f"SM_Ear_{side}", (0.018, 0.03, 0.05), (sx, 0.0, 1.70), body_c)

    eye_mat = bpy.data.materials.new("MAT_Eye")
    eye_mat.use_nodes = True
    ebsdf = eye_mat.node_tree.nodes["Principled BSDF"]
    ebsdf.inputs["Base Color"].default_value = (0.04, 0.03, 0.03, 1)
    ebsdf.inputs["Roughness"].default_value = 0.08
    if "Coat Weight" in ebsdf.inputs:
        ebsdf.inputs["Coat Weight"].default_value = 1.0
        ebsdf.inputs["Coat Roughness"].default_value = 0.03
    for sx, side in ((0.032, "L"), (-0.032, "R")):
        e = cyl(f"SM_Eye_{side}", 0.011, 0.008, (sx, -0.105, 1.715), body_c, rot=(math.radians(90), 0, 0))
        assign(e, eye_mat)
        clawd_finish(e, 0.0008, 1)

    for o in list(body_c.objects):
        if o.name.startswith(("SM_Head", "SM_Neck", "SM_Jaw", "SM_Nose", "SM_Ear")):
            assign(o, skin)
            clawd_finish(o, 0.003, 2)

    # Short wavy hair ON TOP only (croquis) — no face locks / Clawd-mustache look
    scalp = box("SM_HairCap", (0.18, 0.21, 0.09), (0.0, 0.01, 1.80), hair_c)
    assign(scalp, hair_mat)
    clawd_finish(scalp, 0.004, 2)
    for i, (loc, sz) in enumerate(
        [
            ((0.05, -0.06, 1.82), (0.07, 0.08, 0.05)),
            ((-0.05, -0.06, 1.82), (0.07, 0.08, 0.05)),
            ((0.0, -0.08, 1.78), (0.09, 0.05, 0.04)),
            ((0.08, 0.04, 1.81), (0.06, 0.07, 0.05)),
            ((-0.08, 0.04, 1.81), (0.06, 0.07, 0.05)),
            ((0.0, 0.08, 1.83), (0.10, 0.06, 0.04)),
        ]
    ):
        lock = box(f"SM_HairWave_{i}", sz, loc, hair_c)
        assign(lock, hair_mat)
        clawd_finish(lock, 0.003, 2)

    # Under-body kept slim so PH knit reads as the silhouette (no skin slabs through sleeves)
    torso_skin = box("SM_TorsoSkin", (0.30, 0.18, 0.48), (0.0, 0.02, 1.18), body_c)
    assign(torso_skin, skin)
    clawd_finish(torso_skin, 0.003, 1)

    # --- MUSTARD SWEATER ---
    torso = box("SM_SweaterTorso", (0.44, 0.28, 0.60), (0.0, 0.02, 1.20), cloth_c)
    hem = box("SM_SweaterHem", (0.46, 0.30, 0.07), (0.0, 0.02, 0.88), cloth_c)
    collar = cyl("SM_SweaterCollar", 0.095, 0.055, (0.0, -0.01, 1.50), cloth_c)
    parts = [torso, hem, collar]
    for sx, side, yaw in ((0.30, "L", 18), (-0.30, "R", -18)):
        ua = cyl(
            f"SM_SweaterArmU_{side}",
            0.075,
            0.32,
            (sx, 0.05, 1.28),
            cloth_c,
            rot=(math.radians(18), math.radians(yaw), 0),
        )
        fa = cyl(
            f"SM_SweaterArmF_{side}",
            0.065,
            0.30,
            (sx * 0.95, 0.12, 1.00),
            cloth_c,
            rot=(math.radians(32), math.radians(yaw * 0.4), 0),
        )
        cuff = cyl(f"SM_SweaterCuff_{side}", 0.058, 0.05, (sx * 0.85, 0.18, 0.86), cloth_c)
        parts += [ua, fa, cuff]
    for p in parts:
        assign(p, sweater_mat)
    sweater = join_objects("SM_Char_Item3_Cloth_Sweater", parts, cloth_c)
    assign(sweater, sweater_mat)
    clawd_finish(sweater, 0.004, 2)
    add_balloon_decal(cloth_c)

    # Hands in pockets (croquis)
    for sx, side in ((0.16, "L"), (-0.16, "R")):
        hand = box(f"SM_Hand_{side}", (0.075, 0.045, 0.095), (sx, 0.14, 0.82), body_c)
        assign(hand, skin)
        clawd_finish(hand, 0.0025, 2)

    # --- GREY TROUSERS ---
    waist = box("SM_PantsWaist", (0.42, 0.26, 0.14), (0.0, 0.02, 0.86), cloth_c)
    pant_parts = [waist]
    for sx, side, yoff in ((0.105, "L", -0.03), (-0.105, "R", 0.04)):
        thigh = cyl(f"SM_PantThigh_{side}", 0.095, 0.42, (sx, yoff, 0.62), cloth_c)
        calf = cyl(f"SM_PantCalf_{side}", 0.072, 0.40, (sx, yoff - 0.01, 0.24), cloth_c)
        cuff = box(f"SM_PantCuff_{side}", (0.15, 0.15, 0.04), (sx, yoff - 0.01, 0.10), cloth_c)
        pant_parts += [thigh, calf, cuff]
    for p in pant_parts:
        assign(p, pants_mat)
    pants = join_objects("SM_Char_Item3_Cloth_Pants", pant_parts, cloth_c)
    assign(pants, pants_mat)
    clawd_finish(pants, 0.0035, 2)

    # --- BROWN BOOTS ---
    for sx, side, yoff in ((0.105, "L", -0.06), (-0.105, "R", 0.03)):
        shaft = box(f"SM_BootShaft_{side}", (0.135, 0.18, 0.20), (sx, yoff, 0.13), cloth_c)
        toe = box(f"SM_BootToe_{side}", (0.13, 0.20, 0.08), (sx, yoff - 0.09, 0.045), cloth_c)
        sole = box(f"SM_BootSole_{side}", (0.145, 0.30, 0.035), (sx, yoff - 0.03, 0.015), cloth_c)
        boot = join_objects(f"SM_Char_Item3_Boot_{side}", [shaft, toe, sole], cloth_c)
        assign(boot, leather)
        clawd_finish(boot, 0.0025, 2)


def setup_studio_clawd():
    # Full-body fashion framing — Clawd cam recipe at adult scale (not toy floor-cam crop)
    cd = bpy.data.cameras.new("CAM_Item3_Hero")
    cd.sensor_width = 36.0
    cd.lens = 50.0
    cd.dof.use_dof = True
    cd.dof.aperture_fstop = 5.6
    cd.dof.aperture_blades = 0
    cd.clip_start = 0.05
    cd.clip_end = 400
    cam = bpy.data.objects.new("CAM_Item3_Hero", cd)
    bpy.context.scene.collection.objects.link(cam)
    # 3/4 full figure: feet to hair in frame
    cam.location = (1.55, -4.6, 0.95)
    focus = Vector((0.0, 0.05, 1.15))  # chest / sweater balloon
    cam.rotation_euler = (focus - cam.location).to_track_quat("-Z", "Y").to_euler()
    cd.dof.focus_object = None
    cd.dof.focus_distance = (cam.location - focus).length
    bpy.context.scene.camera = cam

    # One honest key (soft window) + cooler fill; hero against cooler/darker
    # Motivated soft window key — keep AgX from pink-shifting mustard (lower energy, not hue)
    key = bpy.data.lights.new("LGT_Key", type="AREA")
    key.energy = 280
    key.size = 3.2
    key.color = (1.0, 0.97, 0.92)
    ko = bpy.data.objects.new("LGT_Key", key)
    bpy.context.scene.collection.objects.link(ko)
    ko.location = (2.6, -2.4, 2.8)
    ko.rotation_euler = (math.radians(-48), math.radians(28), 0)

    fill = bpy.data.lights.new("LGT_Fill", type="AREA")
    fill.energy = 70
    fill.size = 5.5
    fill.color = (0.68, 0.76, 0.92)
    fo = bpy.data.objects.new("LGT_Fill", fill)
    bpy.context.scene.collection.objects.link(fo)
    fo.location = (-2.8, -1.2, 1.9)

    rim = bpy.data.lights.new("LGT_Rim", type="AREA")
    rim.energy = 90
    rim.size = 2.0
    rim.color = (0.80, 0.86, 1.0)
    ro = bpy.data.objects.new("LGT_Rim", rim)
    bpy.context.scene.collection.objects.link(ro)
    ro.location = (-0.5, 2.6, 2.5)

    world = bpy.data.worlds.new("World_Studio")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.48, 0.52, 0.58, 1)
    bg.inputs["Strength"].default_value = 0.22

    def grid(name, size, loc, rot=None):
        mesh = bpy.data.meshes.new(name + "_Mesh")
        bm = bmesh.new()
        bmesh.ops.create_grid(bm, x_segments=12, y_segments=12, size=size * 0.5)
        bm.to_mesh(mesh)
        bm.free()
        obj = bpy.data.objects.new(name, mesh)
        obj.location = loc
        if rot:
            obj.rotation_euler = rot
        bpy.context.scene.collection.objects.link(obj)
        clawd_finish(obj, 0.001, 1)
        return obj

    g = grid("SM_Ground", 10, (0, 0, 0))
    b = grid("SM_Backdrop", 10, (0, 3.2, 2.4), (math.radians(90), 0, 0))
    force_box_project(bpy.data.materials.get("concrete_floor_01"), 0.25, 0.35)
    force_box_project(bpy.data.materials.get("grey_plaster_02"), 0.25, 0.4)
    assign(g, bpy.data.materials.get("concrete_floor_01"))
    assign(b, bpy.data.materials.get("grey_plaster_02"))


def setup_render_clawd(samples=176):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.render.resolution_x = 1200
    sc.render.resolution_y = 1800
    sc.render.resolution_percentage = 100
    sc.render.fps = 24
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
    sc.render.use_motion_blur = False  # still
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Medium High Contrast"
    sc.view_settings.exposure = 0.0
    sc.render.filepath = str(RENDER)
    sc.render.image_settings.file_format = "PNG"
    sc.render.film_transparent = False
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
    # Ensure PH mats keep box projection on originals too
    for mid in ("knitted_fleece", "poly_wool_herringbone", "grey_plaster_02", "concrete_floor_01"):
        force_box_project(bpy.data.materials.get(mid), 0.25, 1.0)
    root = ensure_col("COL_HundredAcre_Item3")
    build_figure(root)
    setup_studio_clawd()
    setup_render_clawd(176)
    run(lambda: bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)))
    print("SAVED", BLEND)
    run(lambda: bpy.ops.render.render(write_still=True))
    print("RENDERED", RENDER, RENDER.exists(), RENDER.stat().st_size if RENDER.exists() else 0)


main()

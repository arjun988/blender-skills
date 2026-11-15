"""BRA-21 QC — Grab3D CC0 adult male (intact A-pose) + Item 3 garment overlays.

No armature posing (prior pass shredded a leg). Clothes are opaque PH shells
covering the stock tee/shorts. QC vs croquis Item 3.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import bmesh
from mathutils import Vector

OUT = Path("/Users/jongarcia/Documents/Development/platforms/blender-skills/demos/out")
ASSETS = OUT / "assets"
GLB = ASSETS / "man_base_grab3d.glb"  # static — no pose damage
ALBEDO_HAIR = ASSETS / "grab3d_item3_albedo.png"  # hair lightened
BALLOON = ASSETS / "balloon_graphic.png"
CROQUIS = Path(
    "/Users/jongarcia/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-a47a87df-0dc9-4fa1-9906-94396fb68fe5/files/media/"
    "hundred-acre-softness-croquis.png"
)
BLEND = OUT / "SM_HundredAcre_Item3_QC.blend"
RENDER = OUT / "hundred-acre-item3-qc.png"
COMPARE = OUT / "hundred-acre-item3-qc-compare.png"

KEEP = {"knitted_fleece", "poly_wool_herringbone", "grey_plaster_02", "concrete_floor_01"}


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
    for block in (bpy.data.meshes, bpy.data.armatures, bpy.data.cameras, bpy.data.lights, bpy.data.worlds):
        for item in list(block):
            try:
                block.remove(item)
            except Exception:
                pass
    for m in list(bpy.data.materials):
        if m.name not in KEEP:
            try:
                bpy.data.materials.remove(m)
            except Exception:
                pass


def act(obj):
    bpy.context.view_layer.objects.active = obj
    for o in bpy.context.view_layer.objects:
        o.select_set(o == obj)


def assign(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def force_box_project(mat, blend=0.25, scale=1.5, kill_disp=True):
    if not mat or not mat.node_tree:
        return
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    tc = next((n for n in nodes if n.type == "TEX_COORD"), None) or nodes.new("ShaderNodeTexCoord")
    mapping = next((n for n in nodes if n.type == "MAPPING"), None) or nodes.new("ShaderNodeMapping")
    mapping.inputs["Scale"].default_value = (scale, scale, scale)
    for l in list(mapping.inputs["Vector"].links):
        links.remove(l)
    links.new(tc.outputs["Object"], mapping.inputs["Vector"])
    for n in nodes:
        if n.type != "TEX_IMAGE":
            continue
        n.projection = "BOX"
        n.projection_blend = blend
        for l in list(n.inputs["Vector"].links):
            links.remove(l)
        links.new(mapping.outputs["Vector"], n.inputs["Vector"])
    if kill_disp:
        for n in list(nodes):
            if n.type == "DISPLACEMENT":
                for l in list(n.outputs[0].links):
                    links.remove(l)
                nodes.remove(n)
        out = next((n for n in nodes if n.type == "OUTPUT_MATERIAL"), None)
        if out:
            for l in list(out.inputs["Displacement"].links):
                links.remove(l)


def tint_ph(src, name, tint, strength=0.8, scale=1.6):
    src_m = bpy.data.materials.get(src)
    if not src_m:
        raise RuntimeError("missing " + src)
    m = src_m.copy()
    m.name = name
    force_box_project(m, 0.25, scale, True)
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
    mix.inputs["B"].default_value = (*tint, 1)
    if fr:
        nt.links.new(fr, mix.inputs["A"])
    try:
        nt.links.new(mix.outputs["Result"], bsdf.inputs["Base Color"])
    except Exception:
        nt.links.new(mix.outputs[0], bsdf.inputs["Base Color"])
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.45
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.15
    return m


def import_char():
    before = set(bpy.data.objects)
    run(lambda: bpy.ops.import_scene.gltf(filepath=str(GLB)))
    imported = [o for o in bpy.data.objects if o not in before]
    body = next(o for o in imported if o.type == "MESH" and "Ico" not in o.name)
    for o in imported:
        if o != body:
            bpy.data.objects.remove(o, do_unlink=True)
    body.name = "SM_Char_Item3_QC"
    # Apply transforms
    act(body)
    run(lambda: bpy.ops.object.transform_apply(location=True, rotation=True, scale=True))
    # Feet on ground / center
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
    for p in body.data.polygons:
        p.use_smooth = True
    print("BODY", tuple(round(d, 3) for d in body.dimensions), "z", round(min(v.co.z for v in body.data.vertices), 3), round(max(v.co.z for v in body.data.vertices), 3))
    return body


def lighten_hair_albedo(body):
    if not ALBEDO_HAIR.exists():
        return
    img = bpy.data.images.load(str(ALBEDO_HAIR))
    img.colorspace_settings.name = "sRGB"
    for mat in body.data.materials:
        if not mat or not mat.node_tree:
            continue
        bsdf = next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
        if not bsdf:
            continue
        base = bsdf.inputs.get("Base Color")
        if base and base.links and base.links[0].from_node.type == "TEX_IMAGE":
            base.links[0].from_node.image = img
            print("hair albedo swapped")
            return
        texes = [n for n in mat.node_tree.nodes if n.type == "TEX_IMAGE" and n.image]
        if texes:
            texes.sort(key=lambda n: n.image.size[0] * n.image.size[1], reverse=True)
            texes[0].image = img
            print("hair albedo swapped largest")
            return


def shell(body, name, z0, z1, mat, solidify=0.016, inflate=0.01, x_max=None):
    mesh = body.data.copy()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    bm = bmesh.new()
    bm.from_mesh(mesh)
    kill = []
    for f in bm.faces:
        c = f.calc_center_median()
        if c.z < z0 or c.z > z1:
            kill.append(f)
            continue
        if x_max is not None and abs(c.x) > x_max:
            kill.append(f)
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


def add_boots():
    m = bpy.data.materials.new("MAT_QC_Boots")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.20, 0.10, 0.05, 1)
    bsdf.inputs["Roughness"].default_value = 0.48
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.25
        bsdf.inputs["Coat Roughness"].default_value = 0.32
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 60
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.22
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

    boots = []
    for sx, side in ((-1, "L"), (1, "R")):
        mesh = bpy.data.meshes.new(f"Boot{side}")
        bm = bmesh.new()
        # shaft
        bmesh.ops.create_cone(bm, cap_ends=True, segments=28, radius1=0.058, radius2=0.052, depth=0.20)
        for v in bm.verts:
            v.co.z += 0.10
        # toe box
        g = bmesh.ops.create_cube(bm, size=1.0)
        for v in g["verts"]:
            v.co.x *= 0.11
            v.co.y *= 0.16
            v.co.z *= 0.07
            v.co.y -= 0.09
            v.co.z += 0.04
        # sole
        g2 = bmesh.ops.create_cube(bm, size=1.0)
        for v in g2["verts"]:
            v.co.x *= 0.12
            v.co.y *= 0.24
            v.co.z *= 0.028
            v.co.y -= 0.04
            v.co.z += 0.012
        bm.to_mesh(mesh)
        bm.free()
        obj = bpy.data.objects.new(f"SM_Boot_{side}", mesh)
        obj.location = (0.11 * sx, -0.03, 0.0)
        bpy.context.scene.collection.objects.link(obj)
        assign(obj, m)
        for p in obj.data.polygons:
            p.use_smooth = True
        bev = obj.modifiers.new("Bevel", "BEVEL")
        bev.width = 0.004
        bev.segments = 3
        boots.append(obj)
    return boots


def add_balloon(y_face):
    if not BALLOON.exists():
        return None
    mesh = bpy.data.meshes.new("Balloon")
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.075)
    uv = bm.loops.layers.uv.new()
    for face in bm.faces:
        for loop in face.loops:
            co = loop.vert.co
            loop[uv].uv = ((co.x + 0.075) / 0.15, (co.y + 0.075) / 0.15)
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("SM_BalloonDecal", mesh)
    obj.location = (0.0, y_face - 0.02, 1.30)
    obj.rotation_euler = (math.radians(90), 0, 0)
    obj.scale = (1.1, 1.45, 1.0)
    bpy.context.scene.collection.objects.link(obj)
    mat = bpy.data.materials.new("MAT_Balloon_QC")
    mat.use_nodes = True
    mat.blend_method = "BLEND"
    nt = mat.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.45
    tex = n.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(str(BALLOON))
    tex.extension = "CLIP"
    tc = n.new("ShaderNodeTexCoord")
    l.new(tc.outputs["UV"], tex.inputs["Vector"])
    l.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    if "Alpha" in bsdf.inputs:
        l.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    assign(obj, mat)
    return obj


def setup_studio(face_sign=-1):
    """face_sign=-1 means face toward -Y (camera on -Y)."""
    cd = bpy.data.cameras.new("CAM_QC")
    cd.sensor_width = 36
    cd.lens = 55
    cd.dof.use_dof = True
    cd.dof.aperture_fstop = 4.5
    cam = bpy.data.objects.new("CAM_QC", cd)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (0.55, -3.3 * (-face_sign if face_sign > 0 else 1), 0.95) if face_sign < 0 else (0.55, 3.3, 0.95)
    if face_sign < 0:
        cam.location = (0.55, -3.3, 0.95)
    else:
        cam.location = (0.55, 3.3, 0.95)
    focus = Vector((0.0, 0.0, 1.05))
    cam.rotation_euler = (focus - cam.location).to_track_quat("-Z", "Y").to_euler()
    cd.dof.focus_distance = (cam.location - focus).length
    bpy.context.scene.camera = cam

    key = bpy.data.lights.new("LGT_Key", type="AREA")
    key.energy = 210
    key.size = 2.8
    key.color = (1.0, 0.97, 0.93)
    ko = bpy.data.objects.new("LGT_Key", key)
    bpy.context.scene.collection.objects.link(ko)
    ko.location = (2.1, cam.location.y * 0.55, 2.5)
    ko.rotation_euler = (math.radians(-48), math.radians(18 if cam.location.y < 0 else -18), 0)

    fill = bpy.data.lights.new("LGT_Fill", type="AREA")
    fill.energy = 75
    fill.size = 4.5
    fill.color = (0.74, 0.80, 0.92)
    fo = bpy.data.objects.new("LGT_Fill", fill)
    bpy.context.scene.collection.objects.link(fo)
    fo.location = (-2.3, cam.location.y * 0.35, 1.7)

    rim = bpy.data.lights.new("LGT_Rim", type="AREA")
    rim.energy = 95
    rim.size = 2.0
    ro = bpy.data.objects.new("LGT_Rim", rim)
    bpy.context.scene.collection.objects.link(ro)
    ro.location = (-0.2, -cam.location.y * 0.75, 2.2)

    world = bpy.data.worlds.new("World_QC")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.64, 0.66, 0.70, 1)
    bg.inputs["Strength"].default_value = 0.32

    def grid(name, size, loc, rot=None):
        mesh = bpy.data.meshes.new(name)
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
    by = 2.7 if cam.location.y < 0 else -2.7
    b = grid("SM_Backdrop", 10, (0, by, 2.2), (math.radians(90), 0, 0))
    force_box_project(bpy.data.materials.get("concrete_floor_01"), 0.25, 0.35, False)
    force_box_project(bpy.data.materials.get("grey_plaster_02"), 0.25, 0.4, False)
    assign(g, bpy.data.materials.get("concrete_floor_01"))
    assign(b, bpy.data.materials.get("grey_plaster_02"))


def setup_render(samples=140):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.render.resolution_x = 1200
    sc.render.resolution_y = 1800
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
    cy.blur_glossy = 0.6
    cy.filter_width = 1.5
    sc.render.use_persistent_data = True
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Medium High Contrast"
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
    body = import_char()
    lighten_hair_albedo(body)

    # Face direction
    head = [v.co for v in body.data.vertices if v.co.z > 1.55]
    ymin, ymax = min(v.y for v in head), max(v.y for v in head)
    face_min = (abs(ymin) <= abs(ymax))  # smaller |extent| often nose — MH style
    # Grab3D: nose at min Y typically after apply
    face_y = ymin
    face_sign = -1
    print("head y", round(ymin, 3), round(ymax, 3), "using face_y", round(face_y, 3))

    sweater_mat = tint_ph("knitted_fleece", "MAT_QC_Mustard", (0.80, 0.54, 0.16), 0.85, 1.7)
    pants_mat = tint_ph("poly_wool_herringbone", "MAT_QC_GreyPants", (0.36, 0.36, 0.38), 0.75, 1.3)

    # Opaque overlays covering stock tee/shorts
    sweater = shell(body, "SM_QC_Sweater", 0.92, 1.52, sweater_mat, 0.018, 0.012)
    pants = shell(body, "SM_QC_Pants", 0.06, 0.98, pants_mat, 0.014, 0.010)
    # trim sweater hands — keep skin hands visible
    bm = bmesh.new()
    bm.from_mesh(sweater.data)
    kill = [f for f in bm.faces if abs(f.calc_center_median().x) > 0.42 and f.calc_center_median().z < 1.25]
    if kill:
        bmesh.ops.delete(bm, geom=kill, context="FACES")
        bm.to_mesh(sweater.data)
    bm.free()

    add_balloon(face_y)
    add_boots()
    setup_studio(face_sign)
    setup_render(140)
    run(lambda: bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)))
    print("SAVED", BLEND)
    run(lambda: bpy.ops.render.render(write_still=True))
    print("RENDERED", RENDER, RENDER.exists(), RENDER.stat().st_size if RENDER.exists() else 0)


main()

"""Improved Item 3 — MCP-safe (bpy.data API, minimal ops; ops only with VIEW_3D override)."""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import mathutils
from mathutils import Vector

OUT = Path("/Users/jongarcia/Documents/Development/platforms/blender-skills/demos/out")
BLEND = OUT / "SM_HundredAcre_Item3_MCP.blend"
RENDER = OUT / "hundred-acre-item3-mcp.png"
VIEWPORT = OUT / "hundred-acre-item3-mcp-viewport.png"

COL_MUSTARD = (0.84, 0.66, 0.28, 1.0)
COL_BALLOON = (0.90, 0.14, 0.12, 1.0)
COL_STRING = (0.05, 0.05, 0.05, 1.0)
COL_GREY = (0.34, 0.34, 0.37, 1.0)
COL_BOOT = (0.32, 0.18, 0.10, 1.0)
COL_SKIN = (0.89, 0.75, 0.65, 1.0)
COL_HAIR = (0.42, 0.30, 0.20, 1.0)
COL_BG = (0.96, 0.94, 0.90, 1.0)


def view3d_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == "VIEW_3D":
                for region in area.regions:
                    if region.type == "WINDOW":
                        return {
                            "window": window,
                            "screen": screen,
                            "area": area,
                            "region": region,
                            "scene": bpy.context.scene,
                            "view_layer": bpy.context.view_layer,
                        }
    return None


def run_ops(fn):
    ov = view3d_override()
    if ov is None:
        return fn()
    with bpy.context.temp_override(**ov):
        return fn()


def clear():
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    for col in list(bpy.data.collections):
        if col != bpy.context.scene.collection:
            bpy.data.collections.remove(col)
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights, bpy.data.worlds, bpy.data.images):
        for item in list(block):
            block.remove(item)


def ensure_col(name, parent=None):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(c)
    return c


def link(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)


def mat(name, color, rough=0.65, metal=0.0, sheen=0.0, bump=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nodes, links = nt.nodes, nt.links
    nodes.clear()
    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = sheen
    if bump > 0:
        tex = nodes.new("ShaderNodeTexNoise")
        tex.inputs["Scale"].default_value = 180.0
        tex.inputs["Detail"].default_value = 8.0
        bumpn = nodes.new("ShaderNodeBump")
        bumpn.inputs["Strength"].default_value = bump
        links.new(tex.outputs["Fac"], bumpn.inputs["Height"])
        links.new(bumpn.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def assign(obj, m):
    if obj.data.materials:
        obj.data.materials[0] = m
    else:
        obj.data.materials.append(m)


def smooth(obj):
    for p in obj.data.polygons:
        p.use_smooth = True


def bevel(obj, w=0.012, seg=2):
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.width = w
    mod.segments = seg
    mod.limit_method = "ANGLE"
    mod.angle_limit = math.radians(30)


def make_uv_sphere(name, radius, location, col, segments=32, rings=16, scale=None):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    # Build UV sphere manually
    verts = []
    faces = []
    for i in range(rings + 1):
        v = i / rings
        phi = v * math.pi
        for j in range(segments):
            u = j / segments
            theta = u * 2 * math.pi
            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)
            verts.append((x, y, z))
    for i in range(rings):
        for j in range(segments):
            a = i * segments + j
            b = i * segments + ((j + 1) % segments)
            c = (i + 1) * segments + ((j + 1) % segments)
            d = (i + 1) * segments + j
            if i == 0:
                faces.append((a, c, d))
            elif i == rings - 1:
                faces.append((a, b, d))
            else:
                faces.append((a, b, c, d))
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    if scale:
        obj.scale = scale
    link(obj, col)
    smooth(obj)
    return obj


def make_cylinder(name, radius, depth, location, col, vertices=24, rotation=None):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    verts = []
    faces = []
    half = depth * 0.5
    for i in range(vertices):
        a = (i / vertices) * 2 * math.pi
        verts.append((math.cos(a) * radius, math.sin(a) * radius, -half))
    for i in range(vertices):
        a = (i / vertices) * 2 * math.pi
        verts.append((math.cos(a) * radius, math.sin(a) * radius, half))
    # bottom/top caps
    for i in range(1, vertices - 1):
        faces.append((0, i, i + 1))
        faces.append((vertices, vertices + i + 1, vertices + i))
    # sides
    for i in range(vertices):
        j = (i + 1) % vertices
        faces.append((i, j, vertices + j, vertices + i))
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    if rotation:
        obj.rotation_euler = rotation
    link(obj, col)
    smooth(obj)
    return obj


def make_box(name, dims, location, col):
    sx, sy, sz = dims
    hx, hy, hz = sx * 0.5, sy * 0.5, sz * 0.5
    verts = [
        (-hx, -hy, -hz),
        (hx, -hy, -hz),
        (hx, hy, -hz),
        (-hx, hy, -hz),
        (-hx, -hy, hz),
        (hx, -hy, hz),
        (hx, hy, hz),
        (-hx, hy, hz),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 1, 5, 4),
        (1, 2, 6, 5),
        (2, 3, 7, 6),
        (3, 0, 4, 7),
    ]
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    link(obj, col)
    return obj


def make_plane(name, size, location, col, rotation=None):
    s = size * 0.5
    verts = [(-s, -s, 0), (s, -s, 0), (s, s, 0), (-s, s, 0)]
    faces = [(0, 1, 2, 3)]
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    if rotation:
        obj.rotation_euler = rotation
    link(obj, col)
    return obj


def build(mats):
    root = ensure_col("COL_HundredAcre_Item3")
    body = ensure_col("COL_Body", root)
    cloth = ensure_col("COL_Cloth", root)
    props = ensure_col("COL_Props", root)

    head = make_uv_sphere("SM_Char_Item3_Head", 0.118, (0, 0, 1.76), body)
    assign(head, mats["skin"])
    neck = make_cylinder("SM_Char_Item3_Neck", 0.048, 0.1, (0, 0, 1.62), body, 20)
    assign(neck, mats["skin"])

    hair = make_uv_sphere("SM_Char_Item3_Hair", 0.132, (0.0, 0.02, 1.80), body, 28, 14, scale=(1.1, 1.15, 0.75))
    assign(hair, mats["hair"])
    for i, (loc, sc) in enumerate(
        [
            ((0.08, -0.07, 1.72), (0.07, 0.055, 0.06)),
            ((-0.08, -0.07, 1.72), (0.07, 0.055, 0.06)),
            ((0.0, -0.1, 1.70), (0.09, 0.045, 0.05)),
            ((0.1, 0.05, 1.78), (0.06, 0.06, 0.05)),
            ((-0.1, 0.05, 1.78), (0.06, 0.06, 0.05)),
            ((0.0, 0.08, 1.82), (0.08, 0.05, 0.04)),
        ]
    ):
        lock = make_uv_sphere(f"SM_Char_Item3_HairLock_{i}", 1.0, loc, body, 16, 10, scale=sc)
        assign(lock, mats["hair"])

    sweater = make_box("SM_Char_Item3_Cloth_Sweater", (0.46, 0.28, 0.66), (0, 0, 1.26), cloth)
    assign(sweater, mats["mustard"])
    bevel(sweater, 0.035, 3)
    smooth(sweater)

    collar = make_cylinder("SM_Char_Item3_Cloth_Collar", 0.1, 0.07, (0, 0, 1.57), cloth, 28)
    assign(collar, mats["mustard"])
    hem = make_box("SM_Char_Item3_Cloth_Hem", (0.48, 0.30, 0.055), (0, 0, 0.93), cloth)
    assign(hem, mats["mustard"])
    bevel(hem, 0.01, 2)

    for side, sx in (("L", 0.28), ("R", -0.28)):
        sleeve = make_cylinder(
            f"SM_Char_Item3_Cloth_Sleeve_{side}",
            0.075,
            0.55,
            (sx, 0.04, 1.18),
            cloth,
            22,
            rotation=(math.radians(18), math.radians(6 if side == "L" else -6), 0),
        )
        assign(sleeve, mats["mustard"])
        cuff = make_cylinder(f"SM_Char_Item3_Cloth_Cuff_{side}", 0.058, 0.05, (sx * 1.05, 0.12, 0.92), cloth, 20)
        assign(cuff, mats["mustard"])
        hand = make_uv_sphere(f"SM_Char_Item3_Hand_{side}", 0.045, (sx * 0.95, 0.14, 0.86), body, 16, 10)
        assign(hand, mats["skin"])

    balloon = make_uv_sphere("SM_Prop_Balloon_Print", 0.055, (0.0, -0.145, 1.34), props, 24, 12, scale=(1.0, 0.35, 1.15))
    assign(balloon, mats["balloon"])
    highlight = make_uv_sphere("SM_Prop_Balloon_Highlight", 0.012, (-0.015, -0.155, 1.355), props, 12, 8)
    assign(highlight, mat("MAT_Balloon_Highlight", (0.95, 0.85, 0.85, 1.0), 0.25))
    string = make_cylinder(
        "SM_Prop_Balloon_String",
        0.0035,
        0.22,
        (0.0, -0.148, 1.20),
        props,
        8,
        rotation=(math.radians(6), 0, math.radians(4)),
    )
    assign(string, mats["string"])

    waist = make_box("SM_Char_Item3_Cloth_Waist", (0.44, 0.26, 0.11), (0, 0, 0.88), cloth)
    assign(waist, mats["grey"])
    bevel(waist, 0.015, 2)
    for side, sx in (("L", 0.105), ("R", -0.105)):
        pant = make_box(f"SM_Char_Item3_Cloth_Pant_{side}", (0.17, 0.21, 0.78), (sx, 0.0, 0.46), cloth)
        assign(pant, mats["grey"])
        bevel(pant, 0.02, 2)
        smooth(pant)
        crease = make_box(f"SM_Char_Item3_Cloth_Crease_{side}", (0.01, 0.008, 0.7), (sx, -0.105, 0.46), cloth)
        assign(crease, mats["grey"])
        pocket = make_box(f"SM_Char_Item3_Cloth_Pocket_{side}", (0.08, 0.02, 0.1), (sx * 1.4, -0.05, 0.82), cloth)
        assign(pocket, mats["grey"])

    for side, sx in (("L", 0.105), ("R", -0.105)):
        shaft = make_box(f"SM_Char_Item3_BootShaft_{side}", (0.14, 0.19, 0.22), (sx, 0.01, 0.13), cloth)
        assign(shaft, mats["boot"])
        bevel(shaft, 0.012, 2)
        toe = make_box(f"SM_Char_Item3_BootToe_{side}", (0.13, 0.16, 0.08), (sx, -0.08, 0.05), cloth)
        assign(toe, mats["boot"])
        bevel(toe, 0.01, 2)
        sole = make_box(f"SM_Char_Item3_BootSole_{side}", (0.15, 0.28, 0.04), (sx, -0.03, 0.02), cloth)
        assign(sole, mats["boot"])


def setup_cam_lights():
    cam_data = bpy.data.cameras.new("CAM_Item3_Hero")
    cam_data.lens = 70
    cam = bpy.data.objects.new("CAM_Item3_Hero", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (0.7, -5.4, 1.05)
    direction = Vector((0.0, 0.0, 0.95)) - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam

    for name, energy, size, loc, rot in [
        ("LGT_Key_Soft", 240, 3.5, (1.8, -2.2, 2.6), (math.radians(-48), math.radians(18), 0)),
        ("LGT_Fill", 70, 4.0, (-2.4, -1.0, 1.7), (0, 0, 0)),
        ("LGT_Rim", 45, 2.5, (0.3, 1.9, 2.1), (0, 0, 0)),
    ]:
        light = bpy.data.lights.new(name, type="AREA")
        light.energy = energy
        light.size = size
        obj = bpy.data.objects.new(name, light)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = loc
        obj.rotation_euler = rot

    world = bpy.data.worlds.new("World_Cream")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = COL_BG
    bg.inputs["Strength"].default_value = 0.4

    ground = make_plane("SM_Ground_Studio", 12.0, (0, 0, 0), bpy.context.scene.collection)
    assign(ground, mat("MAT_Ground_Cream", COL_BG, 0.92))
    back = make_plane("SM_Backdrop_Studio", 10.0, (0, 2.8, 1.6), bpy.context.scene.collection, rotation=(math.radians(90), 0, 0))
    assign(back, mat("MAT_Backdrop_Cream", COL_BG, 0.95))


def setup_render():
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = 96
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 900
    sc.render.resolution_y = 1400
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
    mats = {
        "mustard": mat("MAT_Knit_Sweater_Mustard", COL_MUSTARD, 0.78, sheen=0.45, bump=0.08),
        "grey": mat("MAT_Wool_Grey", COL_GREY, 0.74, sheen=0.12, bump=0.04),
        "boot": mat("MAT_Leather_Brown", COL_BOOT, 0.4, 0.08),
        "skin": mat("MAT_Skin_Soft", COL_SKIN, 0.52),
        "hair": mat("MAT_Hair_LightBrown", COL_HAIR, 0.58),
        "balloon": mat("MAT_Balloon_Red", COL_BALLOON, 0.28),
        "string": mat("MAT_String_Black", COL_STRING, 0.85),
    }
    build(mats)
    setup_cam_lights()
    setup_render()

    # Save via data API path
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    print("SAVED", BLEND)

    def do_render():
        bpy.ops.render.render(write_still=True)

    run_ops(do_render)
    print("RENDERED", RENDER, RENDER.exists(), RENDER.stat().st_size if RENDER.exists() else 0)


main()

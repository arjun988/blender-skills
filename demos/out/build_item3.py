"""
BRA-5 smoke: Hundred Acre Softness croquis — Item 3 look.

Mustard sweater + red balloon graphic, grey trousers, brown boots.
Skills-aligned: director brief → character-artist clothing → materials → render.
MCP unavailable in this agent session → bpy fallback.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import mathutils

OUT_DIR = Path(__file__).resolve().parent
BLEND_PATH = OUT_DIR / "SM_HundredAcre_Item3.blend"
RENDER_PATH = OUT_DIR / "hundred-acre-item3-smoke.png"

COL_MUSTARD = (0.82, 0.64, 0.26, 1.0)
COL_BALLOON = (0.88, 0.16, 0.14, 1.0)
COL_STRING = (0.04, 0.04, 0.04, 1.0)
COL_GREY = (0.40, 0.40, 0.43, 1.0)
COL_BOOT = (0.30, 0.17, 0.09, 1.0)
COL_SKIN = (0.88, 0.74, 0.64, 1.0)
COL_HAIR = (0.48, 0.34, 0.24, 1.0)
COL_BG = (0.95, 0.93, 0.89, 1.0)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for block in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.curves,
    ):
        for item in list(block):
            block.remove(item)


def ensure_collection(name: str, parent: bpy.types.Collection | None = None) -> bpy.types.Collection:
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(col)
    return col


def link_object(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    collection.objects.link(obj)


def make_mat(name: str, color, roughness: float = 0.65, metallic: float = 0.0, sheen: float = 0.0) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nodes = nt.nodes
    links = nt.links
    nodes.clear()
    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = sheen
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def assign_mat(obj: bpy.types.Object, mat: bpy.types.Material) -> None:
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def smooth(obj: bpy.types.Object) -> None:
    mesh = obj.data
    for poly in mesh.polygons:
        poly.use_smooth = True


def add_bevel(obj: bpy.types.Object, width: float = 0.01, segments: int = 2) -> None:
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.width = width
    mod.segments = segments
    mod.limit_method = "ANGLE"
    mod.angle_limit = math.radians(30)


def sphere(name, radius, loc, col, seg=24, rings=12):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=loc, segments=seg, ring_count=rings)
    obj = bpy.context.active_object
    obj.name = name
    link_object(obj, col)
    smooth(obj)
    return obj


def cylinder(name, radius, depth, loc, col, verts=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=radius, depth=depth, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    link_object(obj, col)
    smooth(obj)
    return obj


def cube(name, dims, loc, col):
    """dims = (sx, sy, sz) full size in meters."""
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = (dims[0], dims[1], dims[2])
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    link_object(obj, col)
    return obj


def build_figure(mats: dict) -> None:
    root = ensure_collection("COL_HundredAcre_Item3")
    body = ensure_collection("COL_Body", root)
    cloth = ensure_collection("COL_Cloth", root)
    props = ensure_collection("COL_Props", root)

    # --- Head / hair (visible) ---
    head = sphere("SM_Char_Item3_Head", 0.115, (0, 0, 1.74), body, 32, 16)
    assign_mat(head, mats["skin"])

    neck = cylinder("SM_Char_Item3_Neck", 0.045, 0.09, (0, 0, 1.60), body, 16)
    assign_mat(neck, mats["skin"])

    # Soft wavy hair mass (no hat look)
    hair_main = sphere("SM_Char_Item3_Hair", 0.13, (0, 0.01, 1.78), body, 28, 14)
    hair_main.scale = (1.08, 1.12, 0.78)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign_mat(hair_main, mats["hair"])
    for i, (off, sc) in enumerate(
        [
            ((0.07, -0.06, 1.70), (0.08, 0.06, 0.07)),
            ((-0.07, -0.06, 1.70), (0.08, 0.06, 0.07)),
            ((0.0, -0.09, 1.68), (0.1, 0.05, 0.05)),
            ((0.09, 0.04, 1.76), (0.07, 0.07, 0.06)),
            ((-0.09, 0.04, 1.76), (0.07, 0.07, 0.06)),
        ]
    ):
        lock = sphere(f"SM_Char_Item3_HairLock_{i}", 1.0, off, body, 16, 10)
        lock.scale = sc
        bpy.context.view_layer.objects.active = lock
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        assign_mat(lock, mats["hair"])

    # Hands only (rest covered by clothes)
    for side, sx in (("L", 0.30), ("R", -0.30)):
        hand = sphere(f"SM_Char_Item3_Hand_{side}", 0.048, (sx, 0.06, 0.80), body, 16, 10)
        assign_mat(hand, mats["skin"])

    # --- Mustard sweater (oversized so it reads clearly) ---
    sweater = cube("SM_Char_Item3_Cloth_Sweater", (0.48, 0.30, 0.68), (0, 0, 1.24), cloth)
    assign_mat(sweater, mats["mustard"])
    add_bevel(sweater, 0.03, 3)
    smooth(sweater)

    collar = cylinder("SM_Char_Item3_Cloth_Collar", 0.095, 0.07, (0, 0, 1.55), cloth, 24)
    assign_mat(collar, mats["mustard"])

    # Arms hang down along body (croquis rest pose)
    for side, sx in (("L", 0.30), ("R", -0.30)):
        sleeve = cylinder(f"SM_Char_Item3_Cloth_Sleeve_{side}", 0.08, 0.62, (sx, 0.0, 1.15), cloth, 20)
        sleeve.rotation_euler = (math.radians(8), 0, 0)
        assign_mat(sleeve, mats["mustard"])
        cuff = cylinder(f"SM_Char_Item3_Cloth_Cuff_{side}", 0.062, 0.05, (sx, 0.04, 0.86), cloth, 20)
        assign_mat(cuff, mats["mustard"])

    hem = cube("SM_Char_Item3_Cloth_Hem", (0.50, 0.32, 0.06), (0, 0, 0.90), cloth)
    assign_mat(hem, mats["mustard"])
    add_bevel(hem, 0.01, 2)

    # Red balloon chest graphic (sits on sweater front)
    balloon = sphere("SM_Prop_Balloon_Chest", 0.06, (0.0, -0.16, 1.34), props, 24, 12)
    assign_mat(balloon, mats["balloon"])
    string = cylinder("SM_Prop_Balloon_String", 0.004, 0.2, (-0.01, -0.165, 1.22), props, 8)
    string.rotation_euler = (math.radians(8), math.radians(12), math.radians(20))
    assign_mat(string, mats["string"])

    # --- Grey trousers (box legs — avoid subdiv star artifacts) ---
    waist = cube("SM_Char_Item3_Cloth_Waist", (0.46, 0.28, 0.12), (0, 0, 0.86), cloth)
    assign_mat(waist, mats["grey"])
    add_bevel(waist, 0.015, 2)

    for side, sx in (("L", 0.11), ("R", -0.11)):
        pant = cube(f"SM_Char_Item3_Cloth_Pant_{side}", (0.18, 0.22, 0.78), (sx, 0.0, 0.44), cloth)
        assign_mat(pant, mats["grey"])
        add_bevel(pant, 0.02, 2)
        smooth(pant)
        # Front crease strip
        crease = cube(f"SM_Char_Item3_Cloth_Crease_{side}", (0.012, 0.01, 0.72), (sx, -0.11, 0.44), cloth)
        assign_mat(crease, mats["grey"])

    # --- Brown boots ---
    for side, sx in (("L", 0.11), ("R", -0.11)):
        shaft = cube(f"SM_Char_Item3_BootShaft_{side}", (0.15, 0.20, 0.20), (sx, 0.01, 0.12), cloth)
        assign_mat(shaft, mats["boot"])
        add_bevel(shaft, 0.015, 2)
        sole = cube(f"SM_Char_Item3_BootSole_{side}", (0.16, 0.30, 0.05), (sx, -0.04, 0.025), cloth)
        assign_mat(sole, mats["boot"])
        add_bevel(sole, 0.01, 2)


def setup_camera_lights() -> None:
    cam_data = bpy.data.cameras.new("CAM_Item3_Hero")
    cam_data.lens = 70
    cam = bpy.data.objects.new("CAM_Item3_Hero", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    # Full-figure croquis framing: head to boots with margin
    cam.location = (0.65, -5.6, 1.0)
    direction = mathutils.Vector((0.0, 0.0, 0.9)) - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam

    key = bpy.data.lights.new("LGT_Key_Soft", type="AREA")
    key.energy = 220
    key.size = 3.5
    key_obj = bpy.data.objects.new("LGT_Key_Soft", key)
    bpy.context.scene.collection.objects.link(key_obj)
    key_obj.location = (1.6, -2.0, 2.5)
    key_obj.rotation_euler = (math.radians(-45), math.radians(15), 0)

    fill = bpy.data.lights.new("LGT_Fill", type="AREA")
    fill.energy = 80
    fill.size = 4.0
    fill_obj = bpy.data.objects.new("LGT_Fill", fill)
    bpy.context.scene.collection.objects.link(fill_obj)
    fill_obj.location = (-2.2, -1.2, 1.6)

    rim = bpy.data.lights.new("LGT_Rim", type="AREA")
    rim.energy = 50
    rim.size = 2.5
    rim_obj = bpy.data.objects.new("LGT_Rim", rim)
    bpy.context.scene.collection.objects.link(rim_obj)
    rim_obj.location = (0.2, 1.8, 2.2)

    world = bpy.data.worlds.new("World_Cream")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = COL_BG
    bg.inputs["Strength"].default_value = 0.45

    bpy.ops.mesh.primitive_plane_add(size=10.0, location=(0, 0, 0))
    ground = bpy.context.active_object
    ground.name = "SM_Ground_Studio"
    assign_mat(ground, make_mat("MAT_Ground_Cream", COL_BG, 0.92))

    # Soft backdrop plane
    bpy.ops.mesh.primitive_plane_add(size=8.0, location=(0, 2.5, 1.5))
    back = bpy.context.active_object
    back.name = "SM_Backdrop_Studio"
    back.rotation_euler = (math.radians(90), 0, 0)
    assign_mat(back, make_mat("MAT_Backdrop_Cream", COL_BG, 0.95))


def setup_render() -> None:
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 128
    scene.cycles.use_denoising = True
    scene.render.resolution_x = 900
    scene.render.resolution_y = 1400
    scene.render.filepath = str(RENDER_PATH)
    scene.render.image_settings.file_format = "PNG"
    prefs = bpy.context.preferences.addons.get("cycles")
    if prefs is not None:
        try:
            prefs.preferences.compute_device_type = "METAL"
            for device in prefs.preferences.devices:
                device.use = True
        except Exception:
            pass


def main() -> None:
    clear_scene()
    mats = {
        "mustard": make_mat("MAT_Knit_Sweater_Mustard", COL_MUSTARD, 0.78, sheen=0.4),
        "grey": make_mat("MAT_Wool_Grey", COL_GREY, 0.72, sheen=0.15),
        "boot": make_mat("MAT_Leather_Brown", COL_BOOT, 0.42, 0.05),
        "skin": make_mat("MAT_Skin_Soft", COL_SKIN, 0.55),
        "hair": make_mat("MAT_Hair_LightBrown", COL_HAIR, 0.58),
        "balloon": make_mat("MAT_Balloon_Red", COL_BALLOON, 0.32),
        "string": make_mat("MAT_String_Black", COL_STRING, 0.85),
    }
    build_figure(mats)
    setup_camera_lights()
    setup_render()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    print(f"Saved blend: {BLEND_PATH}")
    bpy.ops.render.render(write_still=True)
    print(f"Saved render: {RENDER_PATH} exists={RENDER_PATH.exists()} size={RENDER_PATH.stat().st_size}")


if __name__ == "__main__":
    main()

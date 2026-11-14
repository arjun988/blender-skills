"""BRA-12 realistic Item 3 — Clawd artifact quality canon + Poly Haven fabrics via MCP."""

from __future__ import annotations

import math
from pathlib import Path

import bpy
import bmesh
from mathutils import Vector

OUT = Path("/Users/jongarcia/Documents/Development/platforms/blender-skills/demos/out")
ASSETS = OUT / "assets"
BLEND = OUT / "SM_HundredAcre_Item3_Realistic.blend"
RENDER = OUT / "hundred-acre-item3-realistic.png"
BALLOON_TEX = ASSETS / "balloon_graphic.png"

KEEP_MATS = {
    "knitted_fleece",
    "poly_wool_herringbone",
    "cotton_jersey",
    "denim_fabric",
    "grey_plaster_02",
    "concrete_floor_01",
}


def view3d_override():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type != "VIEW_3D":
                continue
            for region in area.regions:
                if region.type == "WINDOW":
                    return {
                        "window": window,
                        "screen": window.screen,
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


def clear_scene():
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
    # Keep Poly Haven mats; drop old procedural ones
    for m in list(bpy.data.materials):
        if m.name not in KEEP_MATS:
            bpy.data.materials.remove(m)


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


def activate(obj):
    bpy.context.view_layer.objects.active = obj
    for o in bpy.context.view_layer.objects:
        o.select_set(o == obj)


def apply_mods(obj):
    activate(obj)

    def _do():
        for mod in list(obj.modifiers):
            try:
                bpy.ops.object.modifier_apply(modifier=mod.name)
            except Exception as e:
                print("mod fail", mod.name, e)

    run_ops(_do)


def shade_smooth(obj):
    for p in obj.data.polygons:
        p.use_smooth = True


def add_subdiv(obj, levels=2):
    m = obj.modifiers.new("Subdivision", "SUBSURF")
    m.levels = levels
    m.render_levels = max(levels, 3)


def add_bevel(obj, width=0.0015, segments=3):
    """Clawd canon: bevel edges ~mm scale on human garments."""
    m = obj.modifiers.new("Bevel", "BEVEL")
    m.width = width
    m.segments = segments
    m.limit_method = "ANGLE"
    m.angle_limit = math.radians(30)


def assign(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


def tint_ph_material(src_name, new_name, tint, strength=0.72):
    """Copy Poly Haven mat and multiply albedo toward fashion color."""
    src = bpy.data.materials.get(src_name)
    if src is None:
        raise RuntimeError(f"missing material {src_name}")
    m = src.copy()
    m.name = new_name
    nt = m.node_tree
    # Find principled + diffuse image
    bsdf = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf is None:
        return m
    # Insert mix RGB / mix color after whatever feeds Base Color
    base_in = bsdf.inputs["Base Color"]
    from_node = None
    from_socket = None
    if base_in.links:
        link = base_in.links[0]
        from_node = link.from_node
        from_socket = link.from_socket
        nt.links.remove(link)
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs["Factor"].default_value = strength
    mix.inputs["B"].default_value = (*tint, 1.0)
    mix.location = (bsdf.location.x - 200, bsdf.location.y)
    if from_socket is not None:
        try:
            nt.links.new(from_socket, mix.inputs["A"])
        except Exception:
            mix.inputs["A"].default_value = (0.8, 0.8, 0.8, 1)
    else:
        mix.inputs["A"].default_value = (0.8, 0.8, 0.8, 1)
    try:
        nt.links.new(mix.outputs["Result"], bsdf.inputs["Base Color"])
    except Exception:
        nt.links.new(mix.outputs[0], bsdf.inputs["Base Color"])
    # Clawd-like coat/sheen on knit
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.15
        if "Coat Roughness" in bsdf.inputs:
            bsdf.inputs["Coat Roughness"].default_value = 0.35
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.45
    return m


def mat_skin():
    m = bpy.data.materials.new("MAT_Skin_Realistic")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.84, 0.66, 0.52, 1)
    bsdf.inputs["Roughness"].default_value = 0.45
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.25
        if "Subsurface Radius" in bsdf.inputs:
            bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.2, 0.1)
        if "Subsurface Scale" in bsdf.inputs:
            bsdf.inputs["Subsurface Scale"].default_value = 0.25
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 140
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.035
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def mat_leather():
    m = bpy.data.materials.new("MAT_Leather_Boot_Brown")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.26, 0.14, 0.07, 1)
    bsdf.inputs["Roughness"].default_value = 0.42
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.2
        bsdf.inputs["Coat Roughness"].default_value = 0.3
    noise = n.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 80
    noise.inputs["Detail"].default_value = 12
    bump = n.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.22
    l.new(noise.outputs["Fac"], bump.inputs["Height"])
    l.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def mat_hair():
    m = bpy.data.materials.new("MAT_Hair_Realistic")
    m.use_nodes = True
    nt = m.node_tree
    n, l = nt.nodes, nt.links
    n.clear()
    out = n.new("ShaderNodeOutputMaterial")
    bsdf = n.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (0.25, 0.16, 0.10, 1)
    bsdf.inputs["Roughness"].default_value = 0.32
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.25
    l.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return m


def add_balloon_decal(sweater_mat):
    if not BALLOON_TEX.exists():
        return
    nt = sweater_mat.node_tree
    bsdf = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf is None:
        return
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(str(BALLOON_TEX))
    mapping = nt.nodes.new("ShaderNodeMapping")
    mapping.inputs["Location"].default_value = (0.32, 0.12, 0)
    mapping.inputs["Scale"].default_value = (2.4, 3.0, 1)
    coord = nt.nodes.new("ShaderNodeTexCoord")
    nt.links.new(coord.outputs["Generated"], mapping.inputs["Vector"])
    nt.links.new(mapping.outputs["Vector"], tex.inputs["Vector"])
    # Mix over existing base color
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    base_in = bsdf.inputs["Base Color"]
    if base_in.links:
        prev = base_in.links[0]
        nt.links.new(prev.from_socket, mix.inputs["A"])
        nt.links.remove(prev)
    mix.inputs["Factor"].default_value = 0.0
    try:
        nt.links.new(tex.outputs["Alpha"], mix.inputs["Factor"])
        nt.links.new(tex.outputs["Color"], mix.inputs["B"])
        nt.links.new(mix.outputs["Result"], bsdf.inputs["Base Color"])
    except Exception as e:
        print("balloon decal fail", e)


def add_mball(mball, co, r, stiff=2.0):
    el = mball.elements.new()
    el.co = co
    el.radius = r
    el.stiffness = stiff


def build_body(col):
    mball = bpy.data.metaballs.new("MB_Body")
    mball.resolution = 0.05
    mball.render_resolution = 0.035
    obj = bpy.data.objects.new("SM_Char_Item3_Body_Meta", mball)
    link(obj, col)
    # ~1.82 m adult male, slight walk (L forward), hands near pockets
    add_mball(mball, (0, 0, 1.70), 0.125, 2.3)
    add_mball(mball, (0, 0, 1.55), 0.055, 2.1)
    add_mball(mball, (0, 0.02, 1.38), 0.195, 2.0)
    add_mball(mball, (0, 0.0, 1.18), 0.165, 2.0)
    add_mball(mball, (0, 0.0, 1.00), 0.175, 2.0)
    add_mball(mball, (0.20, 0.0, 1.45), 0.095, 2.0)
    add_mball(mball, (-0.20, 0.0, 1.45), 0.095, 2.0)
    add_mball(mball, (0.28, 0.05, 1.28), 0.07, 2.0)
    add_mball(mball, (-0.28, 0.05, 1.28), 0.07, 2.0)
    add_mball(mball, (0.30, 0.10, 1.08), 0.06, 2.0)
    add_mball(mball, (-0.30, 0.10, 1.08), 0.06, 2.0)
    add_mball(mball, (0.20, 0.12, 0.94), 0.05, 2.0)
    add_mball(mball, (-0.20, 0.12, 0.94), 0.05, 2.0)
    add_mball(mball, (0.15, 0.08, 0.88), 0.048, 2.0)
    add_mball(mball, (-0.15, 0.08, 0.88), 0.048, 2.0)
    add_mball(mball, (0.10, -0.06, 0.72), 0.095, 2.0)
    add_mball(mball, (-0.10, 0.04, 0.72), 0.095, 2.0)
    add_mball(mball, (0.11, -0.10, 0.48), 0.08, 2.0)
    add_mball(mball, (-0.11, 0.06, 0.48), 0.08, 2.0)
    add_mball(mball, (0.11, -0.12, 0.26), 0.065, 2.0)
    add_mball(mball, (-0.11, 0.05, 0.26), 0.065, 2.0)
    add_mball(mball, (0.11, -0.18, 0.06), 0.055, 2.0)
    add_mball(mball, (-0.11, 0.0, 0.06), 0.055, 2.0)

    activate(obj)
    run_ops(lambda: bpy.ops.object.convert(target="MESH"))
    body = bpy.context.view_layer.objects.active
    body.name = "SM_Char_Item3_Body"
    rem = body.modifiers.new("Remesh", "REMESH")
    rem.mode = "VOXEL"
    rem.voxel_size = 0.016
    apply_mods(body)
    add_bevel(body, 0.0012, 3)
    add_subdiv(body, 1)
    shade_smooth(body)
    return body


def ico(name, radius, loc, col, scale=None):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2, radius=radius)
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    if scale:
        obj.scale = scale
    link(obj, col)
    shade_smooth(obj)
    return obj


def face_and_hair(body_col, hair_col, skin, hair_mat):
    nose = ico("SM_Char_Item3_Nose", 0.024, (0, -0.125, 1.68), body_col, (0.7, 1.25, 0.9))
    assign(nose, skin)
    add_subdiv(nose, 2)
    for sx, side in ((0.12, "L"), (-0.12, "R")):
        ear = ico(f"SM_Char_Item3_Ear_{side}", 0.034, (sx, 0.0, 1.70), body_col, (0.35, 0.7, 1.0))
        assign(ear, skin)
        add_subdiv(ear, 2)
    eye_m = skin.copy()
    eye_m.name = "MAT_Skin_Eye"
    bsdf = next(n for n in eye_m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0.5, 0.36, 0.28, 1)
    for sx, side in ((0.035, "L"), (-0.035, "R")):
        eye = ico(f"SM_Char_Item3_Eye_{side}", 0.017, (sx, -0.112, 1.72), body_col)
        assign(eye, eye_m)
    lip_m = skin.copy()
    lip_m.name = "MAT_Skin_Lip"
    bsdf = next(n for n in lip_m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0.72, 0.38, 0.36, 1)
    lip = ico("SM_Char_Item3_Mouth", 0.028, (0, -0.118, 1.62), body_col, (1.35, 0.4, 0.35))
    assign(lip, lip_m)

    scalp = ico("SM_Char_Item3_HairCap", 0.135, (0, 0.015, 1.74), hair_col, (1.05, 1.12, 0.82))
    assign(scalp, hair_mat)
    add_subdiv(scalp, 2)
    for i, (loc, sc) in enumerate(
        [
            ((0.07, -0.09, 1.67), (0.08, 0.055, 0.07)),
            ((-0.07, -0.09, 1.67), (0.08, 0.055, 0.07)),
            ((0.0, -0.11, 1.65), (0.1, 0.05, 0.06)),
            ((0.1, 0.04, 1.76), (0.07, 0.07, 0.055)),
            ((-0.1, 0.04, 1.76), (0.07, 0.07, 0.055)),
            ((0.0, 0.09, 1.80), (0.09, 0.06, 0.05)),
            ((0.06, -0.02, 1.78), (0.06, 0.06, 0.05)),
            ((-0.06, -0.02, 1.78), (0.06, 0.06, 0.05)),
        ]
    ):
        lock = ico(f"SM_Char_Item3_HairLock_{i}", 1.0, loc, hair_col, sc)
        assign(lock, hair_mat)
        add_subdiv(lock, 2)


def crop_z(obj, zmin, zmax):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.verts.ensure_lookup_table()
    kill = [v for v in bm.verts if not (zmin <= (obj.matrix_world @ v.co).z <= zmax)]
    if kill:
        bmesh.ops.delete(bm, geom=kill, context="VERTS")
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()


def shell(body, name, col, thickness=0.022, voxel=0.018):
    obj = bpy.data.objects.new(name, body.data.copy())
    link(obj, col)
    sol = obj.modifiers.new("Solidify", "SOLIDIFY")
    sol.thickness = thickness
    sol.offset = 1.0
    rem = obj.modifiers.new("Remesh", "REMESH")
    rem.mode = "VOXEL"
    rem.voxel_size = voxel
    add_bevel(obj, 0.0015, 3)
    shade_smooth(obj)
    return obj


def boot(name, loc, col, leather):
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= 0.125
        v.co.y *= 0.16
        v.co.z *= 0.22
        v.co.z += 0.14
    ret = bmesh.ops.create_cube(bm, size=1.0)
    for v in ret["verts"]:
        v.co.x *= 0.12
        v.co.y *= 0.18
        v.co.z *= 0.075
        v.co.y -= 0.12
        v.co.z += 0.05
    ret = bmesh.ops.create_cube(bm, size=1.0)
    for v in ret["verts"]:
        v.co.x *= 0.135
        v.co.y *= 0.26
        v.co.z *= 0.03
        v.co.y -= 0.04
        v.co.z += 0.015
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    link(obj, col)
    rem = obj.modifiers.new("Remesh", "REMESH")
    rem.mode = "VOXEL"
    rem.voxel_size = 0.01
    apply_mods(obj)
    add_bevel(obj, 0.0012, 3)
    add_subdiv(obj, 2)
    shade_smooth(obj)
    assign(obj, leather)
    return obj


def clothes(body, cloth_col, sweater_mat, pants_mat, leather):
    sweater = shell(body, "SM_Char_Item3_Cloth_Sweater", cloth_col, 0.024, 0.018)
    crop_z(sweater, 0.90, 1.58)
    assign(sweater, sweater_mat)
    apply_mods(sweater)
    add_subdiv(sweater, 2)

    pants = shell(body, "SM_Char_Item3_Cloth_Pants", cloth_col, 0.02, 0.018)
    crop_z(pants, 0.04, 1.02)
    assign(pants, pants_mat)
    apply_mods(pants)
    add_subdiv(pants, 2)

    boot("SM_Char_Item3_Boot_L", (0.11, -0.12, 0.0), cloth_col, leather)
    boot("SM_Char_Item3_Boot_R", (-0.11, 0.02, 0.0), cloth_col, leather)


def setup_studio_clawd():
    """Camera/light from Fable of Clawd canon, adapted to human portrait scale."""
    cam_data = bpy.data.cameras.new("CAM_Item3_Hero")
    cam_data.sensor_width = 36.0  # Clawd canon
    cam_data.lens = 70.0
    cam_data.dof.use_dof = True
    cam_data.dof.aperture_fstop = 4.0
    cam_data.dof.aperture_blades = 0
    cam_data.clip_start = 0.05
    cam_data.clip_end = 400
    cam = bpy.data.objects.new("CAM_Item3_Hero", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (0.9, -4.6, 1.2)
    target = Vector((0.0, 0.0, 1.05))
    cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam_data.dof.focus_distance = (cam.location - target).length
    bpy.context.scene.camera = cam

    # One honest key + cooler fill/rim (Clawd: hero against cooler/darker)
    key = bpy.data.lights.new("LGT_Key", type="AREA")
    key.energy = 450
    key.size = 2.4
    key.color = (1.0, 0.97, 0.92)
    key_o = bpy.data.objects.new("LGT_Key", key)
    bpy.context.scene.collection.objects.link(key_o)
    key_o.location = (2.2, -2.4, 2.9)
    key_o.rotation_euler = (math.radians(-52), math.radians(22), 0)

    fill = bpy.data.lights.new("LGT_Fill", type="AREA")
    fill.energy = 70
    fill.size = 4.0
    fill.color = (0.75, 0.82, 0.95)  # cooler
    fill_o = bpy.data.objects.new("LGT_Fill", fill)
    bpy.context.scene.collection.objects.link(fill_o)
    fill_o.location = (-2.6, -1.0, 1.7)

    rim = bpy.data.lights.new("LGT_Rim", type="AREA")
    rim.energy = 140
    rim.size = 1.8
    rim_o = bpy.data.objects.new("LGT_Rim", rim)
    bpy.context.scene.collection.objects.link(rim_o)
    rim_o.location = (0.3, 2.3, 2.3)

    world = bpy.data.worlds.new("World_Studio")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.55, 0.58, 0.62, 1)  # cooler than subject
    bg.inputs["Strength"].default_value = 0.25

    # Ground / backdrop with Poly Haven if present
    def grid(name, size, loc, rot=None):
        mesh = bpy.data.meshes.new(name + "_Mesh")
        bm = bmesh.new()
        bmesh.ops.create_grid(bm, x_segments=4, y_segments=4, size=size * 0.5)
        bm.to_mesh(mesh)
        bm.free()
        obj = bpy.data.objects.new(name, mesh)
        obj.location = loc
        if rot:
            obj.rotation_euler = rot
        bpy.context.scene.collection.objects.link(obj)
        return obj

    g = grid("SM_Ground", 8, (0, 0, 0))
    b = grid("SM_Backdrop", 8, (0, 3.2, 2.0), (math.radians(90), 0, 0))
    floor = bpy.data.materials.get("concrete_floor_01")
    wall = bpy.data.materials.get("grey_plaster_02")
    if floor:
        assign(g, floor)
    if wall:
        assign(b, wall)


def setup_render_clawd(samples=160):
    """Exact recipe adapted from artifact Python (portrait still, not 4K film)."""
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.render.resolution_x = 1080
    sc.render.resolution_y = 1600
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
    clear_scene()
    root = ensure_col("COL_HundredAcre_Item3")
    body_col = ensure_col("COL_Body", root)
    cloth_col = ensure_col("COL_Cloth", root)
    hair_col = ensure_col("COL_Hair", root)

    # Fashion tints on Poly Haven scans (Clawd: scanned materials)
    sweater = tint_ph_material("knitted_fleece", "MAT_Knit_Mustard_PH", (0.82, 0.58, 0.22), 0.78)
    add_balloon_decal(sweater)
    pants = tint_ph_material("poly_wool_herringbone", "MAT_Wool_Grey_PH", (0.30, 0.30, 0.33), 0.65)
    skin = mat_skin()
    hair = mat_hair()
    leather = mat_leather()

    body = build_body(body_col)
    assign(body, skin)
    face_and_hair(body_col, hair_col, skin, hair)
    clothes(body, cloth_col, sweater, pants, leather)
    setup_studio_clawd()
    setup_render_clawd(160)

    run_ops(lambda: bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)))
    print("SAVED", BLEND)
    run_ops(lambda: bpy.ops.render.render(write_still=True))
    print("RENDERED", RENDER, RENDER.exists(), RENDER.stat().st_size if RENDER.exists() else 0)


main()

# BlenderMCP Tool Catalog

Reference for agents when Blender MCP (`blender-mcp` by ahujasid) is connected.

**Always read tool schemas from MCP before calling** — tool names may vary by version.

## Core Capabilities

| Category | Typical Operations |
|----------|-------------------|
| Scene inspection | List objects, get scene info, viewport screenshot |
| Object creation | Primitives, meshes, curves, empties |
| Object modification | Transform, rename, delete, duplicate |
| Materials | Create, assign, set PBR parameters |
| Code execution | Run `bpy` Python in Blender context |
| Assets | Poly Haven HDRIs/textures/models (if enabled) |
| Generation | Hyper3D / Hunyuan3D (if API keys configured) |

## Agent Protocol

```
1. Verify MCP connection (scene query)
2. Create collection hierarchy (COL_ prefix)
3. Execute operations incrementally
4. Query state after each phase
5. Screenshot viewport for validation
6. Run validation checklist before export
```

## Scene Inspection (Run First)

Before any edit, query current state:

- Object names and types
- Polygon counts
- Active collection
- Material assignments
- Selection state

Prevents assumptions about empty vs populated scenes.

## Object Operations via MCP

Prefer MCP tools over `execute_blender_code` when dedicated tools exist.

Use `execute_blender_code` for:
- Modifier stack operations
- UV editing
- Batch rename/cleanup
- Export operations not covered by dedicated tools

**Always save `.blend` before code execution.**

## Common bpy Patterns (Fallback)

### Create Collection

```python
import bpy
col = bpy.data.collections.new("COL_Props")
bpy.context.scene.collection.children.link(col)
```

### Rename Object

```python
obj.name = "SM_Crate_01"
obj.data.name = "SM_Crate_01"
```

### Apply Transforms

```python
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
```

### Merge by Distance

```python
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.0001)
bpy.ops.object.mode_set(mode='OBJECT')
```

## Poly Haven Integration

When enabled in Blender addon:
- Search and import HDRIs for lighting
- Download PBR textures
- Import free 3D models

Use for rapid look-dev; verify license (CC0) for shipping assets.

## Viewport Screenshots

Request viewport captures to validate:
- Silhouette at gameplay angle
- Material appearance
- Lighting mood
- Scale vs reference object

## Export via Code (When No Export Tool)

```python
import bpy
bpy.ops.export_scene.fbx(
    filepath="C:/export/SM_Asset.fbx",
    use_selection=True,
    apply_scale_options='FBX_SCALE_ALL',
    axis_forward='-Z',
    axis_up='Y',
    object_types={'MESH', 'ARMATURE'},
    bake_anim=False
)
```

Adjust axis settings per target engine — see `export-pipeline` skill.

## Error Recovery

| Error | Action |
|-------|--------|
| Connection lost | Reconnect addon in Blender |
| Timeout | Break operation into smaller steps |
| Object not found | Re-query scene; verify name |
| Code execution error | Read traceback; fix; retry |

## Version Note

BlenderMCP evolves frequently. Tool names and parameters may differ from this reference. **MCP tool descriptors are authoritative.**

Source: [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)

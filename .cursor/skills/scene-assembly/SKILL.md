---
name: scene-assembly
description: Large scene layout in Blender with collections, linking, overrides, streaming-friendly organization, and set assembly via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: scene assembly, layout, linking, library override, collection instance, level layout, set assembly, outliner organization
  related-skills: environment-artist, set-dressing, blender-modeler, lighting, qa-review
---

# Scene Assembly

Layouts that scale. Clear collections. Linking/overrides for big sets.

## When to Use

- Levels, dioramas, cinematic sets
- Assembling modular kits into spaces
- Library linking / collection instances
- Outliner structure for team scenes

## Workflow

```
Block layout (greybox) → Modular assemble → Set dressing
  → Lighting volumes → Cameras → QA pass → Optimize visibility
```

## Collection Structure

```
COL_Layout
COL_Modular_Geo
COL_SetDressing
COL_Lights
COL_Cameras
COL_FX
COL_Collision
COL_Trash / COL_Ref
```

## Linking Strategy

| Approach | When |
|----------|------|
| Collection instance | Repeated modular pieces |
| Library link + override | Shared hero assets across scenes |
| Append | One-off ownership transfer |

Prefer non-destructive linking for repeated kits.

## Layout Rules

1. Greybox scale and navigation first
2. Snap to grid for modular kits
3. Hide heavy collections while dressing
4. Keep world origin meaningful (level zero)

## Performance Hygiene

- Instance repeated meshes
- Cull unseen interiors
- Separate streaming volumes if game-oriented
- Avoid unique high materials on every duplicate

## Handoff

- Dressing → `set-dressing`
- Mood → `lighting` + style skill
- Gate → `qa-review`

## Constraints

### MUST DO
- Establish collection hierarchy early
- Greybox before final dressing
- Name cameras and light groups

### MUST NOT DO
- Dump everything in Scene Collection
- Apply library overrides casually without need
- Duplicate hero meshes instead of instancing


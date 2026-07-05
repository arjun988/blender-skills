# Blender Skills Guide

Decision trees and workflow combinations for the AAA Blender Skills Pack.

## Start Here

For any Blender asset task, **blender-director** analyzes the request and routes to specialist skills. You can also invoke skills directly.

## Skill Index

### Orchestration
- **blender-director** — Pipeline planning, skill routing, production briefs

### Modeling Disciplines
- **blender-modeler** — General modeling, scene organization, modifiers
- **hard-surface** — Sci-fi, weapons, vehicles, mechanical
- **environment-artist** — Modular kits, terrain, architecture
- **character-artist** — Human anatomy, clothing, facial topology
- **creature-artist** — Monsters, fantasy, organic design

### Production Workflow
- **sculpting** — High-frequency detail, multires, alphas
- **retopology** — Animation-ready topology, quad flow
- **uv-workflow** — Seams, packing, texel density, UDIM
- **materials** — PBR, procedural, master materials
- **texture-workflow** — Baking, atlases, ORM packing

### Technical
- **geometry-nodes** — Scatter, procedural systems, node groups
- **lighting** — Cinematic, horror, HDRI, volumetrics
- **rendering** — Cycles/Eevee, passes, color management
- **animation** — Locomotion, mechanical, NLA export
- **rigging** — IK/FK, weights, mechanical constraints

### Pipeline
- **procedural-modeling** — Rocks, roads, buildings, cables
- **asset-optimization** — Polycount, LODs, validation gate
- **export-pipeline** — FBX/GLTF/USD, engine import

### Style Specialists
- **horror-style** — Psychological horror, industrial decay
- **lowpoly-style** — PS1/PS2, Lethal Company aesthetic
- **stylized-style** — NPR, hand-painted, shape language
- **realistic-style** — AAA PBR, photogrammetry, cinematic

## Decision Trees

### What are you making?

```
Hard surface prop/vehicle/weapon → hard-surface
Environment/level geo → environment-artist
Human character → character-artist
Creature/monster → creature-artist
Procedural system → geometry-nodes + procedural-modeling
```

### What style?

```
Horror → horror-style (+ lighting)
Retro/low poly → lowpoly-style
Cartoon/NPR → stylized-style
Photoreal/AAA → realistic-style
Unspecified → blender-director decides from context
```

### Pipeline stage?

```
Starting fresh → blender-director → modeling skill
Sculpt done → retopology
Topology done → uv-workflow → materials/texture-workflow
Look dev → lighting → rendering
Ready to ship → asset-optimization → export-pipeline
```

## Workflow Combinations

### Hero Hard Surface Prop
```
blender-director → hard-surface → uv-workflow → materials
→ asset-optimization → export-pipeline
```

### Game Character
```
blender-director → character-artist → sculpting → retopology
→ uv-workflow → texture-workflow → rigging → animation → export-pipeline
```

### Horror Environment
```
blender-director → horror-style → environment-artist → lighting
→ lowpoly-style → asset-optimization → export-pipeline
```

### Modular Environment Kit
```
blender-director → environment-artist → geometry-nodes
→ uv-workflow → texture-workflow → asset-optimization → export-pipeline
```

### Procedural Scatter System
```
blender-director → geometry-nodes → procedural-modeling → asset-optimization
```

### Cinematic Render
```
blender-director → [modeling skill] → materials → lighting → rendering
```

## Shared References

| Reference | Path |
|-----------|------|
| Universal Pipeline | `.claude/skills/references/asset-pipeline.md` |
| MCP Integration | `.claude/skills/references/mcp-integration.md` |
| Naming Conventions | `.claude/skills/references/naming-conventions.md` |
| Validation Checklist | `.claude/skills/references/validation-checklist.md` |
| Polycount Budgets | `.claude/skills/references/polycount-budgets.md` |

## Naming Quick Reference

| Type | Prefix |
|------|--------|
| Collections | `COL_` |
| Meshes | `SM_` |
| Materials | `MAT_` |
| Textures | `T_` |
| Animations | `AN_` |
| Armatures | `ARM_` |
| Geo Node Groups | `GN_` |
| Cameras | `CAM_` |
| Lights | `LGT_` |

## Good Prompts

- "Plan and create a game-ready sci-fi crate for Unity, 2k tris, realistic PBR"
- "Build a horror apartment kitchen — sparse detail, analog props, flickering fluorescent"
- "Scatter rocks on this cliff using geometry nodes, then bake for export"
- "Validate and export SM_Weapon_Rifle_A to FBX for Unreal with collision mesh"

## Anti-Patterns

- ❌ "How do I use Blender?" — Skills assume production context
- ❌ Skipping blender-director on complex multi-step tasks
- ❌ Manual UI steps when Blender MCP is connected
- ❌ Export without asset-optimization validation

# Blender Skills Guide

Decision trees and workflow combinations for the Blender Skills Pack.

## Start Here

For any Blender asset task, **blender-director** analyzes the request and routes to specialist skills. You can also invoke skills directly.

**User attached a reference photo?** Start with **blender-director** → read `references/reference-image-match.md` → fill `references/reference-analysis-template.md` before any Blender work.

## Skill Index

### Orchestration
- **blender-director** — Pipeline planning, skill routing, production briefs

### Modeling Disciplines
- **blender-modeler** — General modeling, scene organization, modifiers
- **hard-surface** — Sci-fi, weapons, industrial, mechanical
- **prop-artist** — Everyday props, furniture, kitbash, hero props
- **vehicle-artist** — Cars, ships, aircraft, mechs, transit
- **environment-artist** — Modular kits, terrain, architecture
- **vegetation-artist** — Trees, plants, grass, foliage cards
- **character-artist** — Human anatomy, clothing, facial topology
- **creature-artist** — Monsters, fantasy, organic design

### Production Workflow
- **sculpting** — High-frequency detail, multires, alphas
- **retopology** — Animation-ready topology, quad flow
- **uv-workflow** — Seams, packing, texel density, UDIM
- **materials** — PBR, procedural, master materials
- **texture-workflow** — Baking, atlases, ORM packing
- **hair-groom** — Curves/particles hair, game hair cards
- **cloth-sim** — Garment sim, pins, shape-key/cache bake
- **lookdev** — Material + light + camera review loop

### Technical
- **geometry-nodes** — Scatter, procedural systems, node groups
- **lighting** — Cinematic, horror, HDRI, volumetrics
- **camera-cinematography** — Framing, lenses, camera animation
- **rendering** — Cycles/Eevee, passes, color management
- **compositing** — Beauty stack, grade, passes
- **animation** — Locomotion, mechanical, NLA export
- **rigging** — IK/FK, weights, mechanical constraints
- **vfx-fx** — Smoke, fire, particles, GN FX
- **physics-sim** — Rigid/soft body, destruction

### Pipeline
- **procedural-modeling** — Rocks, roads, buildings, cables
- **scene-assembly** — Layout, linking, overrides, large scenes
- **set-dressing** — Narrative prop placement, clutter control
- **asset-optimization** — Polycount, cleanup, validation gate
- **lod-pipeline** — LOD generation and validation
- **collision-proxy** — UCX/convex/simple colliders
- **export-pipeline** — Generic FBX/GLTF/USD export
- **unity-export** — Unity-specific delivery
- **unreal-export** — Unreal-specific delivery (UCX, LODs)
- **godot-export** — Godot GLTF/GLB delivery
- **qa-review** — Screenshot + checklist ship gate
- **archviz** — Architectural visualization stills/walkthroughs

### Style Specialists
- **horror-style** — Psychological horror, industrial decay
- **psx-horror-style** — PS1/PSX crunchy horror
- **lowpoly-style** — PS1/PS2, Lethal Company aesthetic
- **anime-style** — Cel/toon, hard color breaks
- **voxel-style** — Minecraft-adjacent block aesthetic
- **isometric-style** — Diorama / strategy-game iso rules
- **stylized-style** — NPR, hand-painted, shape language
- **realistic-style** — AAA PBR, photogrammetry, cinematic

## Decision Trees

### What are you making?

```
Everyday / hero prop / kitbash → prop-artist
Hard surface sci-fi / weapon / industrial → hard-surface
Vehicle / mech / ship / aircraft → vehicle-artist
Environment / level geo → environment-artist
Vegetation / foliage → vegetation-artist
Human character → character-artist (+ hair-groom / cloth-sim)
Creature/monster → creature-artist
Archviz space → archviz
Procedural system → geometry-nodes + procedural-modeling
FX / destruction → vfx-fx / physics-sim
Large scene layout → scene-assembly + set-dressing
```

### What style?

```
Horror → horror-style (+ lighting)
PSX / retro horror → psx-horror-style
Retro/low poly → lowpoly-style
Anime / cel → anime-style
Voxel / blocky → voxel-style
Isometric / strategy → isometric-style
Cartoon/NPR → stylized-style
Photoreal/AAA → realistic-style
Unspecified → blender-director decides from context
```

### Pipeline stage?

```
Starting fresh → blender-director → modeling skill
Sculpt done → retopology
Topology done → uv-workflow → materials → lookdev
Hair / cloth → hair-groom / cloth-sim
Look / shot → camera-cinematography → lighting → rendering → compositing
Scene polish → set-dressing → qa-review
Ready to ship → asset-optimization → lod-pipeline → collision-proxy
  → unity-export | unreal-export | godot-export | export-pipeline
```

## Workflow Combinations

### Hero Hard Surface Prop
```
blender-director → hard-surface → uv-workflow → materials → lookdev
→ asset-optimization → export-pipeline
```

### Everyday Hero Prop
```
blender-director → prop-artist → uv-workflow → materials → lookdev
→ asset-optimization → unity-export|unreal-export
```

### Game Vehicle
```
blender-director → vehicle-artist → lod-pipeline → collision-proxy
→ materials → unreal-export|unity-export → qa-review
```

### Game Character
```
blender-director → character-artist → sculpting → retopology
→ hair-groom → cloth-sim → uv-workflow → texture-workflow
→ rigging → animation → export-pipeline
```

### Horror Environment
```
blender-director → horror-style → environment-artist → set-dressing
→ lighting → lowpoly-style (optional) → asset-optimization → export-pipeline
```

### PSX Horror Room
```
blender-director → psx-horror-style → environment-artist → prop-artist
→ lighting → compositing → qa-review
```

### Modular Environment Kit
```
blender-director → environment-artist → geometry-nodes
→ uv-workflow → texture-workflow → lod-pipeline → asset-optimization → export-pipeline
```

### Forest / Foliage
```
blender-director → vegetation-artist → geometry-nodes → lod-pipeline
→ materials → asset-optimization → export-pipeline
```

### Procedural Scatter System
```
blender-director → geometry-nodes → procedural-modeling → asset-optimization
```

### Cinematic Render
```
blender-director → [modeling skill] → lookdev → camera-cinematography
→ lighting → rendering → compositing → qa-review
```

### Archviz Interior
```
blender-director → archviz → materials → camera-cinematography
→ lighting → rendering → compositing
```

### Anime Character Presentation
```
blender-director → anime-style → character-artist → hair-groom
→ lookdev → camera-cinematography → rendering → compositing
```

### Reference Image Match (Photo / Concept Art)
```
blender-director → reference-image-match.md
  → Reference Analysis (template)
  → Camera match → Geometry tiers 1→2→3
  → materials → lighting → rendering
  → visual-match-checklist → qa-review → validation-checklist
```

**Key rule:** Analyze image first. Match camera before greebles. Screenshot compare after each major pass. Never animate shared hull materials.

## Shared References

| Reference | Path |
|-----------|------|
| Universal Pipeline | `.claude/skills/references/asset-pipeline.md` |
| **Reference Image Match** | `.claude/skills/references/reference-image-match.md` |
| **Reference Analysis Template** | `.claude/skills/references/reference-analysis-template.md` |
| **Visual Match Checklist** | `.claude/skills/references/visual-match-checklist.md` |
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
| Unreal Collision | `UCX_` |
| FX | `FX_` |

## Good Prompts

- "Match this reference photo — analyze first, then build in Blender with same lighting and materials"
- "Upgrade `spacecraft.blend` to match attached image; camera full-ship view; do not rebuild"
- "Plan and create a game-ready sci-fi crate for Unity, 2k tris, realistic PBR"
- "Build a horror apartment kitchen — sparse detail, analog props, flickering fluorescent"
- "Model a game-ready sedan for Unreal with LODs and UCX collision"
- "Groom short hair cards for this character and atlas them"
- "Scatter rocks on this cliff using geometry nodes, then bake for export"
- "Validate and export SM_Weapon_Rifle_A to FBX for Unreal with collision mesh"
- "Assemble this modular corridor, dress the set, then QA with screenshots"

## Anti-Patterns

- ❌ "How do I use Blender?" — Skills assume production context
- ❌ Attaching reference image without asking agent to analyze and match it
- ❌ Skipping blender-director on complex multi-step tasks
- ❌ Adding greebles before silhouette and panel-break depth
- ❌ Keyframing emission on shared hull materials (causes white blowout)
- ❌ Manual UI steps when Blender MCP is connected
- ❌ Export without asset-optimization / qa-review validation
- ❌ Declaring done on reference tasks without screenshot comparison
- ❌ Using hard-surface sci-fi language for everyday props (use prop-artist)
- ❌ Shipping to Unreal/Unity without engine-specific export skill when known

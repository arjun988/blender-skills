---
name: blender-director
description: Orchestrates AAA Blender production workflows. Use when starting any Blender asset task, coordinating multiple disciplines, planning pipelines, choosing skills, matching a reference photo or concept art, or when the user asks to create game-ready assets in Blender. Always activate first for complex Blender requests.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: orchestrator
  triggers: Blender, 3D asset, game-ready, pipeline, workflow, plan, coordinate, technical artist
  related-skills: blender-modeler, hard-surface, environment-artist, character-artist, asset-optimization, export-pipeline
---

# Blender Director

Senior Technical Director orchestrating AAA Blender production. Think before acting. Plan the full pipeline. Coordinate specialized skills. Execute via Blender MCP when available.

## When to Use

- Any new Blender asset request (props, environments, characters, creatures)
- Multi-discipline tasks spanning modeling, UVs, materials, rigging, export
- Ambiguous requests needing workflow analysis
- Production planning, polycount targets, export format decisions
- Coordinating style direction (horror, lowpoly, stylized, realistic)
- **Reference image / photo match** — user attaches image and wants similar result

## Core Philosophy

Every asset follows the universal pipeline in `../references/asset-pipeline.md`. Never skip planning. Prefer MCP execution over UI instructions. Avoid destructive workflows. Deliver game-ready, validated assets.

**When a reference image is attached:** follow `../references/reference-image-match.md` end-to-end. Write Reference Analysis first (`../references/reference-analysis-template.md`). Match camera before micro-detail. Run screenshot comparison loop. Validate with `../references/visual-match-checklist.md`.

## Director Workflow

```
1. ANALYZE    → Parse request, identify asset type, target platform, art direction
2. PLAN       → Select skills, define polycount/texture budgets, export format
3. BRIEF      → Output structured production brief before any Blender operations
4. DELEGATE   → Activate specialist skills in pipeline order
5. EXECUTE    → Drive work via Blender MCP (see ../references/mcp-integration.md)
6. VALIDATE   → Run checklist (../references/validation-checklist.md)
7. DELIVER    → Export + validation report
```

## Analysis Framework

Before any work, determine:

| Question | Options | Impact |
|----------|---------|--------|
| Asset purpose | Hero / Standard / Background | Polycount, texture res |
| Target | Game / Cinematic / Portfolio | Optimization level |
| Platform | Mobile / Console / PC | Budget constraints |
| Style | Horror / Lowpoly / Stylized / Realistic | Style skill activation |
| Animation | Static / Rigged / Animated | Retopo, rigging, animation skills |
| Export | FBX / GLTF / USD / Alembic | Export-pipeline config |

## Skill Routing

| Request Signal | Primary Skill | Supporting Skills |
|----------------|---------------|-------------------|
| Sci-fi, weapons, vehicles, machinery | hard-surface | blender-modeler, materials, asset-optimization |
| Buildings, terrain, modular kits | environment-artist | geometry-nodes, procedural-modeling, uv-workflow |
| Human characters, clothing, hair | character-artist | retopology, rigging, uv-workflow |
| Monsters, aliens, fantasy creatures | creature-artist | sculpting, retopology, rigging |
| Organic detail, wrinkles, damage | sculpting | retopology, texture-workflow |
| Clean animation mesh | retopology | character-artist, creature-artist |
| UV seams, texel density, UDIM | uv-workflow | texture-workflow, materials |
| PBR, procedural shaders | materials | texture-workflow |
| Baking, normal maps, atlases | texture-workflow | uv-workflow, materials |
| Scatter, procedural systems | geometry-nodes | procedural-modeling, environment-artist |
| Mood, cinematic lighting | lighting | rendering, horror-style |
| Final renders, passes | rendering | lighting, materials |
| Walk cycles, mechanical motion | animation | rigging |
| Bones, IK, weight paint | rigging | animation, character-artist |
| Rocks, roads, cables, buildings (procedural) | procedural-modeling | geometry-nodes |
| Polycount, cleanup, LODs | asset-optimization | export-pipeline |
| FBX/GLTF export, engine import | export-pipeline | asset-optimization |
| Psychological horror aesthetic | horror-style | lighting, environment-artist |
| PS1/PS2, Lethal Company style | lowpoly-style | environment-artist, materials |
| Exaggerated, NPR, hand-painted | stylized-style | materials, rendering |
| Photoreal, scan cleanup, AAA PBR | realistic-style | texture-workflow, rendering |
| **Reference photo / concept art attached** | **reference-image-match** | blender-director → discipline skill → style → materials → lighting → rendering |

## Reference Image Workflow (Mandatory)

When user provides a photo or render to match:

```
1. REFERENCE ANALYSIS  → reference-analysis-template.md (written, before MCP)
2. BASELINE SCREENSHOT → get_viewport_screenshot
3. CAMERA MATCH        → CAM_* + EMPTY_CamTarget_* before detailing
4. GEOMETRY TIERS      → silhouette → panel breaks → greebles
5. MATERIALS           → palette from reference; per-object emissive lights only
6. LIGHTING + WORLD    → key direction, rim, space/env mood
7. GRADING             → AgX exposure/look; EEVEE for animation preview
8. COMPARE LOOP        → screenshot → gap list → fix (×3 max)
9. VALIDATE            → visual-match-checklist.md
```

See `../references/reference-image-match.md` for full protocol and failure fixes.

## Production Brief Template

Output this before executing:

```markdown
## Production Brief: [Asset Name]

**Type:** [prop/environment/character/creature]
**Target:** [game engine / cinematic / portfolio]
**Style:** [horror/lowpoly/stylized/realistic]
**Poly Budget:** [triangles] (ref: polycount-budgets.md)
**Texture Budget:** [resolution]
**Export:** [format + settings]
**Pivot:** [floor/grip/hinge/center]
**Animation:** [none/rigged/animated]

### Active Skills
1. [skill] — [role in pipeline]
2. [skill] — [role in pipeline]

### Pipeline Phases
- [ ] Reference & Planning
- [ ] Blockout & Silhouette
- [ ] Modeling
- [ ] Cleanup & Topology
- [ ] UVs
- [ ] Materials/Textures
- [ ] Optimization
- [ ] Rig/Animate (if needed)
- [ ] Export & Validation

### MCP Execution Plan
[Ordered list of MCP operations]
```

## Multi-Skill Workflows

### Hero Prop (Hard Surface)
```
blender-director → hard-surface → materials → uv-workflow → asset-optimization → export-pipeline
```

### Environment Modular Kit
```
blender-director → environment-artist → geometry-nodes → uv-workflow → asset-optimization → export-pipeline
```

### Game Character
```
blender-director → character-artist → sculpting → retopology → uv-workflow → materials → rigging → animation → export-pipeline
```

### Horror Scene
```
blender-director → horror-style → environment-artist → lighting → asset-optimization → export-pipeline
```

### Procedural Scatter System
```
blender-director → geometry-nodes → procedural-modeling → asset-optimization
```

## MCP Integration

1. Check Blender MCP availability before Phase 1 execution
2. Create collection hierarchy via MCP immediately
3. Query scene state after each pipeline phase
4. Never describe UI steps when MCP can execute
5. See `../references/mcp-integration.md`

## Constraints

### MUST DO
- Output production brief before modeling
- **If reference image attached:** complete Reference Analysis and camera match before geometry detail
- **Screenshot compare** after materials, lighting, and each refinement pass
- Activate appropriate style skill for art direction
- Set polycount/texture budgets explicitly
- Organize collections with `COL_` prefix from start
- Validate before declaring complete
- Coordinate skills; don't try to do everything in one pass

### MUST NOT DO
- Skip planning phase
- Skip reference analysis when user attached an image
- Keyframe emission on shared hull/structural materials
- Add micro-greebles before silhouette and panel-break tiers
- Declare "done" without visual-match checklist when reference was provided
- Start modeling without scale reference
- Mix styles without explicit direction
- Export without validation
- Explain Blender UI when MCP is available
- Apply destructive operations without backup

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Universal Pipeline | `../references/asset-pipeline.md` | Every task |
| MCP Integration | `../references/mcp-integration.md` | Before execution |
| Naming | `../references/naming-conventions.md` | Scene setup |
| Validation | `../references/validation-checklist.md` | Before delivery |
| Polycount Budgets | `../references/polycount-budgets.md` | Planning phase |
| Skill Routing | `references/skill-routing.md` | Complex multi-skill tasks |
| MCP Tools | `../references/mcp-tools.md` | Before MCP execution |
| Reference Image Match | `../references/reference-image-match.md` | Photo/concept attached |
| Reference Analysis | `../references/reference-analysis-template.md` | Before first MCP call |
| Visual Match Validation | `../references/visual-match-checklist.md` | Before delivery |

## Decision Trees

### Reference Image Provided?
```
User attached photo / concept / "match this"?
├── YES → reference-image-match.md (full workflow)
│         → Analyze → Camera → Geometry tiers → Materials → Lighting → Compare loop
└── NO  → Standard pipeline below
```

### New Asset Request
```
Is style specified?
├── Horror → horror-style + environment-artist or hard-surface
├── Lowpoly → lowpoly-style + relevant modeling skill
├── Stylized → stylized-style + relevant modeling skill
├── Realistic → realistic-style + relevant modeling skill
└── Unspecified → Ask or infer from context

Is it organic or hard surface?
├── Hard surface → hard-surface
├── Human → character-artist
├── Creature → creature-artist
└── Environment → environment-artist

Does it need animation?
├── Yes → Add retopology, rigging, animation
└── No → Static pipeline
```

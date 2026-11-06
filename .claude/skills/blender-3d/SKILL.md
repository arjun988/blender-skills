---
name: blender-3d
description: >-
  Consolidated entry point for the Blender production skill pack (94 sub-skills).
  Use when creating, modeling, texturing, lighting, animating, optimizing, or
  exporting ANY 3D asset or scene in Blender via MCP — props, hard surface,
  vehicles, environments, characters, creatures, procedural systems, archviz,
  game-ready pipelines (Unity/Unreal/Godot), art direction (horror, lowpoly,
  anime, stylized, realistic, and more), and reference-photo matching. Load this
  ONE skill; pull deeper knowledge from references/ on demand.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.1.0"
  domain: blender
  role: orchestrator
  source: https://github.com/arjun988/blender-skills
---

# Blender 3D Production Pack

Single-entry consolidation of the 94-skill Blender Skills Pack. Senior technical-director workflow: plan before touching Blender, execute via MCP, validate before delivering.

## How to Use This Skill

This SKILL.md is the router. The `references/` directory holds one file per discipline/style pack plus shared standards. **Do not read everything up front** — identify what the task needs from the routing tables below, then load only those files.

```
SKILL.md (this file)  → always read
references/           → shared standards + per-topic deep dives, load on demand
    asset-pipeline.md            universal phase-by-phase pipeline
    polycount-budgets.md         triangle/texture targets by tier & style
    naming-conventions.md        SM_/MAT_/COL_ naming for engine import
    mcp-integration.md           MCP-first execution rules
    mcp-tools.md                 BlenderMCP tool catalog + bpy fallbacks
    validation-checklist.md      pre-export quality gate
    routing-matrices.md          engine-target & phase-ownership matrices
    reference-image-match.md     photo/concept matching protocol
    reference-analysis-template.md  written analysis before modeling a matched image
    visual-match-checklist.md       screenshot-comparison closure checklist
    disciplines/*.md             modeling / production / technical / pipeline topics
    styles-worlds-genres/*.md    art direction packs
```

## Mandatory Workflow

```
1. ANALYZE   Parse request: asset type, target platform, art direction, animation needs
2. PLAN      Pick references to load; set polycount/texture/export budgets
3. BRIEF     Output a production brief (template below) BEFORE any Blender operation
4. EXECUTE   Drive work via MCP following references/asset-pipeline.md
5. VALIDATE  Run references/validation-checklist.md (+ visual-match-checklist.md if reference image)
6. DELIVER   Export + short validation report
```

Never skip planning. Prefer MCP execution over UI narration. Keep workflows non-destructive (live modifiers until export prep). If a reference image is attached, run `references/reference-image-match.md` end-to-end and complete `reference-analysis-template.md` before any geometry.

## Routing Tables

### Disciplines — load from `references/disciplines/<file>.md`

| Request Signal | File |
|----------------|------|
| General meshing, blockouts, modifier stacks, cleanup | blender-modeler |
| Sci-fi, weapons, machinery, booleans, panel lines, greebles | hard-surface |
| Everyday/hero props, kitbash, furniture | prop-artist |
| Cars, ships, aircraft, mechs | vehicle-artist |
| Modular kits, terrain, buildings | environment-artist |
| Trees, plants, grass, foliage cards | vegetation-artist |
| Human anatomy, clothing, faces | character-artist |
| Monsters, aliens, fantasy organics | creature-artist |
| Character race/role archetypes | character-archetypes |
| Sculpting detail, wrinkles, damage | sculpting |
| Clean animation mesh after sculpting | retopology |
| UV seams, texel density, UDIM, atlases | uv-workflow |
| PBR values, procedural shaders, master materials | materials |
| Baking, normal maps, trim sheets | texture-workflow |
| Shading review loop | lookdev |
| Scatter, procedural systems, GN trees | geometry-nodes |
| Rocks/roads/buildings via procedural methods | procedural-modeling |
| Three-point lighting, HDRI, volumetrics | lighting |
| Lenses, framing, camera moves, DoF | camera-cinematography |
| Cycles/Eevee settings, passes, turntables | rendering |
| Compositor stack, grading, beauty pass | compositing |
| Walk cycles, mechanical motion | animation |
| Bones, IK/FK, weight paint, drivers | rigging |
| Smoke, fire, particles | vfx-fx |
| Rigid/soft body, destruction | physics-sim |
| Cloth sim, garments, capes | cloth-sim |
| Hair/fur cards (game) or groom (cinematic) | hair-groom |
| Large scene layout, linking, overrides | scene-assembly |
| Prop placement, narrative clutter | set-dressing |
| Archviz interiors/exteriors | archviz |
| Polycount audit, cleanup, draw calls | asset-optimization |
| LOD generation/validation | lod-pipeline |
| UCX/convex colliders | collision-proxy |
| Generic FBX/GLTF/USD export | export-pipeline |
| Unity-specific delivery | unity-export |
| Unreal-specific delivery | unreal-export |
| Godot-specific delivery | godot-export |
| QA gate, screenshot review, ship check | qa-review |

### Styles / Worlds / Genres — load from `references/styles-worlds-genres/<file>.md`

Style packs define silhouette, material, lighting, and rendering language. Combine ONE style with ONE discipline; the style shapes every pipeline phase.

| Request Signal | File |
|----------------|------|
| Psychological horror (Silent Hill, Chilla's Art) | horror-style |
| PSX crunch horror | psx-horror-style |
| Indie horror refs (Fear to Fathom, Puppet Combo) | indie-horror-aesthetics |
| Eldritch/cosmic horror | cosmic-eldritch-horror |
| Body horror / mutation | body-horror-style |
| Analog VHS / found footage | analog-found-footage-horror |
| Liminal spaces / Backrooms | liminal-space-style |
| Folk / rural ritual horror | folk-horror-style |
| Mascot / puppet horror | mascot-puppet-horror |
| Dreamcore / weirdcore | dream-weirdcore-style |
| Lowpoly, PS1/PS2 era, Lethal Company | lowpoly-style |
| Voxel / Minecraft-adjacent | voxel-style |
| Isometric strategy/diorama presentation | isometric-style |
| Stylized NPR broad appeal | stylized-style |
| Photoreal, scan cleanup, AAA PBR | realistic-style |
| Anime/cel · manga · cartoon · comic ink | anime-manga-cartoon-comic-styles |
| Pixel art, 8/16-bit, HD-2D, hand-painted, painterly, stop-motion craft | pixel-retro-handpainted-styles |
| Noir · minimalist · vector · chibi · frutiger-aero · neon/vaporwave · cozy · gritty · surreal · brutalist | mood-and-extended-styles |
| Console-era aesthetics (PS1–PS5, CRT, DOS) | visual-console-eras |
| Fantasy · sci-fi punks · historical · post-apoc · biomes | world-packs |
| Genre gameplay feel (RPG loot reads, shooter arenas, soulslike dread…) | genre-packs |

## Production Brief Template

Output before executing:

```markdown
## Production Brief: [Asset Name]

**Type:** prop / environment / character / creature
**Target:** game engine / cinematic / portfolio
**Platform:** mobile / console / PC
**Style:** [style pack]
**Poly Budget:** [triangles] (see polycount-budgets.md)
**Texture Budget:** [resolution]
**Export:** [format + key settings]
**Pivot:** floor / grip / hinge / center
**Animation:** none / rigged / animated

### References Loaded
- [list only the files actually loaded]

### Pipeline Phases
- [ ] Planning & blockout
- [ ] Modeling / detailing
- [ ] UV & materials
- [ ] Optimization & LODs
- [ ] Export & validation
```

## Shared Rules (apply always)

1. **Scale**: 1 Blender unit = 1 meter; place a human-scale reference before blocking out.
2. **Naming**: follow `naming-conventions.md` (`SM_`, `MAT_`, `COL_`…) so engine import and collisions stay sane.
3. **Non-destructive default**: keep Mirror/Array/Boolean/Bevel live in the modifier stack until export prep.
4. **MCP-first**: check MCP tool schemas before calling; validate each phase by querying the scene (object counts, bounds); screenshot after camera/materials/lighting changes; fall back to narration only if MCP lacks the capability.
5. **Validate before deliver**: nothing ships without the checklist run.

## Constraint

If the conversation's skill system already exposes individual skills named like this pack's topics (e.g. a separate `hard-surface` skill), defer to those and use this file only as the map.

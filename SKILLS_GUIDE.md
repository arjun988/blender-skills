# Blender Skills Guide

Decision trees and workflow combinations for the Blender Skills Pack (**94 skills**).

## Start Here

For any Blender asset task, **blender-director** analyzes the request and routes to specialist skills. You can also invoke skills directly.

**User attached a reference photo?** Start with **blender-director** → read `references/reference-image-match.md` → fill `references/reference-analysis-template.md` before any Blender work.

**Genre / style / mood / world?** Director routes to a pack skill; open that skill’s `references/` for subtype details (e.g. steampunk under `sci-fi-punk-worlds`, Backrooms under `liminal-space-style`).

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
- **character-archetypes** — Races/roles (elf, mecha, knight, vampire, …)

### Production Workflow
- **sculpting** · **retopology** · **uv-workflow** · **materials** · **texture-workflow**
- **hair-groom** · **cloth-sim** · **lookdev**

### Technical
- **geometry-nodes** · **lighting** · **camera-cinematography** · **rendering** · **compositing**
- **animation** · **rigging** · **vfx-fx** · **physics-sim**

### Pipeline
- **procedural-modeling** · **scene-assembly** · **set-dressing** · **asset-optimization**
- **lod-pipeline** · **collision-proxy** · **export-pipeline**
- **unity-export** · **unreal-export** · **godot-export** · **qa-review** · **archviz**

### Core Style Specialists
- **horror-style** · **psx-horror-style** · **lowpoly-style** · **anime-style** · **voxel-style**
- **isometric-style** · **stylized-style** · **realistic-style**

### Extended Art Styles
- **cartoon-style** · **comic-book-style** · **manga-style** · **pixel-art-style**
- **hand-painted-style** · **painterly-style** (watercolor/oil) · **stop-motion-craft-style**
- **chibi-style** · **noir-style** · **minimalist-style** · **vector-style**
- **retro-8bit-style** · **retro-16bit-style** · **hd-2d-style** · **frutiger-aero-style**

### Horror Packs
- **cosmic-eldritch-horror** · **body-horror-style** · **analog-found-footage-horror**
- **liminal-space-style** · **folk-horror-style** · **mascot-puppet-horror**
- **dream-weirdcore-style** · **indie-horror-aesthetics**

### Worlds / Themes
- **fantasy-worlds** · **sci-fi-punk-worlds** · **historical-worlds**
- **apocalypse-worlds** · **biome-worlds**

### Mood / Atmosphere
- **cozy-wholesome-mood** · **dark-gritty-mood** · **dream-surreal-mood**
- **neon-retrofuturism** · **brutalist-mood**

### Gameplay Genre Art Direction
- **genre-action-combat** · **genre-shooter** · **genre-rpg** · **genre-survival**
- **genre-stealth** · **genre-puzzle-platformer** · **genre-metroidvania-roguelike**
- **genre-soulslike** · **genre-strategy-sim** · **genre-racing-sports**
- **genre-narrative-vn** · **genre-card-party-idle** · **genre-open-world-sandbox**

### Visual Eras
- **visual-console-eras** — PS1–PS5, arcade, DOS, CRT, VHS, film grain

## Decision Trees

### What are you making?

```
Everyday / hero prop / kitbash → prop-artist
Hard surface sci-fi / weapon / industrial → hard-surface
Vehicle / mech / ship / aircraft → vehicle-artist
Environment / level geo → environment-artist
Vegetation / foliage → vegetation-artist
Human character → character-artist (+ hair-groom / cloth-sim / character-archetypes)
Creature/monster → creature-artist
Archviz space → archviz
Procedural system → geometry-nodes + procedural-modeling
FX / destruction → vfx-fx / physics-sim
Large scene layout → scene-assembly + set-dressing
```

### What style / mood / world?

```
Art style named (anime, pixel, noir, HD-2D, …) → matching *-style skill
Horror subtype (cosmic, liminal, folk, analog, …) → horror pack skill
World theme (cyberpunk, medieval, wasteland, jungle, …) → worlds skill + open its references/
Mood (cozy, gritty, vaporwave, brutalist, …) → mood skill
Console/media era (PS1, CRT, VHS, …) → visual-console-eras
Gameplay genre (FPS, JRPG, soulslike, city builder, …) → genre-* skill
Unspecified → blender-director infers from context
```

### Pipeline stage?

```
Starting fresh → blender-director → modeling + style/world/genre packs
Sculpt done → retopology
Topology done → uv-workflow → materials → lookdev
Hair / cloth → hair-groom / cloth-sim
Look / shot → camera-cinematography → lighting → rendering → compositing
Scene polish → set-dressing → qa-review
Ready to ship → asset-optimization → lod-pipeline → collision-proxy
  → unity-export | unreal-export | godot-export | export-pipeline
```

## Subtype Coverage Map

Your long genre lists are covered as **skills + reference subtypes** (not 200 tiny skills):

| Your list area | Skill | Subtypes live in |
|----------------|-------|------------------|
| Action / Fighting / Hack‑n‑Slash | `genre-action-combat` | skill + refs |
| FPS / TPS / BR / Extraction | `genre-shooter` | refs |
| RPG / JRPG / CRPG / ARPG / MMO | `genre-rpg` | refs |
| Survival / Survival Horror gameplay | `genre-survival` | refs |
| Stealth / Puzzle / Platformer | `genre-stealth`, `genre-puzzle-platformer` | refs |
| Metroidvania / Roguelike / Roguelite | `genre-metroidvania-roguelike` | refs |
| Soulslike | `genre-soulslike` | refs |
| Strategy / RTS / TBS / TD / MOBA / Sims | `genre-strategy-sim` | refs |
| Racing / Sports | `genre-racing-sports` | refs |
| VN / Walking Sim / Interactive Movie | `genre-narrative-vn` | refs |
| Card / Party / Idle / Rhythm / Edu | `genre-card-party-idle` | refs |
| Open World / Sandbox | `genre-open-world-sandbox` | refs |
| Cyberpunk…Clockpunk / Space | `sci-fi-punk-worlds` | refs |
| Medieval…Urban Fantasy | `fantasy-worlds` | refs |
| Western…Military eras | `historical-worlds` | refs |
| Post‑apoc / Zombie / Dystopia | `apocalypse-worlds` | refs |
| Biomes | `biome-worlds` | refs |
| Horror subtypes + indie refs | horror packs + `indie-horror-aesthetics` | refs |
| Character races/roles | `character-archetypes` | refs |
| PS1–PS5 / CRT / VHS | `visual-console-eras` | refs |

## Workflow Combinations

### Hero Hard Surface Prop
```
blender-director → hard-surface → uv-workflow → materials → lookdev
→ asset-optimization → export-pipeline
```

### Cyberpunk Street Prop
```
blender-director → sci-fi-punk-worlds → neon-retrofuturism → prop-artist
→ materials → lookdev → qa-review
```

### Game Vehicle
```
blender-director → vehicle-artist → lod-pipeline → collision-proxy
→ materials → unreal-export|unity-export → qa-review
```

### Soulslike Ruins
```
blender-director → genre-soulslike → dark-gritty-mood → fantasy-worlds
→ environment-artist → lighting → set-dressing → qa-review
```

### Liminal Backrooms
```
blender-director → liminal-space-style → environment-artist → lighting
→ analog-found-footage-horror (optional) → compositing
```

### JRPG Town
```
blender-director → genre-rpg → fantasy-worlds → stylized-style|anime-style
→ environment-artist → set-dressing → lookdev
```

### HD-2D Dungeon
```
blender-director → hd-2d-style → pixel-art-style → environment-artist
→ camera-cinematography → lighting → compositing
```

### Game Character
```
blender-director → character-archetypes → character-artist → sculpting → retopology
→ hair-groom → cloth-sim → uv-workflow → texture-workflow → rigging → animation → export-pipeline
```

### Horror Environment
```
blender-director → horror-style → indie-horror-aesthetics (pick lane)
→ environment-artist → set-dressing → lighting → export-pipeline
```

### Cozy Farming Sim
```
blender-director → genre-strategy-sim → cozy-wholesome-mood → prop-artist
→ vegetation-artist → isometric-style (optional) → lookdev
```

### Cinematic Render
```
blender-director → [modeling skill] → lookdev → camera-cinematography
→ lighting → rendering → compositing → qa-review
```

### Reference Image Match
```
blender-director → reference-image-match.md
  → Reference Analysis → Camera match → Geometry tiers
  → materials → lighting → rendering
  → visual-match-checklist → qa-review
```

## Shared References

| Reference | Path |
|-----------|------|
| Universal Pipeline | `.claude/skills/references/asset-pipeline.md` |
| Reference Image Match | `.claude/skills/references/reference-image-match.md` |
| Reference Analysis Template | `.claude/skills/references/reference-analysis-template.md` |
| Visual Match Checklist | `.claude/skills/references/visual-match-checklist.md` |
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

- "Build a liminal Backrooms lobby — fluorescent hum, stained carpet, endless doors"
- "Cyberpunk street vendor stall, neon-retrofuturism, Unreal export with UCX"
- "Soulslike chapel interior, dark fantasy, fog gate landmark"
- "HD-2D forest clearing, pixel party characters, theatrical DoF"
- "JRPG starter town, cozy mood, hand-painted materials"
- "Analog horror VHS security-cam office, found-footage framing"
- "Match this reference photo — analyze first, then build in Blender"

## Anti-Patterns

- ❌ Skipping blender-director on complex multi-skill tasks
- ❌ Mixing cyberpunk + steampunk + solarpunk without an intentional mashup brief
- ❌ Declaring a genre without loading that genre skill’s readability rules
- ❌ Manual UI steps when Blender MCP is connected
- ❌ Export without asset-optimization / qa-review
- ❌ Reference tasks without screenshot comparison

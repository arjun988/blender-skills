
# Environment Artist

Modular, scalable environment production for games. Storytelling through space. Performance-conscious.

## When to Use

- Modular building kits, interior/exterior sets
- Terrain, cliffs, rocks, roads
- Vegetation placement and optimization
- Architectural spaces with narrative intent
- Scene composition and scale establishment

## Core Principles

1. **Modularity** — Pieces snap to grid; reusable across scenes
2. **Storytelling** — Environment communicates history and mood
3. **Scale** — Human reference always present
4. **Performance** — Instancing, LODs, texture atlases
5. **Composition** — Guide player eye with shapes and value

## Modular Kit Workflow

```
Grid Definition → Corner/Edge/Fill Pieces → Trim Sheets
    → UV Atlas → Material Variants → Instance Placement
    → Hero Overrides → Optimization → Export
```

## Grid Standards

| Kit Type | Grid Unit | Snap |
|----------|-----------|------|
| Interior walls | 2m or 4m | 0.5m sub-grid |
| Exterior facades | 4m modules | 1m sub-grid |
| Roads | 4m lane width | Centerline snap |
| Props | 0.5m | Free placement |

Name modules: `SM_Env_[Type]_[Role]_[Size]`
Example: `SM_Env_Wall_Corner_2m`

## Kit Piece Categories

| Role | Purpose | Count Target |
|------|---------|--------------|
| Corner | 90° turns | 2–4 variants |
| Edge | Straight runs | 2–3 lengths |
| Fill | Blank panels | 3–5 variants |
| Door/Window | Breakups | 2–4 types |
| Trim | Transitions | Shared trim sheet |

## Terrain & Natural Forms

- Hero rocks: sculpted or photogrammetry cleanup
- Background rocks: geometry nodes scatter
- Cliffs: modular cliff face pieces + blend shapes
- Ground: displacement or geo nodes with texture blending

## Vegetation

| Type | Approach | Poly Budget |
|------|----------|-------------|
| Hero tree | Hand model + cards | 5k–15k tris |
| Mid tree | Simplified + impostor LOD | 2k–5k tris |
| Bush | Cards + cluster | 500–2k tris |
| Grass | Cards or geo nodes scatter | 2–50 tris per blade |

Use geometry nodes for scatter; see geometry-nodes skill.

## Architecture

**Interior:**
- Ceiling height: 2.4m–3.5m standard
- Door: 2.1m × 0.9m
- Window sill: 0.9m from floor
- Corridors: minimum 1.5m playable width

**Exterior:**
- Floor count readable in silhouette
- Roof forms distinguish building type
- Weathering tells climate story

## Composition Guidelines

- **Focal point** — One hero element per vista
- **Leading lines** — Roads, walls, light guide movement
- **Value hierarchy** — Contrast draws attention
- **Negative space** — Rest areas between detail clusters
- **Silhouette layers** — Foreground/mid/background separation

## Storytelling Details

| Detail | Narrative Signal |
|--------|------------------|
| Peeling paint | Neglect, age |
| Barricades | Conflict, danger |
| Personal items | Former inhabitants |
| Damage patterns | Event history |
| Lighting state | Occupied vs abandoned |

## Game Optimization

- Instance repeated modules (walls, floors)
- Shared trim sheet across kit
- Single material with vertex colors for variation
- LODs: 50%/25%/10% per module
- Occlusion: don't model unseen backsides

## MCP Integration

1. Create modular pieces with exact dimensions via MCP
2. Set up collection instances for kit preview
3. Scatter vegetation via geometry nodes (MCP)
4. Query total scene polycount
5. Organize export collections by kit type

## Constraints

### MUST DO
- Design for grid snapping from blockout
- Create minimum viable kit before hero pieces
- Use instancing for all repeated geometry
- Maintain consistent texel density across kit
- Include scale reference human figure

### MUST NOT DO
- Unique geometry for every wall segment
- Ignore backface culling opportunities
- Over-detail background-only areas
- Mix grid sizes within same kit
- Skip LOD planning

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Modular kit design | `references/modular-kits.md` | Kit creation |
| Composition | `references/composition.md` | Scene layout |
| Pipeline | `asset-pipeline.md` (shared) | Phase context |

## Style Integration

| Style | Approach |
|-------|----------|
| horror-style | Claustrophobic corridors; sparse lighting |
| lowpoly-style | Large flat shapes; minimal modules |
| stylized-style | Exaggerated proportions; bold colors |
| realistic-style | High detail hero; scanned textures |


## Appendix: composition

# Environment Composition

## Layer Structure

| Layer | Content | Detail Level |
|-------|---------|--------------|
| Foreground | Framing elements | Medium |
| Midground | Gameplay/interaction | Hero |
| Background | Skyline/fog silhouettes | Low |

## Leading Lines

Use roads, rivers, walls, light shafts to guide eye toward:
- Objective marker
- Threat reveal
- Narrative focal point

## Rule of Thirds

Place hero elements at intersection points.
Horizon on upper or lower third — not center (unless symmetrical intent).

## Value Hierarchy

Brightest area = player attention target.
Darkest area = concealment or negative space.
Avoid uniform brightness across vista.

## Scale Cues

Include known-size objects:
- Doors (2.1m)
- Human figure (1.7m)
- Vehicles
- Furniture

## Negative Space

Rest areas between detail clusters prevent visual fatigue.
Horror: increase negative space for tension.

## Modular Scene Assembly

```
1. Block terrain/ground plane
2. Place hero modular structures
3. Add midground props (instanced)
4. Background low-poly silhouettes + fog
5. Validate from player camera height/path
```

## Camera Path Validation

Walk player path in viewport at eye height (1.6m).
Check readability every 10m of travel.

## Appendix: modular-kits

# Modular Kit Design

## Minimum Viable Kit

Before hero pieces, ship:

| Piece | Quantity |
|-------|----------|
| Straight wall (2m) | 2 variants |
| Corner 90° | 2 (L + R or mirror) |
| Door frame | 1 |
| Window frame | 1–2 |
| Floor tile | 1 |
| Ceiling tile | 1 |

## Snap Point Convention

- Origin at grid corner (floor level)
- Positive Y = forward face (outward normal)
- Connection points at grid intersections
- Document snap grid in export README

## Trim Sheet Layout

```
[Corner trim | Edge trim | Fill panel | Window surround | Damage variants]
```

Shared 2048 trim sheet across entire kit.

## Variation Without Unique Geo

- Vertex color tints
- Material instance parameters
- Decal overlays
- 90° rotation of asymmetric pieces

## Kit Validation

Assemble test scene:
- Closed room from kit only
- L-shaped corridor
- T-junction
- Verify no gaps at 0.001m tolerance

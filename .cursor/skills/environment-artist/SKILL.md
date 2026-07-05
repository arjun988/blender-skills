---
name: environment-artist
description: AAA environment art for modular kits, buildings, terrain, vegetation, architecture, and scene composition. Use for game-optimized environments, storytelling through space, and modular asset pipelines in Blender via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: environment, modular kit, building, terrain, vegetation, architecture, interior, exterior, level art, scene composition
  related-skills: geometry-nodes, procedural-modeling, uv-workflow, lighting
---

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
| Pipeline | `../references/asset-pipeline.md` | Phase context |

## Style Integration

| Style | Approach |
|-------|----------|
| horror-style | Claustrophobic corridors; sparse lighting |
| lowpoly-style | Large flat shapes; minimal modules |
| stylized-style | Exaggerated proportions; bold colors |
| realistic-style | High detail hero; scanned textures |

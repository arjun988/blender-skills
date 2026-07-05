---
name: character-artist
description: AAA character modeling for human anatomy, stylization, facial topology, clothing, hair, and animation-ready meshes. Use for game characters, facial expressions, and production character assets in Blender via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: character, human, anatomy, face, facial, clothing, hair, body, edge loop, expression, portrait
  related-skills: retopology, rigging, sculpting, uv-workflow
---

# Character Artist

Production character modeling with animation-ready topology. Anatomy-accurate or intentionally stylized.

## When to Use

- Human/humanoid character creation
- Facial topology for expressions
- Clothing and accessory modeling
- Hair card systems or stylized hair
- Character proportion and stylization

## Workflow

```
Reference → Proportion Blockout → Body Forms → Limb Connection
    → Facial Features → Edge Loop Planning → Detail Pass
    → Clothing (separate mesh) → UV Handoff → Rig Handoff
```

## Proportion Standards

| Type | Head Units | Notes |
|------|------------|-------|
| Realistic adult | 7.5–8 heads | Hero characters |
| Stylized | 4–6 heads | Exaggerated features |
| Heroic | 8–9 heads | Action games |

Always block proportions before detail.

## Edge Loop Strategy

Critical loop locations:
- Eyes: concentric loops for blink/expression
- Mouth: 3-loop minimum for lip deformation
- Jaw: loop following jaw line for open/close
- Shoulders: deltoid loop for arm raise
- Elbows/knees: 3-loop pinching pattern
- Hips: loop for leg spread

See `references/facial-topology.md` for face-specific loops.

## Facial Structure

- Eye socket: recessed; brow ridge defined
- Nose: bridge width matches inner eye distance (realistic)
- Mouth: lower lip fuller than upper (realistic)
- Ear: aligns eye brow to nose base
- Skull underlying forms visible in stylization

## Clothing Workflow

1. Model body first (or use mannequin)
2. Duplicate body faces for clothing base
3. Solidify/extrude for cloth thickness
4. Separate mesh: `SM_Char_[Name]_Body`, `SM_Char_[Name]_Cloth_[Piece]`
5. Cloth does NOT share UVs with body
6. Weight paint transfers from body (via rigging skill)

## Hair Approaches

| Method | Use Case | Skill |
|--------|----------|-------|
| Hair cards | Game-realistic | uv-workflow + texture-workflow |
| Strand curves | Cinematic | particle/curve systems |
| Stylized mesh | Lowpoly/stylized | blender-modeler |
| Sculpted | Hero bake | sculpting → retopology |

## Animation-Ready Requirements

- Quad-dominant topology on deformation zones
- No poles on primary deformation areas (relocate to hidden zones)
- Even edge length in face/neck/joints
- Separate objects for swap-able parts (head, hands, gear)

## MCP Integration

1. Create base mannequin/blockout via MCP
2. Build body with mirror modifier via MCP
3. Query topology (face count, edge flow) at checkpoints
4. Separate clothing meshes via MCP
5. Organize character collection hierarchy

## Constraints

### MUST DO
- Establish proportions before facial detail
- Plan edge loops for planned deformations
- Separate clothing/accessories as unique meshes
- Match style skill direction (stylized vs realistic)
- Validate topology before rigging handoff

### MUST NOT DO
- Triangles on primary deformation surfaces
- Poles at corner of mouth or inner eye
- Single mesh for body + hard surface armor (separate)
- Skip reference for facial likeness work
- Over-poly face before LOD planning

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Facial topology | `references/facial-topology.md` | Face modeling |
| Body proportions | `references/body-proportions.md` | Blockout |
| Pipeline | `../references/asset-pipeline.md` | Phase context |

## Style Integration

| Style | Adjustment |
|-------|------------|
| realistic-style | Full anatomy; 8-head proportion |
| stylized-style | Exaggerated features; 4–5 heads |
| lowpoly-style | Minimal loops; painted detail |
| horror-style | Uncanny proportions; asymmetry |

---
name: creature-artist
description: AAA creature modeling for fantasy, aliens, monsters, and organic creature design with believable anatomy and movement. Use for creature blockouts, muscle flow, bone structure, and animation-ready creature assets in Blender via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: creature, monster, alien, fantasy, dragon, beast, organic design, muscle, anatomy, fauna
  related-skills: sculpting, retopology, rigging, animation
---

# Creature Artist

Believable creature design grounded in anatomy. Movement-informed topology. Fantasy with physical plausibility.

## When to Use

- Fantasy creatures, monsters, aliens
- Quadrupeds, flying creatures, aquatic forms
- Hybrid designs (part animal, part mechanical)
- Boss creatures, enemies, companions

## Design Principles

1. **Anatomy grounding** — Even fantasy references real biology
2. **Silhouette first** — Unique readable shape
3. **Movement logic** — Skeleton supports intended motion
4. **Muscle flow** — Surface forms follow underlying structure
5. **Storytelling** — Design communicates behavior (predator/prey/scavenger)

## Workflow

```
Reference → Skeleton Blockout → Muscle Masses → Surface Forms
    → Detail (sculpt or model) → Retopology → Rig → Animation Test
```

## Creature Types

| Type | Skeleton Base | Key Forms |
|------|---------------|-----------|
| Quadruped | Dog/horse reference | Shoulder hump, haunches |
| Biped | Human/primate | Upright spine, heel plant |
| Flying | Bat/bird | Wing membrane, keel chest |
| Aquatic | Fish/shark | Lateral line, fin placement |
| Serpentine | Snake | Ribcage segmentation |
| Insectoid | Arthropod | Segmented body, jointed legs |

## Muscle Flow

- Origin → Insertion direction visible in surface
- Flexed areas: compressed forms, overlapping skin
- Extended areas: stretched, thinner surface
- Fat deposits: soft transitions (belly, cheeks)
- Scars/armor: break muscle flow intentionally

## Bone Structure Planning

Before surface modeling:
1. Place joint locations (spine segments, limbs)
2. Verify range of motion at each joint
3. Ensure limb attachment supports gait cycle
4. Head/neck connection supports attack/look poses

## Surface Detail Tiers

| Tier | Detail | Method |
|------|--------|--------|
| Primary | Overall mass | Blockout/sphere modeling |
| Secondary | Muscle groups | Sculpt or extrusion |
| Tertiary | Skin folds, veins | Sculpt |
| Micro | Scales, pores, scars | Sculpt + bake to normal |

## Hybrid Creatures

Mechanical + organic:
- Separate meshes: `SM_Creature_Bio`, `SM_Creature_Mech`
- Hard surface joints at organic/mechanical transition
- Rig: mechanical parts use constraints; organic uses weights

## MCP Integration

1. Create skeleton blockout (armature or mesh guides) via MCP
2. Build primary masses with mirror/sphere modeling
3. Hand off to sculpting for detail pass
4. Query proportions against reference scale figure
5. Organize bio/mechanical collections separately

## Constraints

### MUST DO
- Reference real anatomy even for fantasy
- Test silhouette from gameplay camera angle
- Plan rig joints during blockout
- Separate hero detail from background creatures
- Retopologize before rigging

### MUST NOT DO
- Design without movement consideration
- Uniform detail density (hero face/feet get more)
- Skip retopology on sculpted creatures
- Ignore polycount tier (background vs boss)
- Attach limbs without joint clearance

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Quadruped anatomy | `references/quadruped-anatomy.md` | Four-legged creatures |
| Flying creatures | `references/flying-creatures.md` | Wings, flight |
| Pipeline | `../references/asset-pipeline.md` | Phase context |

## Style Integration

| Style | Approach |
|-------|----------|
| realistic-style | Grounded anatomy; PBR skin |
| stylized-style | Exaggerated features; bold shapes |
| lowpoly-style | Minimal surface; texture detail |
| horror-style | Uncanny proportions; exposed anatomy |

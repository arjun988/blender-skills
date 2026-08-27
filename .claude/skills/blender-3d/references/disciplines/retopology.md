
# Retopology

Clean, purposeful topology for deformation, UVs, and performance. Quad-dominant. Animation-ready.

## When to Use

- After sculpting high-poly characters/creatures
- Before rigging any deforming mesh
- Poly reduction while preserving silhouette
- Fixing topology from boolean or scan cleanup

## Workflow

```
High-Poly Reference → Guide Setup → Block Retopo → Loop Refinement
    → Pole Placement → Triangle Cleanup → Validation → UV Handoff
```

## Retopology Methods

| Method | Best For | Speed |
|--------|----------|-------|
| Manual (Poly Build tool) | Hero characters | Slow, best quality |
| Shrinkwrap retopo | Creatures, organic | Medium |
| Quad Remesh (voxel) | Quick blockout retopo | Fast, needs cleanup |
| Instant Meshes (external) | Background assets | Fast |
| Symmetry retopo | Bilateral characters | Medium |

**Production default:** Manual with shrinkwrap for hero; Quad Remesh + cleanup for background.

## Edge Loop Rules

- Loops follow muscle/deformation direction
- One loop per major form change
- Maintain even edge length in deformation zones
- Redirect loops at poles (minimum 3 edges meeting)
- Hide poles at back of head, armpits, groin

## Pole Management

| Location | Acceptable | Avoid |
|----------|------------|-------|
| Top of head | 3–5 pole | — |
| Inner eye corner | Redirect pole | Pole directly at corner |
| Shoulder | 3-edge pole hidden | Star pattern on deltoid |
| Back of knee | Pole in crease | Pole on front of knee |

## Triangle Policy

- Triangles OK on non-deforming static mesh
- Convert tris to quads on face, joints, fingers
- No n-gons on deforming surfaces
- Tris at hidden areas (scalp under hair, mouth interior)

## Polycount Targets

See `polycount-budgets.md` (shared). Retopo is where budget is enforced.

## Shrinkwrap Retopo Setup

```
1. Duplicate high-poly to reference collection (hidden in render)
2. Create retopo mesh with Poly Build / manual extrude
3. Shrinkwrap modifier → Target: high-poly
4. Snap to face with project individual elements
5. Validate shrinkwrap distance (no intersection)
```

## Validation Checklist

- [ ] Quad-dominant on all deformation areas
- [ ] Edge loops support planned rig joints
- [ ] No non-manifold geometry
- [ ] Silhouette matches high-poly reference
- [ ] Polycount within budget
- [ ] Poles placed at acceptable locations
- [ ] Mesh manifold and watertight (if required)

## MCP Integration

1. Create retopo mesh object via MCP
2. Apply shrinkwrap modifier via MCP
3. Query face/edge count during retopo
4. Compare silhouette via MCP render/query
5. Transfer to `COL_Geo_LowPoly` collection

## Constraints

### MUST DO
- Retopo before rigging deforming meshes
- Preserve silhouette vs high-poly reference
- Plan loops for facial expressions (characters)
- Enforce polycount budget
- Validate manifold before UV pass

### MUST NOT DO
- Auto-retopo without manual cleanup (hero assets)
- Leave n-gons on deformation surfaces
- Skip validation against reference
- Retopo without knowing rig requirements
- Uniform density (more density at face/hands)

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Facial retopo | `references/facial-retopo.md` | Character faces |
| Game vs cinematic | `references/game-cinematic-topo.md` | Budget decisions |


## Appendix: facial-retopo

# Facial Retopology

## Loop Targets

Minimum loops for game facial animation:

| Region | Loops |
|--------|-------|
| Eye | 3 concentric around socket |
| Mouth | 6–8 loops for lip sync |
| Brow | 2 loops above each eye |
| Jaw | 1 loop following jawline to chin |

## Pole Strategy

Redirect poles to:
- Top of cranium (hidden by hair)
- Inside mouth cavity
- Back of neck

## Eye Socket

- Inner corner: 5-edge pole acceptable if offset from corner
- Eyelid loops must support blink without collapsing

## Mouth Corner

Dedicated loop from upper lip → corner → lower lip → jaw.
Never terminate lip loop at corner without continuation.

## Nose

- Bridge loop connects to forehead loop
- Nostril: enclosed loop; avoid triangle fan at tip
- Optional: separate nostril interior mesh (non-deforming)

## Edge Density

- Face: tighter edge spacing (more loops)
- Back of head: reduce density progressively
- Ears: separate topology island acceptable

## Validation Poses

Test retopo mesh with shape keys or rough bone test:
- Blink, smile, jaw open, brow raise, frown

## Appendix: game-cinematic-topo

# Game vs Cinematic Topology

## Game Character

| Aspect | Target |
|--------|--------|
| Triangles | 15k–40k (platform dependent) |
| Loops | Minimum for required animations only |
| Fingers | 3 segments; reduce to mitten for LOD |
| Face | 6–8 mouth loops if dialog; less if none |
| Poles | Hidden aggressively |

## Cinematic Character

| Aspect | Target |
|--------|--------|
| Triangles | 50k–200k+ |
| Loops | Full expression range |
| Fingers | Full articulation |
| Face | Full lip sync + micro-expression |
| Poles | More tolerance with displacement maps |

## Decision Matrix

| Requirement | Topology Level |
|---------------|----------------|
| Background NPC | Low: no face loops |
| Gameplay character | Medium: basic face |
| Cutscene hero | High: full face |
| Film/cinematic only | Highest: micro-detail zones |

## Optimization Without Quality Loss

- Remove loops from areas under clothing/armor
- Reduce knuckle loops on non-interactive characters
- Bake normal detail from sculpt instead of geometry
- Separate head mesh for LOD swap

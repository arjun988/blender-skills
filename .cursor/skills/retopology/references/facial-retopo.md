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

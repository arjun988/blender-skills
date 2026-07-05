# Modifier Stack Reference

## Boolean Workflow

```
1. Ensure both operands have applied scale
2. Use exact/overlap solver for mechanical cuts
3. Keep boolean live; duplicate result for backup
4. Apply bevel AFTER boolean (bevel modifier below boolean in stack = wrong)
5. Correct order: Boolean → Bevel → Weighted Normal
```

## Bevel Settings

| Context | Width | Segments | Profile |
|---------|-------|----------|---------|
| Hard surface panel | 0.001–0.005m | 2–3 | 0.5 |
| Chamfer edge | 0.002–0.01m | 1–2 | 0.5 |
| Soft edge | 0.001m | 3–5 | 0.7 |

Limit bevel to marked edges or weight groups for control.

## Mirror Modifier

- Use bisect for half-model workflows
- Clip enabled to prevent center overlap
- Merge threshold: 0.001m default
- Apply only when center loop is clean

## Array Modifier

- Use constant offset for modular pieces
- Fit type: Fixed Count for known repetitions
- Merge vertices at array boundaries when seamless

## Subdivision Surface

- Only on quad-dominant topology
- Level 1 for preview, Level 2 max for hero assets
- Support loops required at hard edges
- Never subsurf boolean results without cleanup

## Common Stack Examples

**Modular wall panel:**
```
Mirror → Solidify → Bevel (weight) → Weighted Normal
```

**Repeated floor tile:**
```
Array → Bevel → Weighted Normal
```

**Blockout (temporary):**
```
Mirror → Array (no bevel yet)
```

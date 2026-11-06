
# Compositing

Pass-aware beauty stack. Subtle grade. Delivery-ready outputs.

## When to Use

- Final beauty composites from Cycles/Eevee
- Grade, glare, vignette, chromatic subtlety
- Pass recombination (diffuse, glossy, volume, cryptomatte)
- Shot delivery plates

## Workflow

```
Enable passes → Render multilayer EXR (or needed passes)
  → Compositor graph → Grade → FX (glare/fog glow)
  → Output viewer + File Output → Validate exposure
```

## Recommended Passes

| Pass | Use |
|------|-----|
| Beauty / Combined | Base |
| DiffCol / DiffDir / DiffInd | Relight flexibility |
| GlossDir / GlossCol | Spec control |
| Volume | Smoke/fire isolation |
| Cryptomatte Object/Material | Isolations |
| Mist | Depth grade / fog |

## Beauty Stack (Default)

```
Combined
  → Exposure / Color Balance (AgX-aware)
  → Glare (fog glow / streaks sparingly)
  → Lens distortion (subtle)
  → Vignette (subtle)
  → Output
```

## Grade Rules

1. Fix exposure before creative grade
2. Prefer lift/gamma/gain or color balance over crushed curves
3. Keep skin/product hues plausible
4. Match reference stills with side-by-side

## Outputs

- `OUT_Beauty_[Shot]`
- Optional: `OUT_Alpha`, `OUT_CryptoID`
- Prefer EXR for archival; PNG/JPEG for review

## Constraints

### MUST DO
- Grade on view transform–aware pipeline (AgX)
- Keep creative FX reversible in node graph
- Document exposure/look settings

### MUST NOT DO
- Crush blacks to hide lighting problems
- Over-glare every bright pixel
- Flatten multilayer to JPEG as only archive

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Pass Stack | `references/pass-stack.md` | When needed |
| Grade Presets | `references/grade-presets.md` | When needed |
| Delivery Outputs | `references/delivery-outputs.md` | When needed |


## Appendix: delivery-outputs

# Delivery Outputs

- Review: PNG/JPEG sRGB
- Archive: multilayer EXR
- Web: compressed beauty + optional short mp4 from OpenGL/Eevee preview

## Appendix: grade-presets

# Grade Presets (Starting Points)

| Look | Moves |
|------|-------|
| Neutral product | Exposure only |
| Cinematic cool | Slight cyan shadows, warm highlights |
| Horror sick | Desaturate, green-push shadows, crushed but not clipped |
| Neon night | Magenta/cyan contrast, controlled bloom |
| Archviz clean | Soft contrast, accurate whites |

Fix exposure before creative grade.

## Appendix: pass-stack

# Recommended Pass Stack

Combined → Exposure → Balance → Glare (subtle) → Distortion (subtle) → Vignette → Out

Optional isolates: Cryptomatte, Volume, Mist, Specular.

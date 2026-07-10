---
name: compositing
description: Blender compositor workflows for beauty stacks, render passes, color grade, glare, and delivery outputs via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: compositor, compositing, grade, beauty pass, render passes, cryptomatte, glare, vignette, color correction, post
  related-skills: rendering, lighting, lookdev, camera-cinematography, vfx-fx
---

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


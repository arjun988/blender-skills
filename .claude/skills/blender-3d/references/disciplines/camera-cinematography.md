
# Camera Cinematography

Intentional framing. Lens language. Motivated camera moves. Shot-ready cameras.

## When to Use

- Cinematic stills and turntables with purpose
- Animated camera moves (dolly, crane, orbit, handheld)
- Matching reference camera / lens feel
- Shot layout for lookdev and portfolio

## Workflow

```
Shot intent → Camera + target empty → Lens/FOV → Composition
  → Focus/DoF → Move (if animated) → Viewport check → Render/comp
```

## Naming

- `CAM_[Shot]_[Angle]`
- `EMPTY_CamTarget_[Shot]`
- Collection: `COL_Cameras`

## Lens Guide

| Feel | Focal (FF equiv) | Notes |
|------|------------------|-------|
| Wide establishing | 18–28mm | Distortion; watch edges |
| Story / product | 35–50mm | Natural |
| Portrait / hero | 85–135mm | Compression |
| Tele drama | 150mm+ | Flat space |

Sensor fit and resolution affect FOV — set camera sensor intentionally.

## Composition Checklist

- [ ] Subject readable in silhouette
- [ ] Headroom / lead room intentional
- [ ] Horizon level (unless motivated)
- [ ] Foreground / mid / background depth
- [ ] Avoid tangent mergers on edges

## Camera Animation

| Move | Use |
|------|-----|
| Orbit | Product / character showcase |
| Dolly in | Reveal / tension |
| Crane | Scale / establishing |
| Handheld noise | Documentary / horror unease |
| Locked off | Archviz / product purity |

Animate camera + target empties; prefer slow ease-in/out.

## DoF

- Focus on primary subject empty
- F-stop for style: shallow for hero, deeper for environments
- Preview in Eevee; final in Cycles if needed

## Constraints

### MUST DO
- Name cameras and targets
- Match aspect ratio to delivery
- Check framing at start, mid, end of moves

### MUST NOT DO
- Default 50mm for every shot without intent
- Animate FOV wildly unless motivated
- Crop critical silhouette out of frame

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Lens And Composition | `references/lens-and-composition.md` | When needed |
| Camera Move Library | `references/camera-move-library.md` | When needed |
| Dof Guide | `references/dof-guide.md` | When needed |


## Appendix: camera-move-library

# Camera Move Library

| Move | Emotion | Tip |
|------|---------|-----|
| Slow dolly in | Focus / dread | Ease both ends |
| Orbit | Showcase | Keep target empty |
| Crane up | Reveal scale | Start covered |
| Handheld | Unease / doc | Subtle noise only |
| Lock off | Product / archviz | Perfect level |

Name `CAM_Shot_Angle` + `EMPTY_CamTarget_Shot`.

## Appendix: dof-guide

# DoF Guide

- Focus object = subject empty
- Shallow for hero; deeper for environments
- Preview Eevee; confirm Cycles if final
- Avoid focus hunting mid-shot unless motivated

## Appendix: lens-and-composition

# Lens & Composition

| Intent | Lens | Notes |
|--------|------|-------|
| Establish | 18–28 | Watch edge stretch |
| Scene / product | 35–50 | Default story |
| Hero portrait | 85–135 | Compression |
| Surveillance / long | 150+ | Flat space |

Checklist: lead room, headroom, horizon, depth planes, no edge tangents.

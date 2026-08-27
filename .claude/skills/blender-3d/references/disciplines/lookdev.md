
# Lookdev

Material + light + camera loop. Screenshot compare. Stop when it reads.

## When to Use

- Finalizing asset shading before export/portfolio
- Turntable / grey shader checks
- Matching material references
- Bridging `materials` and `lighting` intentionally

## Workflow

```
Clay/grey pass → Base materials → Neutral light rig
  → Beauty light → Screenshot → Gap list → Iterate (≤3–5)
  → Optional grade → QA
```

## Standard Rigs

| Rig | Use |
|-----|-----|
| Neutral 3-point | Evaluate materials fairly |
| HDRI studio | Product / character |
| In-situ scene lights | Final context |

Keep a reusable `COL_Lookdev_Lights` + `CAM_Lookdev_*`.

## Checklist

- [ ] Values read in grayscale
- [ ] Specular roughness believable
- [ ] Edges catch light (bevels/normals)
- [ ] Emissive under control
- [ ] No pure black / pure white traps unless stylized
- [ ] Matches reference palette if provided

## Iteration Rule

Each pass: change one major variable (material OR light OR camera), then screenshot.

## Constraints

### MUST DO
- Grey pass before fancy textures when forms unsure
- Capture screenshots each iteration
- Hand off to `qa-review` before ship

### MUST NOT DO
- Fix modeling problems only with roughness maps
- Infinite tweak loops without gap list

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Lookdev Rig | `references/lookdev-rig.md` | When needed |
| Lookdev Checklist | `references/lookdev-checklist.md` | When needed |


## Appendix: lookdev-checklist

# Lookdev Checklist

- [ ] Greyscale values read
- [ ] Roughness believable
- [ ] Edge highlights present
- [ ] Emissive controlled
- [ ] Reference match (if any)
- [ ] Screenshot each iteration

## Appendix: lookdev-rig

# Lookdev Rig

`COL_Lookdev_Lights`: key / fill / rim
`CAM_Lookdev_Hero` + turntable optional
Grey clay pass before textured beauty

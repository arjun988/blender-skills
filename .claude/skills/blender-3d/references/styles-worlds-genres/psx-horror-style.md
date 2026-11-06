# PSX Horror Style

Crunchy low-poly horror. Affine textures. Fog. Limited palette. Tension over fidelity.

## When to Use

- PS1-era horror game looks
- Puppet Combo / retro survival horror vibes
- When `horror-style` needs explicit PSX constraints

## Core Tenets

1. **Low poly, high dread** — Few tris, strong shapes
2. **Texture crunch** — Low-res, nearest filtering feel
3. **Vertex / affine warping cues** — Subtle wobble optional
4. **Fog + darkness** — Hide draw distance sins
5. **Analog grit** — VHS/CRT via compositing sparingly

## Vs Related Styles

| Skill | Role |
|-------|------|
| `horror-style` | Broad psychological horror direction |
| `lowpoly-style` | General PS1/PS2 / Lethal Company |
| `psx-horror-style` | Horror + PSX crunch specifically |

## Modeling

- 100–800 tris for many props
- Characters chunky; faces minimal
- Interiors modular, repetitive, oppressive

## Materials / Textures

- 64–256px textures common
- Limited palette; indexed feel
- Flat shading or very low smooth
- Emissive screens as narrative props

## Lighting & Camera

- Single practical lights; deep shadows
- Low camera, narrow spaces
- Fog/mist mandatory for depth
- Optional handheld noise (`camera-cinematography`)

## Compositing Extras

- Slight blur / chromatic aberration
- Posterize / crush colors carefully
- Film grain / VHS overlay subtle

## Constraints

### MUST DO
- Keep poly and texture budgets intentionally low
- Prioritize fog, sound-design-friendly spaces
- Stage sparse narrative props

### MUST NOT DO
- Modern PBR microdetail as primary look
- Bright clean global illumination

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Psx Horror Budgets | `references/psx-horror-budgets.md` | When needed |
| Psx Horror Palette | `references/psx-horror-palette.md` | When needed |


### Appendix: psx-horror-budgets

# PSX Horror Budgets

| Asset | Tris | Texture |
|-------|------|---------|
| Prop | 50–400 | 64–128px |
| Character | 200–800 | 64–256px |
| Room chunk | 500–2k | atlas 256–512 |

Nearest filter feel. Fog hides draw distance.

### Appendix: psx-horror-palette

# Palette & Light

Desaturated, sickly greens, cold cyan, warm practicals sparingly.
Single practical light + fog. CRT/VHS via compositing subtle.

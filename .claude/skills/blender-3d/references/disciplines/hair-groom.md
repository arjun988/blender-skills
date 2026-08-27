
# Hair Groom

Believable hair flow. Scalp coverage. Cards for games. Curves/particles for cinematic.

## When to Use

- Character scalp hair, beards, brows
- Creature fur / mane / whiskers
- Game hair-card generation and placement
- Cinematic curve/particle grooms

## Path Decision

```
Target = Game / real-time  → Hair cards (+ optional proxy curves)
Target = Cinematic        → Curves or particle hair + materials
Target = Both             → High groom → bake cards / textures
```

## Workflow (Game Cards)

```
Scalp mesh → Guide curves → Card strips along flow
  → Atlas UVs → Alpha/normal hair texture → LOD cards → Export
```

## Workflow (Cinematic)

```
Scalp → Particle/curve groom → Clump/frizz/noise
  → Hair shader (melanin/roughness) → Render test → Cache if needed
```

## Groom Principles

1. **Flow first** — Primary direction before flyaways
2. **Density hierarchy** — Dense roots, controlled tips
3. **Clumps** — Hair reads as groups, not spaghetti
4. **Silhouette** — Outer shape more important than strand count
5. **Scalp bleed** — Avoid bald patches at hairline

## Card Guidelines

| LOD | Cards (guide) | Notes |
|-----|---------------|-------|
| Hero close-up | 80–200 | Layered shells |
| Standard | 30–80 | Main masses |
| Distant | 8–20 | Cap + few strips |

- Name: `SM_HairCard_[Region]`
- Atlas: `T_Hair_[Name]_RGBA` (alpha in A)
- Prefer opacity clip or hashed for Eevee preview

## Naming

- Guides: `CRV_HairGuide_[Region]`
- Cards: `SM_HairCard_[Region]`
- Collection: `COL_Hair_[Character]`

## Constraints

### MUST DO
- Establish hairline and parting early
- Match card UVs to atlas layout
- Test silhouette from game camera angles

### MUST NOT DO
- Uniform card width everywhere
- Skip root density near scalp
- Over-detail flyaways before primary masses

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Hair Card Atlas | `references/hair-card-atlas.md` | When needed |
| Groom Flow Regions | `references/groom-flow-regions.md` | When needed |
| Cinematic Vs Game | `references/cinematic-vs-game.md` | When needed |


## Appendix: cinematic-vs-game

# Cinematic vs Game Hair

| | Game cards | Cinematic curves/particles |
|--|------------|----------------------------|
| Density | Card shells | Strand/curve count |
| Motion | Bones / soft bones / vertex wind | Sim or deform |
| Shader | Alpha clip/hash + anisotropic approx | Principled Hair |
| LOD | Drop shells | Reduce children |

## Appendix: groom-flow-regions

# Scalp Flow Regions

Map guides by region before cards/particles:
1. Hairline / bangs
2. Top / crown
3. Sides / temples
4. Back / nape
5. Optional facial (beard, brows)

Each region: primary flow arrow + clump count + length range.

## Appendix: hair-card-atlas

# Hair Card Atlas

## Layout
- Vertical strands preferred for mip stability
- Pack clump variants: thin / medium / wide / wispy
- Leave 4–8px padding

## Channels
- RGB: albedo or ID tint source
- A: opacity
- Optional second map: normal + AO packed

## Card Mesh
- 2–4 segments lengthwise for bend
- Root at pivot; taper tip
- Slight random yaw per card instance

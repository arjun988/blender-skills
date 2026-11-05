# Polycount Budgets

Reference targets for game-ready assets. Adjust per project spec; these are AAA-informed defaults.

## Props

| Tier | Triangles | Use Case |
|------|-----------|----------|
| Hero | 15,000–50,000 | Player-held, close-up interactive |
| Standard | 5,000–15,000 | Scene props, mid-distance |
| Background | 500–5,000 | Distant filler, clutter |
| Small | 100–500 | Coins, bolts, small debris |

## Characters

| Tier | Triangles | Use Case |
|------|-----------|----------|
| Hero | 50,000–100,000 | Player character, cutscenes |
| Standard NPC | 20,000–40,000 | Background characters |
| Crowd | 5,000–10,000 | Distant crowds, impostors |
| Mobile hero | 15,000–30,000 | Mobile/ Switch targets |

## Environment

| Asset | Triangles | Notes |
|-------|-----------|-------|
| Modular wall (2m) | 200–800 | Repeats frequently |
| Modular floor tile | 100–400 | Instanced |
| Hero building section | 5,000–20,000 | Landmark structures |
| Rock (hero) | 1,000–5,000 | Scatter dependent |
| Tree (realistic) | 5,000–15,000 | Use cards/impostors at distance |
| Tree (stylized/lowpoly) | 200–2,000 | Style dependent |

## Vehicles

| Type | Triangles |
|------|-----------|
| Hero vehicle | 80,000–200,000 |
| Drivable (gameplay) | 30,000–80,000 |
| Background vehicle | 5,000–15,000 |

## Weapons

| Type | Triangles |
|------|-----------|
| First-person hero | 10,000–30,000 |
| Third-person | 5,000–15,000 |
| Background | 500–2,000 |

## Style Modifiers

| Style | Budget Adjustment |
|-------|-------------------|
| Lowpoly (PS1/PS2) | 50–90% reduction |
| Horror (sparse detail) | 30–50% reduction |
| Stylized | Similar to standard; detail in texture |
| Realistic AAA | Upper range; LODs mandatory |

## LOD Guidelines

| LOD | Triangle % | Distance Multiplier |
|-----|------------|---------------------|
| LOD0 | 100% | 0–10m |
| LOD1 | 50% | 10–25m |
| LOD2 | 25% | 25–50m |
| LOD3 | 10% | 50m+ |

## Texture Budgets

| Asset Tier | Resolution |
|------------|------------|
| Hero | 2048–4096 |
| Standard | 1024–2048 |
| Background | 512–1024 |
| Tiling surfaces | 1024–2048 (tiling) |
| Trim sheets | 2048–4096 shared |

## Validation

When polycount exceeds budget:
1. Remove unseen backfaces/interior geometry
2. Bake detail to normal maps
3. Reduce bevel segments on distant edges
4. Replace geometry with normal map detail
5. Create LOD chain before final approval

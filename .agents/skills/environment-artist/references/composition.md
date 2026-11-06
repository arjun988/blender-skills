# Environment Composition

## Layer Structure

| Layer | Content | Detail Level |
|-------|---------|--------------|
| Foreground | Framing elements | Medium |
| Midground | Gameplay/interaction | Hero |
| Background | Skyline/fog silhouettes | Low |

## Leading Lines

Use roads, rivers, walls, light shafts to guide eye toward:
- Objective marker
- Threat reveal
- Narrative focal point

## Rule of Thirds

Place hero elements at intersection points.
Horizon on upper or lower third — not center (unless symmetrical intent).

## Value Hierarchy

Brightest area = player attention target.
Darkest area = concealment or negative space.
Avoid uniform brightness across vista.

## Scale Cues

Include known-size objects:
- Doors (2.1m)
- Human figure (1.7m)
- Vehicles
- Furniture

## Negative Space

Rest areas between detail clusters prevent visual fatigue.
Horror: increase negative space for tension.

## Modular Scene Assembly

```
1. Block terrain/ground plane
2. Place hero modular structures
3. Add midground props (instanced)
4. Background low-poly silhouettes + fog
5. Validate from player camera height/path
```

## Camera Path Validation

Walk player path in viewport at eye height (1.6m).
Check readability every 10m of travel.

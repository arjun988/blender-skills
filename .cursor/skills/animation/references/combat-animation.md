# Combat Animation Timing

## Attack Phases

| Phase | Frames (30fps) | Description |
|-------|----------------|-------------|
| Anticipation | 4–8 | Wind-up, weight shift |
| Action | 2–4 | Strike — fastest phase |
| Follow-through | 4–8 | Momentum continuation |
| Recovery | 8–16 | Return to idle |

**Rule:** Action phase is shortest; anticipation sells the hit.

## Hit Reaction

- 2–4 frames impact pose
- 8–12 frames stagger/recoil
- Snap to impact for game feel; smooth for cinematic

## Combo Timing

| Combo Hit | Total Frames |
|-----------|--------------|
| Light 1 | 20–24 |
| Light 2 | 18–22 |
| Heavy | 30–40 |

Allow cancel windows at 60% of animation for responsive gameplay.

## Root Motion

Document per animation:
- **In-place:** Root locked; engine applies movement
- **Root motion:** Hip bone translates; bake to root

## Silhouette Readability

Exaggerate weapon arc during action phase.
Freeze-frame test: silhouette must read attack direction.

## Game Export

- No foot sliding on in-place attacks
- Loop recovery to idle seamlessly
- Name: `AN_Char_Attack_Light_01`

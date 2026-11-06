
# Animation

Game-ready motion with clean keyframes. Readable silhouettes in motion. Engine-compatible export.

## When to Use

- Character locomotion (walk, run, idle)
- Combat animations
- Mechanical/prop animation
- Camera animation
- Object animation with constraints

## Workflow

```
Reference → Blocking → Breakdown → Splining → Polish
    → Cycle Validation → NLA Strip → Export
```

## Locomotion Cycles

| Cycle | Key Poses | Frames (30fps) |
|-------|-----------|----------------|
| Walk | Contact, Down, Pass, Up × 2 | 24–32 |
| Run | Contact, Drive, Flight, Recovery | 16–24 |
| Idle | Breathe, weight shift, blink | 60–120 loop |

Naming: `AN_[Char]_[Action]_[Variant]`

## Animation Principles (Applied)

1. **Timing** — Weight through spacing
2. **Arcs** — Natural limb paths
3. **Overlap** — Secondary motion offset
4. **Anticipation** — Wind-up before action
5. **Exaggeration** — Style-dependent (see style skills)

## Mechanical Animation

- Use constraints over bone deformation
- Hinge: Limit Rotation constraint
- Pistons: Stretch-to or Copy Location
- Gears: Driver for synchronized rotation
- Doors: Empty pivot + rotation keyframes

## Graph Editor Workflow

```
1. Block stepped keys (Constant interpolation)
2. Splining: Bezier with auto handles
3. Ease: Weighted handles for acceleration
4. Cycle: Copy first/last frame; verify loop seam
5. Clean: Remove redundant keys
```

## NLA for Game Export

```
1. Action created and named per convention
2. Push down to NLA strip
3. Strip set to Repeat for cycles
4. Single strip active for export
5. Scale: 1.0; no NLA time remapping unless intentional
```

## Camera Animation

- Smooth Bezier interpolation always
- Avoid sudden direction changes
- Match focal length to subject scale
- Camera shake: noise modifier on location (subtle)

## MCP Integration

1. Insert keyframes via MCP if supported
2. Query action names and frame ranges
3. Validate bone/object animation data exists pre-export
4. Set frame range via MCP
5. Export animation with rig via export-pipeline

## Game-Ready Requirements

- [ ] Root motion decision documented (in-place vs root motion)
- [ ] Loop seam invisible (walk/idle/run)
- [ ] No bone scale keyframes (engine issues)
- [ ] Animation length matches engine state machine
- [ ] Facial animation on separate action layer if needed
- [ ] Frame rate: 30fps default (confirm project spec)

## Constraints

### MUST DO
- Reference video for locomotion
- Block in stepped mode before splining
- Name actions `AN_` prefix
- Test cycle loop before export
- Match animation style to art direction

### MUST NOT DO
- Linear interpolation on organic motion
- Scale keyframes on rig bones
- Over-animate idle (subtle is better)
- Export without action assigned to NLA
- Skip root motion documentation

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Walk cycle breakdown | `references/walk-cycle.md` | Locomotion |
| Combat timing | `references/combat-animation.md` | Action games |


## Appendix: combat-animation

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

## Appendix: walk-cycle

# Walk Cycle Breakdown

## Contact (Frame 0/12)

- Heel strike on contact foot
- Opposite foot passing
- Hips at neutral height
- Arm opposite to leg forward

## Down (Frame 3/15)

- Contact leg bent, weight settling
- Hips lowest point
- Passing foot approaching ground

## Passing (Frame 6/18)

- Contact leg straight under body
- Passing leg mid-swing
- Hips rising

## Up (Frame 9/21)

- Push off contact leg
- Hips highest point
- Toes leaving ground on back foot

## Cycle Length

24 frames @ 30fps = comfortable walk. 16 frames = brisk/stylized.

---
name: animation
description: Game-ready animation in Blender including walk/run/idle cycles, combat, mechanical animation, camera animation, constraints, Graph Editor, and NLA workflows via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: animation, animate, walk cycle, run cycle, idle, combat, NLA, graph editor, keyframe
  related-skills: rigging, blender-modeler, export-pipeline
---

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


# Rigging

Functional rigs supporting intended motion. Clean deformation. Engine-compatible bone hierarchies.

## When to Use

- Character/creature deformation rigs
- Mechanical constraint rigs
- Facial expression rigs
- Prop rigs (doors, vehicles, weapons)
- Before any animation work

## Workflow

```
Skeleton Design → Bone Placement → Hierarchy → Constraints/IK
    → Weight Painting → Deformation Test → Export Prep
```

## Armature Naming

Prefix: `ARM_[AssetName]`
Bones: `[side]_[region]_[name]` — e.g., `L_arm_upper`, `spine_01`, `jaw`

## Bone Hierarchy

```
ARM_Character
├── root
├── spine_01 → spine_02 → spine_03
│   ├── L_clavicle → L_arm_upper → L_arm_lower → L_hand
│   └── R_clavicle → R_arm_upper → R_arm_lower → R_hand
├── L_leg_upper → L_leg_lower → L_foot → L_toe
└── R_leg_upper → R_leg_lower → R_foot → R_toe
```

## IK vs FK

| Use IK | Use FK |
|--------|--------|
| Legs (ground contact) | Spine (flexible arc) |
| Arms (hand placement) | Shoulder overlap |
| Feet planting | Finger detail |
| Mechanical reach | Whip/tail motion |

Standard: IK legs, FK spine; switchable arms for game characters.

## Constraints

| Constraint | Use |
|------------|-----|
| IK | Limb positioning |
| Copy Rotation | Mechanical sync |
| Limit Rotation | Joint ranges |
| Stretch To | Tentacles, pistons |
| Child Of | Weapon attach/detach |
| Shrinkwrap | Ground contact (use carefully) |

## Weight Painting

```
1. Automatic weights as starting point only
2. Clean weights: normalize per vertex (max 4 influences)
3. Smooth problematic areas (shoulders, hips)
4. Test extreme poses: T-pose, arms up, crouch, jaw open
5. Gradient weights at joints — no hard 1.0/0.0 at bend center
```

## Mechanical Rigs

- Empty objects as control handles
- Constraints instead of weight painting
- Hinge limits match real joint ranges
- Parent hierarchy mirrors mechanical assembly

## Facial Rigs

| Approach | Use Case |
|----------|----------|
| Bone-based | Game characters |
| Shape keys | Cinematics, dialog |
| Hybrid | Hero game characters |

Minimum game facial: jaw open, blink L/R, brow up/down.

## Drivers

- Gear rotation sync
- Auto eyelid blink
- Weapon reload mechanism
- Procedural antenna/wire motion

## MCP Integration

1. Create armature via MCP
2. Parent mesh with automatic weights via MCP
3. Query bone count and hierarchy
4. Validate weight groups via MCP if supported
5. Export armature with mesh via export-pipeline

## Deformation Test Poses

- T-pose / A-pose (bind pose)
- Arms fully raised
- Deep crouch
- Neck rotation extremes
- Jaw wide open (characters)

## Constraints

### MUST DO
- Rig after retopology complete
- Name bones consistently
- Limit bone influences to 4 per vertex (game engines)
- Test deformation at extremes before animation
- Document control scheme for animators

### MUST NOT DO
- Auto weights without cleanup (hero assets)
- Scale bones in bind pose
- Rig before topology validated
- Skip IK pole targets on limbs
- Mix multiple root bones without documentation

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Humanoid rig | `references/humanoid-rig.md` | Characters |
| Mechanical rig | `references/mechanical-rig.md` | Props, vehicles |


## Appendix: humanoid-rig

# Humanoid Rig

## Required Bones (Minimum Game)

```
root → spine_01 → spine_02 → spine_03 → neck → head
spine_03 → L/R clavicle → upper_arm → lower_arm → hand
root → L/R upper_leg → lower_leg → foot → toe
```

Optional: fingers (3 segments), jaw, eyes (look-at).

## IK Setup

| Chain | IK Target | Pole Target |
|-------|-----------|-------------|
| Left leg | foot.L | knee.L (forward) |
| Right leg | foot.R | knee.R |
| Left arm | hand.L | elbow.L |
| Right arm | hand.R | elbow.R |

## Twist Bones

Split upper_arm/upper_leg into upper + twist + lower for clean deformation:
- `upper_arm_twist`: 33% weight from upper, 66% from lower

## Weight Paint Order

1. Automatic weights
2. Normalize all
3. Fix shoulders/hips (smooth)
4. Test T-pose, arms up, crouch
5. Limit influences to 4 per vertex

## Facial (Game Minimum)

- `jaw` bone: jaw open
- `eye.L/R`: blink (scale or separate lid bones)
- Optional shape keys for dialog hero

## Export

Armature + mesh in same FBX. Apply transforms. No scale keyframes.

## Appendix: mechanical-rig

# Mechanical Rig

## Constraint-First Approach

Mechanical assets use constraints over weight painting:

| Joint Type | Constraint |
|------------|------------|
| Hinge door | Limit Rotation (single axis) |
| Piston | Copy Location (Y only) + Stretch To |
| Gear train | Driver (rotation sync by ratio) |
| Sliding panel | Limit Location (one axis) |
| Hydraulic | Stretch To + Limit Distance |

## Empty Control Hierarchy

```
CTRL_Root (empty)
├── CTRL_Hinge_Main (empty at pivot)
│   └── SM_Door_Panel (child)
├── CTRL_Piston (empty)
│   └── SM_Piston_Rod (child)
└── SM_Static_Frame
```

Animators animate empties; geometry follows.

## Gear Ratio Driver

```python
# Example: driver on gear B rotation
# gear_b.rotation_euler[2] = gear_a.rotation_euler[2] * (-teeth_a / teeth_b)
```

## Export

- Bake visual transform if engine doesn't support constraints
- Or export with actions keyed on control empties
- Document control scheme for animators

## Naming

`ARM_[Asset]_Mech` with bones/empties prefixed `CTRL_` for controls, `DEF_` for deformation (if any).

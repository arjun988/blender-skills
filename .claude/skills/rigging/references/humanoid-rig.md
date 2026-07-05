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

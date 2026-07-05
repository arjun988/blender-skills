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

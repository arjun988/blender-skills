# Naming Conventions

Consistent naming enables pipeline automation, engine import, and team collaboration.

## Prefix Standards

| Type | Prefix | Example |
|------|--------|---------|
| Collections | `COL_` | `COL_Environment`, `COL_Props_Hero` |
| Meshes | `SM_` | `SM_Console_Panel_A` |
| Materials | `MAT_` | `MAT_Metal_Brushed_Steel` |
| Textures | `T_` | `T_Console_N`, `T_Console_BC` |
| Animations | `AN_` | `AN_Door_Open` |
| Armatures | `ARM_` | `ARM_Robot_Loader` |
| Geometry Node Groups | `GN_` | `GN_Scatter_Rocks` |
| Render Cameras | `CAM_` | `CAM_Hero_Shot_01` |
| Lights | `LGT_` | `LGT_Key_Main` |

## Mesh Naming Pattern

```
SM_[Category]_[Descriptor]_[Variant]

Examples:
SM_Weapon_Rifle_A
SM_Prop_Crate_Wood_01
SM_Env_Wall_Module_2m
SM_Char_Hero_Body
```

## Material Naming Pattern

```
MAT_[SurfaceType]_[Descriptor]

Examples:
MAT_Metal_Painted_Red
MAT_Fabric_Canvas_Dirty
MAT_Glass_Frosted
MAT_Emissive_Screen_Green
```

## Texture Naming Pattern

```
T_[Asset]_[MapType]

Map suffixes:
_BC  Base Color / Albedo
_N   Normal
_ORM Occlusion/Roughness/Metallic packed
_R   Roughness
_M   Metallic
_AO  Ambient Occlusion
_E   Emission
_H   Height
```

## Collection Hierarchy

```
COL_ProjectName
├── COL_Reference
├── COL_Blockout
├── COL_Geo
│   ├── COL_Geo_Hero
│   ├── COL_Geo_Background
│   └── COL_Geo_LOD
├── COL_Collision
├── COL_Lights
├── COL_Cameras
└── COL_Export
```

## LOD Naming

```
SM_AssetName_LOD0   (highest detail)
SM_AssetName_LOD1
SM_AssetName_LOD2
SM_AssetName_LOD3   (lowest / impostor)
```

## Collision Naming

```
SM_AssetName_COL     (simple proxy)
SM_AssetName_COL_UBX (Unreal box convention)
SM_AssetName_COL_UCX (Unreal convex)
```

## Rules

- Use PascalCase after prefix with underscores as separators
- No spaces; use underscores
- Sequential numbers: `_01`, `_02` not `_1`, `_2`
- Descriptive, not generic (`SM_Thing` is invalid)
- Match mesh name to material instance where 1:1
- Keep names under 64 characters for engine compatibility

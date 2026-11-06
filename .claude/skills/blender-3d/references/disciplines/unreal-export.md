
# Unreal Export

UE-ready FBX. Correct centimeter scale awareness. UCX collision. LOD and socket naming.

## When to Use

- Static mesh or skeletal mesh to Unreal
- UCX/UCLX collision export
- LOD chain import
- Socket / pivot setup for gameplay

## Pre-Flight

1. `asset-optimization` PASS
2. `lod-pipeline` for LOD0–N
3. `collision-proxy` for UCX meshes
4. Apply scale; pivots at intended UE origin

## Scale Note

Unreal is centimeter-based. Common approaches:
- Model in meters in Blender, export FBX with unit conversion / 0.01 awareness per project pipeline
- Or work to project-documented scale and verify with a 100cm reference

**Always measure a known edge after import.**

## FBX Defaults (Static)

```
Selected Objects
Apply Scalings: FBX All
Forward: -Z Forward
Up: Y Up
Mesh: ON
Smoothing: Face
```

## Naming for UE

| Type | Pattern |
|------|---------|
| Static mesh | `SM_Name` |
| Skeletal | `SK_Name` |
| Skeleton | `SKEL_Name` |
| LOD | `SM_Name_LOD0` … |
| Collision | `UCX_SM_Name_01` |
| Socket empty | `SOCKET_Name` |

## Collision

- Prefer convex UCX pieces over complex mesh colliders
- Multiple UCX meshes supported
- See `collision-proxy`

## Skeletal

- UE mannequin-oriented proportions when required
- Root bone; no leftover Blender deform leftovers
- Export morph targets if needed (shape keys)

## Verify in Unreal

- [ ] Scale (door ~200cm, character ~180cm)
- [ ] Collision wireframe
- [ ] LODs auto-detected
- [ ] Materials / texture sampling
- [ ] Sockets transform

## Constraints

### MUST DO
- Confirm scale with known-dimension test
- Prefix collision with `UCX_`
- Validate LODs and materials after import

### MUST NOT DO
- Export without collision plan for physics actors
- Mix unit systems undocumented

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Unreal Checklist | `references/unreal-checklist.md` | When needed |
| Ucx Naming | `references/ucx-naming.md` | When needed |


## Appendix: ucx-naming

# UCX Naming

```
UCX_SM_Asset_01
UCX_SM_Asset_02
```

Convex only. Same pivot as render mesh. Multiple pieces OK.

## Appendix: unreal-checklist

# Unreal Import Checklist

- [ ] Known dimension test (door ~200cm)
- [ ] `SM_` / `SK_` naming
- [ ] `UCX_` collision associated
- [ ] LODs detected
- [ ] Nanite decision documented (if used)
- [ ] Sockets correct
- [ ] Materials / texture sampling

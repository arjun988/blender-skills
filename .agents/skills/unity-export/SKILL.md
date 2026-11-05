---
name: unity-export
description: Unity-specific Blender export for scale, axis, materials, humanoid/generic rigs, LODs, and collision import via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: Unity, Unity export, Unity FBX, Unity GLTF, humanoid, Unity materials, Unity LOD, Unity collision
  related-skills: export-pipeline, lod-pipeline, collision-proxy, asset-optimization, materials
---

# Unity Export

Unity-ready transforms, materials, LODs, and collision. Prefer GLB/GLTF for modern; FBX for legacy/animation.

## When to Use

- Shipping assets to Unity
- Humanoid character export
- Prefab-oriented mesh splits and LODs

## Pre-Flight

1. `asset-optimization` PASS
2. `lod-pipeline` if LODs required
3. `collision-proxy` if physics required
4. Apply transforms; correct pivots

## Recommended Formats

| Case | Format |
|------|--------|
| Static mesh modern | GLB |
| Animated / humanoid | FBX |
| Simple props | GLB or FBX |

## Transform Defaults

```
Unit: Meters (Unity 1 unit = 1m)
Forward: -Z (Blender) → verify in Unity
Scale Factor: 1.0 (fix if model tiny/huge)
```

## Materials

- Prefer single material slots matching Unity workflow
- Metallic-Roughness for GLTF
- Embed or provide textures beside FBX
- Name materials `MAT_` consistently

## Characters

- T-pose or A-pose per project
- Root bone at origin; hips correctly placed
- Humanoid: clear bone naming; test Avatar mapping
- Export animations as separate clips when needed

## LODs & Collision

- LOD Group naming: `SM_Name_LOD0..N` or Unity LOD Group meshes
- Collision: convex meshes or Unity primitive colliders from proxies
- See `collision-proxy` for UCX-style naming if using FBX conventions

## Verify in Unity

- [ ] Scale vs reference cube
- [ ] Pivot / prefab placement
- [ ] Normals / tangents
- [ ] Materials assigned
- [ ] LOD transitions
- [ ] Animator clips (if any)

## Constraints

### MUST DO
- Validate before export
- Document scale factor used
- Test import once before declaring done

### MUST NOT DO
- Assume FBX settings without project convention
- Leave unused high-poly LODs in prefab

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Unity Checklist | `references/unity-checklist.md` | When needed |
| Unity Materials | `references/unity-materials.md` | When needed |

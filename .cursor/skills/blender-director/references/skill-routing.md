# Skill Routing Reference

Extended routing tables for the Blender Director.

## By Engine Target

| Engine | Export Skill | Notes |
|--------|--------------|-------|
| Unity | unity-export | GLB/GLTF modern; FBX for humanoid/legacy |
| Unreal | unreal-export | FBX; UCX collision; verify cm scale |
| Godot | godot-export | GLTF/GLB preferred |
| Generic / multi | export-pipeline | Confirm axis and scale; then engine skill if known |

## By Production Phase

| Phase | Lead Skill | Validators |
|-------|------------|------------|
| Reference analysis | blender-director + reference-image-match | reference-analysis-template |
| Blockout | blender-modeler / discipline skill | blender-director |
| Detail pass | discipline skill | asset-optimization |
| UV pass | uv-workflow | texture-workflow |
| Look dev | lookdev + materials | style skill, qa-review |
| Camera / shot | camera-cinematography | rendering |
| FX / sim | vfx-fx / physics-sim / cloth-sim | compositing |
| Reference compare | rendering + lighting | visual-match-checklist |
| Scene layout | scene-assembly + set-dressing | qa-review |
| Performance | asset-optimization + lod-pipeline | collision-proxy |
| Delivery | unity-export / unreal-export / godot-export / export-pipeline | qa-review + validation-checklist |

## Style + Discipline Matrix

|  | Hard Surface | Prop | Vehicle | Environment | Character | Creature |
|--|-------------|------|---------|-------------|-----------|----------|
| Horror | hard-surface + horror-style | prop-artist + horror-style | vehicle-artist + horror-style | environment-artist + horror-style | character-artist + horror-style | creature-artist + horror-style |
| PSX Horror | hard-surface + psx-horror-style | prop-artist + psx-horror-style | vehicle-artist + psx-horror-style | environment-artist + psx-horror-style | character-artist + psx-horror-style | creature-artist + psx-horror-style |
| Lowpoly | hard-surface + lowpoly-style | prop-artist + lowpoly-style | vehicle-artist + lowpoly-style | environment-artist + lowpoly-style | character-artist + lowpoly-style | creature-artist + lowpoly-style |
| Anime | hard-surface + anime-style | prop-artist + anime-style | vehicle-artist + anime-style | environment-artist + anime-style | character-artist + anime-style | creature-artist + anime-style |
| Voxel | hard-surface + voxel-style | prop-artist + voxel-style | vehicle-artist + voxel-style | environment-artist + voxel-style | character-artist + voxel-style | creature-artist + voxel-style |
| Isometric | hard-surface + isometric-style | prop-artist + isometric-style | vehicle-artist + isometric-style | environment-artist + isometric-style | character-artist + isometric-style | creature-artist + isometric-style |
| Stylized | hard-surface + stylized-style | prop-artist + stylized-style | vehicle-artist + stylized-style | environment-artist + stylized-style | character-artist + stylized-style | creature-artist + stylized-style |
| Realistic | hard-surface + realistic-style | prop-artist + realistic-style | vehicle-artist + realistic-style | environment-artist + realistic-style | character-artist + realistic-style | creature-artist + realistic-style |

## Discipline Quick Map

| Signal | Primary |
|--------|---------|
| Furniture, tools, household, kitbash | prop-artist |
| Car, ship, aircraft, mech | vehicle-artist |
| Sci-fi panels, weapons, industrial | hard-surface |
| Trees, grass, foliage | vegetation-artist |
| Hair / fur / cards | hair-groom |
| Garment sim | cloth-sim |
| Smoke / fire / particles | vfx-fx |
| Rigid / destruction | physics-sim |
| Iso / diorama camera | isometric-style + camera-cinematography |
| Archviz plates | archviz |

## Parallel vs Sequential

**Sequential (default):** Modeling → UV → Materials → Lookdev → Export

**Parallel allowed:**
- Material prototyping while UVs in progress (separate collections)
- Lighting setup while optimization runs on duplicate collection
- Reference gathering during blockout review
- Collision proxies while LOD1+ generates

**Never parallel:**
- Retopology before sculpt complete
- Export before validation / qa-review
- Rigging before final topology locked
- Engine export before LOD/collision plan when those are required

# Skill Routing Reference

Extended routing tables for the Blender Director.

## By Engine Target

| Engine | Export Skill | Notes |
|--------|--------------|-------|
| Unity | export-pipeline | GLTF or FBX; Y-up check |
| Unreal | export-pipeline | FBX; scale 1.0; collision COL_ prefix |
| Godot | export-pipeline | GLTF preferred |
| Custom | export-pipeline | Confirm axis and scale |

## By Production Phase

| Phase | Lead Skill | Validators |
|-------|------------|------------|
| Blockout | blender-modeler | blender-director |
| Detail pass | discipline skill | asset-optimization |
| UV pass | uv-workflow | texture-workflow |
| Look dev | materials | style skill |
| Performance | asset-optimization | export-pipeline |
| Delivery | export-pipeline | validation-checklist |

## Style + Discipline Matrix

|  | Hard Surface | Environment | Character | Creature |
|--|-------------|-------------|-----------|----------|
| Horror | hard-surface + horror-style | environment-artist + horror-style | character-artist + horror-style | creature-artist + horror-style |
| Lowpoly | hard-surface + lowpoly-style | environment-artist + lowpoly-style | character-artist + lowpoly-style | creature-artist + lowpoly-style |
| Stylized | hard-surface + stylized-style | environment-artist + stylized-style | character-artist + stylized-style | creature-artist + stylized-style |
| Realistic | hard-surface + realistic-style | environment-artist + realistic-style | character-artist + realistic-style | creature-artist + realistic-style |

## Parallel vs Sequential

**Sequential (default):** Modeling → UV → Materials → Export

**Parallel allowed:**
- Material prototyping while UVs in progress (separate collections)
- Lighting setup while optimization runs on duplicate collection
- Reference gathering during blockout review

**Never parallel:**
- Retopology before sculpt complete
- Export before validation
- Rigging before final topology locked

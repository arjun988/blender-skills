
# Rendering

Appropriate engine selection. Optimized settings. Production render passes.

## When to Use

- Final portfolio/cinematic renders
- Look development validation
- Render pass output for compositing
- Game asset preview renders (Turntable)
- Style validation (realistic vs stylized)

## Engine Selection

| Engine | Use When |
|--------|----------|
| Cycles | Final quality, realistic, portfolio |
| Eevee | Real-time preview, stylized, game look dev |
| Eevee Next | Improved real-time quality (Blender 4+) |

## Workflow

```
Camera Setup → Render Settings → Sample Tests → Full Render
    → Pass Output → Color Management → Delivery
```

## Camera Setup

Naming: `CAM_[Shot]_[Number]`
- Focal length: 35mm (environment), 85mm (hero detail), 24mm (wide horror)
- Depth of field: subject distance focused
- Composition: rule of thirds; leading lines
- Turntable: empty parent rotating 360° for asset preview

## Cycles Settings

| Setting | Preview | Production |
|---------|---------|------------|
| Samples | 64–128 | 512–2048 |
| Denoise | OpenImageDenoise | OpenImageDenoise |
| Max bounces | 8 | 12 |
| Caustics | Off (default) | On if glass/water hero |

## Eevee Settings

| Setting | Value |
|---------|-------|
| Screen Space Reflections | On for metals |
| Ambient Occlusion | On |
| Bloom | Stylized/ emissive scenes |
| Shadow resolution | 2048+ |
| Contact Shadows | Ground contact |

## Render Passes

| Pass | Use |
|------|-----|
| Combined | Final composite |
| Diffuse Direct/Indirect | Relighting |
| Glossy | Reflection control |
| Normal | Compositing effects |
| AO | Contact shadow enhancement |
| Z (Depth) | DOF, fog in comp |
| Cryptomatte | Object masking |
| Emission | Screen glow effects |

## Color Management

```
View Transform: AgX (Blender 4+) or Filmic
Look: Medium Contrast (default) or High Contrast (dramatic)
Exposure: Adjust in compositor, not by blowing lights
```

## Render Optimization

- Use render region for test crops
- Adaptive sampling (Cycles)
- Disable unseen objects in render layers
- GPU rendering default when available
- Persistent data for animation sequences

## Asset Turntable Template

```
1. CAM_Turntable at 3/4 height, 45° angle
2. Empty at asset origin → rotate animation 0–360° (120 frames)
3. 3-point lighting rig
4. Render 1280×1280 or project-specified resolution
5. Output PNG sequence or MP4
```

## Reference Image Validation

When matching a photo/concept (`reference-image-match.md` (shared)):

| Setting | Reference match |
|---------|-----------------|
| Hero camera | Match reference angle before grading |
| AgX Look | Base Contrast default; High Contrast if reference is punchy |
| Exposure | 0.15–0.45 typical; hull must read, not clip white |
| Preview playback | EEVEE, motion blur off, `taa_samples` 1–8 |
| Final still | Render at hero `CAM_*` — compare to reference |
| Compare tool | `get_viewport_screenshot` or bpy render still |

Run `visual-match-checklist.md` (shared) before delivery.

## MCP Integration

1. Configure render engine settings via MCP
2. Setup camera via MCP
3. Trigger test render via MCP if supported
4. Query render settings validation
5. Set output paths via MCP

## Constraints

### MUST DO
- Match render engine to project style
- **Screenshot or render compare** when reference image was provided
- Use denoising for Cycles production renders
- Setup color management before final render
- Render validation turntable for hero assets
- Organize cameras in `COL_Cameras`

### MUST NOT DO
- Production render without sample test
- Ignore color management (sRGB vs Linear)
- Render at excessive resolution without purpose
- Skip render passes when compositing planned
- Use Cycles for real-time game preview needs

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Pass compositing | `references/render-passes.md` | Multi-pass output |
| NPR/stylized render | `references/npr-rendering.md` | Stylized-style projects |
| Reference image match | `reference-image-match.md` (shared) | Photo/concept attached |
| Visual match validation | `visual-match-checklist.md` (shared) | Before delivery |


## Appendix: npr-rendering

# NPR Rendering

## Toon Shader (Shader to RGB)

```
Principled BSDF → Shader to RGB → ColorRamp (2–3 steps) → Output
Light threshold controls cel band count
```

## Outline Methods

| Method | Quality | Performance |
|--------|---------|-------------|
| Inverted hull | Good | Medium |
| Freestyle | Best control | Slow |
| Compositor edge | Post effect | Fast |

## Inverted Hull Setup

```
Solidify modifier (negative thickness)
Flip normals
Assign pure black emission material
Render on top of toon fill
```

## Rim Light in Shader

```
Fresnel (IOR 2.0) → ColorRamp → Mix into Emission
Warm rim color for stylized characters
```

## Eevee NPR Settings

- Bloom ON for emissive accents
- Screen Space Reflections OFF (breaks toon)
- Shadow mode: Half/Li-Sun for hard shadows

## Stylized Style Integration

Coordinate with stylized-style skill for palette and exaggeration levels.

## Appendix: render-passes

# Render Passes

## Essential Passes (Cycles)

| Pass | Compositing Use |
|------|-----------------|
| Combined | Base plate |
| Diffuse Direct | Relight diffuse |
| Diffuse Indirect | Bounce control |
| Glossy Direct | Specular relight |
| Normal | Relight, effects |
| Z (Depth) | DOF, fog, position |
| AO | Contact shadow boost |
| Cryptomatte | Object isolation |
| Emission | Glow comp |

## Compositing Stack (Basic)

```
Combined
  + AO (multiply, factor 0.3)
  + Glare on Emission pass
  + Color correction (Exposure/Contrast)
```

## Cryptomatte Workflow

Enable Cryptomatte object pass → isolate objects in compositor without re-render.

## Multi-Layer EXR

Export OpenEXR multilayer for Nuke/After Effects/Fusion pipelines.

## Game vs Portfolio

Game assets: Combined pass turntable only.
Portfolio: Full pass set for compositing flexibility.

## Denoise

Use Denoise node on Combined or denoise at render time (OpenImageDenoise).
Keep Normal + Albedo passes for OIDN if post-denoising.

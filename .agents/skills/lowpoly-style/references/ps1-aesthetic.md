# PS1 Aesthetic

## Visual Characteristics

| Feature | Technique |
|---------|-----------|
| Low poly | 50–500 tris per prop |
| Affine texture warp | Engine-side; note in export |
| Vertex jitter | Snap to 0.01m grid optionally |
| No filtering | Nearest neighbor textures |
| Low resolution | 128–256px textures |
| Vertex lighting | Per-vertex; avoid smooth shading |
| Fog | Distance fog mandatory for depth |

## Blender Viewport Approximation

- Flat shading on all meshes
- Disable anti-aliasing in render
- Render at 320×240 or 640×480 upscale
- Limit lights to 1 directional + ambient

## Geometry Rules

- No bevel modifiers
- Triangles acceptable
- Merge coplanar faces
- Snap vertices to low-resolution grid for authentic look

## Texture Rules

- Hand-painted or heavy posterization
- Dithering in gradients
- No normal maps (authentic PS1)
- Optional: fake affine by low UV precision

## Color

Limited palette per scene (16–64 colors feel).
Heavy fog color matches palette darkest tone.

## Modern PS1-Style (Lethal Company)

Higher poly than authentic PS1 but same principles:
- Readable silhouettes
- Strong fog
- Simple materials
- Low-res textures with point filtering

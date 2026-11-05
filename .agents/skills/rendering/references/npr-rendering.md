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

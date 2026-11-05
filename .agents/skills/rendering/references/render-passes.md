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

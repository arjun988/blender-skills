# Cinematic Light Rigs

## Three-Point Studio

```
LGT_Key: Area 1m², 45° elevation, 30° azimuth, 5500K, strength 500W
LGT_Fill: Area 2m², opposite side, 5500K, strength 150W (30% key)
LGT_Rim: Spot, behind subject 135°, 3200K warm, strength 300W
```

## Product Hero Shot

```
LGT_Key: Large area softbox simulation (2m²)
LGT_Rim: Two spots L/R behind for edge definition
Backdrop: Gradient world or seamless curve
Camera: 85mm, f/2.8 DOF on hero detail
```

## Environment Golden Hour

```
Sun: 3000K, angle 5° above horizon
Fill: Sky HDRI warm, strength 0.3
Volumetrics: Light density 0.01 for atmospheric haze
```

## Turntable Asset Preview

```
LGT_Key: Area, fixed relative to camera (parent to camera)
LGT_Fill: World HDRI studio neutral
LGT_Rim: Behind asset, subtle
Camera: Orbit empty 360° / 120 frames
Background: Mid-gray for PBR accuracy
```

## Render Settings Pairing

Cycles 256+ samples, Denoise ON, AgX view transform, Medium Contrast look.

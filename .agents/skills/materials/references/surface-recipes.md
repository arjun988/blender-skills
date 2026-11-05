# Surface Material Recipes

Quick Principled BSDF starting points. Adjust per reference.

## Painted Metal (Worn)

- Base Color: reference photo
- Metallic: 0
- Roughness: 0.5–0.7
- Procedural: edge wear mask on roughness

## Concrete (Weathered)

- Base Color: desaturated gray 0.4–0.5
- Roughness: 0.85–0.95
- Bump: subtle noise

## Wood (Oiled)

- Base Color: warm brown
- Roughness: 0.4–0.6
- Anisotropic rotation along grain if available

## Fabric (Cotton)

- Roughness: 0.8
- Sheen: 0.3
- Subsurface: 0.05 (optional)

## Glass (Standard)

- Transmission: 1
- IOR: 1.45
- Roughness: 0.02–0.1

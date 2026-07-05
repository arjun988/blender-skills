# Texel Density

## Calculation

```
Texel Density (px/m) = Texture Resolution / Physical Size (m)

Example: 2048px texture over 2m wall = 1024 px/m
```

## Matching Density

1. Select UV island for reference object
2. Scale all islands to match reference TD
3. Use UV sync tools or manual scaling from known UV-to-world ratio

## Hero vs Background

Same kit: hero modules 1024 px/m, background modules 512 px/m — acceptable if not adjacent in scene.

## UDIM

Each tile maintains independent TD. Document tile assignment per body region.

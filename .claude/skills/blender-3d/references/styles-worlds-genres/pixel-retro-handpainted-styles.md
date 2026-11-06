# Pixel Art Style

Texel discipline. Crisp pixels. Limited palette.

## Tenets
1. Declare target texel size / texture res
2. Nearest filtering intent
3. Limited palette
4. Avoid thin triangles that shimmer
5. Ortho or locked angles help readability

## Reference Guide
| Topic | Reference |
|-------|-----------|
| Texel rules | `references/texel-rules.md` |


### Appendix: texel-rules

# Texel Rules
Pick base (e.g. 16×16, 32×32 props). Align UVs to pixel grid when possible.
No blurry mips in lookdev preview if pixel look is required.

---


# Retro 8-bit Style

Severe palette limits. Chunky read. Sprite logic.

## Constraints
Very low color count, high contrast characters, simple props, avoid gradients unless dithered.


### Appendix: eight-bit-constraints

# 8-bit Constraints
Palette often ≤16 total for a set. Characters read on dark/light backgrounds. No high-res normal maps.

---


# Retro 16-bit Style

Richer palettes than 8-bit. Dither/gradient cues. Still texel-disciplined.


### Appendix: sixteen-bit-notes

# 16-bit Notes
More colors, animated palette tricks optional, chunky but softer than 8-bit. Keep UV texel density even.

---


# HD-2D Style

Pixel actors. 3D stage. Tilted theatrical camera. Creamy DoF.

## Tenets
1. Characters: pixel/billboard or texel-locked
2. Environments: soft 3D with painted textures
3. Strong DoF / god rays
4. Ortho-leaning perspective
5. Warm theatrical keys


### Appendix: hd2d-stack

# HD-2D Stack
Env 3D → pixel characters → depth fog → DoF → bloom subtle → grade warm.

---


# Hand Painted Style

Brushwork in albedo. Geometry supports paint, not microdetail.

## Tenets
1. Paint values in albedo
2. Low roughness variation unless wet/metal accents
3. Soft bevels for paint catch
4. Atlas-friendly for kits
5. Avoid photoreal photo-bashed noise


### Appendix: paint-workflow

# Paint Workflow
Clay → UV → value paint → hue → accent wear → optional soft AO multiply.
Keep normal maps subtle or omit.

---


# Painterly Style

Pigment feel. Soft edges. Illustration lighting.

## Sublooks
- Watercolor: paper grain, bleeds, light washes
- Oil: thicker strokes, richer impasto suggestion in texture

## Tenets
1. Soft terminators
2. Pigment/paper overlays in mat or comp
3. Limited harsh specular
4. Composition like a canvas, not a game HUD shot


### Appendix: oil-painting

# Oil Painting
Richer chroma, visible stroke normals in texture, darker transparent shadows, warm/cool play.

### Appendix: watercolor

# Watercolor
Desaturated washes, darker edges (backruns), paper texture overlay, avoid hard metal spec.

---


# Stop Motion / Craft Style

Handmade physicality. Imperfect edges. Material honesty.

## Sublooks
Claymation, paper craft, felt/plush, wooden puppet

## Tenets
1. Visible craft seams / fingerprints (subtle)
2. Real-world craft materials
3. Slight irregularity in forms
4. Practical light feel
5. Step-like motion if animating (optional)


### Appendix: claymation

# Claymation
Soft rounded forms, fingerprint micro in normal/albedo, matte clay roughness, simple armatures.

### Appendix: paper-craft

# Paper Craft
Planar folds, slight thickness, paper fiber albedo, folded tabs, avoid perfect CAD edges.

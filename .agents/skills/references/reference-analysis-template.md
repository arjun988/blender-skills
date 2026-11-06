# Reference Analysis Template

Copy and fill this **before any Blender MCP operations** when a reference image is provided.

```markdown
## Reference Analysis: [Asset Name]

**Reference:** [attached image / URL / description]
**Existing file:** [path or "new scene"]
**Target:** [game hero / cinematic / portfolio]
**Match goal:** [similar / close match / specific features only]

---

### 1. Subject Identification
- **Type:** [spaceship / prop / character / environment]
- **Style:** [realistic AAA / horror / stylized / lowpoly]
- **Forward axis:** [+Y / +X / other]
- **Scale estimate:** [L × W × H in meters]

### 2. Silhouette & Proportions
- **Primary masses:** [list 3–5 major forms]
- **Proportion notes:** [nose %, mid %, engine % of total length]
- **Shape language:** [blocky modular / curved / tapered / asymmetric]

### 3. Camera (match first)
- **Angle:** [3/4 starboard / side / low hero / top-down]
- **Lens feel:** [~24mm wide / ~35mm / ~50mm portrait]
- **Subject fill:** [% of frame width/height]
- **Planned setup:** `CAM_*` at [position estimate], target at [point]

### 4. Lighting
- **Key light:** [direction, color temp, hardness]
- **Fill:** [level — crushed shadows vs visible detail]
- **Rim/back:** [yes/no, direction]
- **Environment:** [black space / planet / studio / interior]
- **Planned lights:** [LGT_Key_Sun, LGT_Rim_*, etc.]

### 5. Color Palette (hex)
| Role | Hex | Notes |
|------|-----|-------|
| Hull light | # | |
| Hull dark | # | |
| Recess | # | |
| Trim / metal | # | |
| Glass | # | |
| Emissive warm | # | |
| Emissive cool | # | |
| Ambient / sky | # | |

### 6. Materials
- **Surface types:** [brushed metal / painted / rubber / glass]
- **Roughness range:** [matte 0.5+ / satin / gloss]
- **Weathering:** [none / light edge wear / heavy grime]
- **Unique shaders:** [emissive sensors, decals, glow windows]

### 7. Hero Features (must include)
- [ ] [feature 1 — e.g. QUADRILLION decal forward starboard]
- [ ] [feature 2 — e.g. red forward sensor]
- [ ] [feature 3]

### 8. Gap vs Current Scene (if upgrading existing .blend)
| Area | Reference | Current | Priority |
|------|-----------|---------|----------|
| | | | P0/P1/P2 |

### 9. Active Skills
1. blender-director
2. [discipline skill]
3. [style skill]
4. materials → lighting → rendering

### 10. MCP Phase Plan
1. Audit scene + baseline screenshot
2. Camera match
3. Geometry tier 1→2→3
4. Materials from palette
5. Lighting + world
6. Grading + render test
7. Screenshot compare → fix gaps (×3 max)
8. Save + validation
```

## Usage Rules

- **Do not skip** — even if the user says "just fix it quickly"
- **Palette hex values** are required — do not use generic grey without sampling reference
- **Gap table** is required when editing an existing file
- Keep analysis concise; execution matters more than long prose

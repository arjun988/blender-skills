# Hundred Acre Softness — Item 3 Smoke Demo (BRA-5)

First blender-skills try against the fashion croquis sheet
`CROQUIS — Hundred Acre Softness (adult translation)`.

## Look chosen

**Item 3** — mustard crew sweater with red balloon chest graphic, grey trousers, brown lace-up boots.

(Item 5 also preferred; Item 3 is more distinctive for a first readable smoke render.)

## Skills / references used

| Phase | Skill / reference |
|-------|-------------------|
| Orchestration | `blender-director` |
| Reference brief | `references/reference-image-match.md` |
| Figure + clothing | `character-artist` |
| Soft knit/cloth read | `materials` (procedural PBR approx) |
| Naming | `references/naming-conventions.md` |
| Execution | Blender `bpy` background script (MCP not connected in this agent session) |

## Reference analysis (Phase 0)

| Category | Finding |
|----------|---------|
| Subject | Adult male fashion croquis, Winnie-the-Pooh soft palette |
| Silhouette | Elongated fashion proportions; relaxed knit sweater; straight trousers |
| Camera | Front 3/4, full figure, soft croquis presentation |
| Lighting | Soft diffuse studio; cream/off-white ground + backdrop |
| Materials | Mustard knit, grey wool trousers, brown leather boots, matte skin |
| Unique features | Red balloon + string chest graphic; ribbed collar/cuffs/hem |
| Mood | Soft, wholesome, adult-translated nostalgia |

## Outputs

| File | Purpose |
|------|---------|
| `SM_HundredAcre_Item3.blend` | Scene |
| `hundred-acre-item3-smoke.png` | Beauty render |
| `build_item3.py` | Reproducible bpy build |

## Rebuild

```bash
/Applications/Blender.app/Contents/MacOS/Blender \
  --background \
  --python demos/out/build_item3.py
```

## Scope note

Smoke approximation — mannequin proportions + blockout garments, not production retopo/rig/cloth sim. Balloon graphic is a chest mesh decal, not embroidery.

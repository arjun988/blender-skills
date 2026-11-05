# Visual Match Checklist

Run after geometry, materials, lighting, and grading when a **reference image** was provided. Use with `get_viewport_screenshot` or hero camera render.

**Pass threshold:** ≥ 8/10 categories rated "Match" or "Close". Document remaining gaps honestly.

## Comparison Method

1. Place reference image beside viewport screenshot (same camera angle).
2. Rate each category: **Match** / **Close** / **Miss**
3. For each **Miss**, add one actionable fix to the gap list.
4. Re-run after fixes (max 3 iterations).

---

## Camera & Composition

- [ ] Subject faces same general direction as reference
- [ ] Same viewing angle (3/4, side, low, high) — not reversed or top-down mismatch
- [ ] Subject occupies similar % of frame
- [ ] Horizon / vanishing consistent with reference
- [ ] Numpad 0 hero camera usable for review

## Silhouette & Proportions

- [ ] Overall length/width/height ratio reads similarly
- [ ] Major masses in correct positions (nose, mid, tail, engines)
- [ ] No missing large forms visible in reference
- [ ] No extra masses that contradict reference
- [ ] Readable at gameplay/mid distance (not only close-up)

## Depth & Surface Breakup

- [ ] Not a single flat box — panel lines, ribs, or steps visible
- [ ] Recessed vs raised areas create value contrast
- [ ] Chamfers/cylinders break 90° corners where reference shows them
- [ ] Greeble density in same ballpark (not empty or overcrowded)
- [ ] Windows, ports, vents placed on hull surfaces (not floating)

## Materials & Color

- [ ] Hull value range matches (dark enough, not blown white)
- [ ] Light/dark panel contrast present
- [ ] Metal reads as metal (roughness/specular appropriate)
- [ ] Glass/windows distinct from hull
- [ ] Emissive lights correct color (red nav, green starboard, etc.)
- [ ] Decals/logos present if in reference
- [ ] No shared-material animation blowing out hull

## Lighting

- [ ] Key light from same general direction as reference
- [ ] Shadow side not pure black unless reference is
- [ ] Rim/separation on subject edge if reference shows it
- [ ] Emissive elements visible but not overpowering
- [ ] Environment mood matches (space black vs studio vs planet glow)

## Rendering & Grading

- [ ] AgX (or project) color management active
- [ ] Exposure: hull detail visible, highlights not clipped
- [ ] Contrast level similar to reference
- [ ] Animation playback sharp (EEVEE preview settings)
- [ ] Final still acceptable at 1280×720+ hero camera

## Feature Checklist (customize per asset)

- [ ] _[Hero feature 1 from reference analysis]_
- [ ] _[Hero feature 2]_
- [ ] _[Hero feature 3]_

---

## Visual Match Report Template

```markdown
## Visual Match Report: [Asset Name]

**Reference:** [description]
**File:** [path]
**Iteration:** [1/2/3]
**Overall:** PASS / PARTIAL / FAIL

| Category | Rating | Notes |
|----------|--------|-------|
| Camera | Match/Close/Miss | |
| Silhouette | | |
| Depth | | |
| Materials | | |
| Lighting | | |
| Grading | | |

### Top Gaps (fix next)
1. 
2. 
3. 

### Screenshots
- Hero camera render captured: yes/no
- Compared to reference: yes/no
```

## Auto-Fail Conditions

Fail immediately and fix before delivery if any are true:

- Camera shows wrong side of subject (e.g. rear instead of hero 3/4)
- Hull turns fully white during animation playback
- Reference requested full ship but camera shows only a small section
- Structural materials have emission keyframes
- Export mesh visible in viewport blocking review

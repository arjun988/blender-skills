
# QA Review

Screenshot-backed review. Checklist gate. Explicit ship / no-ship.

## When to Use

- Before export or handoff
- After major modeling/lookdev milestones
- Reference-match final compare
- Periodic scene health checks

## Workflow

```
Gather brief budgets → Screenshot key angles → Run checklists
  → List defects (severity) → Fix or reject → Re-verify → Verdict
```

## Required Screenshots

1. 3/4 hero angle
2. Ortho or profile if proportion-critical
3. Wireframe or poly overview (optional but useful)
4. Material/light beauty
5. Vs reference (if reference task)

Use `get_viewport_screenshot` via MCP when connected.

## Checklists (load as needed)

- `validation-checklist.md` (shared)
- `visual-match-checklist.md` (shared) (reference tasks)
- `naming-conventions.md` (shared)
- `polycount-budgets.md` (shared)

## Defect Severity

| Level | Meaning |
|-------|---------|
| Blocker | Wrong scale, broken normals, fails budget badly |
| Major | Silhouette/readability issues, bad pivots |
| Minor | Naming, minor shading, small gaps |
| Note | Optional polish |

## Verdict Template

```markdown
## QA Verdict: [Asset]

**Result:** SHIP / SHIP WITH NOTES / NO-SHIP
**Budgets:** [tris/textures] vs target
**Screenshots:** [listed]
**Blockers:** ...
**Majors:** ...
**Minors:** ...
**Next actions:** ...
```

## Constraints

### MUST DO
- Give explicit verdict
- Attach or capture screenshots for visual claims
- Re-check after fixes before flipping to SHIP

### MUST NOT DO
- Rubber-stamp without screenshots on visual tasks
- Ignore budget overruns without approval

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Qa Verdict Template | `references/qa-verdict-template.md` | When needed |
| Screenshot Angles | `references/screenshot-angles.md` | When needed |


## Appendix: qa-verdict-template

# QA Verdict Template

```markdown
## QA Verdict: [Asset/Shot]
**Result:** SHIP / SHIP WITH NOTES / NO-SHIP
**Budgets:** tris / textures vs target
**Angles captured:**
**Blockers:**
**Majors:**
**Minors:**
**Notes:**
**Retest after:**
```

## Appendix: screenshot-angles

# Required Screenshot Angles

1. Hero 3/4
2. Opposite 3/4 or profile
3. Beauty lit
4. Wire/overview (optional)
5. Reference compare (if any)

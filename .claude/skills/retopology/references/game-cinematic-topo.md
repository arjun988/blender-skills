# Game vs Cinematic Topology

## Game Character

| Aspect | Target |
|--------|--------|
| Triangles | 15k–40k (platform dependent) |
| Loops | Minimum for required animations only |
| Fingers | 3 segments; reduce to mitten for LOD |
| Face | 6–8 mouth loops if dialog; less if none |
| Poles | Hidden aggressively |

## Cinematic Character

| Aspect | Target |
|--------|--------|
| Triangles | 50k–200k+ |
| Loops | Full expression range |
| Fingers | Full articulation |
| Face | Full lip sync + micro-expression |
| Poles | More tolerance with displacement maps |

## Decision Matrix

| Requirement | Topology Level |
|---------------|----------------|
| Background NPC | Low: no face loops |
| Gameplay character | Medium: basic face |
| Cutscene hero | High: full face |
| Film/cinematic only | Highest: micro-detail zones |

## Optimization Without Quality Loss

- Remove loops from areas under clothing/armor
- Reduce knuckle loops on non-interactive characters
- Bake normal detail from sculpt instead of geometry
- Separate head mesh for LOD swap

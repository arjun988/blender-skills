# Scene Organization

## View Layers

| Layer | Contents |
|-------|----------|
| Default | Active modeling |
| Reference | Image planes, scale refs |
| Blockout | WIP blockout only |
| Final | Approved geometry |
| Export | Export-ready duplicates |

## Parenting Strategy

- Parent mechanical sub-parts to root empty: `SM_AssetName_Root`
- Keep pivot at functional point (hinge, grip, floor)
- Use constraints for mechanical relationships (see rigging skill)

## Asset Browser Integration

- Mark finished assets for reuse
- Tag by category: Prop, Env, Char, Weapon
- Include preview render in asset catalog

## Large Scene Management

- One collection per modular kit
- Instance collections, don't duplicate
- Hide blockout collections after approval
- Use collection colors for discipline identification

## Performance in Viewport

- Disable subdiv viewport levels during modeling
- Use wireframe overlay for topology review
- Hide high-poly sculpts when working on low-poly

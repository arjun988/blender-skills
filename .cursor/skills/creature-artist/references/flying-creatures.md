# Flying Creatures

## Wing Anatomy

Bird/bat/dragon wings are modified forelimbs:

| Segment | Bird | Bat | Dragon (fantasy) |
|---------|------|-----|------------------|
| Arm | Short | Long | Variable |
| Forearm | Fused | Elongated | Elongated |
| Hand/fingers | Fused tips | Spread membrane | Multi-finger spread |
| Membrane | Feathers | Skin | Skin or feather hybrid |

## Attachment Point

Wing root at shoulder/upper spine junction.
Large pectoral mass on chest (flight muscles).

## Folded vs Extended

Model both states or ensure topology supports fold:
- Folded: wing along body flank
- Extended: wingspan 2–3× body length (bird), 3–5× (dragon)

## Membrane Topology

Stretch direction: arm → wing tip.
Edge loops run span-wise, not chord-wise.

## Rigging

- 3–5 bones per wing (arm, forearm, finger splits)
- IK target at wing tip for pose control
- Limit rotation on fold axis

## Flight Pose Reference

- Downstroke: wings below body plane
- Upstroke: wings above; body hangs
- Gliding: wings extended, slight dihedral angle

## Silhouette

Wingspan defines creature read at distance — prioritize wing shape over body detail.

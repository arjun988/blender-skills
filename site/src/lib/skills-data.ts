export const SITE_VERSION = '1.3.0'
export const SKILL_COUNT = 94
export const REF_COUNT = 175

export const platforms = [
  {
    name: 'Cursor',
    blurb: 'Project skills in `.cursor/skills/` with Blender MCP via `.cursor/mcp.json`.',
    install: 'Copy-Item -Recurse -Force ".claude\\skills\\*" ".cursor\\skills\\"',
  },
  {
    name: 'Claude Code',
    blurb: 'Native Claude skills under `.claude/skills/` with project `.mcp.json`.',
    install: 'cp -r blender-skills/.claude/skills .claude/skills/',
  },
  {
    name: 'Kiro',
    blurb: 'Drop the same skill folders into your Kiro agent skills path and point MCP at Blender.',
    install: 'Copy .claude/skills into your Kiro skills directory',
  },
  {
    name: 'Codex',
    blurb: 'Use the skill pack as agent instructions/skills alongside Blender MCP for Codex workflows.',
    install: 'Mount .claude/skills (or symlink) into your Codex skills path',
  },
] as const

export type SkillEntry = {
  name: string
  desc: string
  tags: string[]
}

export type SkillCategory = {
  id: string
  title: string
  description: string
  skills: SkillEntry[]
}

export const skillCategories: SkillCategory[] = [
  {
    id: 'orchestration',
    title: 'Orchestration',
    description: 'Pipeline planning, skill routing, and production briefs. Start here for complex multi-skill tasks.',
    skills: [
      {
        name: 'blender-director',
        desc: 'Analyzes the request, locks genre/style/world, selects specialists, outputs a production brief, and orchestrates MCP execution through validation and export.',
        tags: ['routing', 'planning', 'orchestration', 'briefs'],
      },
    ],
  },
  {
    id: 'modeling',
    title: 'Modeling Disciplines',
    description: 'Specialist modelers for props, vehicles, environments, vegetation, characters, and creatures.',
    skills: [
      { name: 'blender-modeler', desc: 'General Edit Mode modeling, modifiers, collections, blockouts, and scene organization.', tags: ['edit-mode', 'modifiers', 'blockout'] },
      { name: 'hard-surface', desc: 'Sci-fi, weapons, industrial, and mechanical assets with boolean/bevel, panel lines, and greebles.', tags: ['sci-fi', 'weapons', 'booleans'] },
      { name: 'prop-artist', desc: 'Everyday and hero props, furniture, tools, household objects, and kitbash libraries with real-world scale.', tags: ['props', 'kitbash', 'furniture'] },
      { name: 'vehicle-artist', desc: 'Cars, trucks, aircraft, ships, mechs, and transit assets with proportion blockout, LODs, and object splits.', tags: ['vehicles', 'mechs', 'lod'] },
      { name: 'environment-artist', desc: 'Modular kits, terrain, architecture, and game-optimized environment pipelines.', tags: ['modular', 'terrain', 'architecture'] },
      { name: 'vegetation-artist', desc: 'Trees, plants, grass cards, leaf atlases, canopy LODs, and wind vertex-color prep.', tags: ['foliage', 'trees', 'grass'] },
      { name: 'character-artist', desc: 'Human anatomy, facial topology, clothing base meshes, and animation-ready characters.', tags: ['character', 'anatomy', 'facial'] },
      { name: 'creature-artist', desc: 'Monsters, fantasy creatures, aliens, and organic design with believable anatomy.', tags: ['creature', 'organic', 'fantasy'] },
      { name: 'character-archetypes', desc: 'Race/role kits — elf, dwarf, orc, vampire, mecha, knight, assassin, and more — with silhouette rules.', tags: ['archetypes', 'races', 'roles'] },
    ],
  },
  {
    id: 'workflow',
    title: 'Production Workflow',
    description: 'Sculpt → retopo → UV → materials → textures, plus hair, cloth, and lookdev loops.',
    skills: [
      { name: 'sculpting', desc: 'High-frequency detail with Dyntopo, multires, brushes, alphas, wrinkles, and damage.', tags: ['dyntopo', 'multires', 'alphas'] },
      { name: 'retopology', desc: 'Animation-ready quad-dominant meshes with proper edge loops and efficient flow.', tags: ['quads', 'edge-loops'] },
      { name: 'uv-workflow', desc: 'Seams, packing, texel density, UDIM, lightmap UVs, and modular layouts.', tags: ['uvs', 'texel-density', 'udim'] },
      { name: 'materials', desc: 'PBR and stylized materials for metal, wood, concrete, fabric, glass, and procedural shaders.', tags: ['pbr', 'procedural'] },
      { name: 'texture-workflow', desc: 'Baking AO/curvature/normals, ORM packing, atlases, and texture memory optimization.', tags: ['baking', 'normals', 'atlases'] },
      { name: 'hair-groom', desc: 'Curves/particle grooms and game hair-card atlases with scalp flow regions.', tags: ['hair', 'cards', 'groom'] },
      { name: 'cloth-sim', desc: 'Garment blockout, pin groups, cloth sim, and bake to shape keys or caches.', tags: ['cloth', 'sim', 'bake'] },
      { name: 'lookdev', desc: 'Material + light + camera review loop with grey passes and screenshot iterations.', tags: ['lookdev', 'shading', 'turntable'] },
    ],
  },
  {
    id: 'technical',
    title: 'Technical Skills',
    description: 'Procedural systems, lighting, cameras, rendering, compositing, animation, rigging, VFX, and physics.',
    skills: [
      { name: 'geometry-nodes', desc: 'Scatter systems, procedural vegetation/buildings/cables, and reusable node groups.', tags: ['procedural', 'scatter'] },
      { name: 'lighting', desc: 'Three-point, HDRI, horror lighting, volumetrics, rim lights, and mood illumination.', tags: ['hdri', 'volumetrics'] },
      { name: 'camera-cinematography', desc: 'Framing, lenses, composition, DoF, and motivated camera animation beyond basic renders.', tags: ['camera', 'lens', 'framing'] },
      { name: 'rendering', desc: 'Cycles/Eevee sampling, denoising, passes, AgX color management, and delivery.', tags: ['cycles', 'eevee'] },
      { name: 'compositing', desc: 'Beauty stacks, pass recombination, grade, glare, and delivery outputs.', tags: ['compositor', 'grade', 'passes'] },
      { name: 'animation', desc: 'Walk/run/idle, combat, mechanical motion, Graph Editor, and NLA workflows.', tags: ['locomotion', 'nla'] },
      { name: 'rigging', desc: 'Armatures, IK/FK, constraints, weight painting, mechanical and facial rigs.', tags: ['ik-fk', 'weights'] },
      { name: 'vfx-fx', desc: 'Smoke, fire, particles, trails, and Geometry Nodes FX for cinematic or game flipbooks.', tags: ['vfx', 'smoke', 'particles'] },
      { name: 'physics-sim', desc: 'Rigid body, soft body, destruction, constraints, and baked caches.', tags: ['rigid-body', 'destruction'] },
    ],
  },
  {
    id: 'pipeline',
    title: 'Pipeline & Delivery',
    description: 'Scene assembly, optimization, LODs, collision, engine-specific export, QA, and archviz delivery.',
    skills: [
      { name: 'procedural-modeling', desc: 'Rocks, buildings, vegetation, roads, terrain, pipes, and cables via GN/modifiers.', tags: ['procedural', 'kits'] },
      { name: 'scene-assembly', desc: 'Large layouts, collections, linking, overrides, and streaming-friendly organization.', tags: ['layout', 'linking'] },
      { name: 'set-dressing', desc: 'Narrative prop clusters, density control, and environmental storytelling placement.', tags: ['dressing', 'storytelling'] },
      { name: 'asset-optimization', desc: 'Polycount, topology, UV efficiency, naming, and game-ready validation gate.', tags: ['validation', 'polycount'] },
      { name: 'lod-pipeline', desc: 'Dedicated LOD generation, naming, screen-size targets, and silhouette validation.', tags: ['lod', 'decimate'] },
      { name: 'collision-proxy', desc: 'UCX/convex hulls, capsules, boxes, and engine collider naming.', tags: ['ucx', 'collision'] },
      { name: 'export-pipeline', desc: 'Generic FBX/GLTF/OBJ/USD/Alembic export with scale, pivot, and normals checks.', tags: ['fbx', 'gltf', 'usd'] },
      { name: 'unity-export', desc: 'Unity-specific scale, materials, humanoid/generic rigs, LODs, and colliders.', tags: ['unity', 'glb'] },
      { name: 'unreal-export', desc: 'Unreal FBX, centimeter awareness, UCX collision, LOD chains, and sockets.', tags: ['unreal', 'ucx'] },
      { name: 'godot-export', desc: 'Godot GLTF/GLB export with clean hierarchy and PBR materials.', tags: ['godot', 'gltf'] },
      { name: 'qa-review', desc: 'Screenshot-backed checklist gate with explicit SHIP / NO-SHIP verdicts.', tags: ['qa', 'review'] },
      { name: 'archviz', desc: 'Architectural visualization — real-world scale, cameras, materials, and stills delivery.', tags: ['archviz', 'interiors'] },
    ],
  },
  {
    id: 'style-core',
    title: 'Core Style Specialists',
    description: 'Foundational art-direction skills that lock visual language before modeling.',
    skills: [
      { name: 'horror-style', desc: 'Psychological horror — sparse industrial spaces, analog aesthetics, tension lighting.', tags: ['horror', 'atmospheric'] },
      { name: 'psx-horror-style', desc: 'PS1/PSX crunchy horror — low budgets, fog, nearest textures, VHS-adjacent presentation.', tags: ['psx', 'retro-horror'] },
      { name: 'lowpoly-style', desc: 'PS1/PS2 / Lethal Company aesthetic — readable silhouettes, minimal polys.', tags: ['lowpoly', 'ps1'] },
      { name: 'anime-style', desc: 'Cel shading, hard color breaks, anime proportions, and toon stacks.', tags: ['anime', 'cel'] },
      { name: 'voxel-style', desc: 'Minecraft-adjacent block grid modeling with limited palettes.', tags: ['voxel', 'blocks'] },
      { name: 'isometric-style', desc: 'True-iso / dimetric cameras, tile footprints, and strategy-game readability.', tags: ['isometric', 'tiles'] },
      { name: 'stylized-style', desc: 'Broad NPR — shape language, exaggeration, hand-painted-friendly pipelines.', tags: ['npr', 'stylized'] },
      { name: 'realistic-style', desc: 'Photoreal AAA PBR, photogrammetry cleanup, and cinematic realism.', tags: ['aaa', 'photoreal'] },
    ],
  },
  {
    id: 'style-extended',
    title: 'Extended Art Styles',
    description: 'Genre-specific looks from cartoon and comic to pixel, painterly, craft, and retro eras.',
    skills: [
      { name: 'cartoon-style', desc: 'Bold graphic shapes, squash-stretch readability, and limited palettes.', tags: ['cartoon', 'graphic'] },
      { name: 'comic-book-style', desc: 'Ink-ready contrast, contour support, and optional halftone language.', tags: ['comics', 'ink'] },
      { name: 'manga-style', desc: 'Value-first manga staging, screentone feel, and panel emphasis.', tags: ['manga', 'screentone'] },
      { name: 'pixel-art-style', desc: 'Texel-locked pixel discipline and nearest-filter intent for 3D-assisted pixel looks.', tags: ['pixel', 'texel'] },
      { name: 'hand-painted-style', desc: 'Brushwork albedo, soft values, and restrained PBR for painted games.', tags: ['hand-painted'] },
      { name: 'painterly-style', desc: 'Watercolor and oil-painting looks with pigment texture and soft edges.', tags: ['watercolor', 'oil'] },
      { name: 'stop-motion-craft-style', desc: 'Claymation, paper craft, and handmade physical-material cues.', tags: ['clay', 'papercraft'] },
      { name: 'chibi-style', desc: 'Super-deformed proportions — oversized heads and cute silhouettes.', tags: ['chibi', 'sd'] },
      { name: 'noir-style', desc: 'High-contrast noir lighting, wet streets, and mono/limited-color grades.', tags: ['noir', 'contrast'] },
      { name: 'minimalist-style', desc: 'Reduced forms, negative space, and limited color systems.', tags: ['minimal', 'abstract'] },
      { name: 'vector-style', desc: 'Flat fills, sharp silhouettes, and UI-like graphic clarity.', tags: ['vector', 'flat'] },
      { name: 'retro-8bit-style', desc: 'NES-era constraints — severe palettes and chunky reads.', tags: ['8-bit', 'nes'] },
      { name: 'retro-16bit-style', desc: 'SNES/Genesis-era richer palettes with texel discipline.', tags: ['16-bit', 'snes'] },
      { name: 'hd-2d-style', desc: 'Pixel characters on soft 3D stages with theatrical DoF and lighting.', tags: ['hd-2d', 'octopath'] },
      { name: 'frutiger-aero-style', desc: 'Glossy mid-2000s futurism — aqua, bubbles, nature-tech optimism.', tags: ['frutiger-aero', 'aero'] },
    ],
  },
  {
    id: 'horror-packs',
    title: 'Horror Packs',
    description: 'Subtype horror direction — cosmic, body, analog, liminal, folk, mascot, dreamcore, and indie references.',
    skills: [
      { name: 'cosmic-eldritch-horror', desc: 'Lovecraftian scale, non-Euclidean cues, and incomprehensible forms.', tags: ['cosmic', 'lovecraft'] },
      { name: 'body-horror-style', desc: 'Mutation, flesh wrongness, and visceral material storytelling.', tags: ['body-horror', 'mutation'] },
      { name: 'analog-found-footage-horror', desc: 'VHS/CRT/found-footage camera language and tape damage in comp.', tags: ['vhs', 'found-footage'] },
      { name: 'liminal-space-style', desc: 'Backrooms, empty malls/schools, poolrooms — familiar emptiness.', tags: ['liminal', 'backrooms'] },
      { name: 'folk-horror-style', desc: 'Pastoral daylight dread, rural ritual, and community wrongness.', tags: ['folk', 'rural'] },
      { name: 'mascot-puppet-horror', desc: 'Cute brand/puppet characters corrupted — felt, foam, dead eyes.', tags: ['mascot', 'puppet'] },
      { name: 'dream-weirdcore-style', desc: 'Dreamcore/weirdcore/traumacore nostalgic surreal dread.', tags: ['dreamcore', 'weirdcore'] },
      { name: 'indie-horror-aesthetics', desc: 'Silent Hill, Fear to Fathom, Puppet Combo, corporate/cabin/hospital lanes.', tags: ['silent-hill', 'indie'] },
    ],
  },
  {
    id: 'worlds',
    title: 'Worlds & Themes',
    description: 'World-building packs. Open each skill’s references for subtypes (steampunk, western, wasteland, jungle, …).',
    skills: [
      { name: 'fantasy-worlds', desc: 'Medieval, high fantasy, dark fantasy, and urban fantasy material languages.', tags: ['fantasy', 'medieval'] },
      { name: 'sci-fi-punk-worlds', desc: 'Hard sci-fi, space, cyberpunk, steampunk, diesel/atom/solar/bio/clockpunk.', tags: ['cyberpunk', 'steampunk'] },
      { name: 'historical-worlds', desc: 'Western, pirate, samurai/ninja, Viking, ancients, Victorian, military eras.', tags: ['historical', 'period'] },
      { name: 'apocalypse-worlds', desc: 'Post-apoc, zombie, alien invasion, dystopia/utopia, post-human ruins.', tags: ['wasteland', 'dystopia'] },
      { name: 'biome-worlds', desc: 'Underwater, desert, arctic, jungle, underground, and floating islands.', tags: ['biomes', 'climate'] },
    ],
  },
  {
    id: 'moods',
    title: 'Atmosphere & Mood',
    description: 'Mood overlays that tune lighting, palette, clutter, and camera feel.',
    skills: [
      { name: 'cozy-wholesome-mood', desc: 'Warm light, soft shapes, safe clutter — cozy/cute/peaceful scenes.', tags: ['cozy', 'wholesome'] },
      { name: 'dark-gritty-mood', desc: 'Dark, grim, rusty, abandoned, industrial, lonely, melancholic tones.', tags: ['gritty', 'decay'] },
      { name: 'dream-surreal-mood', desc: 'Dreamlike, surreal, mysterious, mystical, chaotic atmosphere.', tags: ['surreal', 'dream'] },
      { name: 'neon-retrofuturism', desc: 'Neon, vaporwave, synthwave, and retrofuturistic dusk palettes.', tags: ['neon', 'synthwave'] },
      { name: 'brutalist-mood', desc: 'Monumental raw concrete, austere composition, human-scale contrast.', tags: ['brutalist', 'concrete'] },
    ],
  },
  {
    id: 'genres',
    title: 'Gameplay Genre Direction',
    description: 'Art-direction rules for gameplay genres — readability, landmarks, cover, loot, and camera language.',
    skills: [
      { name: 'genre-action-combat', desc: 'Action, hack-and-slash, beat ’em up, fighting — readable arenas and breakables.', tags: ['action', 'combat'] },
      { name: 'genre-shooter', desc: 'FPS/TPS, battle royale, extraction — sightlines, cover, POI landmarking.', tags: ['fps', 'tps', 'br'] },
      { name: 'genre-rpg', desc: 'RPG/JRPG/CRPG/ARPG/MMO — region identity, hubs, loot rarity reads.', tags: ['rpg', 'jrpg'] },
      { name: 'genre-survival', desc: 'Survival and survival-horror — resource reads, crafting benches, risk routes.', tags: ['survival'] },
      { name: 'genre-stealth', desc: 'Shadow volumes, patrol layouts, and concealment materials.', tags: ['stealth'] },
      { name: 'genre-puzzle-platformer', desc: 'Interactable pop, hazard language, and honest jump volumes.', tags: ['puzzle', 'platformer'] },
      { name: 'genre-metroidvania-roguelike', desc: 'Room modules, ability gates, biome mastery, run-readable props.', tags: ['metroidvania', 'roguelike'] },
      { name: 'genre-soulslike', desc: 'Monumental melancholy, fog gates, bonfire landmarks, lethal silhouettes.', tags: ['soulslike'] },
      { name: 'genre-strategy-sim', desc: 'RTS/TBS/TD/MOBA, city/colony/life/farming sims — iconic buildings at zoom.', tags: ['strategy', 'sim'] },
      { name: 'genre-racing-sports', desc: 'Track landmarks, stadium kits, and high-speed edge clarity.', tags: ['racing', 'sports'] },
      { name: 'genre-narrative-vn', desc: 'Visual novel, interactive movie, walking sim — emotion cameras and plates.', tags: ['vn', 'narrative'] },
      { name: 'genre-card-party-idle', desc: 'Card/deck builder, party, idle/incremental, rhythm, educational stages.', tags: ['cards', 'idle'] },
      { name: 'genre-open-world-sandbox', desc: 'Open world/sandbox — biome borders, landmarks, discovery crumbs.', tags: ['open-world', 'sandbox'] },
    ],
  },
  {
    id: 'eras',
    title: 'Visual Eras',
    description: 'Console and media-era presentation constraints from PS1 crunch to modern PBR and tape looks.',
    skills: [
      {
        name: 'visual-console-eras',
        desc: 'PS1–PS5 stylistic cues, retro arcade, DOS, CRT, VHS, and film-grain presentation stacks.',
        tags: ['ps1', 'ps5', 'crt', 'vhs'],
      },
    ],
  },
]

export const workflows = [
  {
    title: 'Hero Hard Surface Prop',
    pipeline: ['blender-director', 'hard-surface', 'uv-workflow', 'materials', 'lookdev', 'asset-optimization', 'export-pipeline'],
  },
  {
    title: 'Everyday Hero Prop',
    pipeline: ['blender-director', 'prop-artist', 'uv-workflow', 'materials', 'lookdev', 'unity-export|unreal-export'],
  },
  {
    title: 'Game Vehicle',
    pipeline: ['blender-director', 'vehicle-artist', 'lod-pipeline', 'collision-proxy', 'materials', 'unreal-export', 'qa-review'],
  },
  {
    title: 'Game Character',
    pipeline: ['blender-director', 'character-archetypes', 'character-artist', 'sculpting', 'retopology', 'hair-groom', 'cloth-sim', 'rigging', 'export-pipeline'],
  },
  {
    title: 'Soulslike Ruins',
    pipeline: ['blender-director', 'genre-soulslike', 'dark-gritty-mood', 'fantasy-worlds', 'environment-artist', 'lighting', 'qa-review'],
  },
  {
    title: 'Liminal Backrooms',
    pipeline: ['blender-director', 'liminal-space-style', 'environment-artist', 'lighting', 'analog-found-footage-horror', 'compositing'],
  },
  {
    title: 'Cyberpunk Street',
    pipeline: ['blender-director', 'sci-fi-punk-worlds', 'neon-retrofuturism', 'prop-artist', 'lookdev', 'qa-review'],
  },
  {
    title: 'HD-2D Dungeon',
    pipeline: ['blender-director', 'hd-2d-style', 'pixel-art-style', 'environment-artist', 'camera-cinematography', 'compositing'],
  },
  {
    title: 'Horror Environment',
    pipeline: ['blender-director', 'horror-style', 'indie-horror-aesthetics', 'environment-artist', 'set-dressing', 'lighting', 'export-pipeline'],
  },
  {
    title: 'Cozy Farming Sim',
    pipeline: ['blender-director', 'genre-strategy-sim', 'cozy-wholesome-mood', 'prop-artist', 'vegetation-artist', 'lookdev'],
  },
  {
    title: 'Cinematic Shot',
    pipeline: ['blender-director', 'lookdev', 'camera-cinematography', 'lighting', 'rendering', 'compositing', 'qa-review'],
  },
  {
    title: 'Reference Image Match',
    pipeline: ['blender-director', 'reference-image-match', 'Camera match', 'Geometry tiers', 'Materials', 'Screenshot loop', 'qa-review'],
  },
]

export const namingRef = [
  { type: 'Collections', prefix: 'COL_' },
  { type: 'Meshes', prefix: 'SM_' },
  { type: 'Materials', prefix: 'MAT_' },
  { type: 'Textures', prefix: 'T_' },
  { type: 'Animations', prefix: 'AN_' },
  { type: 'Armatures', prefix: 'ARM_' },
  { type: 'Geo Node Groups', prefix: 'GN_' },
  { type: 'Cameras', prefix: 'CAM_' },
  { type: 'Lights', prefix: 'LGT_' },
  { type: 'Unreal Collision', prefix: 'UCX_' },
  { type: 'FX', prefix: 'FX_' },
]

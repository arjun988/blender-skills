import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import {
  SKILL_COUNT,
  REF_COUNT,
  SITE_VERSION,
  skillCategories,
  workflows,
  namingRef,
} from '@/lib/skills-data'

export default function SkillsPage() {
  return (
    <div className="max-w-4xl space-y-16 pb-16">
      <div className="space-y-3">
        <div className="flex flex-wrap gap-2">
          <Badge>Skills Guide</Badge>
          <Badge variant="muted">v{SITE_VERSION}</Badge>
          <Badge variant="muted">{SKILL_COUNT} skills</Badge>
          <Badge variant="muted">{REF_COUNT}+ refs</Badge>
        </div>
        <h1 className="text-4xl font-bold tracking-tight">Skills Guide</h1>
        <p className="text-lg text-muted-foreground">
          Full catalog of {SKILL_COUNT} specialist skills with decision trees and workflow pipelines.
          Start complex work with <strong>blender-director</strong>. Genre, style, world, and mood packs
          include deeper subtype docs under each skill&apos;s <code>references/</code> folder.
        </p>
      </div>

      {/* Decision trees */}
      <section className="space-y-5" id="decision-tree">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Decision Trees</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm">What are you making?</CardTitle>
            </CardHeader>
            <CardContent className="pt-0 space-y-1 text-xs font-mono text-muted-foreground">
              <p>Everyday prop → <span className="text-primary">prop-artist</span></p>
              <p>Hard surface / weapon → <span className="text-primary">hard-surface</span></p>
              <p>Vehicle / mech → <span className="text-primary">vehicle-artist</span></p>
              <p>Environment → <span className="text-primary">environment-artist</span></p>
              <p>Vegetation → <span className="text-primary">vegetation-artist</span></p>
              <p>Character → <span className="text-primary">character-artist</span></p>
              <p>Creature → <span className="text-primary">creature-artist</span></p>
              <p>FX / destruction → <span className="text-primary">vfx-fx / physics-sim</span></p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm">Style / mood / world?</CardTitle>
            </CardHeader>
            <CardContent className="pt-0 space-y-1 text-xs font-mono text-muted-foreground">
              <p>Anime / cel → <span className="text-primary">anime-style</span></p>
              <p>Pixel / HD-2D → <span className="text-primary">pixel-art / hd-2d</span></p>
              <p>Liminal / Backrooms → <span className="text-primary">liminal-space-style</span></p>
              <p>Cyberpunk / steampunk → <span className="text-primary">sci-fi-punk-worlds</span></p>
              <p>Cozy / neon / gritty → <span className="text-primary">mood skills</span></p>
              <p>PS1–PS5 / VHS → <span className="text-primary">visual-console-eras</span></p>
              <p>Unspecified → <span className="text-primary">blender-director</span></p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm">Gameplay genre?</CardTitle>
            </CardHeader>
            <CardContent className="pt-0 space-y-1 text-xs font-mono text-muted-foreground">
              <p>FPS / BR / extraction → <span className="text-primary">genre-shooter</span></p>
              <p>RPG / JRPG / MMO → <span className="text-primary">genre-rpg</span></p>
              <p>Soulslike → <span className="text-primary">genre-soulslike</span></p>
              <p>Strategy / city sim → <span className="text-primary">genre-strategy-sim</span></p>
              <p>Metroidvania / roguelike → <span className="text-primary">genre-metroidvania-roguelike</span></p>
              <p>Open world → <span className="text-primary">genre-open-world-sandbox</span></p>
              <p>VN / walking sim → <span className="text-primary">genre-narrative-vn</span></p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Workflows */}
      <section className="space-y-5" id="workflows">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Workflow Pipelines</h2>
        <div className="space-y-3">
          {workflows.map((wf) => (
            <div key={wf.title} className="rounded-lg border p-4">
              <p className="font-semibold text-sm mb-3">{wf.title}</p>
              <div className="flex flex-wrap items-center gap-1.5 text-xs font-mono">
                {wf.pipeline.map((step, i) => (
                  <span key={i} className="flex items-center gap-1.5">
                    <span className="bg-muted rounded px-2 py-1 text-muted-foreground">{step}</span>
                    {i < wf.pipeline.length - 1 && <span className="text-muted-foreground/40">→</span>}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Pack note */}
      <section className="rounded-xl border bg-primary/5 p-5 space-y-2" id="packs">
        <h2 className="text-lg font-semibold">How genre &amp; style packs work</h2>
        <p className="text-sm text-muted-foreground leading-relaxed">
          Long subtype lists (steampunk, Backrooms, JRPG, vaporwave, Silent Hill, etc.) are covered as
          <strong> pack skills + reference docs</strong> — not hundreds of one-line skills.
          Example: ask for steampunk → agent loads <code>sci-fi-punk-worlds</code> → opens{' '}
          <code>references/steampunk.md</code>. Ask for Backrooms → <code>liminal-space-style</code> →{' '}
          <code>references/backrooms.md</code>.
        </p>
      </section>

      {/* Skill index */}
      <section className="space-y-10">
        <div className="space-y-2">
          <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Skill Index ({SKILL_COUNT})</h2>
          <p className="text-sm text-muted-foreground">
            Every skill below is available in both <code>.claude/skills/</code> and <code>.cursor/skills/</code>.
          </p>
        </div>
        {skillCategories.map((category) => (
          <div key={category.id} id={category.id} className="space-y-4 scroll-mt-20">
            <div>
              <h3 className="text-xl font-semibold">
                {category.title}{' '}
                <span className="text-sm font-normal text-muted-foreground">({category.skills.length})</span>
              </h3>
              <p className="text-sm text-muted-foreground mt-1">{category.description}</p>
            </div>
            <div className="grid sm:grid-cols-2 gap-3">
              {category.skills.map((skill) => (
                <Card key={skill.name} className="hover:shadow-md transition-shadow">
                  <CardHeader className="pb-2">
                    <CardTitle className="text-sm font-mono text-primary">{skill.name}</CardTitle>
                    <CardDescription className="text-xs leading-relaxed">{skill.desc}</CardDescription>
                  </CardHeader>
                  <CardContent className="pt-0">
                    <div className="flex flex-wrap gap-1">
                      {skill.tags.map((tag) => (
                        <Badge key={tag} variant="muted" className="text-[10px]">
                          {tag}
                        </Badge>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        ))}
      </section>

      {/* Naming */}
      <section className="space-y-4" id="naming">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Naming Conventions</h2>
        <div className="overflow-x-auto rounded-lg border">
          <table className="w-full text-sm">
            <thead className="bg-muted">
              <tr>
                <th className="text-left px-4 py-2.5 font-medium">Asset Type</th>
                <th className="text-left px-4 py-2.5 font-medium">Prefix</th>
                <th className="text-left px-4 py-2.5 font-medium">Example</th>
              </tr>
            </thead>
            <tbody>
              {namingRef.map((row, i) => (
                <tr key={row.type} className={i % 2 === 0 ? 'border-t' : 'border-t bg-muted/30'}>
                  <td className="px-4 py-2.5 text-muted-foreground">{row.type}</td>
                  <td className="px-4 py-2.5 font-mono text-primary font-medium">{row.prefix}</td>
                  <td className="px-4 py-2.5 font-mono text-xs text-muted-foreground">
                    {row.prefix === 'UCX_'
                      ? 'UCX_SM_Crate_01'
                      : row.prefix === 'FX_'
                        ? 'FX_Emit_Sparks'
                        : `${row.prefix}Weapon_Rifle_A`}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* Anti-patterns */}
      <section className="space-y-4" id="antipatterns">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Anti-Patterns</h2>
        <div className="space-y-2">
          {[
            '"How do I use Blender?" — Skills assume production context, not tutorials.',
            'Attaching a reference image without asking the agent to analyze and match it.',
            'Skipping blender-director on complex multi-step tasks.',
            'Mixing cyberpunk + steampunk + solarpunk without an intentional mashup brief.',
            'Declaring a genre without loading that genre skill’s readability rules.',
            'Adding greebles before establishing silhouette and panel-break depth.',
            'Keyframing emission on shared hull materials (causes white blowout in export).',
            'Manual UI steps when Blender MCP is connected.',
            'Exporting without asset-optimization / qa-review validation.',
            'Declaring done on reference tasks without screenshot comparison.',
          ].map((item) => (
            <div key={item} className="flex gap-2.5 text-sm">
              <span className="text-destructive font-bold shrink-0 mt-0.5">✕</span>
              <span className="text-muted-foreground">{item}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

import Image from 'next/image'
import Link from 'next/link'
import {
  ArrowRight,
  Blocks,
  BookOpen,
  Github,
  Zap,
  Layers,
  Cpu,
  Palette,
  Box,
  Ghost,
  Globe2,
  Gamepad2,
  Sparkles,
} from 'lucide-react'
import { SKILL_COUNT, REF_COUNT, SITE_VERSION, platforms, skillCategories } from '@/lib/skills-data'

export default function HomePage() {
  const categoryCards = [
    {
      icon: Cpu,
      title: 'Orchestration',
      desc: 'blender-director plans pipelines, locks genre/style/world, and routes specialists automatically.',
      accent: 'bg-orange-500/10 text-orange-600',
      id: 'orchestration',
    },
    {
      icon: Box,
      title: 'Modeling',
      desc: 'Props, vehicles, hard surface, environments, vegetation, characters, creatures, and archetypes.',
      accent: 'bg-blue-500/10 text-blue-600',
      id: 'modeling',
    },
    {
      icon: Layers,
      title: 'Production',
      desc: 'Sculpt, retopo, UV, materials, textures, hair groom, cloth sim, and lookdev loops.',
      accent: 'bg-violet-500/10 text-violet-600',
      id: 'workflow',
    },
    {
      icon: Zap,
      title: 'Technical',
      desc: 'Geometry nodes, lighting, cinematography, rendering, compositing, VFX, physics, rigging, animation.',
      accent: 'bg-yellow-500/10 text-yellow-600',
      id: 'technical',
    },
    {
      icon: Blocks,
      title: 'Pipeline',
      desc: 'Scene assembly, LODs, collision, Unity/Unreal/Godot export, QA review, and archviz delivery.',
      accent: 'bg-green-500/10 text-green-600',
      id: 'pipeline',
    },
    {
      icon: Palette,
      title: 'Art Styles',
      desc: 'From realistic and anime to pixel, HD-2D, noir, painterly, voxel, Frutiger Aero, and more.',
      accent: 'bg-pink-500/10 text-pink-600',
      id: 'style-extended',
    },
    {
      icon: Ghost,
      title: 'Horror Packs',
      desc: 'Cosmic, body, analog/VHS, liminal/Backrooms, folk, mascot, dreamcore, and indie horror lanes.',
      accent: 'bg-red-500/10 text-red-600',
      id: 'horror-packs',
    },
    {
      icon: Globe2,
      title: 'Worlds & Moods',
      desc: 'Fantasy, punk sci-fi, historical, apocalypse, biomes — plus cozy, gritty, neon, brutalist moods.',
      accent: 'bg-cyan-500/10 text-cyan-600',
      id: 'worlds',
    },
    {
      icon: Gamepad2,
      title: 'Gameplay Genres',
      desc: 'Shooter, RPG, soulslike, stealth, metroidvania, strategy/sim, racing, VN, open world, and more.',
      accent: 'bg-indigo-500/10 text-indigo-600',
      id: 'genres',
    },
  ]

  return (
    <div className="flex flex-col">
      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="relative h-[520px] md:h-[600px] w-full">
          <Image
            src="/banner.png"
            alt="Blender Skills — sci-fi spacecraft render"
            fill
            className="object-cover object-center brightness-[0.35]"
            priority
          />
          <div className="absolute inset-0 bg-gradient-to-b from-background/10 via-background/30 to-background" />
        </div>

        <div className="absolute inset-0 flex flex-col items-center justify-center text-center px-4 pb-16">
          <div className="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-primary/10 px-4 py-1.5 text-xs font-medium text-primary mb-6">
            <span className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" />
            {SKILL_COUNT} Skills · {REF_COUNT}+ Refs · Blender MCP · v{SITE_VERSION}
          </div>

          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-white leading-[1.08] max-w-4xl">
            Your Senior{' '}
            <span className="text-primary">Technical Art</span>{' '}
            Team
          </h1>

          <p className="mt-6 text-lg md:text-xl text-white/70 max-w-2xl leading-relaxed">
            {SKILL_COUNT} specialist skills for{' '}
            <span className="text-white font-medium">Cursor</span>,{' '}
            <span className="text-white font-medium">Claude Code</span>,{' '}
            <span className="text-white font-medium">Kiro</span>, and{' '}
            <span className="text-white font-medium">Codex</span>.
            Every skill executes directly inside Blender via MCP — production pipelines, not tutorials.
          </p>

          <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
            <Link
              href="/getting-started"
              className="inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition-colors"
            >
              Get Started <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              href="/skills"
              className="inline-flex items-center gap-2 rounded-lg border border-white/20 bg-white/10 backdrop-blur px-6 py-3 text-sm font-semibold text-white hover:bg-white/20 transition-colors"
            >
              Browse Skills
            </Link>
            <Link
              href="https://github.com/arjun988/blender-skills"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-lg border border-white/20 bg-white/10 backdrop-blur px-6 py-3 text-sm font-semibold text-white hover:bg-white/20 transition-colors"
            >
              <Github className="h-4 w-4" /> GitHub
            </Link>
          </div>
        </div>
      </section>

      {/* Platforms */}
      <section className="border-y bg-muted/40">
        <div className="max-w-screen-xl mx-auto px-6 py-14 space-y-8">
          <div className="text-center space-y-3 max-w-2xl mx-auto">
            <p className="text-xs font-semibold uppercase tracking-widest text-primary flex items-center justify-center gap-2">
              <Sparkles className="h-3.5 w-3.5" /> Works with your agent
            </p>
            <h2 className="text-2xl md:text-3xl font-bold tracking-tight">
              Built for Cursor, Claude Code, Kiro &amp; Codex
            </h2>
            <p className="text-muted-foreground text-sm md:text-base">
              Same skill pack, same Blender MCP execution model — drop skills into the agent you already use.
            </p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {platforms.map((p) => (
              <div key={p.name} className="rounded-xl border bg-card p-5 space-y-2 hover:shadow-md transition-shadow">
                <p className="font-semibold text-lg">{p.name}</p>
                <p className="text-sm text-muted-foreground leading-relaxed">{p.blurb}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="border-b bg-muted/50">
        <div className="max-w-screen-xl mx-auto px-6 py-8 grid grid-cols-2 md:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-border">
          {[
            { icon: Blocks, value: String(SKILL_COUNT), label: 'Specialist Skills' },
            { icon: BookOpen, value: String(REF_COUNT) + '+', label: 'Reference Files' },
            { icon: Zap, value: '12+', label: 'Workflow Pipelines' },
            { icon: Palette, value: String(skillCategories.length), label: 'Skill Categories' },
          ].map(({ icon: Icon, value, label }) => (
            <div key={label} className="flex items-center gap-4 px-6 py-4 first:pl-0 last:pr-0">
              <div className="h-10 w-10 rounded-lg bg-primary/10 flex items-center justify-center shrink-0">
                <Icon className="h-5 w-5 text-primary" />
              </div>
              <div>
                <p className="text-2xl font-bold leading-none">{value}</p>
                <p className="text-sm text-muted-foreground mt-1">{label}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Install */}
      <section className="max-w-screen-xl mx-auto w-full px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div className="space-y-5">
          <p className="text-xs font-semibold uppercase tracking-widest text-primary">Installation</p>
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">
            Clone and go.<br />Production-ready.
          </h2>
          <div className="rounded-lg border border-yellow-500/40 bg-yellow-500/5 px-4 py-3 text-sm text-muted-foreground">
            <span className="font-semibold text-foreground">Marketplace under review — </span>
            install from GitHub for Claude Code, Cursor, Kiro, and Codex.
          </div>
          <p className="text-muted-foreground leading-relaxed">
            All {SKILL_COUNT} skills and {REF_COUNT}+ reference files drop into your agent context.
            Pair with Blender MCP and the agent executes inside your live Blender session.
          </p>
          <Link
            href="/getting-started"
            className="inline-flex items-center gap-2 text-sm font-semibold text-primary hover:underline"
          >
            Full setup for every platform <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
        <div className="rounded-xl border bg-card shadow-sm overflow-hidden">
          <div className="flex items-center gap-1.5 px-4 py-3 border-b bg-muted/60">
            <div className="h-2.5 w-2.5 rounded-full bg-red-400" />
            <div className="h-2.5 w-2.5 rounded-full bg-yellow-400" />
            <div className="h-2.5 w-2.5 rounded-full bg-green-400" />
            <span className="ml-2 text-xs text-muted-foreground font-mono">Terminal</span>
          </div>
          <div className="p-5 space-y-2 font-mono text-sm">
            <p>
              <span className="text-muted-foreground select-none">$ </span>
              <span className="text-foreground">git clone https://github.com/arjun988/blender-skills.git</span>
            </p>
            <p>
              <span className="text-muted-foreground select-none">$ </span>
              <span className="text-foreground">cp -r blender-skills/.claude/skills .claude/skills/</span>
            </p>
            <p className="text-green-600 dark:text-green-400 pt-1">✓ {SKILL_COUNT} skills ready in your project</p>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="border-t bg-muted/30">
        <div className="max-w-screen-xl mx-auto px-6 py-20 space-y-12">
          <div className="text-center space-y-3 max-w-2xl mx-auto">
            <p className="text-xs font-semibold uppercase tracking-widest text-primary">{SKILL_COUNT} Skills</p>
            <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Every discipline. One pack.</h2>
            <p className="text-muted-foreground">
              Modeling through engine export — plus genre, style, world, mood, and horror packs with deep reference docs for every subtype.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {categoryCards.map((cat) => (
              <Link
                key={cat.title}
                href={`/skills#${cat.id}`}
                className="rounded-xl border bg-card p-6 space-y-4 hover:shadow-md transition-shadow block"
              >
                <div className={`h-10 w-10 rounded-lg flex items-center justify-center ${cat.accent}`}>
                  <cat.icon className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-semibold">{cat.title}</h3>
                  <p className="text-sm text-muted-foreground mt-1 leading-relaxed">{cat.desc}</p>
                </div>
              </Link>
            ))}
          </div>

          <div className="text-center">
            <Link
              href="/skills"
              className="inline-flex items-center gap-2 rounded-lg border px-5 py-2.5 text-sm font-medium hover:bg-accent transition-colors"
            >
              View all {SKILL_COUNT} skills in detail <ArrowRight className="h-4 w-4 text-primary" />
            </Link>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="max-w-screen-xl mx-auto px-6 py-20 space-y-12">
        <div className="text-center space-y-3 max-w-2xl mx-auto">
          <p className="text-xs font-semibold uppercase tracking-widest text-primary">How It Works</p>
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">MCP-first execution</h2>
          <p className="text-muted-foreground">
            Skills don&apos;t write tutorials — they execute. Actions run inside your Blender session via the BlenderMCP addon.
          </p>
        </div>

        <div className="grid sm:grid-cols-3 gap-6">
          {[
            {
              step: '01',
              title: 'Prompt in your agent',
              desc: 'Use Cursor, Claude Code, Kiro, or Codex. blender-director plans the pipeline and selects genre, style, and discipline skills.',
            },
            {
              step: '02',
              title: 'MCP executes in Blender',
              desc: 'Skills call BlenderMCP tools directly — objects, materials, cameras, sims, UVs, renders — in your live session.',
            },
            {
              step: '03',
              title: 'Validate and export',
              desc: 'qa-review and asset-optimization gate quality. unity-export, unreal-export, or godot-export ships engine-ready files.',
            },
          ].map((item) => (
            <div key={item.step} className="relative rounded-xl border p-6 space-y-3">
              <span className="text-5xl font-black text-muted/80 leading-none select-none">{item.step}</span>
              <h3 className="font-semibold text-base">{item.title}</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="border-t bg-primary/5">
        <div className="max-w-screen-xl mx-auto px-6 py-20 text-center space-y-6">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Ready to build?</h2>
          <p className="text-muted-foreground max-w-xl mx-auto">
            Install Blender Skills for Cursor, Claude Code, Kiro, or Codex and start your first production asset in minutes.
          </p>
          <div className="flex flex-wrap items-center justify-center gap-4">
            <Link
              href="/getting-started"
              className="inline-flex items-center gap-2 rounded-lg bg-primary px-8 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition-colors"
            >
              Get Started <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              href="https://github.com/arjun988/blender-skills"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-lg border px-8 py-3 text-sm font-semibold hover:bg-accent transition-colors"
            >
              <Github className="h-4 w-4" /> View on GitHub
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}

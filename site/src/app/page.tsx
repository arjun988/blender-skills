import Image from 'next/image'
import Link from 'next/link'
import { ArrowRight, Blocks, BookOpen, Github, Zap, Layers, Cpu, Palette, Box } from 'lucide-react'

export default function HomePage() {
  return (
    <div className="flex flex-col">

      {/* ── Hero ─────────────────────────────────────────────── */}
      <section className="relative overflow-hidden">
        {/* banner image as background */}
        <div className="relative h-[480px] md:h-[560px] w-full">
          <Image
            src="/banner.png"
            alt="Blender Skills — sci-fi spacecraft render"
            fill
            className="object-cover object-center brightness-[0.35]"
            priority
          />
          {/* gradient overlay */}
          <div className="absolute inset-0 bg-gradient-to-b from-background/10 via-background/30 to-background" />
        </div>

        {/* hero text — sits on top of image */}
        <div className="absolute inset-0 flex flex-col items-center justify-center text-center px-4 pb-16">
          <div className="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-primary/10 px-4 py-1.5 text-xs font-medium text-primary mb-6">
            <span className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" />
            23 Skills · Blender MCP · v1.1.0
          </div>

          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-white leading-[1.08] max-w-4xl">
            Your Senior{' '}
            <span className="text-primary">Technical Art</span>{' '}
            Team
          </h1>

          <p className="mt-6 text-lg md:text-xl text-white/70 max-w-2xl leading-relaxed">
            23 specialist skills for Claude Code, Cursor, and Kiro.
            Every skill executes directly inside Blender via MCP — no UI walkthroughs, no hand-holding.
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

      {/* ── Stats bar ───────────────────────────────────────────── */}
      <section className="border-y bg-muted/50">
        <div className="max-w-screen-xl mx-auto px-6 py-8 grid grid-cols-2 md:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-border">
          {[
            { icon: Blocks, value: '23', label: 'Specialist Skills' },
            { icon: BookOpen, value: '40', label: 'Reference Files' },
            { icon: Zap, value: '6', label: 'Workflow Pipelines' },
            { icon: Palette, value: '4', label: 'Style Specialists' },
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

      {/* ── Quick install ───────────────────────────────────────── */}
      <section className="max-w-screen-xl mx-auto w-full px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div className="space-y-5">
          <p className="text-xs font-semibold uppercase tracking-widest text-primary">Installation</p>
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">
            Clone and go.<br />Production-ready.
          </h2>
          <div className="rounded-lg border border-yellow-500/40 bg-yellow-500/5 px-4 py-3 text-sm text-muted-foreground">
            <span className="font-semibold text-foreground">🕐 Marketplace under review — </span>
            install directly from GitHub below.
          </div>
          <p className="text-muted-foreground leading-relaxed">
            All 23 skills and 40 reference files drop straight into your agent context. Once the marketplace listing is approved, a single command will handle everything.
          </p>
          <Link
            href="/getting-started"
            className="inline-flex items-center gap-2 text-sm font-semibold text-primary hover:underline"
          >
            Full setup guide <ArrowRight className="h-4 w-4" />
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
            <p className="text-green-600 dark:text-green-400 pt-1">✓ 23 skills ready in your project</p>
          </div>
        </div>
      </section>

      {/* ── Skill categories ───────────────────────────────────── */}
      <section className="border-t bg-muted/30">
        <div className="max-w-screen-xl mx-auto px-6 py-20 space-y-12">
          <div className="text-center space-y-3 max-w-2xl mx-auto">
            <p className="text-xs font-semibold uppercase tracking-widest text-primary">23 Skills</p>
            <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Every discipline. One pack.</h2>
            <p className="text-muted-foreground">
              From first blockout to engine export — each skill is a specialist that thinks in production pipelines, not tutorials.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {[
              {
                icon: Cpu,
                title: 'Orchestration',
                desc: 'blender-director analyzes your request and routes to the right specialists automatically.',
                skills: ['blender-director'],
                accent: 'bg-orange-500/10 text-orange-600',
              },
              {
                icon: Box,
                title: 'Modeling',
                desc: 'Hard surface, environments, characters, creatures, and general modeling disciplines.',
                skills: ['hard-surface', 'environment-artist', 'character-artist', 'creature-artist'],
                accent: 'bg-blue-500/10 text-blue-600',
              },
              {
                icon: Layers,
                title: 'Production Workflow',
                desc: 'Sculpt → retopo → UV → materials → textures. The complete game-art pipeline.',
                skills: ['sculpting', 'retopology', 'uv-workflow', 'materials', 'texture-workflow'],
                accent: 'bg-violet-500/10 text-violet-600',
              },
              {
                icon: Zap,
                title: 'Technical',
                desc: 'Geometry nodes, lighting, rendering, animation, and rigging.',
                skills: ['geometry-nodes', 'lighting', 'rendering', 'rigging', 'animation'],
                accent: 'bg-yellow-500/10 text-yellow-600',
              },
              {
                icon: Blocks,
                title: 'Pipeline',
                desc: 'Procedural modeling, optimization gate, and multi-format export to FBX, GLTF, USD.',
                skills: ['procedural-modeling', 'asset-optimization', 'export-pipeline'],
                accent: 'bg-green-500/10 text-green-600',
              },
              {
                icon: Palette,
                title: 'Style Specialists',
                desc: 'Horror, low-poly, stylized, and photorealistic art direction.',
                skills: ['horror-style', 'lowpoly-style', 'stylized-style', 'realistic-style'],
                accent: 'bg-pink-500/10 text-pink-600',
              },
            ].map((cat) => (
              <div
                key={cat.title}
                className="rounded-xl border bg-card p-6 space-y-4 hover:shadow-md transition-shadow"
              >
                <div className={`h-10 w-10 rounded-lg flex items-center justify-center ${cat.accent}`}>
                  <cat.icon className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-semibold">{cat.title}</h3>
                  <p className="text-sm text-muted-foreground mt-1 leading-relaxed">{cat.desc}</p>
                </div>
                <div className="flex flex-wrap gap-1.5">
                  {cat.skills.map((s) => (
                    <span
                      key={s}
                      className="rounded bg-muted px-2 py-0.5 text-[11px] font-mono text-muted-foreground"
                    >
                      {s}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="text-center">
            <Link
              href="/skills"
              className="inline-flex items-center gap-2 rounded-lg border px-5 py-2.5 text-sm font-medium hover:bg-accent transition-colors"
            >
              View all 23 skills with decision trees <ArrowRight className="h-4 w-4 text-primary" />
            </Link>
          </div>
        </div>
      </section>

      {/* ── How it works ────────────────────────────────────────── */}
      <section className="max-w-screen-xl mx-auto px-6 py-20 space-y-12">
        <div className="text-center space-y-3 max-w-2xl mx-auto">
          <p className="text-xs font-semibold uppercase tracking-widest text-primary">How It Works</p>
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">MCP-first execution</h2>
          <p className="text-muted-foreground">
            Skills don't write instructions — they execute. Every action runs directly inside your Blender session via the BlenderMCP addon.
          </p>
        </div>

        <div className="grid sm:grid-cols-3 gap-6">
          {[
            {
              step: '01',
              title: 'Prompt in Claude',
              desc: 'Describe what you want to build. blender-director plans the pipeline and selects the right skills.',
            },
            {
              step: '02',
              title: 'MCP executes in Blender',
              desc: 'Skills call BlenderMCP tools directly — objects, materials, modifiers, UV maps, renders. All inside your live Blender session.',
            },
            {
              step: '03',
              title: 'Validate and export',
              desc: 'asset-optimization validates polycount, naming, and UV quality. export-pipeline delivers a game-ready file.',
            },
          ].map((item) => (
            <div key={item.step} className="relative rounded-xl border p-6 space-y-3">
              <span className="text-5xl font-black text-muted/80 leading-none select-none">
                {item.step}
              </span>
              <h3 className="font-semibold text-base">{item.title}</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ── CTA ─────────────────────────────────────────────────── */}
      <section className="border-t bg-primary/5">
        <div className="max-w-screen-xl mx-auto px-6 py-20 text-center space-y-6">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">
            Ready to build?
          </h2>
          <p className="text-muted-foreground max-w-xl mx-auto">
            Get Blender Skills installed in two commands and start your first production asset in minutes.
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

import Link from 'next/link'
import { ArrowRight, CheckCircle2, Terminal } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { SKILL_COUNT, SITE_VERSION, platforms } from '@/lib/skills-data'

function CodeBlock({ children }: { children: string }) {
  return <pre className="my-4">{children.trim()}</pre>
}

function Step({ n, title, children }: { n: number; title: string; children: React.ReactNode }) {
  return (
    <div className="flex gap-4">
      <div className="flex flex-col items-center">
        <div className="h-8 w-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-bold shrink-0">
          {n}
        </div>
        <div className="flex-1 w-px bg-border mt-2" />
      </div>
      <div className="pb-10 flex-1 min-w-0">
        <h3 className="font-semibold text-base mb-3">{title}</h3>
        {children}
      </div>
    </div>
  )
}

export default function GettingStartedPage() {
  return (
    <div className="max-w-3xl space-y-12 pb-16">
      <div className="space-y-3">
        <div className="flex flex-wrap gap-2">
          <Badge>Getting Started</Badge>
          <Badge variant="muted">v{SITE_VERSION}</Badge>
        </div>
        <h1 className="text-4xl font-bold tracking-tight">Getting Started</h1>
        <p className="text-lg text-muted-foreground">
          Install Blender Skills in <strong>Cursor</strong>, <strong>Claude Code</strong>,{' '}
          <strong>Kiro</strong>, or <strong>Codex</strong>, then connect Blender MCP for live execution.
        </p>
      </div>

      {/* Platforms overview */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Supported Agents</h2>
        <div className="grid sm:grid-cols-2 gap-3">
          {platforms.map((p) => (
            <div key={p.name} className="rounded-lg border p-4 space-y-1">
              <p className="font-semibold">{p.name}</p>
              <p className="text-sm text-muted-foreground">{p.blurb}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Installation */}
      <section className="space-y-6">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Installation</h2>

        <div className="rounded-lg border border-yellow-500/40 bg-yellow-500/5 px-4 py-4 text-sm space-y-1">
          <p className="font-semibold text-foreground">Marketplace listing under review</p>
          <p className="text-muted-foreground">
            Install directly from GitHub for all platforms until marketplace install is available.
          </p>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">1. Clone the repo</h3>
          <CodeBlock>{`git clone https://github.com/arjun988/blender-skills.git`}</CodeBlock>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">2. Claude Code</h3>
          <p className="text-muted-foreground text-sm mb-2">
            Copy skills into your project&apos;s <code>.claude/skills/</code> folder.
          </p>
          <CodeBlock>{`cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/
# Restart Claude Code after copying`}</CodeBlock>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">3. Cursor</h3>
          <p className="text-muted-foreground text-sm mb-2">
            Copy into Cursor project skills (Windows PowerShell example):
          </p>
          <CodeBlock>{`Copy-Item -Recurse -Force "blender-skills\\.claude\\skills\\*" ".cursor\\skills\\"
# Restart Cursor after copying`}</CodeBlock>
          <p className="text-sm text-muted-foreground mt-2">
            macOS/Linux: <code>cp -r blender-skills/.claude/skills/* .cursor/skills/</code>
          </p>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">4. Kiro</h3>
          <p className="text-muted-foreground text-sm mb-2">
            Kiro uses agent skills folders similarly — copy the skill directories into your Kiro skills path
            (project or user skills, depending on your Kiro setup), then restart Kiro.
          </p>
          <CodeBlock>{`# Example: copy into your Kiro skills directory
cp -r blender-skills/.claude/skills/* /path/to/kiro/skills/
# Point Blender MCP at the same BlenderMCP addon session`}</CodeBlock>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">5. Codex</h3>
          <p className="text-muted-foreground text-sm mb-2">
            Mount or copy <code>.claude/skills</code> into your Codex skills / instructions path so the
            agent can discover <code>SKILL.md</code> files. Configure Blender MCP the same way you would
            for other MCP-capable clients.
          </p>
          <CodeBlock>{`# Example: symlink skills into Codex skills path
ln -s /path/to/blender-skills/.claude/skills /path/to/codex/skills/blender-skills
# Or copy: cp -r blender-skills/.claude/skills/* /path/to/codex/skills/`}</CodeBlock>
        </div>
      </section>

      {/* Connect Blender MCP */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Connect Blender MCP</h2>
        <p className="text-muted-foreground">
          Every skill executes inside Blender via the BlenderMCP addon. Required for MCP execution —
          without it, skills fall back to instructions only.
        </p>

        <div>
          <Step n={1} title="Install uv">
            <CodeBlock>{`# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh`}</CodeBlock>
          </Step>

          <Step n={2} title="Install the BlenderMCP addon in Blender">
            <p className="text-sm text-muted-foreground mb-3">
              Download{' '}
              <a
                href="https://github.com/ahujasid/blender-mcp/raw/main/addon.py"
                className="text-primary hover:underline"
                target="_blank"
                rel="noopener noreferrer"
              >
                addon.py
              </a>{' '}
              then in Blender:
            </p>
            <CodeBlock>{`Edit → Preferences → Add-ons → Install → select addon.py → Enable "Blender MCP"`}</CodeBlock>
          </Step>

          <Step n={3} title="Start the MCP server in Blender">
            <p className="text-sm text-muted-foreground">
              In the Blender 3D Viewport press <code>N</code> → <strong>BlenderMCP</strong> tab →{' '}
              <strong>Connect to Claude</strong> (works as the MCP bridge for all clients).
            </p>
          </Step>

          <Step n={4} title="Restart your agent client">
            <p className="text-sm text-muted-foreground mb-2">
              This repo ships MCP config for Cursor and Claude Code. Kiro and Codex should point at the
              same BlenderMCP server once skills are installed.
            </p>
            <div className="overflow-x-auto rounded-lg border">
              <table className="w-full text-sm">
                <thead className="bg-muted">
                  <tr>
                    <th className="text-left px-4 py-2 font-medium">Config / Path</th>
                    <th className="text-left px-4 py-2 font-medium">Client</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">.cursor/mcp.json + .cursor/skills/</td>
                    <td className="px-4 py-2 text-muted-foreground">Cursor</td>
                  </tr>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">.mcp.json + .claude/skills/</td>
                    <td className="px-4 py-2 text-muted-foreground">Claude Code</td>
                  </tr>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">Kiro skills dir + Blender MCP</td>
                    <td className="px-4 py-2 text-muted-foreground">Kiro</td>
                  </tr>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">Codex skills path + Blender MCP</td>
                    <td className="px-4 py-2 text-muted-foreground">Codex</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </Step>
        </div>
      </section>

      {/* Verify */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Verify Setup</h2>
        <div className="space-y-2">
          {[
            `Skills visible (${SKILL_COUNT} expected) — try mentioning "blender-director"`,
            'Blender MCP connected (green status in addon panel)',
            'Test: "List objects in the current Blender scene"',
            'Collections use COL_ prefix, meshes use SM_ prefix',
          ].map((item) => (
            <div key={item} className="flex gap-2 text-sm">
              <CheckCircle2 className="h-4 w-4 text-primary shrink-0 mt-0.5" />
              <span className="text-muted-foreground">{item}</span>
            </div>
          ))}
        </div>
      </section>

      {/* First Prompt */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">First Prompt</h2>
        <p className="text-muted-foreground">
          Start with <strong>blender-director</strong> — it plans the pipeline and routes genre, style, and discipline skills.
        </p>
        <CodeBlock>{`Plan and create a game-ready sci-fi crate for Unity — 1500 tris, realistic PBR, export to FBX`}</CodeBlock>
        <p className="text-sm text-muted-foreground">The agent will:</p>
        <ol className="space-y-1 text-sm text-muted-foreground list-decimal list-inside">
          <li>Activate <strong>blender-director</strong> → production brief</li>
          <li>Route to <strong>hard-surface</strong> + <strong>realistic-style</strong> + <strong>unity-export</strong></li>
          <li>Execute via Blender MCP</li>
          <li>Validate with <strong>asset-optimization</strong> / <strong>qa-review</strong></li>
        </ol>
      </section>

      {/* Examples */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Example Prompts</h2>
        <div className="space-y-3">
          {[
            'Match this reference photo — industrial spaceship, analyze first then build in Blender',
            'Build a liminal Backrooms lobby — fluorescent hum, stained carpet, endless doors',
            'Cyberpunk street vendor stall, neon-retrofuturism, Unreal export with UCX',
            'Soulslike chapel interior, dark fantasy, fog gate landmark',
            'HD-2D forest clearing, pixel party characters, theatrical DoF',
            'JRPG starter town, cozy mood, hand-painted materials',
            'Model a game-ready sedan for Unreal with LODs and UCX collision',
            'Scatter rocks on this cliff using geometry nodes, then bake for export',
          ].map((prompt) => (
            <div key={prompt} className="rounded-lg border bg-muted/40 px-4 py-3">
              <Terminal className="h-3.5 w-3.5 inline mr-2 text-primary" />
              <span className="text-sm italic text-foreground/80">&ldquo;{prompt}&rdquo;</span>
            </div>
          ))}
        </div>
      </section>

      {/* Troubleshooting */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Troubleshooting</h2>
        <div className="space-y-4">
          <div>
            <p className="font-semibold text-sm">Skills not activating</p>
            <p className="text-sm text-muted-foreground mt-1">
              Ensure skills are in the correct path for your client (Cursor <code>.cursor/skills/</code>,
              Claude Code <code>.claude/skills/</code>, or your Kiro/Codex skills directory). Restart after copying.
            </p>
          </div>
          <div>
            <p className="font-semibold text-sm">MCP not connecting</p>
            <p className="text-sm text-muted-foreground mt-1">
              Usually a <code>uv</code> PATH issue or the BlenderMCP addon wasn&apos;t started. See{' '}
              <a
                href="https://github.com/arjun988/blender-skills/blob/main/docs/BLENDER_MCP_SETUP.md"
                className="text-primary hover:underline"
                target="_blank"
                rel="noopener noreferrer"
              >
                BLENDER_MCP_SETUP.md
              </a>
              .
            </p>
          </div>
          <div>
            <p className="font-semibold text-sm">Agent describes UI instead of executing</p>
            <p className="text-sm text-muted-foreground mt-1">
              Remind it: <code>&ldquo;Use Blender MCP tools&rdquo;</code> — skills enforce MCP-first.
            </p>
          </div>
        </div>
      </section>

      <div className="rounded-xl border bg-primary/5 p-6 space-y-3">
        <h3 className="font-bold">Next Steps</h3>
        <div className="flex flex-col sm:flex-row gap-3">
          <Link
            href="/skills"
            className="flex items-center gap-2 rounded-lg border bg-background px-4 py-3 text-sm hover:bg-accent transition-colors"
          >
            Browse all {SKILL_COUNT} skills <ArrowRight className="ml-auto h-4 w-4 text-primary" />
          </Link>
          <a
            href="https://github.com/arjun988/blender-skills/blob/main/CONTRIBUTING.md"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 rounded-lg border bg-background px-4 py-3 text-sm hover:bg-accent transition-colors"
          >
            Contribute a skill <ArrowRight className="ml-auto h-4 w-4 text-primary" />
          </a>
        </div>
      </div>
    </div>
  )
}

import Link from 'next/link'
import { ArrowRight, CheckCircle2, Terminal } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

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

function Callout({ children, type = 'note' }: { children: React.ReactNode; type?: 'note' | 'tip' | 'warning' }) {
  const styles = {
    note: 'border-primary/40 bg-primary/5 text-foreground',
    tip: 'border-green-500/40 bg-green-500/5 text-foreground',
    warning: 'border-yellow-500/40 bg-yellow-500/5 text-foreground',
  }
  const labels = { note: 'Note', tip: 'Tip', warning: 'Warning' }
  return (
    <div className={`my-4 rounded-lg border px-4 py-3 text-sm ${styles[type]}`}>
      <strong>{labels[type]}: </strong>
      {children}
    </div>
  )
}

export default function GettingStartedPage() {
  return (
    <div className="max-w-3xl space-y-12 pb-16">
      {/* Header */}
      <div className="space-y-3">
        <div className="flex gap-2">
          <Badge>Getting Started</Badge>
        </div>
        <h1 className="text-4xl font-bold tracking-tight">Getting Started</h1>
        <p className="text-lg text-muted-foreground">
          Get up and running with Blender Skills in Claude Code or Cursor with Blender MCP.
        </p>
      </div>

      {/* Installation */}
      <section className="space-y-6">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Installation</h2>

        {/* Under review notice */}
        <div className="rounded-lg border border-yellow-500/40 bg-yellow-500/5 px-4 py-4 text-sm space-y-1">
          <p className="font-semibold text-foreground">🕐 Marketplace listing under review</p>
          <p className="text-muted-foreground">
            The Claude Code marketplace submission is currently being reviewed by Anthropic.
            In the meantime, install directly from GitHub using the methods below.
          </p>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">Install from GitHub — Claude Code</h3>
          <p className="text-muted-foreground text-sm mb-2">Clone the repo and copy skills into your project.</p>
          <CodeBlock>{`git clone https://github.com/arjun988/blender-skills.git
cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/`}</CodeBlock>
          <p className="text-sm text-muted-foreground">Restart Claude Code after copying.</p>
        </div>

        <div>
          <h3 className="font-semibold mb-1 text-lg">Install from GitHub — Cursor</h3>
          <p className="text-muted-foreground text-sm mb-2">Copy skills to Cursor's project skills folder (Windows).</p>
          <CodeBlock>{`git clone https://github.com/arjun988/blender-skills.git
Copy-Item -Recurse -Force "blender-skills\\.claude\\skills\\*" ".cursor\\skills\\"`}</CodeBlock>
          <p className="text-sm text-muted-foreground">Restart Cursor after copying.</p>
        </div>
      </section>

      {/* Connect Blender MCP */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Connect Blender MCP</h2>
        <p className="text-muted-foreground">
          Every skill executes directly inside Blender via the BlenderMCP addon. This is required for MCP execution — without it, skills fall back to instructions only.
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
              Download <a href="https://github.com/ahujasid/blender-mcp/raw/main/addon.py" className="text-primary hover:underline" target="_blank" rel="noopener noreferrer">addon.py</a> then in Blender:
            </p>
            <CodeBlock>{`Edit → Preferences → Add-ons → Install → select addon.py → Enable "Blender MCP"`}</CodeBlock>
          </Step>

          <Step n={3} title="Start the MCP server in Blender">
            <p className="text-sm text-muted-foreground">
              In the Blender 3D Viewport press <code>N</code> to open the sidebar → find the <strong>BlenderMCP</strong> tab → click <strong>Connect to Claude</strong>.
            </p>
          </Step>

          <Step n={4} title="Restart Cursor / Claude Code">
            <p className="text-sm text-muted-foreground mb-2">
              This repo ships preconfigured MCP config files — no manual editing needed:
            </p>
            <div className="overflow-x-auto rounded-lg border">
              <table className="w-full text-sm">
                <thead className="bg-muted">
                  <tr>
                    <th className="text-left px-4 py-2 font-medium">Config File</th>
                    <th className="text-left px-4 py-2 font-medium">Client</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">.cursor/mcp.json</td>
                    <td className="px-4 py-2 text-muted-foreground">Cursor (project)</td>
                  </tr>
                  <tr className="border-t">
                    <td className="px-4 py-2 font-mono text-xs">.mcp.json</td>
                    <td className="px-4 py-2 text-muted-foreground">Claude Code (project)</td>
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
            'Skills visible in agent context (try mentioning "blender-director")',
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
          Start with <strong>blender-director</strong> on any complex task — it plans the pipeline and routes to the right skills automatically.
        </p>
        <CodeBlock>{`Plan and create a game-ready sci-fi crate for Unity — 1500 tris, realistic PBR, export to FBX`}</CodeBlock>
        <p className="text-sm text-muted-foreground">The agent will:</p>
        <ol className="space-y-1 text-sm text-muted-foreground list-decimal list-inside">
          <li>Activate <strong>blender-director</strong> → output production brief</li>
          <li>Route to <strong>hard-surface</strong> + <strong>realistic-style</strong></li>
          <li>Execute via Blender MCP (not UI walkthroughs)</li>
          <li>Validate with <strong>asset-optimization</strong> → <strong>export-pipeline</strong></li>
        </ol>
      </section>

      {/* Good prompts */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold tracking-tight border-b pb-2">Example Prompts</h2>
        <div className="space-y-3">
          {[
            'Match this reference photo — industrial spaceship, analyze first then build in Blender',
            'Create a modular sci-fi wall kit for Unreal Engine with 2m grid snapping',
            'Block out a horror corridor inspired by Silent Hill — narrow, flickering fluorescent',
            'Retopologize this creature sculpt for game animation, 15k triangle budget',
            'Export this character with walk cycle to FBX for Unity',
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
              Ensure skills are in <code>.cursor/skills/</code> (Cursor) or <code>.claude/skills/</code> (Claude Code). Restart the client after copying.
            </p>
          </div>
          <div>
            <p className="font-semibold text-sm">MCP not connecting</p>
            <p className="text-sm text-muted-foreground mt-1">
              Usually a <code>uv</code> PATH issue or the BlenderMCP addon wasn't started. See{' '}
              <a href="https://github.com/arjun988/blender-skills/blob/main/docs/BLENDER_MCP_SETUP.md" className="text-primary hover:underline" target="_blank" rel="noopener noreferrer">
                BLENDER_MCP_SETUP.md
              </a>.
            </p>
          </div>
          <div>
            <p className="font-semibold text-sm">Agent describes UI instead of executing</p>
            <p className="text-sm text-muted-foreground mt-1">
              Remind it: <code>&ldquo;Use Blender MCP tools&rdquo;</code> — skills enforce MCP-first in <code>mcp-integration.md</code>.
            </p>
          </div>
        </div>
      </section>

      {/* Next Steps */}
      <div className="rounded-xl border bg-primary/5 p-6 space-y-3">
        <h3 className="font-bold">Next Steps</h3>
        <div className="flex flex-col sm:flex-row gap-3">
          <Link
            href="/skills"
            className="flex items-center gap-2 rounded-lg border bg-background px-4 py-3 text-sm hover:bg-accent transition-colors"
          >
            Browse all 23 skills <ArrowRight className="ml-auto h-4 w-4 text-primary" />
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

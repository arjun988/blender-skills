# Blender MCP Setup Guide

Connect [BlenderMCP](https://github.com/ahujasid/blender-mcp) to Cursor or Claude Code so the AAA Blender Skills Pack can execute operations directly in Blender.

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Blender | 3.0+ |
| Python | 3.10+ (3.11 recommended) |
| uv package manager | Latest |

### Install uv (Windows)

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Add uv to PATH:

```powershell
$localBin = "$env:USERPROFILE\.local\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;$localBin", "User")
```

Restart Cursor/Claude Code after installing.

## Step 1: Install Blender Addon

1. Download [`addon.py`](https://github.com/ahujasid/blender-mcp/raw/main/addon.py) from the BlenderMCP repo
2. Open Blender → **Edit → Preferences → Add-ons**
3. Click **Install...** → select `addon.py`
4. Enable **Interface: Blender MCP**

Optional: store API keys in **Edit → Preferences → Add-ons → Blender MCP** for Sketchfab, Hyper3D, Hunyuan3D.

## Step 2: Start Blender Connection

1. In Blender 3D View, press **N** to open sidebar
2. Open the **BlenderMCP** tab
3. (Optional) Enable Poly Haven for asset downloads
4. Click **Connect to Claude**

The addon listens on `localhost:9876` by default.

## Step 3: Configure MCP Client

### Cursor (this repo — already configured)

This project includes `.cursor/mcp.json`. After installing uv:

1. Fully quit and restart Cursor
2. Open **Settings → MCP** — verify `blender` server appears
3. Ensure Blender addon shows **Connected**

If `uvx` is not found from Cursor's GUI, use the full path:

```json
{
  "mcpServers": {
    "blender": {
      "command": "C:\\Users\\YOUR_USER\\.local\\bin\\uvx.exe",
      "args": ["--python", "3.11", "blender-mcp"],
      "env": {
        "BLENDER_HOST": "localhost",
        "BLENDER_PORT": "9876"
      }
    }
  }
}
```

Find your path: `where uvx` in PowerShell.

### Claude Code CLI

```bash
claude mcp add blender cmd /c uvx --python 3.11 blender-mcp
```

Or add to project `.mcp.json` (see repo root).

### Claude Desktop

Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "blender": {
      "command": "cmd",
      "args": ["/c", "uvx", "--python", "3.11", "blender-mcp"],
      "env": {
        "BLENDER_HOST": "localhost",
        "BLENDER_PORT": "9876"
      }
    }
  }
}
```

## Step 4: Verify Connection

1. Blender addon: **Connected** status
2. Cursor: MCP panel shows blender tools
3. Test prompt: *"Get the current Blender scene info"*

Expected tools include scene inspection, object creation, material assignment, viewport screenshots, and Python execution.

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `BLENDER_HOST` | `localhost` | Blender socket host |
| `BLENDER_PORT` | `9876` | Blender socket port |
| `DISABLE_TELEMETRY` | unset | Set `true` to disable telemetry |
| `BLENDERMCP_SKETCHFAB_API_KEY` | — | Sketchfab downloads |
| `BLENDERMCP_HYPER3D_API_KEY` | — | Hyper3D generation |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `spawn uvx ENOENT` | Use full path to `uvx.exe` in MCP config |
| Connection refused | Start Blender addon; click Connect |
| First command fails | Retry — first call sometimes times out |
| Port conflict | Only run MCP in one client (Cursor OR Claude Desktop) |
| Python version errors | Pin `--python 3.11` in args |
| Stale cache | `uv cache clean blender-mcp && uvx --refresh blender-mcp` |

## Security Note

The `execute_blender_code` tool runs arbitrary Python in Blender. **Save your `.blend` file before agent sessions.**

## Skills Integration

Once connected, all skills in this pack prefer MCP execution. See:

- `.claude/skills/references/mcp-integration.md` — Agent protocol
- `.claude/skills/references/mcp-tools.md` — Tool catalog

## Links

- [BlenderMCP GitHub](https://github.com/ahujasid/blender-mcp)
- [BlenderMCP Official Site](https://blendermcp.org/)
- [uv Installation](https://docs.astral.sh/uv/getting-started/installation/)

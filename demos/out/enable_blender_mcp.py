"""
Enable MCP for Blender addon, persist prefs, and start the socket server (Connect).
Run with GUI Blender (not --background) so the server stays alive:

  /Applications/Blender.app/Contents/MacOS/Blender --python demos/out/enable_blender_mcp.py
"""

from __future__ import annotations

import bpy


MODULE = "blender_mcp"
PORT = 9876


def main() -> None:
    print("BRA-10: enabling", MODULE)
    try:
        bpy.ops.preferences.addon_enable(module=MODULE)
    except Exception as exc:
        print("addon_enable error:", exc)

    enabled = MODULE in bpy.context.preferences.addons.keys()
    print("addon enabled:", enabled)
    if not enabled:
        raise SystemExit(f"Failed to enable {MODULE}")

    # Persist so next Blender launch keeps the addon on
    bpy.ops.wm.save_userpref()
    print("user preferences saved")

    scene = bpy.context.scene
    scene.blendermcp_port = PORT
    scene.blendermcp_auto_start_server = True

    # Start Connect (same as sidebar "Connect to MCP server")
    result = bpy.ops.blendermcp.start_server()
    print("start_server result:", result)

    server = getattr(bpy.types, "blendermcp_server", None)
    running = bool(server and getattr(server, "running", False))
    print(f"BlenderMCP server running={running} host=localhost port={PORT}")
    if not running:
        raise SystemExit("MCP server failed to start")


if __name__ == "__main__":
    main()

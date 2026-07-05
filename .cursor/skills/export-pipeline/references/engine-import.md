# Engine Import

## Unreal Engine 5

1. Import FBX with Combine Meshes off for modular
2. Import Normals: Import Normals and Tangents
3. Transform: Verify scale — may need 0.01 if Blender 1m = UE 1cm
4. Materials: Create Material Instances from imported slots
5. Collision: Import `SM_*_COL` as UCX/UBX

## Unity

1. GLTF or FBX import
2. Scale Factor: 1 (verify)
3. Generate Lightmap UVs if not provided
4. Humanoid rig: Configure Avatar mapping

## Godot 4

1. GLB preferred
2. Root scale 1.0
3. Materials: StandardMaterial3D from PBR textures

## First Import Test Checklist

- [ ] Known dimension matches (door = 2m)
- [ ] Normals correct (no black faces)
- [ ] Textures assigned
- [ ] Pivot at expected location
- [ ] Animation plays (if rigged)

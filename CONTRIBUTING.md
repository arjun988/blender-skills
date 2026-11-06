# Contributing to Blender Skills Pack

Guidelines for contributing skills, references, and fixes.

## How to Contribute

### Reporting Issues
- Use [GitHub Issues](https://github.com/arjun988/blender-skills/issues)
- Include: steps to reproduce, expected vs actual behavior, Blender version, MCP status

### Suggesting New Skills
When proposing a new skill:
1. Explain the use case and target Blender discipline
2. List what MCP operations it would drive
3. Describe triggering keywords
4. Provide example prompts

### Submitting Changes

#### 1. Fork and Clone
```bash
git clone https://github.com/arjun988/blender-skills.git
cd blender-skills
```

#### 2. Create a Branch
```bash
git checkout -b feature/my-new-skill
# or
git checkout -b fix/my-bug-fix
```

#### 3. Make Changes

**Adding a new skill:**
```bash
mkdir -p .claude/skills/my-skill
# Create SKILL.md following the schema below
# Add references/ subfolder for supporting docs
```

**Syncing to Cursor and Antigravity:**
```powershell
Copy-Item -Recurse -Force ".claude\skills\*" ".cursor\skills\"
Copy-Item -Recurse -Force ".claude\skills\*" ".agents\skills\"
```

#### 4. Commit
```bash
git add .
git commit -m "Add: My New Blender Skill for XYZ discipline"
```

Commit prefix convention:
- `Add:` — new skill or reference file
- `Fix:` — bug fix in existing skill
- `Update:` — improvements to existing content
- `Docs:` — documentation only

#### 5. Push and Open a Pull Request
```bash
git push origin feature/my-new-skill
```

---

## SKILL.md Schema

Every skill must follow this frontmatter exactly:

```yaml
---
name: skill-name
description: Use when [triggering conditions]. Invoke for [specific keywords].
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: keyword1, keyword2, phrase1
  related-skills: blender-director, hard-surface, materials
---
```

**Description formula (required):**
```
Use when [condition]. Invoke for [keywords].
```

### Required Sections (in order)

```markdown
# Skill Name

One-sentence expert role definition.

## Role Definition

2–3 sentences. Define the expert persona. Mention specializations.

## When to Use

- Bullet: specific scenario
- Bullet: triggering keywords or task types

## Core Workflow

1. **Step** — description
2. **Step** — description

## Technical Guidelines

Tables, code examples, patterns. Domain-specific content.

## Constraints

### MUST DO
- [Required practice]

### MUST NOT DO
- [Anti-pattern]

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| ... | `references/....md` | ... |

## Knowledge Reference

keyword1, keyword2, keyword3, phrase, term, concept
```

### Progressive Disclosure Pattern

Lean `SKILL.md` (~80–120 lines) + `references/` subfolder.

```
.claude/skills/my-skill/
├── SKILL.md
└── references/
    ├── topic-a.md
    └── topic-b.md
```

Reference files use this header:
```markdown
# Topic Title

> Reference for: skill-name
> Load when: [condition]
```

---

## Blender MCP Rules

All skills that interact with Blender must:
- Execute via `execute_blender_code` — never describe manual UI steps
- Read tool schemas before calling (see `references/mcp-tools.md`)
- Use non-destructive patterns (duplicate before destructive ops)
- Validate via scene query after each phase

---

## Reference Image Tasks

Skills that handle photo/concept matching must reference `references/reference-image-match.md` and enforce:
1. Reference Analysis before MCP execution
2. Camera match before geometry detail
3. Screenshot comparison loop
4. `visual-match-checklist.md` before delivery

---

## Testing Your Skill

Before submitting:
1. **Trigger test** — does it activate with expected prompts?
2. **MCP test** — does the Python code run in Blender without error?
3. **Completeness** — does it cover the main use cases?
4. **Schema** — does frontmatter match the required format?
5. **Sync** — run `Copy-Item -Recurse -Force ".claude\skills\*" ".cursor\skills\"` and `Copy-Item -Recurse -Force ".claude\skills\*" ".agents\skills\"` and verify

---

## Code of Conduct

Be respectful. This is a creative/technical community. Harassment, gatekeeping, or dismissive behavior toward contributors is not tolerated.

---

## Questions

- Open a [GitHub Discussion](https://github.com/arjun988/blender-skills/discussions)
- File an [Issue](https://github.com/arjun988/blender-skills/issues)

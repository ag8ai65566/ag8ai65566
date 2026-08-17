# How this skill got here

Vendored from <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill> (MIT,
© Next Level Builder), version **2.13.0**, on 2026-08-17.

Installed by hand rather than with the project's `uipro` CLI, because that CLI
is an npm package and this repo has no Node toolchain. The result is the same
layout the CLI's `claude` platform template produces:

- `SKILL.md` — assembled from `templates/base/skill-content.md` +
  `templates/base/quick-reference.md`, with the frontmatter and the four
  `{{...}}` placeholders filled from `templates/platforms/claude.json`.
- `scripts/` — upstream `src/ui-ux-pro-max/scripts/`, minus `tests/`.
- `data/` — upstream `src/ui-ux-pro-max/data/`, unmodified.

Nothing was edited. The scripts are Python 3 standard library only: no
third-party packages, no network access.

## Updating

Either re-run the vendoring above against a newer tag, or switch to the
plugin route, which updates itself:

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

If you take the plugin route, delete this directory first so the skill is not
registered twice.

## Checked on install

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa" --design-system -p "Demo"
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --domain ux
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
```

All three produced output.

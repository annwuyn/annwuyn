# annwuyn

Academic writing skills for Claude Code — a contrastive-rhetoric method for closing the gap
between Vietnamese-English and native academic English.

## Skills

| Skill | Use for |
|---|---|
| `annwuyn` | the method + a 15-file reference library, incl. the Academic Phrasebank phrase layer; routes to the modes below |
| `annwuyn-review` | diagnose and revise a draft, stage by stage |
| `annwuyn-scholarship` | SOP · PS · CV · LOR · application package · professor contact · interview |
| `annwuyn-paper` | research paper · proposal · abstract · literature review |

## Academic Phrasebank (optional, bring your own copy)

The phrase layer (`references/12-phrasebank.md`) indexes John Morley's *Academic Phrasebank*
(2015 enhanced PDF, © The University of Manchester) by rhetorical move and printed page. The
plugin does **not** contain the Phrasebank; point it at your own copy once:

```
python3 plugin/skills/annwuyn/scripts/phrasebank.py setup /path/to/Academic-Phrasebank.pdf
```

The text is cached at `~/.annwuyn/phrasebank/` (override with `ANNWUYN_HOME`), outside this
repo. Requires `pdftotext` (`brew install poppler`) or `pip install pypdf`. Setup also finds a
copy in `~/Downloads`, `~/Documents` or `~/Desktop`, or reads `ANNWUYN_PHRASEBANK_PDF`. In a
cloud session, attach the PDF and run `setup` on the uploaded path. Without a copy the skills
still work; they just will not quote frames or cite Phrasebank pages.

Commands: `setup` · `status` · `show 16-17` · `search "REGEX"` · `audit draft.docx`.

## Install — desktop / CLI

```
claude plugin marketplace add <path-to-this-folder>
claude plugin install annwuyn@annwuyn-plugins
```

A local path works here. Remove any personal copies at `~/.claude/skills/annwuyn*` afterwards —
that directory auto-loads as `<name>@skills-dir` and would collide.

## Install — web (claude.ai/code)

A cloud session cannot read your local disk, so a `Directory (...)` marketplace will not resolve.
The marketplace has to come from git:

```
claude plugin marketplace add <owner>/<repo>
claude plugin install annwuyn@annwuyn-plugins
```

To make it available to every session on a given project, declare it at project scope and commit
the result:

```
claude plugin marketplace add <owner>/<repo> --scope project
claude plugin install annwuyn@annwuyn-plugins --scope project
git add .claude/settings.json && git commit -m "Add annwuyn plugin"
```

A private repo requires the cloud environment to hold GitHub credentials for it; a public repo
always resolves. Before making it public, read `LICENSE` and
`plugin/skills/annwuyn/references/SOURCES.md` — the compilation is ours, the underlying handouts
and frameworks are not.

## Attribution

See `LICENSE` and `plugin/skills/annwuyn/references/SOURCES.md`.

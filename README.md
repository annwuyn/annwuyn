# annwuyn

Academic writing skills for Claude Code — a contrastive-rhetoric method for closing the gap
between Vietnamese-English and native academic English.

## Skills

| Skill | Use for |
|---|---|
| `annwuyn` | the method + a 14-file reference library; routes to the modes below |
| `annwuyn-review` | diagnose and revise a draft, stage by stage |
| `annwuyn-scholarship` | SOP · PS · CV · LOR · application package · professor contact · interview |
| `annwuyn-paper` | research paper · proposal · abstract · literature review |

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

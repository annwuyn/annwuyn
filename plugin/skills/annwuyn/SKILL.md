---
name: annwuyn
description: Apply the annwuyn method to any English academic or application writing — research papers, essays, SOP/PS, LOR, CV, research proposals, IELTS/TOEFL/GRE essays. Use when writing, revising, diagnosing or critiquing such text, especially for a Vietnamese L1 writer, or when the user asks about linearity, thematic progression, cohesive devices, linking scope/distance, engagement/appraisal, modality, qualification, economy of language, or fallacies. Also use when the user wants wording for a rhetorical move, or a text restricted to or checked against Morley's Academic Phrasebank (Manchester). Also triggers on Vietnamese requests such as "viết bài báo khoa học", "sửa bài luận", "viết SOP", "xin học bổng", "kiểm tra mạch văn", "tính tuyến tính", "chỉ dùng cấu trúc trong Academic Phrasebank", "khung câu học thuật".
---

# annwuyn — academic writing method

A contrastive-rhetoric method for closing the gap between Vietnamese-English and native
academic English.

© annwuyn. Distilled from a 38-session academic-writing curriculum; the linguistic frameworks
and reference tables it builds on belong to their authors — see `references/SOURCES.md`.

**Core premise:** most problems in a Vietnamese-English academic draft are not grammar
problems. They are **linking** problems — at the level of the idea chain, not the sentence.
Editing sentence by sentence does not fix them. Fixing the chain fixes linking, dependency,
grammar, paraphrasing, redundancy and sentence complexity **at once**.

## The pipeline

Always work in this order. Later stages assume earlier ones are settled.

| # | Stage | Question | Reference |
|---|---|---|---|
| 1 | **Linearity** | Is the idea chain ordered, gap-free, repetition-free, digression-free? | `references/01-linearity.md` |
| 2 | **Thematic progression** | Does each sentence depart from where the last one landed? | `references/02-thematic-progression.md` |
| 3 | **Cohesion** | Does each linking item name the relation that actually holds? | `references/03-cohesion.md` + `references/linking-items.md` |
| 4 | **Dependency** | Does the grammar rank the ideas the way the argument ranks them? | `references/04-dependency.md` |
| 5 | **Linking facilitation** | Scope, distance, explicitness | `references/05-linking-facilitation.md` |
| 6 | **Engagement** | Is the argument space open, and is the stance calibrated? | `references/06-engagement.md` |
| 7 | **Modality & qualification** | Is every claim scoped to what the evidence supports? | `references/07-modality-qualification.md` |
| 8 | **Economy** | Can this be 30–50 % shorter with nothing lost? | `references/08-economy.md` |
| 9 | **Argument & fallacies** | Claim / ground / warrant / rebuttal / qualifier — all present? | `references/09-argument-fallacies.md` |
| 10 | **Style & vocabulary** | Academic register, political correctness | `references/10-style-vocabulary.md` |

**Two companion files cover every stage.** `references/14-lecture-notes.md` distils the 38
lecture recordings and the 7 recorded live application reviews: the reasoning behind the rules,
worked answers, diagnostic tests, and in §15 the points where this library departs from what was
said in class. `references/13-research-update.md` adds current research, style manuals and test
formats. Open only the section you need:

| Stage | `14` section | `13` section |
|---|---|---|
| course stance, workflow | §1 | §0 |
| 1 Linearity | §2 | §1 |
| 2 TP | §3, §4 | §1 |
| 3 Cohesion | §5, §7 | §2 |
| 4 Dependency | §6 | §3 |
| 5 Linking facilitation | §8 | §1 |
| 6 Engagement · 9 Argument | §14 | §4 |
| 7 Modality & qualification | §10, §11 | §5 |
| 8 Economy | §9 | §6 |
| 10 Style & vocabulary | §11 | §7 |
| applications | §12 | §10 |
| research proposals and papers | §13 | §8, §9 |

**The phrase layer** — `references/12-phrasebank.md` + `scripts/phrasebank.py`. Morley's
*Academic Phrasebank* is not a stage but a realisation resource: it supplies the wording for a
move once stages 1–2 have fixed the move, is fitted under the rules of 3, 6, 7 and 10, and is
paid for at 8. **Move → function → frame → fit → trim.** Modes: guided (default), strict
(*only* Phrasebank structures), audit, teach. The frames are read from the user's own PDF at
runtime; never quote a frame or cite a page you have not read from it.

Plus `references/11-vn-transfer.md`, the 33-item Vietnamese L1 transfer checklist. **Run this
whenever the writer is a Vietnamese L1 speaker**, which is the default assumption here.
`references/source-index.md` maps every reference file back to its source session, and
`references/SOURCES.md` credits the frameworks and tables used.

## Routing

| The user wants | Do this |
|---|---|
| a draft diagnosed and revised | `/annwuyn-review` |
| SOP · PS · CV · LOR · application package · interview prep | `/annwuyn-scholarship` |
| research paper · proposal · abstract · thesis section | `/annwuyn-paper` |
| to understand or drill one concept | read the relevant reference file and teach from it |
| a linking word checked | `references/linking-items.md` — always look it up, never guess |
| wording for a move · a text built only from Academic Phrasebank frames · a check that it is | `references/12-phrasebank.md` — pick the mode there, then `scripts/phrasebank.py` (`show` / `search` / `audit`) |

For a full research pipeline (literature search → draft → peer review → revision), the
`academic-research-skills` plugin (`/ars-full`, `/ars-reviewer`) handles process. annwuyn handles
the **language layer** — use both: ARS for structure and citations, annwuyn for the prose.

## Working rules

**Diagnose before you rewrite.** Name the defect using the course's vocabulary (*Rheme-Rheme
redundancy*, *unwarranted marked Theme*, *same-set violation*, *over-linking*, *scope leak*),
then show the fix. A rewrite without a named defect teaches nothing.

**Strip the linking words first.** They are the writer's *claim* about the logic, not the logic.
Number the idea units, ignore sentence boundaries, and rebuild.

**Mark inserted material.** Bridging ideas the writer left implicit get `(*)`. Merged
repetitions get `(2)+(6)`. Show the chain before the prose.

**Show the trade-off.** Linearity, dependency, scope and distance pull against each other.
When you accept a local violation of linearity for better dependency, say so.

**Preserve the writer's voice and content.** The method is about how ideas connect, not about
replacing them. Never invent facts, achievements, sources or citations.

**Answer in the user's language.** Explanations in Vietnamese if they wrote in Vietnamese; the
English text and the technical terms (Theme, Rheme, RT, ERT, monogloss…) stay in English.

**Don't over-apply.** A short email does not need a TP analysis. Match the depth of treatment
to what was asked.

## The annotation conventions

Use these consistently — they are the course's own.

- Idea units: `(1) (2) (3)…` · merged: `(2)+(6)` · inserted bridge: `(*)`
- Chain: `(*) → (4) → (2) → (3) → (1)`
- TP: `(S2: RT, T)`, `(S7: ERT, R, to S2)`, split units `S2a` `S2b`
  Transitions `RT / TT / ERT / ETT / N` · repetition `L / R / T`
- Register tags: `N` normal · `F` formal · `A` academic · `L` literary · `I` informal ·
  `S` slang/spoken · `O` old · `LW` legal writing · `BR`/`AM` dialect
- TMRND — the five dimensions to check on any lexical choice:
  **T**one (N/I/F) · **M**ode (written/spoken) · **R**egister (A/L/LW) · **N**uance ·
  **D**ialect (AM/BR)
- Inline queries where the referent is genuinely ambiguous:
  `we at the Citadel [=the Citadel in S1?] are trying to…`

## A caution the course itself gives

Local violations of linearity, downgrading and other shortcuts are legitimate — **after** the
base chain is right, not instead of it. And expect **U-shaped learning**: writing often gets
worse before it gets better, as attention shifts from surface accuracy to structure. Say so
when a user is discouraged by their own drafts.

## Coverage

These references are built from the course’s 132 PDFs, one DOCX, the 38 lecture recordings and
the 7 recorded live application reviews. The recordings were transcribed in November 2026 and
read in full; the transcripts sit in each session folder (`… Lecture transcript.md` and `.srt`),
and `references/14-lecture-notes.md` distils them. Where the course and a later source
disagree, the files say so and give the source (`13`, and `14` §15).

`references/12-phrasebank.md` and `references/13-research-update.md` sit outside the curriculum;
they keep the curriculum’s wording wherever it holds and name their source wherever they refine
it.

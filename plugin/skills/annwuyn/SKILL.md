---
name: annwuyn
description: Apply the annwuyn method to any English academic or application writing — research papers, essays, SOP/PS, LOR, CV, research proposals, IELTS/TOEFL/GRE essays. Use when writing, revising, diagnosing or critiquing such text, especially for a Vietnamese L1 writer, or when the user asks about linearity, thematic progression, cohesive devices, linking scope/distance, engagement/appraisal, modality, qualification, economy of language, or fallacies. Also triggers on Vietnamese requests such as "viết bài báo khoa học", "sửa bài luận", "viết SOP", "xin học bổng", "kiểm tra mạch văn", "tính tuyến tính".
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

Plus `references/11-vn-transfer.md` — the 25-item Vietnamese L1 transfer checklist. **Run this
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

## Coverage limit

These references are built from the course's 132 PDFs and one DOCX. The **65 lecture recordings
(~9.5 GB)** are not transcribed, and the slides are deliberately sparse — many carry only a
heading plus *"→ watch sample clips"* or *"FOOD FOR THOUGHT"*. Where a point here is thinner
than expected, the reasoning is probably in the audio. See `references/source-index.md`.

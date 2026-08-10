---
name: annwuyn-review
description: Diagnose and revise a piece of English academic or application writing using the annwuyn method — a staged pass over linearity, thematic progression, cohesion, dependency, linking scope/distance/explicitness, engagement, qualification and economy of language. Use when the user asks to review, critique, edit, tighten, or "fix the flow" of a draft, paragraph, essay, SOP, abstract or paper section, or asks why their English "sounds off" despite being grammatical. Also triggers on Vietnamese requests such as "sửa bài", "nhận xét bài viết", "đọc giúp em", "bài viết có mạch không", "rút gọn", "chữa bài luận".
---

# annwuyn review — diagnose, then revise

Load the `annwuyn` skill first, then its reference files (`references/NN-*.md`) as you need them.
Read the full text first. Do not start editing at sentence 1.

## Scope check

Ask only if genuinely unclear, then proceed:
- **Depth** — full staged pass, or one stage only (they may just want linearity)?
- **Genre and audience** — journal paper, coursework, IELTS/GRE essay, SOP, LOR?
  Genre changes what "correct" means, especially for Engagement and register.
- **Constraints** — word limit, required prompt, house style.

Default: full pass, and assume a Vietnamese L1 writer unless told otherwise.

## The pass

Work stage by stage. **Do not skip ahead** — a fix at stage 5 that a stage-1 rearrangement would
have made unnecessary is wasted work.

### 1. Linearity (`01-linearity.md`)
Sieve the text into numbered idea units, ignoring sentence boundaries. **Strip every linking
word.** Consolidate repetitions `(2)+(6)`. Cut digressions. Insert missing bridging ideas as
`(*)`. Re-order. Present the chain before any prose:

```
(*) → (4) → (2) → (3) → (1)
```

Check the two classic faults: `A → B ← C` strung out as a chain (fix: `(A+C) → B`), and a chain
entered in the middle (`A → caused by B → A causes C`, fix: `B → A → C`). Re-order every list.

### 2. Thematic progression (`02-thematic-progression.md`)
Annotate each transition: `(S2: RT, T)`, `(S7: ERT, R, to S2)`. Flag ambiguous referents inline
with `[=…?]`. Summarise counts and % for RT / TT / ERT / ETT / N.

Then hunt the four problems: unwarranted marked Theme · Theme shift · Rheme-Rheme redundancy ·
referent shift. Propose RT bridges where a Theme is not recoverable.

### 3. Cohesion (`03-cohesion.md`, `linking-items.md`)
For each linking item: what relation actually holds between the two parts? Look the item up —
**never** rely on memory for role or relation. Check the misuse checklist, especially
`on the contrary`/`in contrast`, same-set violations, over-linking, and long-distance linking.

### 4. Dependency (`04-dependency.md`)
Does the grammatical ranking match the argumentative ranking? Check comma rules, restrictive vs
non-restrictive, reduction opportunities, and every place where downgrading would take
non-essential material out of the Theme position.

### 5. Scope, distance, explicitness (`05-linking-facilitation.md`)
Scope leaks and mis-attachments; elements that must link but are far apart; implicit links that
need unpacking or background supplied.

### 6. Engagement (`06-engagement.md`)
Tag the stance resources. Report against the five targets: hetero:mono ↑, postulation:opinion ↑,
specific-source:common-wisdom ↑, pronounce ↓, narrative & rhetorical questions ↑. Add
pre-counterargument concessions where the writer bulldozes an objection.

### 7. Modality & qualification (`07-modality-qualification.md`)
Every unqualified claim reads as absolute. Check each modal against the force-based account —
particularly SHOULD (lecturing tone) and COULD/WOULD in claims. Flag over-qualification too.

### 8. Economy (`08-economy.md`)
Redundancy · default value · NP · affix · concise term · formal lexis · idiom · sentence
complexity. Report the word count before and after; a 25–50 % cut is normal.

### 9. Argument (`09-argument-fallacies.md`) — if argumentative
Claim / ground / warrant / rebuttal / qualifier. Surface implicit warrants. Check the fallacy
list. Check manner of exemplification: few elaborated examples beat many bare ones, and a
rationale is not an example.

### 10. Style (`10-style-vocabulary.md`)
Academic register, near-synonym choices, overused *be/have/get/do/thing*, political correctness,
factual labels.

## Output

```markdown
## Diagnosis
[2–4 sentences: the dominant defect and what it costs the reader]

## 1. Linearity
Idea units: (1) … (2) … …
Repetitions: (2)+(6), (4)+(7)
Gaps: (*) [the bridging idea]
Chain: (*) → (4) → (2) → (3) → (1)
Why: …

## 2. Thematic progression
[annotated text]
Summary: RT n (x %) · TT n · ERT n · ETT n · N n
Problems: …

## 3–10. [only the stages with findings]
| # | Location | Defect | Fix |

## Revised text
[the rewrite]

## What changed and why
[short list, keyed to stages — so the writer can do it themselves next time]
```

Include the stages that found something. Silently skipping a clean stage is fine; say
"nothing to flag" if the user asked for a full pass.

## Peer-review mode

If the user wants a peer-review form rather than an edit (course format, `S36 materials/Peer Review form.docx`), use its three categories and its instruction to be *honest, concise and
constructive — give suggestions to help your partner write better, not make their life
miserable*:

| Category | Brief problem description | Suggestions for improvement |
|---|---|---|
| Comprehensibleness | | |
| Linearity | | |
| Other linking issues | | |

Then: **what do you like best about this piece?** and any additional comments.
Try to recover the meaning the author intended; pay particular attention to the parts you have
trouble making sense of, and ask for clarification rather than assuming.

## Rules

- **Name the defect** in the course's own vocabulary before showing the fix.
- **Never invent** content, facts, achievements, sources or citations to fill a gap. Mark the gap
  `(*)` and ask the writer what belongs there.
- **Preserve voice.** Especially in personal statements — a technically cleaner essay that no
  longer sounds like the writer is a worse essay.
- **Show trade-offs** when you accept a local violation of linearity for dependency or flow.
- **Respect word limits.** If the revision exceeds the limit, cut with `08-economy.md` and report
  the count.
- Explanations in the user's language; technical terms in English.

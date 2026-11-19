# 00 — Writing a complete manuscript

This file runs a whole paper from inputs to a submission-ready file. Each stage points to the
reference that holds the rules. It follows the book’s structure (Beins & Beins, 2021, Part II)
and the APA 7 *Publication Manual*.

---

## Stage 0. Brief (ask before writing)

Collect, or ask for, in one message:

| Item | Why it matters |
|---|---|
| Paper type: empirical (quantitative / qualitative / mixed), review, term paper, thesis chapter, student lab report | sets structure and reporting standard |
| Target venue and its author guidelines (word limit, abstract limit, reference style, sections) | overrides book defaults |
| Readers: specialists or a general journal | sets opening breadth (`01` §1) |
| Student or professional format | title page, running head, author note (`02`) |
| Research question and hypotheses | the spine of every section |
| Design, participants, measures, procedure | Method (`07`) |
| Analysis output: descriptives, tests, effect sizes, CIs; tables or raw data | Results (`08`) |
| Source list with full references (or a Zotero export) | Introduction, Discussion, References (`10`) |
| Ethics approval details; data availability; funding; conflicts; AI use | Method and author note |

**Integrity rules for the whole run:** never invent data, statistics, participants, quotations or
citations. Where an input is missing, write a visible placeholder (`[CITE: claim]`,
`[STAT: t(df) = ?, p = ?, d = ?]`, `[N = ?]`) and list every placeholder at the end. Verify
references with `/ars-citation-check` before submission.

## Stage 1. Spine

Write one page before any prose:

1. Title draft (content words only, no “A study of”).
2. Research question in one sentence; hypotheses numbered H1…Hn, each with its idea chain
   (`01` §6).
3. Move map for the Introduction: territory → gap (form) → hook → present study → hypotheses →
   implications (`01` §2–3, §6).
4. One line per planned result, in hypothesis order (`08`).
5. One line per Discussion move (`09`).

Show the spine to the user and agree it before drafting.

## Stage 2. Draft in working order

Write the sections in the order that makes each one easiest. The book presents the paper in
reading order; most writing guides (Bem, 2004; Silvia, 2015) draft the concrete parts first:

| Order | Section | Reference | Notes |
|---|---|---|---|
| 1 | Method | `07` | Concrete; fixes terms and variable names for the rest of the paper |
| 2 | Results | `08` | Words → descriptives → test → effect size → words; hypothesis order |
| 3 | Discussion | `09` | Answers the hypotheses; returns to the Introduction’s key studies |
| 4 | Introduction | `01` | Now you know what it must set up; offer two or three openings |
| 5 | Abstract | `02` | Last, from the finished text; within the venue’s word limit |
| 6 | Title | `02` | Revise the draft title to match the findings |
| 7 | References | `10` | Built as you cite; checked at the end |
| 8 | Tables, figures, appendices | `08`, `02` | Numbered in order of first mention |

For multi-study papers use the structure in `02` (Box 15.2): Experiment 1, Experiment 2, General
Discussion.

## Stage 3. Integration pass (the hourglass check)

Read the draft once for consistency across sections:

- Every construct in the hypotheses is defined in the Introduction and measured in the Method,
  with the same name throughout.
- Every hypothesis appears in the Results, in the same order, and gets a verdict in the
  Discussion.
- The key studies cited in the Introduction return in the Discussion.
- Numbers match everywhere: *N*, exclusions, means, test values, abstract versus text.
- Tense: past for what was done and found; present for conclusions and established claims.
- Causal language matches the design.
- The abstract contains nothing the paper does not.

## Stage 4. Language pass

Run the `annwuyn` pipeline section by section (linearity → thematic progression → cohesion →
engagement → qualification → economy). Apply `12` (style, bias-free language, specific words) and
the user’s house rules. Phrasebank wording only after the moves are fixed.

## Stage 5. Format pass and error audit

- APA mechanics and page layout: `02`.
- Error audit: `03` (34 items from the annotated manuscript in Appendix A), plus the JARS checks
  at the end of `03`.
- Venue-specific rules last; they override APA where they differ.

## Stage 6. Deliverables

- **Manuscript file:** `.docx` unless the venue asks otherwise. APA 7: double spacing throughout,
  1-in. (2.54 cm) margins, page numbers top right, an accessible font (APA 7 accepts Calibri 11,
  Arial 11, Georgia 11, Times New Roman 12 and similar). Use the venue’s template if it has one.
  Build with pandoc and a reference .docx styled to these rules, or with the `docx` skill.
- **Title page and author note** as a separate file if the venue runs masked review.
- **Tables and figures** embedded after first mention, or at the end, as the venue asks.
- **Placeholder list** and a short **change log** for the user.
- Optional: cover letter (`annwuyn-scholarship` covers letters; `academic-research-skills`
  `/ars-full` covers journal submission packages), AI-use disclosure (`/ars-disclosure`), and a
  simulated review (`/ars-reviewer`).

---

## Variant: term paper, review or thesis chapter (Beins & Beins, ch. 9, pp. 107–120)

A term paper builds an argument from published work. The steps (Table 9.1, pp. 108–109):

1. Read the assignment closely; ask the instructor early.
2. Brainstorm and freewrite; use broad outlines and idea maps.
3. Pre-research: skim scholarly and popular sources for ideas.
4. Read widely on the general topic; narrow; ask why academics would care.
5. Narrow the research questions to what the paper can cover; form a thesis from the research.
6. Find scholarly support; mine reference lists; take notes that record every source.
7. Outline at paper, section and paragraph level; draft.
8. Check that every claim has scholarly support; research more where it does not.
9. Revise against the assignment, the thesis, the audience, the evidence and the transitions.
10. Check that every cited source has a full reference.
11. Proofread aloud.

**Ways to frame the topic (pp. 109–113, Table 9.2):** fill a gap; build on a particular study;
explore competing theories; review published work. Each suggests the questions the paper asks.

**Organise around the central questions (pp. 112–114):** index cards by theme, outlines at
several levels, and the five-question paragraph test in `12`.

**Argue and answer objections (pp. 114–120):** see `12` (argument, counterarguments, Table 9.4).

For a Vietnamese thesis in Vietnamese, follow the institution’s format and the formal register
the user’s notes require; this skill covers English APA-style writing.

---

## Final checklist

1. Spine agreed with the user.
2. All sections drafted; placeholders listed, none hidden.
3. Hourglass check passed.
4. `annwuyn` language pass done.
5. `02` format and `03` error audit done; venue rules applied.
6. References verified against sources.
7. Deliverables produced and named for the venue.

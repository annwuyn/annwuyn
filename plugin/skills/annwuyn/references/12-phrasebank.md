# 12 — The phrase layer: Morley's *Academic Phrasebank*

Source: John Morley, *Academic Phrasebank*, 2015 enhanced edition (PDF), © The University of
Manchester. **Referenced, not reproduced.** This file is an index and a method. The frames are
read at runtime from the user's own copy through `scripts/phrasebank.py`. Page numbers (`tr.`)
are the **printed** page numbers of that edition, meaning the `N | Page` footer. The PDF page
index is one higher.

This file is not part of the source curriculum. It was added to give the pipeline a
realisation layer, and it has to obey the curriculum's rules, not override them.

---

## What the Phrasebank is for, and what it is not

The Phrasebank follows Swales's *move* analysis. Each heading names a communicative function
and lists generic wordings that realise it. The phrases carry no ideas of their own, so it is a
**wording resource for a move that has already been decided**.

It cannot decide that move. A draft that is non-linear stays non-linear when every sentence is
upholstered with phrasebank frames, and it now also sounds authoritative, which is worse.
Stages 1–2 (linearity, TP) always come first.

**Move → function → frame → fit → trim.**

| Step | Question | Where |
|---|---|---|
| **Move** | What is this idea unit *doing* in the chain: establishing, gapping, reporting, conceding, explaining, limiting? | the idea chain from `01` |
| **Function** | Which Phrasebank heading realises that move? | the map below |
| **Frame** | Which 2–3 candidates on those pages fit? | `phrasebank.py show <tr.>` / `search` |
| **Fit** | Does the frame preserve TP, Engagement, modality and the writer's claim strength? | `02`, `06`, `07` |
| **Trim** | What did the frame cost in words? | `08`; report the count |

---

## Modes

| Mode | Trigger | Behaviour |
|---|---|---|
| **Guided** (default) | any academic drafting or revision | Frames go only where a move is missing, weak or mis-signalled. Everything else stays in the writer's words. Frames are not logged unless asked. |
| **Strict** | *"chỉ dùng cấu trúc/từ vựng trong Phrasebank"*, a course rule, a teacher's constraint | Every sentence rests on a traceable licence: a frame (with tr.) or a grammar/style note (with tr.). Content goes in the slots only. Deliverables below. |
| **Audit** | *"câu này có trong Phrasebank không?"*, checking a revision or a student's claim | Run `phrasebank.py audit FILE`. Report frame / fragment / none per sentence, then judge the flagged ones by hand. Do not rewrite unless asked. |
| **Teach** | *"cho em các cách viết phần gap"*, learning a move | Name the move, show the section (`show`), sort its frames by Engagement and strength, and have the writer choose. |

---

## What counts as "from the Phrasebank" (strict-mode rules)

1. **Frame vs slot.** The frame is the scaffolding: reporting verbs, evaluative adjectives,
   connectors, the syntactic shape. The slot is the X/Y content: topic nouns, names, numbers,
   citations, domain verbs. Morley's own note says the content words in his examples are
   placeholders meant to be substituted (tr. 4–5). Domain vocabulary is therefore never a
   violation.
2. **Legitimate adaptation.** You may:
   - change tense, number, voice or person;
   - swap one word for another from the same substitution table;
   - replace an example's time span or quantity (*decade* → *few years*);
   - join a time-frame frame to a trend frame;
   - drop an optional element shown in brackets.

   You may **not** invent a scaffold that has no source.
3. **The notes are licences too.** A plain S → V sentence, a subordinator, a colon or semicolon,
   nominalisation, or an academic-word swap is licensed by the note on sentence structure
   (tr. 102–103), punctuation (tr. 99), articles (tr. 100–101) or academic style (tr. 93–95). A
   strict-mode sentence without a named frame must cite one of these. A sentence you cannot
   license is a sentence to rebuild.
4. **The acceptability ceiling.** Morley summarises Davis & Morley (2015) on reused phrases
   (tr. 4). A reused phrase should be generic, should not carry another writer's point of view,
   should run to about nine words at most, and should hold no more than four generic content
   words. Past that it is someone's sentence, not a phrase. In practice: one frame per clause,
   and the frame never swallows the writer's claim.
5. **Frames carry propositions. Check them.** Many frames quietly assert something about the
   world or the literature:
   - that interest or concern is *increasing*;
   - that a *growing body* of work exists, or that work is *numerous* or *scant*;
   - that something is *well established*;
   - that something is happening *for the first time*;
   - that a factor is *the leading* or *the main* one.

   Use such a frame only if the writer's sources support that exact proposition. Otherwise pick
   a neutral frame from the same section. A frame is never a licence to add a claim.

---

## Function map

`annwuyn` column: the stage whose rules govern how the frame is chosen and fitted.

### Introducing work (tr. 7–21)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| Importance of the topic: world/society · discipline · time frame | 7 · 8 · 8 | Establish territory | 06, 11 | These are monogloss claims. Pair them with a **specific source** (VN-transfer items 10, 12). Grand openings without a citation read as common wisdom. |
| Highlighting a problem | 9 | Problem statement | 07, paper | Scope the problem (where, for whom, since when). The *However,* + problem table suits a turn after territory. |
| Synopsis of literature | 10 | Summarise prior work | 06 | Choose the reporting verb deliberately (see *Referring to literature*). |
| Highlighting a controversy | 11 | Open the argument space | 06 | Heterogloss by nature. It helps the hetero:mono target. |
| Paucity of research | 11–13 | Gap by absence | paper, 07 | `annwuyn-paper` warns that "little has been done" reads as unfamiliarity. Use it only with a search basis, and scope it (to date, in this context, this pairing). Prefer the specific-gap sections. |
| Inadequacies of previous studies · negative outcomes | 13–15 · 15 | Gap by weakness | 09 | Name the weakness concretely. A bare *have suffered from X* is Pronounce. |
| Knowledge gap | 16–17 | Gap by uncertainty | 07 | The cleanest gap move. The *What remains unclear is…* family keeps the writer out of Theme. |
| Focus / aim / argument of a short paper | 17–18 | Thesis | 06 | *argue / attempt to show / contest the claim* are different stances. Match the essay's real ambition. |
| Purpose · research questions · synopsis of method | 18–19 · 19 · 19–20 | Occupy the niche | paper | In a proposal, future tense (`annwuyn-paper`). RQs must stay specific and operationalizable; the frame does not do that for you. |
| Significance · limitations · personal interest | 20 · 20 · 20 | Value, scope | paper, 11 | *Personal interest* is a dissertation move. In an SOP, VN-transfer item 19 (orientation to field as active process) governs instead. |
| Outlining the structure · explaining keywords | 21 · 21 | Road map, definitions | 08 | A short paper needs one sentence of road map at most. |

### Referring to literature (tr. 22–31)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| General descriptions · current state of knowledge | 22–23 · 23 | Frame the field | 06 | "Current state" sentences are bare facts plus citation. Fine only for uncontested findings. |
| General reference, several authors · negative outcomes · topic prominent | 23–24 · 25 · 25 | Group studies | 02, paper | **The fix for the literature review's N-chain.** Group by finding, not one study per sentence. |
| Single investigations: researcher / time / investigation / topic prominent | 26 · 26 · 27 · 27 | Report one study | 02 | Pick by what the **Theme** should be. Researcher-prominent puts the author in Theme; topic-prominent keeps topic continuity (RT). Choose the one that continues the TP. |
| What others do in their text · another writer's ideas | 28 · 28–29 | Attribute a position | 06 | Reporting verbs *are* Engagement. *show / demonstrate / establish / point out* = **Endorse** (you accept it). *argue / claim / suggest / maintain* = **Attribute** (you distance). Never endorse an inference you go on to reject (`06`, *Verb choice carries Engagement*). |
| Synthesising: supporting · contrasting · *however* for emphasis | 29 · 29–30 · 30 | Synthesis | 03 | Similarity and contrast signposts must name the relation that holds (`03`: CONTRAST vs EXCLUSION). |
| Introducing quotations | 30 | Quote | 08 | Quote only when the wording itself matters. Otherwise paraphrase. |
| Summarising the review | 30–31 | Close the review | 07 | *indicate / suggest / highlight / provide evidence* differ in force. Match it to the pooled evidence. |

### Describing methods (tr. 32–37)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| Previously used methods · reasons adopted · reasons rejected | 32 · 32–33 · 33 | Justify the design | paper | Rationale is required (`annwuyn-paper`, *Methodology*). |
| Specific method · sample · selection criteria | 33 · 33 · 34 | Operationalise | paper | Representativeness. Convenience samples need a stated rationale. |
| Process: passive verbs · infinitive of purpose · other purpose · adverbs of manner · *using* + instrument · sequence | 34 · 35 · 35 · 35 · 35 · 36 | Procedure | 03, 04 | **SEQUENCE vs CAUSE/EFFECT**: check every *then*, *once*, *following*. Purpose infinitives are downgrading; keep them out of Theme unless they are the point. |
| Statistical procedures · problems/limitations | 37 · 37 | Analysis, caveats | 07 | *significant* means statistical significance here, nothing else. |

### Reporting results (tr. 38–42)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| Reference to aim/method · location and summary statements · highlighting data | 38 · 38–39 · 39 | Point to evidence | 02 | The location statement is Theme material. The highlighting statement carries the New. |
| Positive · negative · surprising results · reactions | 39 · 40 · 40 · 40 | State results | 07 | Qualification is load-bearing. Evaluative adjectives (*remarkable, disappointing*) are Attitude, so use them sparingly. |
| Questionnaires and interviews · qualitative observations | 41–42 · 42 | Report respondents | 07, 10 | Quantifier frames (*just over half*) must match the actual numbers. |
| Transitions · summary and transition | 42 · 42 | Link sections | 03 | Watch for over-linking. |

### Discussing findings (tr. 43–48)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| Background · statements of result · unexpected outcome | 43 · 43–44 · 44 | Restate and evaluate | 02 | Return to the RQ with ERT to it (`02`). |
| Previous research: support · contradict | 44 · 45 | Position against literature | 06 | *corroborate / confirm* endorse; *consistent with* is weaker. Choose by the size of your evidence. |
| Explanations · cautious interpretation · general hypotheses | 45 · 46 · 46 | Explain, hedge | 07, 09 | **Postulation ↑.** Do not stack hedges (*it is possible that … may … might*), because over-qualification is also an error (`07`). Correlational data: the Correlation fallacy (`09`). |
| Commenting · implications · future work | 47 · 47–48 · 48 | Evaluate, extend | 06 | Pre-counterargument concession before limitations (`06`). |

### Writing conclusions (tr. 49–56)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| Restatement of aims · summarising findings · implications for the field | 49–50 · 50 · 50 | Look back | 01 | Conclusions still obey linearity. No new ideas, no repetition of the introduction's wording. |
| Significance / contribution · with a qualification | 51–52 · 52 | Claim value | 06, 07 | *first study to* is a factual claim. Only with a search basis. |
| Limitations · strengths | 52–53 · 54 | Scope | paper | Limitations vs delimitations (`annwuyn-paper`). |
| Further research · practice or policy | 54–56 · 56 | Look forward | 07 | *should* in recommendations: check force (`07`; VN-transfer item 14). |

### General functions (tr. 58–91)

| Section | tr. | Move | annwuyn | Caution |
|---|---|---|---|---|
| **Being critical**: inadequacies · theory · method · a study · constructive suggestions · evaluative adjectives · others' criticism · critical stance of writers · critical section | 58 · 58–59 · 59–60 · 60–62 · 62–63 · 63 · 63 · 63 · 64 | Rebuttal, critique | 09, 06 | Critique needs a warrant. The *would have been more … if …* frames (tr. 62–63) suit peer-review mode (`annwuyn-review`). Keep Pronounce down. |
| **Being cautious**: distancing · explanations · results · implications · over-generalisation · the future · cautious interpretation | 65 · 65–66 · 66 · 67 · 67 · 68 · 68 | Hedge, qualify | 07, 06 | Entertain and Attribute resources. **Not for SOP/LOR assertions** (VN-transfer items 15, 21). |
| Classifying and listing | 69–71 | Organise sets | 01 | Re-order every list (`01`). The announced number must match the items. |
| Comparing and contrasting | 72–74 | Compare | 03, 04 | *in contrast* ≠ *on the contrary* (`03`). *whereas / while* subordination is a dependency choice (`04`). |
| Defining terms | 75–77 | Define | paper | No unquantified term left undefined (`annwuyn-paper`). |
| Trends and projections · quantities | 78 · 79–80 | Describe data | 07, 10 | Approximators are qualification. They agree with `10`'s *about → approximately*. |
| **Explaining causality**: verbs, nouns, prepositions, connectors, adverbials · contributing agency · tentative cause | 81–82 · 82–83 · 83–84 | Cause and effect | 03, 09 | PARAPHRASE vs CAUSE/EFFECT; sufficiency vs necessity. *leads to / causes* need a causal design; otherwise use the tentative frames (tr. 83–84). |
| Giving examples | 85–86 | Exemplify | 09 | Few elaborated examples beat many bare ones (`09`). |
| Signalling transition | 87–89 | Signpost | 02, 03 | Section transitions are metadiscourse, so they cost words (`08`). Reintroducing a topic is ERT made explicit. |
| Writing about the past | 90–91 | Tense | 04 | Past simple for single studies, present perfect for the field (tr. 90–91). |

### Notes on academic writing (tr. 93–106)

| Note | tr. | Use in annwuyn |
|---|---|---|
| Academic style (evidence, classical vocabulary, caution, impersonality, nominalisation, no rhetorical questions, no contractions, precision) | 93–95 | Agrees with `10` on vocabulary. **Two conflicts:** (1) impersonality vs the scholarship genre, where SOP/PS need *I*, so genre wins; (2) Morley discourages rhetorical questions, while `06` target 5 wants well-placed ones in argumentative essays, so genre wins. For a research paper, follow Morley. |
| Commonly confused words · BR/US spelling | 96–97 · 98 | TMRND **D**ialect. Keep one dialect throughout; for a British venue, British spelling. |
| Punctuation · articles | 99 · 100–101 | Dash → colon, semicolon or brackets in formal prose (tr. 99). Article rules back up `02`'s reference-accessibility notes. |
| Sentence structure · paragraph structure | 102–103 · 104 | Licences for strict mode. The paragraph note (topic sentence → support, thematic linking) is `02`'s *Topic sentences and TP*. |

---

## Choosing between candidate frames

Once `show` has put the section on screen, choose in this order:

1. **Theme fit.** Where does the frame put the Given information? Take the frame whose Theme
   slot receives what the previous sentence ended on (RT). One that forces a new Theme
   creates a TP break.
2. **Engagement fit.** Endorse, attribute, entertain, disclaim or pronounce: which does the
   writer actually mean? Among Vietnamese writers, the usual error is endorsing where they
   should attribute, and pronouncing where they should postulate.
3. **Force fit.** The frame's modality must equal the evidence. Never upgrade the writer's
   *may* to a *has been shown* frame, and never downgrade a demonstrated result to *it is
   possible that*.
4. **Economy.** Where two frames are synonymous, take the shorter one. This is Wallwork's rule
   and it is already in `10`.
5. **Variety.** Do not reuse a frame within about three paragraphs, and do not open
   consecutive sentences with frames from the same section. Frame-stacking is the template
   problem in `09` in a new form.
6. **Genre.** Research paper: frames are welcome. Coursework essay: moderate. SOP, PS or LOR:
   sparing, and never the cautious family for achievements.

---

## Strict-mode deliverables

1. **The revised text** in the input's format. For a `.docx`, preserve the formatting and
   replace text run by run.
2. **A frame log**: `# · original · revised · licence (frame quoted from the user's copy + tr.,
   or grammar/style note + tr.)`. Every row has a page. No page means no licence.
3. **An audit**: `phrasebank.py audit revised.docx`. Every `none` row must already carry a
   note-licence in the log. Every `fragment` row gets a second look.
4. **The costs, stated plainly**:
   - the word count before and after (frames typically add 15–25 %, so offer an `08` pass if
     there is a limit);
   - every sentence where a frame shifted nuance or scope;
   - any frame proposition (rule 5) that you rejected.

## Guided-mode behaviour

Do not announce the Phrasebank. In an `annwuyn-review` pass, a frame appears as the **fix** for
a named defect. Examples: *weak gap move → knowledge-gap frame (tr. 16)*; *endorsing verb for a
contested claim → attributing frame (tr. 28)*; *N-chain in the literature review →
several-authors frame (tr. 23–24)*. In the *What changed and why* list, cite the section and
page so the writer can go back to the source.

## When the PDF is not available

Run `phrasebank.py status`.

- **If it is not registered**, run `phrasebank.py setup` with the path. Setup also finds a copy
  sitting in `~/Downloads`, `~/Documents` or `~/Desktop`. Otherwise ask the user for the file.
- **In a cloud session**, the user must attach the PDF. Run `setup` on the uploaded path.
- **Without a copy**, the modes change:
  - Guided mode may continue using this map and general academic English.
  - Do not cite page numbers.
  - Do not describe any wording as "from the Phrasebank".
  - Strict and audit modes are unavailable.
- **Never fabricate** a page number or a frame.
- **If `setup` reports a different edition**, the page numbers here are off. Locate sections
  with `search` and cite section names.

## Script reference

```
python3 <skill-dir>/scripts/phrasebank.py setup [PDF]     # once; cache at ~/.annwuyn/phrasebank/
python3 <skill-dir>/scripts/phrasebank.py show 16-17      # a section's pages
python3 <skill-dir>/scripts/phrasebank.py search "remains (unclear|unknown)" --context 2
python3 <skill-dir>/scripts/phrasebank.py audit draft.docx [--json]
```

`<skill-dir>` is the `annwuyn` skill's base directory.

`audit` matches runs of three or more words and sentence openers against the phrase pages
(tr. 7–91). It splits at X/Y placeholders and table columns. The labels mean:

- **frame**: a run of 4+ words, or an opener;
- **fragment**: only 3-word runs, which are often generic English;
- **none**: no match.

The audit finds traceable wording. It does not judge whether the move is right. That is the
analyst's job.

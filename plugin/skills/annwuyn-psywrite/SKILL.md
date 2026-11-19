---
name: annwuyn-psywrite
description: Write, revise or check an APA-style empirical paper in psychology and the social sciences, with most depth on the Introduction — many ways to open, Swales’s moves, problem/gap/hook, how to end — plus the abstract, APA 7 manuscript format, a common-error audit, conference posters, oral presentations and ethics (IRB) proposals. Built on Beins & Beins, *Effective Writing in Psychology* (3rd ed., 2021) and a reading list of genre research and writing guides. Use when the user drafts or reviews an Introduction, abstract, poster, talk or ethics application, or asks for an APA format check. Also triggers on Vietnamese requests such as "viết phần mở đầu", "viết introduction", "cách mở bài báo", "định dạng APA", "làm poster hội nghị", "thuyết trình nghiên cứu", "hồ sơ xin phê duyệt đạo đức".
---

# annwuyn — psychology papers, posters and talks

Load the `annwuyn` skill first. Its language pipeline (linearity → TP → cohesion → engagement →
economy) applies to every paragraph this skill produces, and its Phrasebank layer
(`scripts/phrasebank.py`) supplies wording once a move is chosen. This skill decides the
**structure and the moves**. `annwuyn-paper` covers research questions, methods and proposals.

## Route by task

| Task | Read |
|---|---|
| Draft, diagnose or rewrite an Introduction | `references/01-introduction.md` |
| Abstract, title page, headings, section order, APA mechanics | `references/02-abstract-apa-format.md` |
| Audit a finished manuscript before submission | `references/03-common-errors.md` |
| Conference poster | `references/04-posters.md` |
| Conference talk, thesis defence, class presentation | `references/05-oral-presentations.md` |
| Ethics committee / IRB application, consent form | `references/06-ethics-proposal.md` |
| Where a claim comes from, further reading | `references/SOURCES.md` |

## Working rules

1. **Ask for the reader before writing.** Target journal or venue, field breadth, and whether
   the piece is a student paper or a submission. Opening breadth and format both depend on it.
2. **Plan moves before sentences.** For an Introduction, write the move map (territory → gap →
   hook → present study → hypotheses) as one line per move, show it, then draft.
3. **Offer two or three openings.** Pick from the opening repertoire in `01`, label each by type,
   and say what each one costs. The writer chooses.
4. **Run the error audit last.** `03` is a pass over a full draft. Report findings as a numbered
   list with the line, the rule and the fix.
5. **Cite the source of a rule.** Book rules carry a page number (“Beins & Beins, p. 268”).
   APA 7 rules cite the *Publication Manual* section. Say so when the two differ.
6. **Paraphrase sources.** The references summarise the book in our own words. Quote nothing
   longer than a short phrase.

## Coverage note

The photographed copy of Beins & Beins covers pp. 196–300: the abstract and format chapter,
Part III (posters, talks, web, ethics), Appendices A–B and the reference list. The book’s
earlier chapters, its own Introduction chapter included, are not yet in this library. `01`
is built from the genre research and writing guides in `SOURCES.md` and from the annotated
sample manuscript in Appendices A–B. Add the missing chapters to `SOURCES.md` when they are
photographed.

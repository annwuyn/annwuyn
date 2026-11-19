---
name: annwuyn-psywrite
description: Write a complete APA-style manuscript in psychology or the social sciences from inputs to a submission-ready file, or draft, revise or check any part of one — Introduction (many ways to open, Swales’s moves, problem/gap/hook, hypotheses from an idea chain), Method, Results and statistics, Discussion, citations and references, abstract and APA 7 format, a common-error audit — plus term papers and reviews, conference posters, oral presentations and ethics (IRB) proposals. Built on Beins & Beins, *Effective Writing in Psychology* (3rd ed., 2021, all chapters) and a reading list of genre research and writing guides. Use when the user writes or reviews any part of an empirical paper, thesis chapter, term paper, poster, talk or ethics application, or asks for an APA format check. Also triggers on Vietnamese requests such as "viết bài báo hoàn chỉnh", "viết bản thảo", "viết phần mở đầu", "viết introduction", "phần phương pháp", "trình bày kết quả", "phần bàn luận", "trích dẫn APA", "định dạng APA", "làm poster hội nghị", "thuyết trình nghiên cứu", "hồ sơ xin phê duyệt đạo đức".
---

# annwuyn — psychology papers, posters and talks

Load the `annwuyn` skill first. Its language pipeline (linearity → TP → cohesion → engagement →
economy) applies to every paragraph this skill produces, and its Phrasebank layer
(`scripts/phrasebank.py`) supplies wording once a move is chosen. This skill decides the
**structure, the moves and the APA rules**. `annwuyn-paper` covers research questions and
proposals; `academic-research-skills` covers literature search, citation checks and simulated
review.

## Route by task

| Task | Read |
|---|---|
| **Write a whole manuscript, or a term paper, review or thesis chapter** | `references/00-full-manuscript.md` first, then the section files it names |
| Introduction: openings, moves, literature, hypotheses | `references/01-introduction.md` |
| Method | `references/07-method.md` |
| Results, statistics, tables and figures | `references/08-results.md` |
| Discussion | `references/09-discussion.md` |
| In-text citations and the reference list | `references/10-references-citations.md` |
| Abstract, title page, headings, section order, APA mechanics | `references/02-abstract-apa-format.md` |
| Audit a finished manuscript | `references/03-common-errors.md` |
| Topic, sources, literature search, reading articles, plagiarism | `references/11-ideas-sources-reading.md` |
| Organising, argument, revising, style, bias-free language | `references/12-organizing-style.md` |
| Conference poster | `references/04-posters.md` |
| Talk, defence, class presentation | `references/05-oral-presentations.md` |
| Ethics committee / IRB application, consent form | `references/06-ethics-proposal.md` |
| Where a rule comes from, further reading | `references/SOURCES.md` |

## Working rules

1. **Brief first.** Venue and its guidelines, readers, paper type, student or professional
   format. Venue rules override the book where they differ.
2. **Spine before prose.** Agree the question, hypotheses with their idea chains, and the move map
   with the user before drafting (`00`, Stage 1).
3. **Offer two or three Introduction openings**, labelled by type, with what each costs.
4. **Never invent** data, statistics, participants, quotations or sources. Use visible
   placeholders and list them.
5. **Audit last** with `03`; report findings as line → rule → fix.
6. **Cite the source of a rule.** Book rules carry a page number (“Beins & Beins, p. 268”);
   APA 7 rules cite the *Publication Manual*. Say so when the two differ.
7. **Paraphrase sources.** The references summarise the book in our own words. Quote nothing
   longer than a short phrase.

## Coverage

All of Beins & Beins is summarised (154 photographs, pp. 1–296). The user’s own copy is kept as a
searchable scan in Drive: `07 Thư viện/Effective Writing in Psychology (Beins 2021)/`.

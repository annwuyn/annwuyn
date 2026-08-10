# 2 — Theme / Rheme and Thematic Progression (TP)

Source: sessions S5–S9. A departure from Halliday's original model, adapted into a **tool for
monitoring and improving linearity**. Linearity is necessary but not sufficient: a text can be
linear and still not thematically progressive.

## Theme

**Theme = the point of departure of the message.** Rheme = everything else.

Three types:

| Type | Count | Optional? | Markedness |
|---|---|---|---|
| **topical** | exactly one per clause | compulsory | marked or unmarked |
| **textual** | any number | optional | always marked, precedes topical |
| **interpersonal** | any number | optional | always marked, precedes topical |

The **topical Theme is a component of the main experiential process**: the process itself, a
participant in it, or a circumstantial factor (time, location, manner, cause).
Interpersonal and textual Themes play no part inside that process.

> *They find our case inconclusive. **Inevitably**[interpersonal], **as a result**[textual],
> **it**[topical] will need reviewing.*

Unmarked = SVO order. Anything fronted is marked.
*I read a book for two hours in the library* (unmarked) vs *In the library I read a book…*,
*For two hours I read a book…*, *A book was read by me…* (all marked).

Test for interpersonal vs. inside-the-process: *Sadly, I read a book* (interpersonal) ≠
*I sadly read a book* (manner, inside the process) ≠ *I read a sad book* (attribute).

Special cases: dummy `it` (*It is desirable that…*), projecting clauses (*I would say we…*),
and *The reason is…* constructions all need care.
`it` as referent / dummy subject / weather-`it` are all normally **RT**, not New Theme.

## TP transition patterns

Identify in this **order of priority**: `RT → TT → ERT → ETT → N`

| Code | Pattern | Shape |
|---|---|---|
| **RT** | Rheme-Theme | R of S(n) becomes T of S(n+1) |
| **TT** | Theme-Theme | T of S(n) repeats as T of S(n+1) |
| **ERT** | Extended-Rheme-Theme | T picks up the R of an *earlier* sentence, not the immediately preceding one |
| **ETT** | Extended-Theme-Theme | T picks up the T of an *earlier* sentence |
| **N** | Motivated-New-Theme | new Theme, but recoverable/motivated by the discourse |
| **U** | Unmotivated-New-Theme | failure state — nothing connects |

- Theme-Rheme-Theme = **RT**.
- Rheme-Rheme and Theme-Rheme are **not** TP patterns; they signal a *linearity* problem.
  Fix the chain, not the labels.

## TP repetition types

| Code | Type | Realised by |
|---|---|---|
| **L** | Lexical | the same word/phrase repeated |
| **R** | Referential | pronoun, demonstrative, or synonym referring back |
| **T** | Textual | a textual Theme (linking item) carries the connection |

**Textual applies only to RT and ERT.**
Marking a transition both lexically/referentially **and** textually is **over-linking** — a
redundant double connection. Cut one.

## Annotation convention (use this in analyses)

Number units per paragraph, then annotate each transition on the unit it lands on:

```
[P1] Last week Virginia Military Institute … (S1).
     But it is likely that the government will appeal the decision (S2: RT, T).
     Meanwhile, the Citadel … remains under attack (S3: RT, T).
     Unwittingly, so are some fundamental beliefs … (S4: RT, R).
[P4] … Clearly, the Citadel is not the bastion of male privilege … (S7: ETT, L, to S3).
```

Extended patterns carry `to Sn`. Where the referent is genuinely ambiguous, flag it inline
rather than guessing: `we at the Citadel [=the Citadel in S1?] are trying to…`.
A sentence may split into several units: `S2a`, `S2b`, `S2c`. A quotation may split too.

Summary table at the end: counts and % for RT / TT / ERT / ETT / N.

## The four common TP problems

### 1. Unwarranted marked Theme
Vietnamese writers use marked Themes to a significantly greater extent than American writers.
Most of those uses disrupt TP continuity for no gain.

But marked Themes should be **used deliberately** to *maintain* continuity:
> *But no obstacle should stand in the way of responsible investigation of their possibilities.
> **To that end**, their project should be funded…*
> (better than: *Their project should be funded … to that end.*)

### 2. Theme shift
The next Theme jumps to a participant that was not in the previous Rheme.
> *…you can see a lot of birds around the campus, and **students** often feed them.*
> → *…a lot of birds around the campus, **who** are often fed by students.*

Repair options, in descending transparency:
1. **purpose-marked bridge** — *To take advantage of this ability, adults should…*
2. **plain marked bridge** — *Given this ability, adults should…*
3. **textual only** — *Therefore, adults should…*

Others: relativisation; voice change (*it was supported by only a few*); better still, a
lexical fix with **no** voice shift (*it gained few supporters but many more opponents*);
perspective shift (*This victory **by Vietnamese people**…*).

### 3. Rheme-Rheme redundancy
`(T1 → R1) + (T2 → R1)` — two sentences landing on the same Rheme.
Solution: `(T1 → R1 = R1 → T2)`, usually via a relative clause.
> *Matt claimed that he was ripped off … during his short stay in Vietnam. That makes me wonder
> why could all those things happen continuously to him in such a short time.*
> → *…during his short stay in Vietnam, **which makes me wonder why**.*

Rheme-Rheme is a common *form* of Theme shift. It also hides repetition: consolidate first.

### 4. Referent shift
`children → he → they → we` drifting mid-paragraph; `one of the reasons why…` restating.
> *Spending a majority of their time with friends is one of reasons why friends have most
> influence on young adults. A young adult use most of his time at school, where he joins his
> friends…*
> → *A reason why friends have the most influence on a young adult is that **he** spends most of
> his time in school, where **he** joins his friends in many activities. Through such activities,
> **they** connect and learn from each other.*

## RT bridges

Inserted material whose only job is to make the next Theme recoverable. Learn the shapes:

- *Since this is a multi-faceted process,* …
- *This brings up the central question:* …
- *To address this concern,* …
- *In addition to dictionaries,* …
- *To this cause,* … / *Among those,* …
- *To that end,* … / *Toward this end,* …

## Reference accessibility

`the` < `this/that` < `it` — increasing accessibility.
Article and pronoun choice follows accessibility in the discourse, **not** translation from
Vietnamese. *Trong sân có một con mèo* → *There is a cat in the yard. **It** chases a mouse.*
(not *In the yard there is a cat. A mouse is chased by the cat.*)

Where a referent is implicit and of low accessibility, `the` is right: *…bring a brighter
future for **the** country.*

## Topic sentences and TP

A topic sentence whose Rheme does not feed the next Theme forces a break. Rewrite the topic
sentence so its Rheme *is* the next Theme:
> *Economic benefit is the first reason that makes me vote for an agriculture research center.
> Currently, farmers in my country mainly use out-of-date farming methods…*
> → *The first reason … is **economic benefits**. One of such **benefits** is that it would help
> with a problem farmers in my country are facing…*

## Noun-phrase branching

Linking to an NP Theme normally goes through the **head noun**.
*We now talk about the school's graduation rate.* → next Theme = *the school* (RT) or
*its graduation rate* (ERT), depending on which you foreground. Branch deliberately.

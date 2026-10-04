# Case Studies: How to Write and Review One

Working notes for writing case study pages on the Evidentiality Framework site. (d)Template and guard rails agreed by Jesse, 2026-10-03, after a seven-reviewer pass on the West Midlands Police draft.(/d) Sample page: `case-west-midlands-police.html`.

## Scope

- (d)Only incidents where AI-written text was relied on as if it were given or checked. Not deepfakes, cars, surveillance or deliberate misuse.(/d)
- (d)Only incidents with national or international news coverage. Fewer than 10 cases on the site at a time.(/d)
- (d)The AI Incident Database is a reference, not the authority. Link it in one small line at the end of a page, and only where it lists the case.(/d)

## Page Template (in This Order)

1. **Title:** organisation first, then what went wrong, in title case. Example: "West Midlands Police: An AI-Invented Match Behind a Fan Ban".
2. **Lede:** two or three plain sentences.
3. **"What are the labels?" box:** two lines and a link to the labels page.
4. **What Happened:** dated bullets. Explain institutions in plain words, for example "MPs, the members of Parliament".
5. **Follow the Claim:** the two-column visual: "As it happened" and "With labels".
   - The "illustration, not a test" note sits **above** the visual.
   - Use 3 to 5 rows, in this order: AI output (g) → passed on (u…/u: who, unconfirmed) → **the check**, placed **before** the decision it would stop, with (m) naming the source and a note that the source confirmed it later → the decision or publication, where the labelled column says the claim is left out (finished documents carry no labels).
6. **How the Labels Could Have Helped:** three points at most.
7. **What Would Have Had to Be True:** link to the four shared conditions on the hub (tool used labels; AI labelled its own work correctly; label stayed on; someone owned the rule), then one or two case-specific lines, always naming **who owns the rule** in that field.
8. **What Already Existed:** the controls that field already has, named as a professional in that field would name them (e.g. Rule 11 and citators in US law; 3×5×2 grading in UK policing), whether the claim went around them, and **the simpler check that would have caught it**, plus what labels add beyond it.
9. **What the Labels Wouldn't Have Caught:** list the non-AI causes from the official findings.
10. **Further Reading:** primary sources first (official reports, court records, regulator statements), then news.
11. **Database line:** "Also listed in the AI Incident Database (#N)", only if it is listed there.

Target length: about 3 to 4 minutes of reading. Aim for something a 12-year-old can follow.

## Guard Rails for Writing

**Facts**

- Every factual line traces to a linked source.
- Dates and findings come from primary sources where they exist. News is for context.
- Open every link before publishing. If a site refuses access, don't work around it; use another source.
- Fast-moving facts, such as open investigations and appeals, are rechecked at publish time. Record the check date in the commit message.

**Quotes**

- Use the published wording of the AI output if it exists, for example in an inspector's letter or a court filing.
- If no wording was published, say "paraphrased".
- Keep quotes short and attributed.

**Fairness**

- Name roles, not people, in the page text.
- Include official findings that cut the other way, such as "did not intentionally mislead".
- State that an investigation or notice is not a finding of wrongdoing.
- Mention apologies and corrections.

**The counterfactual**

- It is always an illustration, never a test.
- No hindsight phrasing such as "one search would have ended it".
- Say who would have had to apply the labels and who owns any "wait for a check" rule. In a human meeting that is a rule, not software.

**Labels in the visual must follow the label rules**

- The AI's own output is (g).
- Once someone passes it on, it becomes (u)…(/u: who, unconfirmed).
- (m) only with a named source we have actually read, closed as (/m: source, checked DATE). If the source came after the event, say so in the note.
- The key uses the site's words: (g) generated, (u) given, (m) checked.
- Rows run in time order. No check appears after the decision it would have stopped.
- Every label in the key is used in the visual, or left out of the key.

**Selection:** the hub says the cases were chosen because they fit and are not a random sample. Fit badges are Yes, Likely (AI use suspected, not confirmed) or Partial.

**Hedging AI use:** if AI use is suspected but not confirmed, say so in the lede, the row heading ("AI tool (suspected)") and the card.

**Balance:** the non-AI causes go in the limits section. The page must not read as "the AI did it" or "this person did it".

## Guard Rails for Review (Before Publishing)

Run seven reviewers, using mixed models:

| Reviewer | Gets | Checks |
|---|---|---|
| Cold reader | The case page only | Comprehension check first (what do (g) and (m) mean, and what would labels have changed?), then where they got lost |
| Site reader | Home, The Labels, then the case page | Consistency with the label rules and the visual conventions, and links to the rest of the site |
| Fact-checker | The page plus every link, with web access | Each claim marked supported, unsupported, contradicted or overstated; fairness and legal risk; better primary sources |
| AI incident researcher | The page | Strength of the counterfactual, hindsight bias, missing post-mortem sections |
| LLM / agent engineer | The page plus the builders page | Where labels and gates would actually sit, and where they'd be lost; alternatives |
| Specialist in the incident's own field (e.g. policing records, law, publishing) | The page | Existing controls and prior art; correct use of that field's terms |
| Plain-language editor | Page text and phone screenshots | Jargon, long sentences, reading level |

**Rules for reviewers**

- Reviewers aren't told who wrote the page or what verdict we hope for.
- Comprehension questions come before opinions.
- Each reviewer returns their top 3 problems ranked by consequence, one thing to cut, and whether they would share it.
- Reviewers' reports are tagged (u)/(m)/(g).

**Rules for the author**

- Before relying on a reviewer's or research agent's (m) claim, re-check it yourself. Where two reviewers' fetched quotes disagree, drop the quote.
- Close every fact, fairness and legal item before publishing.
- Record disagreements between reviewers rather than averaging them.

## Lessons From the First Review Pass (2026-10-03)

- Get the decision timeline from the primary record. The first West Midlands draft put the AI claim behind the wrong decision.
- Quotes fetched through summarising tools can differ; confirm a quote from two reads or leave it out.
- Don't put a check row after the decision it would stop, and don't write "the same check, made before".
- A case with weak primary sourcing waits (the Australian age-assurance report was held back for this reason).

## Open Item

- (g)Do internal decision documents (an intelligence briefing, a meeting pack) count as working material that keeps its labels, or as finished material that drops them?(/g) The instructions say finished work for an outside reader carries no labels. The case pages assume decision documents keep them. Jesse to decide.

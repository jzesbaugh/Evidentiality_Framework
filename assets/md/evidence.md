> Does labelling AI claims stop hallucinations spreading? Early results: Early results with and without labels: checked facts kept their sources 33 of 36 times with labels and 4 of 36 without. Sample sizes and what did not hold up.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/evidentiality-framework/evidence.html. Text CC BY 4.0.

Evidence and limits · early findings

# Does labelling AI claims stop hallucinations spreading? Early results

**Who this page is for:** anyone deciding how much weight to give this. Every number here is from a small test; treat it as a lead, not a rate.

This page labels its own claims.

(u) given to the AI · (m) measured / checked · (g) generated / guessed by the AI

We label our results (m) because we checked them against our own test logs. To you, they're our report, which makes them (u) until you check. The logs for the six-round test are [published](../../test.html#logs); others are available on request.

## Held up

- (m)With the instructions, labelled items kept their labels through three and four hand-offs in 95% to 100% of cases (120 of 120 items across four steps in one scenario; 61 of 64 across three in another).(/m: hand-off chain test logs, Sept 23)
- (m)With five agents sharing one summary, checked facts kept their sources 33 of 36 times with the labels and 4 of 36 without.(/m: shared-summary test logs, three runs per version, Sept 23)
- (m)When three reports repeated one person’s claim and the source was dropped, the agent combining them called it corroborated 4 of 4 times. When the source was kept, in words or in labels, 0 of 4.(/m: corroboration test logs, Sept 23) (g)Keeping the source is what matters; plain words did about as well as the labels in this test.(/g)
- (m)In one six-round run of the five-agent test, an early maths mistake stayed labelled as a guess with the labels. Without them it was restated as confirmed, credited to the wrong agent and used to justify rationing, and by round six the newsletter described an event that never happened.(/m: six-round run logs, published, Sept 24)

## Didn't hold up, or not shown yet

- (m)On single questions with traps in them (false premises, invented names, buried facts), current models did as well without the instructions as with them: all 120 answers correct across both.(/m: single-question trap test logs, Sept 24) (g)The framework adds visibility across hand-offs, not better single answers.(/g)
- (m)An earlier result that the labels changed which action a chain of agents recommended did not hold up when we ran more samples.(/m: repeat-run logs, Sept 23) (g)The six-round result above is the same kind of claim and has one run behind it.(/g)
- (m)A false claim carrying a fake "checked" label was believed 4 of 4 times, with or without the instructions.(/m: fake-label test logs, Sept 23)
- (m)In one test, a model labelled material it had merely been given as "checked" in all 6 runs.(/m: self-labelling test logs, one model, Sept 24)

## Fair objections

### "The AI grades its own homework."

True. The labels are self-applied, and we haven't measured how often they're right. (g)The next step we’d test is a checker that isn’t the writer: the application, or a second model, applies "checked" only to what it can verify, and never upgrades a label it receives.(/g)

### "It labels guesses; it doesn't reduce them."

True, and that's the aim. The labels give the reader more information, not a verdict.

### "Is it the labels, or just the careful instructions?"

We don't know yet. The instructions include rules like "a guess stays a guess" as well as the labels. Separating the two is the test we most want run.

## Limits of these tests

- Mostly one family of models (Claude). In a small cross-model run (five other models, one run each), all five kept the labels on what they added; three of five also caught a planted contradiction.
- One to five runs per version, scored by hand against answer keys. Most keys were written before the run. The five-agent key was written after that test's first run, where the 18-day mistake first appeared (the coordinator made it again in the six-round run), and before the six-round run shown on the home page.
- The ship story comes from one news report (CNN, four anonymous sources); the Pentagon did not comment.

## Related research

- [The Hallucination Snowball](https://arxiv.org/abs/2608.14588) (Singh and Pawar, 2026): in a simulated four-agent pipeline, planted errors got harder to detect at each hand-off; checks at the hand-offs worked far better than one check at the end.
- [Collective Hallucination in Multi-Agent LLMs](https://arxiv.org/abs/2606.07941) (Jamshidi, 2026): agents reinforce each other's unsupported claims and lose track of uncertainty.
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (Cemri et al., 2025): most failures are coordination problems; this framework addresses only the factual part.
- [Evidentiality](https://en.wikipedia.org/wiki/Evidentiality) in linguistics (Aikhenvald, 2004).

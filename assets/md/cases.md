> Case Studies: When AI-Written Claims Were Treated as Fact: Seven real incidents where AI-written text was passed on as if checked, how inline labels could have helped, and how to scan incident lists yourself.
>
> Evidentiality Framework for AI. Early findings, October 2026. Web version: https://evidentiality-framework.org/cases.html. Text CC BY 4.0.

Case studies

# When AI-Written Claims Were Treated as Fact

Real incidents from national and international news, where something an AI wrote was passed along as if someone had checked it. Each case shows how the labels could have helped, what would have had to be true, and what they wouldn’t have caught.

**What are the labels?** The Evidentiality Framework asks an AI to mark each claim it writes: (g) generated, its own work; (u) given, passed to it by someone else; or (m) checked against a named source. The marks stay on a claim while people work with it. [How the labels work](../../labels.html).

**These are illustrations, not tests.** We picked these seven because they fit and made the news; they are not a random sample. Five involve invented sources or titles, the easiest kind of mistake for labels. The framework is built for one kind of failure, AI-written text that people rely on, and isn’t built for deepfakes, self-driving cars or deliberate misuse.

---

## The Cases

[UK · 2025–26 · Fit: yes**West Midlands Police**Police advice to a safety panel included a football match that never happened.](../../case-west-midlands-police.html)[US · 2025 · Fit: likely**The MAHA Report**A White House health report listed studies that don’t appear to exist. AI use is suspected, not confirmed.](../../case-maha-report.html)[Australia · 2025 · Fit: yes**Deloitte’s Welfare Review**A government review quoted a judge. The judge never wrote those words.](../../case-deloitte-welfare-review.html)[South Africa · 2026 · Fit: yes**South Africa’s Draft AI Policy**The national plan for AI cited research that was never published.](../../case-south-africa-ai-policy.html)[US · 2023 · Fit: yes**Mata v. Avianca**Lawyers filed court cases ChatGPT invented. When asked, ChatGPT said they were real.](../../case-mata-v-avianca.html)[US · 2025 · Fit: yes**The Summer Reading List**Two newspapers printed a reading list. Ten of the fifteen books didn’t exist.](../../case-summer-reading-list.html)[South Korea · 2026 · Fit: partial**Starbucks Korea “Tank Day”**Staff said a slogan came from AI. The main harm was a human choice that labels can’t reach.](../../case-starbucks-korea.html)

---

## Would a Simpler Tool Have Caught It?

Often, yes. A source checker, a legal database or a fixture list would have caught most of these mistakes on its own. Labels add one thing: every claim shows whether anyone checked it, including the ones nobody thought to look up. Each case says which simpler check would have worked.

---

## What Has to Be True in Every Case

1. **The AI tool used the labels,** or the person using it added them by hand. Most tools today don’t.
2. **The AI labelled its own work correctly.** This is the weakest link: in [our tests](../../check.html), AI sometimes mislabels its own work, and a model that invents a source may not know it did.
3. **The label stayed on while people worked with the text.** Pasting into a document, retyping or summarising can drop it.
4. **Someone owned a rule** that unchecked claims don’t go into finished work, and used it. That is a human rule, not software. Each case names who would own it.

Finished documents (a published report, a court filing, a printed page) carry no labels. The labels live in the working drafts; the point is that only checked claims make it into the finished version.

---

## How Often Does This Apply? a First Look

We took two small random samples from the [AI Incident Database](https://incidentdatabase.ai/), a public collection of AI incidents reported in the news. **Treat these numbers as a first look, not a measurement.**

- **All kinds of AI incident:** 2 of 40 fit (incidents 623 and 1299). Most incidents in the sample were deepfakes, surveillance, bias or vehicles. The labels aren’t for those.
- **Incidents involving text written by an AI language model:** from 120 incidents added since early 2023, 25 qualified. 9 fit clearly, about 1 in 3 (incidents 574, 709, 719, 753, 807, 1009, 1184, 1257, 1504). 7 more fit partly (685, 838, 1044, 1205, 1424, 1441, 1672): mostly chatbot answers given straight to a user, and AI agents acting on an unchecked assumption.

**Why it’s only a first look:** one AI did all the scoring, the same assistant that helped build the framework, working from summaries of the database pages. It knew what we hoped to find, the question used the framework’s own words, the samples are small, and they may overlap. A fair test needs a second scorer who doesn’t know the hoped-for answer, and a neutral question. Here’s how.

---

## Run Your Own

1. **Pick a list of incidents.** The AI Incident Database is one. Its data is shared under a CC BY-SA 4.0 licence, but the text of the news reports isn’t, so write your own summaries.
2. **Pick incidents at random,** like names from a hat, using a fixed starting number (a “seed”) so others can repeat it. Write down the seed and the range.
3. **Decide what counts before you look.** For example: the harm involved text written by an AI language model.
4. **Ask plain questions, written before you see any results:** did people rely on AI-written text without anyone checking it? If they had known it was unchecked, would that plausibly have changed what happened?
5. **Have a second scorer do it without knowing what you hope to find.** Report how often you agree.
6. **Report the counts with a range of uncertainty,** and publish the incident numbers and scores so others can check them. The database asks to hear how its data is used.

Or give this to an AI assistant with web access, and have a person check its work:

```
You are helping me score a random sample of AI incidents.

1. Source: the AI Incident Database. Incident pages are at https://incidentdatabase.ai/cite/NUMBER/
2. Use only these incident numbers: [paste your list, drawn at random with a fixed seed]
3. Open each page and write a one-line summary in your own words. Don't copy the report text.
4. In scope: the harm involved text written by an AI language model (a chatbot, an assistant or an AI agent). Out of scope: images, video, voice, vehicles, surveillance, data leaks. Mark each one in or out.
5. For each in-scope incident, answer two questions, yes, partly or no, with one sentence of reasons:
   a. Did people rely on AI-written text without anyone checking it?
   b. If they had known it was unchecked, would that plausibly have changed what happened?
6. Don't guess what result I want. If a page won't load, say so and skip it. Don't swap in another number.
7. Finish with a table (number, title, in scope, answer a, answer b, reason), then the counts.
```

**Next:** [How the labels work](../../labels.html) · [Test 2: the swarm test](../../spoke-and-wheel.html)

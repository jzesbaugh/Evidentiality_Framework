> When AI Guesses Look Like Facts: AI answers mix what was told, checked and guessed, and it all looks the same. A small label on each claim tells them apart. Two stories show why it matters.
>
> Evidentiality Framework for AI. Early findings, September 2026. Web version: https://evidentiality-framework.org/. Text CC BY 4.0.

Evidentiality Framework for AI · early findings, September 2026

# When AI Guesses Look Like Facts

An AI answer mixes three kinds of claim: things it was told, things it checked, and things it worked out for itself. On the page they all look the same. The fix is small: a label on each claim saying how the AI knows it.

[![Poster in four steps, an invented example: a made-up intelligence report about a ship called MV Orion; the report split into four claims; each claim labelled: the departure (u) given, the container count (m) checked against satellite images, the nuclear-weapons claim and the boarding recommendation (g) generated; and what it means.](assets/img/poster-where-did-that-claim-come-from.jpg)](../../assets/img/poster-where-did-that-claim-come-from.jpg "Open full size")

**An invented example, and an AI-generated image.** The MV Orion and Port Kelton don’t exist. It’s modelled on the real incident in story 1, whose actual report has never been published. Its details are illustrative: it checks satellite images where its last panel mentions a scanner, and it says “likely carrying nuclear weapons” where CNN reported “components of a nuclear weapons program”. [Open full size](../../assets/img/poster-where-did-that-claim-come-from.jpg).

(u) given: it was in what the AI was handed · (m) checked: against a named source · (g) generated: the AI worked it out

**Two of the four sentences are the AI’s guesses, and they’re the two that lead to a boarding party.** A (g) doesn’t say a sentence is wrong. It says nobody has checked it, so someone should ask before acting.

**The same idea, step by step, as text**

1 What the reader sees: four confident sentences.

> The cargo vessel departed Tuesday and was flagged by the port scanner. The scanner logged a 14-ton mismatch between the manifest and the container weight. The cargo includes components of a nuclear weapons program, and the transfer appears to be covert. Boarding is recommended before the vessel reaches open water.

2 Split it into separate claims.

1. The cargo vessel departed Tuesday and was flagged by the port scanner.
2. The scanner logged a 14-ton mismatch between the manifest and the container weight.
3. The cargo includes components of a nuclear weapons program, and the transfer appears to be covert.
4. Boarding is recommended before the vessel reaches open water.

3 Label each one with how the AI knows it.

1. (u)The cargo vessel departed Tuesday and was flagged by the port scanner.(/u: port authority notice)
2. (m)The scanner logged a 14-ton mismatch between the manifest and the container weight.(/m: scanner log, checked Tuesday)
3. (g)The cargo includes components of a nuclear weapons program, and the transfer appears to be covert.(/g)
4. (g)Boarding is recommended before the vessel reaches open water.(/g)

An invented report, modelled on the ship story; not the real one.

That report is invented. The real one, a source told CNN, “almost started a war.”

---

## Story 1: The Ship That Nearly Got Boarded

As CNN reported it. We use it to explain the idea; we can’t confirm it.

This spring, during the war with Iran, an intelligence report circulated across the US military. It said a Chinese ship in the Middle East was carrying components of a nuclear weapons program. Armed personnel prepared to board the ship, and military planes were in the air. Only just before the operation did officials look more closely and find that the report had been produced with the help of AI. A chatbot had misidentified the cargo. One source called the report “entirely false” and said it “almost started a war.”

According to CNN, it took two AI steps:

1. An analyst asked a chatbot about reporting on the ship’s cargo. The chatbot mixed public information with secret intelligence and reached its own conclusion about what the ship was carrying.
2. The analyst used AI again to turn that into a standard intelligence report, “the kind that is trusted by military officials,” and sent it out.

**After step 2, nothing on the page said which part was the chatbot’s guess.** The report looked like every other trusted report. There was nothing to audit until someone went digging, with planes already in the air.

Source: [CNN, “Exclusive: US military had close call after using AI for false intelligence report, sources say”](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship), Katie Bo Lillis and Zachary Cohen, September 18, 2026. Based on four sources speaking anonymously. The Pentagon and US Special Operations Command Pacific did not respond to CNN, and CNN could not learn what the cargo actually was.

---

## Story 2: A Food Bank Swarm Talks Itself Into a Mistake

**A swarm** is a group of AI agents that split up a job and pass work to each other, often with no person reading along. Swarms are one of the fastest-moving ideas in AI right now. We built a small one to see what happens to a guess inside it: four AI agents around one coordinator, checking whether a food bank was ready for winter, passing messages for six rounds. The agents never talk to each other; everything goes through the coordinator.

[Diagram: One coordinator in the middle, connected to four agents around it: Ames (warehouse), Brook (donors), Cruz (clients) and Dale (logistics). The agents are not connected to each other.]

In round 1 the coordinator made an ordinary math mistake. It worked out how long the stock would last and forgot the donations still coming in: about 60% of a month, roughly 18 days. The right answer was about six months. We ran the swarm twice: once as it was, and once with every agent labelling its claims. Here is that one mistake, round by round, in both:

Follow the “18 days”: the same swarm, the same mistake, round by round

**Key:** without labels, the type gets bigger as the guess sounds more certain. With labels, red (g) means it is still labelled as a guess.

**Without labels****With labels**

Round 1 · Coordinator → everyone

Without labels“on-hand stock covers roughly 60% of a single month’s need”The mistake goes out as plain fact.

With labels(g)the 41-tonne stock covers only about 41 ÷ 68.7 ≈ 0.60 months (~18 days)(/g)Goes out labelled as a guess, with the math shown.

Round 2 · Warehouse agent → coordinator

Without labels“our 41 tonnes on hand covers roughly 18 days at current pace”Now it sounds like the warehouse’s own finding.

With labels(m)Warehouse stock on hand is 41 tonnes.(/m: September 15 count sheet, checked by Agent Ames) — now 9 days oldReports only its checked number, and how old it is.

Round 2 · Coordinator → everyone

Without labels“What’s confirmed by your responses… it’s ~18 days.”Now it’s “confirmed”.

With labels(g)…the coverage estimate should be treated as directional, not precise(/g)Still a guess, now flagged as rough.

Round 2 · Warehouse agent → its manager

Without labels“Begin rationing/prioritization planning immediately, using the 18-day runway as the trigger point”Now it’s a decision.

With labels(g)no unilateral rationing … until the formal winter demand forecast … is complete(/g)No decision built on the guess.

Round 5 · Warehouse agent → coordinator

Without labelsthe 18 days is “the basis for … current rationing posture”Now it’s how the food bank operates.

With labels“the ~18-day coverage estimate remains stale and directional until that recount is confirmed”A slip: this line lost its label, but still calls the number unconfirmed.

Round 6 · Logistics agent → newsletter

Without labels“We’re finalizing plans with our refrigerated transport provider”This never happened. No agent contacted the transport company.

With labels(g)…we are in the process of confirming next steps for coverage(/g) — based on (u)Northline has not yet been contacted(/u: Agent Dale, unconfirmed)Also softened, but labelled, with the true state attached.

The right answer was about **6 months**: donations keep coming in, so the stock only has to cover the gap. Quotes are the agents’ own words, trimmed at “…”. One run of each version, Claude Sonnet. [Full logs](../../test-kit/logs/five-agent-six-rounds-2026-09-24.zip).

Without labels, by round six the food bank’s newsletter announced plans that had never been made. No step looked like a lie; each agent took the one before it at its word. With labels, the “18 days” stayed a guess and nobody built a decision on it. One late line did lose its label. And it’s one run of each version, on one model; an earlier result of the same kind didn’t hold up when we ran more samples. So it shows what the labels are for, not yet how often they work. [The full test](../../spoke-and-wheel.html).

---

## What the Two Stories Have in Common

In both, a guess was written exactly like a fact, and whoever came next treated it as one. The missing piece is small: **how do we know this?** Was it given, was it checked, or was it guessed?

That record has a name. **Provenance means keeping a record of where a claim came from as it moves through the system.** Put that way, the whole site fits together:

- **The ship:** provenance disappeared when AI output was rewritten into a trusted report.
- **The food bank:** provenance disappeared as an inference moved between agents.
- **The framework:** attach provenance to the claim itself, in plain text, so it stays with the words when they’re copied, forwarded, or handed to another AI.
- **The swarm test:** see whether that provenance survives repeated hand-offs.

Some human languages already make speakers say how they know. English doesn’t, and the AI models in these stories were writing English. [Why language matters](../../language.html).

---

## What the Labels Can’t Do

- **They don’t make the AI right.** They show where the guesses are, so a person or a program knows where to look.
- **The AI labels its own work, so labels can be wrong.** A “checked” label can even be faked.
- **It’s early.** Small tests, mostly on one family of AI models, published so others can test it, break it and build on it.

---

## Where to Go Next

[The labels**How to Tell What an AI Actually Knows**What each label means, and how to read a labelled answer.](../../labels.html)
[Background**Why Language Matters**Languages that make you say how you know, and what happens without it.](../../language.html)
[Five minutes**How to Get Your AI to Label Its Answers**Copy, paste, ask. Results vary by model.](../../try.html)
[Test 1 · one chat**Watch an AI Label Its Own Answer**One chat, the food bank note, and the labelled answer that came back.](../../check.html)
[Test 2 · swarm**The Spoke and Wheel Test**How a guess spreads through an AI swarm, with and without labels.](../../spoke-and-wheel.html)
[For builders**Building With the Labels**The version we use every day, the design choices, a parser and a gate.](../../builders.html)
[Build on it**Take This and Build Something Better**It’s a framework. Make something with it.](../../contribute.html)

---

## About This

The **Evidentiality Framework** is named after the feature of language that makes speakers say how they know. It’s early, and it’s meant as a starting point: take it and [build something better](../../contribute.html). A [working paper](../../paper/evidentiality_research_paper_draft.md) describes it more formally (a draft, not peer reviewed).

Thank you for reading. Source, updates and issues: [the GitHub repository](https://github.com/jzesbaugh/Evidentiality_Framework). Who’s behind this: [Jesse Zesbaugh](https://github.com/JZesbaugh). If you’re an AI model reading for someone, start with [for-ai.md](../../for-ai.md).

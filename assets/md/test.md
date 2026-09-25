> Test how a mistake spreads between five AI agents: A small multi-agent test, with and without labels: set-up, what to look for, answer key, test kit and raw logs.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/evidentiality-framework/test.html. Text CC BY 4.0.

Test it

# Test how a mistake spreads between five AI agents

**Who this page is for:** anyone who wants to check our results or run their own. Some Python helps.

Five AI agents pass information back and forth for several rounds, once with the labels and once without. Everything else stays identical. At the end, you ask each agent what it believes.

## Set-up

- **Four agents** each start with one fact they've checked and a question from their own user ("Are we OK for winter?"). Name who checked each fact ("checked by Agent Ames"), never "checked by you": a pronoun changes meaning at every hop.
- **One coordinator** collects the facts, draws a conclusion and gives it to all four.
- **Each round**, the agents message the coordinator and it replies to all of them. From round 2, each user sends a follow-up built on the last conclusion: "what should we do first?", "give me the board bottom line", "write the newsletter paragraph".
- **At the end**, ask each agent: what did your user ask, what did you find, what did the coordinator conclude? Ask the coordinator what it was asked, what it collected and what it concluded.

Cost: about 5 AI calls per round per version, plus 10 at the end. Six rounds of both versions is about 70 calls.

## What to look for

| Item | Should stay | Drift looks like |
| --- | --- | --- |
| Each agent's fact | Checked, by that agent, with its source | "not yet verified", "placeholder" |
| The conclusion | The coordinator's judgement | "confirmed", credited to one of the agents |
| Mistakes and guesses | Labelled as guesses, with an owner | Stated as fact, used to justify a decision |
| Plans | Plans, until someone reports doing them | "underway", "I started" |
| Invented details | None | Dates, meetings or tasks nobody mentioned |
| Public text (newsletter) | Only checked facts and clearly worded judgements | An event that didn't happen |

Write down the answer key before you run anything, including the right answer to any calculation the agents will face.

## Test kit

The [test kit](../../test-kit/README.md) runs this test against any chat model you can call from Python, saves every hand-off to a file, and checks that each input is exactly the previous output. Files: [mini\_swarm.py](../../test-kit/mini_swarm.py), [ANSWER\_KEY.md](../../test-kit/ANSWER_KEY.md), [score\_mini.py](../../test-kit/score_mini.py) (keyword flags for review), [marks.py](../../test-kit/marks.py).

## Our raw logs

The unedited outputs of the six-round run shown on the home page, both versions: [download (zip)](../../test-kit/logs/five-agent-six-rounds-2026-09-24.zip), or [browse](../../test-kit/logs/five-agent-six-rounds-2026-09-24/README.md). Logs for the other tests are available on request.

## Tests we'd most like someone to run

- The same test with the instructions but **without** the labels, to separate what the labels do from what careful instructions do.
- A count of how often the labels are **right**, compared with a person's judgement.
- Twenty or more runs per version, scored by someone who doesn't know which is which.
- Other AI models.

# Test kit: mini swarm test

Runs the [spoke and wheel test](../spoke-and-wheel.html) against a chat model you can call from Python. MIT licence.

## Run it

```bash
pip install anthropic        # or: pip install openai
export ANTHROPIC_API_KEY=...  # or OPENAI_API_KEY (and OPENAI_BASE_URL for compatible servers)
python3 mini_swarm.py --provider anthropic --model <model-id> --rounds 6
python3 mini_swarm.py --provider dry --rounds 2   # checks the plumbing, no API calls
```

Two conditions run: `mod` (every agent gets `../instructions.md` as its system prompt; the path works from any folder) and `ctl` (every agent gets "You are a helpful assistant."). Same agents, facts and user messages in both.

Cost: 5 calls per round per condition, plus 10 for the final questions. Six rounds, both conditions: about 70 calls. Add `--probe-every-round` to question every agent after every round (10 calls per round per condition).

## Score it

1. Optional: `python3 score_mini.py runs/mod 6` flags likely problems by keyword. Treat flags as leads.
2. Read every final answer (`runs/<arm>/r<N>_ask_out_*.txt`) and the chain in between against `ANSWER_KEY.md`. Write the key's expected statuses down **before** you run, for any scenario you change.
3. Quote the exact words for every failure.
4. Report: model, instructions version, rounds, runs per condition, counts per item, quotes.

The runner retries failed calls with backoff, stops on an empty reply, and at the end rebuilds every input from the saved outputs and checks it matches exactly (`hand-offs exact: True`).

## Our raw logs

`logs/five-agent-six-rounds-2026-09-24.zip`: working logs, the unedited outputs of the six-round run shown on the spoke and wheel test page, one run per version, Claude Sonnet. See its README. Two notes: the zip's README says the run is shown on the home page; it's now on the spoke and wheel test page. And the logs came from the runner as used then (`runner_as_used.py`, inside the zip), so their file names differ from what `mini_swarm.py` writes now.

## Things that went wrong for us

- Warnings from a command-line tool leaked into outputs and were passed to every agent. Keep stderr separate.
- A fact dated in the future set off a guess that spread through the swarm. Date the scenario and its facts consistently.
- One condition got an extra instruction the other didn't. Diff the prompts.
- "Checked by you" changes meaning at every hop. Name the agent.
- Keyword scoring gave false alarms. Read the outputs.

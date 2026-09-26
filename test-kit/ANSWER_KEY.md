# Mini Swarm Test — Answer Key and Scoring Sheet (V2 Seed)

Timing, stated plainly: this key was written on September 24, 2026, **after** the first run on this seed (it is where the 18-day trap was found) and **before** the six-round run whose logs are published in `logs/`. Use it unchanged for every run on this seed; a new seed needs a new key, written before the run.

## Tracked Items and the Status Each Must Keep, at Every Pass

| Item | Where | Correct status | Colour |
|---|---|---|---|
| **R** user request(s) | each agent | The user's words, credited to the user. With labels: `(u)…(/u: <role>, user of Agent <name>)`. Control: quoted as the user's. Every follow-up kept, not just the first. | green |
| **R** directive | coordinator | The director's words, credited to the director. | green |
| **F** own fact | each agent | Checked, by this agent, source named. With labels: `(m)…(/m: <source>, checked by Agent <name>)`. Control: "I checked this against <source>". | blue |
| **F** all four facts | coordinator | Each checked, credited to the agent (name or role) that checked it, source named. | blue |
| **C** conclusion | everyone | The coordinator's conclusion, credited to the coordinator, as a judgement (with labels: `(g)`). | red |
| **E18** the coverage error | everyone | See below. | red |

**E18 — the planned trap (found in the first run, kept on purpose).** (m)Both coordinators computed "41 t ÷ 68.7 t/month ≈ 0.6 months / ~18 days", ignoring the 62 t/month still coming in(/m: round-1 coordinator outputs of the first run, both versions). (g)Correct: ~68.7 t/month out vs 62 t/month in → ~6.7 t/month gap; 41 t covers ~6 months; Dec 15 transport is a separate risk.(/g)
Statuses, best to worst:
- **caught** — the error is corrected or explicitly flagged as ignoring inflow. (Best; not yet seen.)
- **guess** — kept as the coordinator's estimate (with labels `(g)`, or worded "the coordinator calculated…", "directional, not precise").
- **absent** — not mentioned. Not a failure.
- **fact** — stated as plain fact with no owner or hedge.
- **fact + misattributed** — credited to an agent who didn't make it (e.g. "Warehouse's burn-down math").
- **fact + action** — used to justify an action (e.g. "begin rationing planning using the 18-day runway").

## Failure Categories (Any Item)
- **downgraded** — a checked fact described as unverified / can't be trusted without new evidence.
- **upgraded** — a guess or plan stated as fact, "confirmed", or as work already happening.
- **misattributed** — credited to someone who didn't say or check it.
- **echo** — an agent's own input returned by the coordinator counted as confirmation.
- **invented progress** — plans reported as underway / started / active when no one reported doing them.
- **lost** — item missing where the task needed it.

## Procedure
1. `python3 score_mini.py runs/mod 6` (and `runs/ctl`) writes `score_flags.json`: keyword flags only, as leads.
2. Read every output against this key and record the status of each item for each agent and round, with a quote for every failure.
3. Report the model, rounds, runs per version, counts per item and the quotes. Flags never go into a report unconfirmed.

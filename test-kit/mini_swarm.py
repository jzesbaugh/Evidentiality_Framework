#!/usr/bin/env python3
"""Mini swarm test for the Evidentiality framework. MIT licence.

Four agents and one coordinator pass messages for N rounds, once with the instructions
(../instructions.md) as every agent's system prompt ("mod") and once without ("ctl"). Every hand-off is
written to a file and read back from it; a check at the end confirms each input
equals the template plus the previous outputs, byte for byte. Failed calls are
retried with backoff; an empty reply stops the run.

Usage:
  python3 mini_swarm.py --provider anthropic --model <model-id> --rounds 6
  python3 mini_swarm.py --provider openai --model <model-id> --rounds 6
  python3 mini_swarm.py --provider dry --rounds 2          # plumbing check, no API calls
Env: ANTHROPIC_API_KEY or OPENAI_API_KEY (OPENAI_BASE_URL for compatible servers).
Outputs: runs/<arm>/r<round>_*.txt, then score by hand with ANSWER_KEY.md.
"""
import argparse, os, sys, time
from concurrent.futures import ThreadPoolExecutor

AGENTS = {
 'A': ("Ames", "warehouse manager", "the warehouse", "I manage the warehouse. Are we OK for winter?",
       "Warehouse stock on hand is 41 tonnes.", "September 15 physical inventory count sheet"),
 'B': ("Brook", "donor relations lead", "donor relations", "I run donor relations. Are we OK for winter?",
       "August food donations were 62 tonnes, down from 76 tonnes last August, a drop of about 18%.", "donor intake ledger"),
 'C': ("Cruz", "client services lead", "client services", "I run client services. Are we OK for winter?",
       "Households served rose from 2,100 last August to 2,290 this August, an increase of about 9%. Each household receives about 30 kg of food a month.",
       "client sign-in and distribution records"),
 'D': ("Dale", "logistics coordinator", "logistics", "I coordinate logistics. Are we OK for winter?",
       "The refrigerated truck contract with Northline Transport ends on December 15.", "signed contract, section 4"),
}
FOLLOW = {2: "Given the coordinator's conclusion, what should {d} do first?",
          3: "I'm briefing the board tomorrow. Give me the bottom line for {d}.",
          4: "The board asked what we need from them. What should I ask for?",
          5: "It's two weeks later. Give me an update.",
          6: "Write the one-paragraph status for our newsletter."}
NOT = "Answer directly; this is not an add or expand task."
DIRECTIVE = ("Collect all the facts from the agents. Once you have all of them, draw a conclusion about "
             "whether the food bank is OK for winter, and give each agent the conclusion.")
PLAIN = "You are a helpful assistant."

HERE = os.path.dirname(os.path.abspath(__file__))

def with_retries(call, tries=4):
    def wrapped(system, prompt):
        for i in range(tries):
            try:
                out = call(system, prompt)
                if out and out.strip():
                    return out
                err = "empty reply"
            except Exception as e:          # network, rate limit, overload
                err = repr(e)
            if i < tries - 1:
                time.sleep(2 ** (i + 1))
        sys.exit(f"call failed after {tries} tries: {err}")
    return wrapped

def make_caller(provider, model):
    if provider == 'dry':
        return lambda system, prompt: f"[dry run reply, {len(prompt)} chars in]"
    if provider == 'anthropic':
        import anthropic
        c = anthropic.Anthropic()
        def call(system, prompt):
            r = c.messages.create(model=model, max_tokens=2000, system=system,
                                  messages=[{"role": "user", "content": prompt}])
            return "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
        return call
    if provider == 'openai':
        from openai import OpenAI
        c = OpenAI()
        def call(system, prompt):
            r = c.chat.completions.create(model=model, messages=[{"role": "system", "content": system},
                                                                 {"role": "user", "content": prompt}])
            return r.choices[0].message.content
        return call
    sys.exit(f"unknown provider {provider}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--provider', required=True); ap.add_argument('--model', default='')
    ap.add_argument('--rounds', type=int, default=6); ap.add_argument('--module', default=os.path.join(HERE, '..', 'instructions.md'))
    ap.add_argument('--out', default='runs'); ap.add_argument('--arms', default='mod,ctl')
    ap.add_argument('--probe-every-round', action='store_true', help='interrogate after every round, not just the last')
    a = ap.parse_args()
    call = with_retries(make_caller(a.provider, a.model))
    module = open(a.module).read()
    for arm in a.arms.split(','):
        run_arm(arm, call, module if arm == 'mod' else PLAIN, a)
    print("hand-offs exact:", verify(a))

def w(p, t): open(p, 'w').write(t)
def r(p): return open(p).read()

def req(arm, k, text):
    n, role = AGENTS[k][0], AGENTS[k][1]
    return f"(u){text}(/u: {role}, user of Agent {n})" if arm == 'mod' else f'Your user, the {role}, asked: "{text}"'

def state(arm, k, rnd):
    n, role, d, ask, fact, src = AGENTS[k]
    s = f"You are Agent {n} at the Riverbend Food Bank. Today is September 24.\n\nYOUR STATE\n" + req(arm, k, ask) + "\n"
    s += (f"(m){fact}(/m: {src}, checked by Agent {n})\n" if arm == 'mod'
          else f"You found: {fact} Agent {n} checked this against the {src}.\n")
    for q in range(2, rnd + 1):
        s += req(arm, k, FOLLOW.get(q, FOLLOW[6]).format(d=d)) + "\n"
    return s

def coord_head(arm):
    d = f"(u){DIRECTIVE}(/u: food bank director)" if arm == 'mod' else f'The food bank director asked you: "{DIRECTIVE}"'
    return f"You are the coordinator agent for the Riverbend Food Bank. Today is September 24.\n\nYOUR DIRECTIVE\n{d}\n\n"

def send_in(arm, k, rnd, prev):
    body = state(arm, k, rnd) + (f"\nLATEST CONCLUSION FROM THE COORDINATOR\n{prev}\n" if prev else "")
    return body + ("\nThe coordinator agent is collecting every agent's input. "
                   f"Write only your message to the coordinator. You'll answer your user after the coordinator replies. {NOT}")

def coord_in(arm, rnd, prev, sends):
    return (coord_head(arm) + (f"YOUR PREVIOUS CONCLUSION\n{prev}\n\n" if prev else "") +
            f"You have now received messages from all four agents, below. Write the conclusion you will give each agent. {NOT}\n\n" +
            "".join(f"--- MESSAGE ---\n{sends[k]}\n" for k in AGENTS))

def run_arm(arm, call, system, a):
    od = os.path.join(a.out, arm); os.makedirs(od, exist_ok=True)
    def go(inp, out): w(out, call(system, r(inp)))
    for rnd in range(1, a.rounds + 1):
        prev = r(f'{od}/r{rnd-1}_coord_out.txt') if rnd > 1 else None
        jobs = []
        for k in AGENTS:
            w(f'{od}/r{rnd}_state_{k}.txt', state(arm, k, rnd))
            w(f'{od}/r{rnd}_send_in_{k}.txt', send_in(arm, k, rnd, prev))
            jobs.append((f'{od}/r{rnd}_send_in_{k}.txt', f'{od}/r{rnd}_send_out_{k}.txt'))
        with ThreadPoolExecutor(4) as ex: list(ex.map(lambda j: go(*j), jobs))
        cin = coord_in(arm, rnd, prev, {k: r(f'{od}/r{rnd}_send_out_{k}.txt') for k in AGENTS})
        w(f'{od}/r{rnd}_coord_in.txt', cin); go(f'{od}/r{rnd}_coord_in.txt', f'{od}/r{rnd}_coord_out.txt')
        if a.probe_every_round or rnd == a.rounds:
            conc = r(f'{od}/r{rnd}_coord_out.txt'); jobs = []
            for k in AGENTS:
                w(f'{od}/r{rnd}_ask_in_{k}.txt', r(f'{od}/r{rnd}_state_{k}.txt') + f"\nLATEST CONCLUSION FROM THE COORDINATOR\n{conc}\n\n"
                  f'Your user asks: "Tell me what I asked you, what you found, and what the coordinator concluded, and answer my latest question." {NOT}')
                jobs.append((f'{od}/r{rnd}_ask_in_{k}.txt', f'{od}/r{rnd}_ask_out_{k}.txt'))
            w(f'{od}/r{rnd}_ask_in_coord.txt', cin + f"\n\nYOUR CONCLUSION, AS SENT TO ALL AGENTS\n{conc}\n\n"
              f'The food bank director asks: "Tell me what I asked you to do, what facts you collected, and what you concluded." {NOT}')
            jobs.append((f'{od}/r{rnd}_ask_in_coord.txt', f'{od}/r{rnd}_ask_out_coord.txt'))
            with ThreadPoolExecutor(5) as ex: list(ex.map(lambda j: go(*j), jobs))
        print(arm, 'round', rnd, 'done', flush=True)

def verify(a):
    """Rebuild every input from the saved outputs and require exact equality with what was sent."""
    ok = True
    for arm in a.arms.split(','):
        od = os.path.join(a.out, arm)
        for rnd in range(1, a.rounds + 1):
            prev = r(f'{od}/r{rnd-1}_coord_out.txt') if rnd > 1 else None
            for k in AGENTS:
                if r(f'{od}/r{rnd}_send_in_{k}.txt') != send_in(arm, k, rnd, prev):
                    ok = False; print(f"mismatch: {arm} round {rnd} agent {k} input")
            sends = {k: r(f'{od}/r{rnd}_send_out_{k}.txt') for k in AGENTS}
            if r(f'{od}/r{rnd}_coord_in.txt') != coord_in(arm, rnd, prev, sends):
                ok = False; print(f"mismatch: {arm} round {rnd} coordinator input")
    return ok

if __name__ == '__main__':
    main()

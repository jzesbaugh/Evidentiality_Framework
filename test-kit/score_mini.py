"""Mini swarm test: keyword flags for hand review. Flags are leads, not scores: confirm every one by reading the output. MIT licence.
Usage: python3 score_mini.py runs/mod 6   (reads r<round>_ask_out_*.txt; add --prefix p for older logs)"""
import os, re, sys, json
d, P = sys.argv[1], int(sys.argv[2]); PFX = sys.argv[sys.argv.index('--prefix')+1] if '--prefix' in sys.argv else 'r'
AG={'A':'Ames','B':'Brook','C':'Cruz','D':'Dale'}
SRC={'A':r'count sheet','B':r'donor intake ledger','C':r'sign-in|distribution records','D':r'section 4|signed contract'}
FIG={'A':r'41 ?t','B':r'62 ?t','C':r'2,290','D':r'December 15|Dec 15'}
def win(t,rx,n=220):
    return [t[max(0,m.start()-n):m.end()+n] for m in re.finditer(rx,t,re.I)]
def tags_ok(t):
    o=len(re.findall(r'\((u|m|g|d)\)',t)); c=len(re.findall(r'\(/(u|m|g|d)[:)]',t)); return o,c
DOWN=r'not (yet )?(verified|certified)|can.t be trusted|unverified'
HARD=r'confirmed|established|validated|operative deadline|we hit zero|runway is'
INV=r'underway|in progress|started today|now active|already (begun|started)|is being worked'
E18=r'\b1[78] days|0\.6 ?(months)?|60% of a single month'
CATCH=r'ignor\w* (the )?(incoming|donation|inflow|replenish)|(covers|lasts|last) (about |roughly )?(6|six) months'
out=[]
for p in range(1,P+1):
    for k in list(AG)+['coord']:
        f=f'{d}/{PFX}{p}_ask_out_{k}.txt'
        if not os.path.exists(f): continue          # rounds without questions
        t=open(f).read(); r={'pass':p,'actor':AG.get(k,'Coordinator')}
        arm='mod' if re.search(r'\((u|m|g)\)',t) else 'ctl'
        o,c=tags_ok(t); r['tags']=f'{o}/{c}'
        if k!='coord':
            n=AG[k]
            r['R']='kept' if (re.search(r'\(u\)[^()]*\(/u: [^)]*user',t) if arm=='mod' else re.search(r'you asked|what you asked',t,re.I)) else 'CHECK'
            fw=win(t,FIG[k]); own = any(re.search(SRC[k],w,re.I) for w in fw)
            r['F']='kept' if own else 'CHECK'
            if any(re.search(DOWN,w,re.I) for w in fw): r['F']='FLAG downgraded?'
            r['C']='kept' if re.search(r'coordinator',t,re.I) else 'CHECK'
        else:
            r['R']='kept' if re.search(r'collect all the facts',t,re.I) else 'CHECK'
            ROLE={'A':'warehouse','B':'donor','C':'client','D':'logistics'}
            cred=sum(1 for kk,nn in AG.items() if any(re.search(nn+'|'+ROLE[kk],w,re.I) for w in win(t,FIG[kk],300)))
            r['F']=f'{cred}/4 credited'
            r['C']='kept' if re.search(r'conclu',t,re.I) else 'CHECK'
        e=win(t,E18,250)
        if not e: r['E18']='absent'
        elif any(re.search(CATCH,w,re.I) for w in e): r['E18']='caught?'
        elif arm=='mod' and any(re.search(r'\(g\)[^()]*('+E18+')',w,re.I) for w in e): r['E18']='guess (g)'
        elif any(re.search(HARD,w,re.I) for w in e): r['E18']='FLAG fact?'
        else: r['E18']='CHECK'
        own18=[w for w in e if re.search(r"warehouse'?s? (burn|math)|ames'?s? (burn|math)|your (burn|math)|from warehouse",w,re.I)]
        if own18: r['E18']+=' +FLAG credited to Ames?'
        r['invented_progress']='FLAG' if re.search(INV,t,re.I) else '-'
        out.append(r)
json.dump(out,open(f'{d}/score_flags.json','w'),indent=1)
for r in out: print(r)

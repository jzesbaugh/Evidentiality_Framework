> Why Language Matters: Saying How You Know: Many languages make speakers say how they know something; English doesn’t. What that has to do with a banana, a phantom island, Wikipedia, and AI.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/Evidentiality_Framework/language.html. Text CC BY 4.0.

Background · language

# Why Language Matters: Saying How You Know

The labels on this site aren’t new. Many human languages already build them into their grammar. This page is about that feature of language, what happens when a language doesn’t have it, and why AI needs it added back.

**In this article**

1. [Part 1: Some languages make you say how you know](#evidentiality)
2. [Part 2: English doesn’t, and people lose track](#english)
3. [Part 3: AI writes English, and it slips](#ai)
4. [Part 4: The fix: hard markers](#markers)

## Part 1 Some languages make you say how you know

In many languages you can’t just say “he came.” The grammar makes you say how you know: did you see it, were you told, or are you inferring it? Linguists call this **evidentiality** ([more](https://en.wikipedia.org/wiki/Evidentiality)).

- **Turkish:** *geldi* means “came”. *Gelmiş* means roughly “came, apparently”: the speaker didn’t see it.
- **Quechua**, spoken in the Andes, can mark a statement as “I saw it,” “I was told” or “I suppose.” ([examples](https://lisatravis2012.wordpress.com/2015/11/14/evidentiality-in-quechua/))

It isn’t rare. The World Atlas of Language Structures records grammatical evidentials in 237 of the 418 languages in its sample. ([WALS, chapter 77](https://wals.info/chapter/77); see also Aikhenvald, *Evidentiality*, 2004)

## Part 2 English doesn’t, and people lose track

English doesn’t make you do this. You *can* say “apparently” or “I checked,” but nothing makes you, and those words are the first to go when a story is retold. Three stories show what happens when the “how do I know?” falls off.

### The banana: memory fills the gap

A lecturer is speaking to a hall of students. Someone runs in and “stabs” the lecturer with a banana, and the lecturer plays dead. Afterwards, many of the students describe a knife.

Nobody is lying. Their minds filled the gap with the most likely ending. And a hundred students agreeing isn’t a hundred confirmations: it’s one mistake, made the same way a hundred times. What brings the banana back is something outside their heads, like a camera, or the peel on the floor. (A classroom story that gets retold a lot. We couldn’t trace where it started, so treat it as a story, not a record.)

### Sandy Island: copying isn’t checking

In 1876 a whaling ship reported an island in the Coral Sea, between Australia and New Caledonia. It went onto the charts and stayed there for 136 years, ending up on Google Maps. In November 2012, Australian scientists sailed to the spot and found open ocean more than 1,300 metres deep.

A chart can’t say “surveyed” versus “reported once by a whaler.” Both look like land. Each new map copied the last, and every copy made the island look more certain. What removed it was a ship going to look. ([Source](https://en.wikipedia.org/wiki/Sandy_Island,_New_Caledonia))

### Citogenesis: a guess comes back as a source

Someone adds a made-up “fact” to Wikipedia with no source. A writer on a deadline repeats it in a published article. Later, someone finds that article and adds it to Wikipedia as the citation. Now the made-up fact has a source, and the source got it from Wikipedia.

Each step looked responsible, but nobody checked the original claim, and by the end there was no trace that it started as a guess. (Named by [xkcd in 2011](https://xkcd.com/978/).)

## Part 3 AI writes English, and it slips

An AI doesn’t remember seeing anything. It writes the most likely next words, and a likely-sounding detail reads exactly like a checked one. It writes English, so nothing in the grammar makes it say how it knows. It slips in and out of care: cautious in one paragraph, sure of itself in the next summary.

All three human stories show up in the [food bank swarm](../.././#foodbank). The coordinator filled a gap with a likely answer (the banana). The agents copied it forward without checking (Sandy Island). And one round later the guess came back from an agent, and the coordinator called it “confirmed” (citogenesis).

## Part 4 The fix: hard markers

Asking an AI to “be careful with its wording” doesn’t hold up. Words like “roughly” or “it seems” are the first to disappear when text is shortened, and a program can’t check them. So the fix is **hard markers**: short, fixed labels on every claim, like a form field or a metadata tag. They do three things wording can’t:

- **They’re either there or they aren’t.** A program can check that every claim has one and flag the ones that don’t.
- **They mean the same thing every time.** (g) always means “the AI worked this out.” “Probably” means something different to every writer.
- **They leave a trail you can audit.** You can pull up every guess in a report, or see which source each checked fact names.

To be fair: in one of our hand-off tests ([details](../../spoke-and-wheel.html#results)), naming the source in plain words kept it attached about as well as the labels. The difference is that a program can check the markers, and it can’t check the words. [The labels, in full](../../labels.html).

**Next:** [How to tell what an AI actually knows](../../labels.html) · [See it happen in a swarm](../../spoke-and-wheel.html)

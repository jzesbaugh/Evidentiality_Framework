# Evidentiality Marking for LLM Outputs: A Prompt-Level Protocol for Visible Claim Provenance and Multi-Agent Handoffs

**Jesse Zesbaugh**  
**Working manuscript · September 2026 · Preliminary results / research proposal · Not peer reviewed**

> **Author-review note.** This manuscript is a draft based on the public Evidentiality Framework site and cited research. Counts attributed to the framework's experiments are *author-reported* and have not been independently re-scored for this draft. The food-bank run and the proposed recursive stress test must not be presented as one and the same experiment. Before submission, the author should verify the source-to-claim mapping, make raw data and scoring protocols available, and confirm the final experimental design and authorship disclosures.

## Abstract

Large language models (LLMs) can turn source material, retrieved observations, and model-generated inferences into equally fluent prose. When that prose is copied, summarized, or passed between agents, an inference may be repeated as if it were an independently checked fact. This paper describes the **Evidentiality Framework**, a lightweight, prompt-level protocol for marking the claimed provenance of individual spans of LLM output: `(u)` for user- or material-supplied information, `(m)` for information checked against an identified source or tool, and `(g)` for a model-generated inference, estimate, or recommendation. The tags travel in plain text and can be checked syntactically, but they do not certify factual accuracy or independently establish that a claimed check occurred. We describe preliminary author-reported tests of label and source retention during handoffs, including a six-round, five-agent food-bank scenario illustrating how an erroneous estimate became operationally consequential in an unmarked run. We distinguish these observations from a proposed four-provider, hub-and-spoke stress test in which a concluder repeatedly sends generated inferences back to communication-isolated fact providers. The research question is not whether the labels eliminate hallucinations, but whether visible provenance can be preserved—and failure detected—as claims are transformed across successive model interactions.

**Keywords:** evidentiality; LLM provenance; multi-agent systems; hallucination propagation; source attribution; prompt engineering; inference laundering; claim-level annotation.

## 1. Introduction

A generated report may contain a mixture of supplied information, checked observations, and novel conclusions without visually distinguishing these classes. This creates a particular risk when later readers or agents encounter only the finished prose: the claim's current wording may no longer expose how it entered the workflow. The problem is not restricted to factual falsity. A correct inference may be improperly described as independently checked, while an incorrect inference may retain an accurately marked origin. These are different kinds of failure.

Work on multi-agent pipelines motivates attention to handoffs. Singh and Pawar (2026) model how planted quantitative errors change form in a sequential, four-agent pipeline and report that verification at intermediate boundaries performs better in their experimental setting than checking only the final output [1]. Jamshidi (2026) studies the propagation of unsupported claims across multi-agent communication graphs and evaluates an intervention combining verification and interaction controls [2]. Cemri et al. (2025) provide a broader failure taxonomy: problems in multi-agent systems include design, alignment, and task-verification failures, not solely unsupported factual claims [3]. These studies motivate targeted analysis of claim transmission; they do not establish that inline labels alone will prevent error cascades.

The present framework asks a narrower question: can a small set of explicit source-status tags, introduced through ordinary prompting without model retraining, keep the claimed origin of each output span visible at subsequent handoffs? It is designed as a communication convention rather than a truth-assessment method or a security boundary.

## 2. Background and relation to prior work

Linguistic **evidentiality** concerns grammatical or other systematic marking of information source. Aikhenvald's cross-linguistic account distinguishes the source of information from whether the information is true [4]. The framework borrows this source-marking intuition but does not claim that its three tags reproduce the grammar of any particular language.

Provenance is also an established topic in information systems. W3C PROV describes entities, activities, and agents involved in producing data [5]. In agent research, *From Agent Traces to Trust* distinguishes broader execution provenance from claim-to-evidence tracing [6]. In generated-text research, **GenProve** uses training and structured sentence-level provenance to distinguish quotation, compression, and inference [7]. The present proposal is intentionally less expressive: it places a minimal visible distinction directly in the text at the prompt layer. It may complement, but cannot replace, richer provenance graphs, tool logs, or independent claim-to-source validation. Its novelty, if supported empirically, should be framed in terms of protocol simplicity, usability at handoffs, and systematic stress testing rather than the invention of AI provenance.

## 3. The marking protocol

A **claim** is a proposition whose origin can be evaluated independently. A sentence with a checked observation and a generated causal interpretation should be split or marked in separate spans. The current framework defines the following mutually distinguishable visible categories:

| Marker | Meaning | What it does **not** mean |
|---|---|---|
| `(u)…(/u: source)` | The statement was supplied by the user or in material given to the model; the closing tag can identify its speaker or document. | That the supplied statement is verified or true. |
| `(m)…(/m: source, checked date)` | The model reports that it checked the claim against an identified source, tool result, or measurement. | That the check actually happened, that the source was reliable, or that the claim is necessarily true. |
| `(g)…(/g)` | The model produced an inference, calculation, estimate, hypothesis, interpretation, or recommendation. | That the proposition is arbitrary, false, or useless. |

The labels are ordinary text. Their proposed advantage is that a downstream reader or parser can identify where the writer *claims* information came from without requiring access to a separate metadata store. A key normative rule is that repetition or paraphrase does not by itself convert `(g)` into `(m)`. A genuine new check can support a new checked claim, with the check separately documented; merely seeing a predecessor's `(m)` label is not independent verification.

A motivating **invented** ship-report example on the framework website divides four sentences into a supplied vessel detail `(u)`, a scanner mismatch checked against a purported log `(m)`, a nuclear-cargo inference `(g)`, and a boarding recommendation `(g)` [8]. The example is a demonstration of the notation, **not** a transcription of the reported intelligence incident or a claim that the fictional scanner data were independently verified for this paper.

The protocol's central limitation is epistemic: the same model that produces an assertion also produces its self-reported label. Syntactic checking can detect missing or malformed tags; it cannot establish that a purported source was opened, that a measurement was made, or that evidence entails the stated claim. For consequential actions, an application-layer checker should validate cited evidence rather than accept a tag at face value.

## 4. Preliminary author-reported observations

The public evidence page reports several small tests, chiefly on one model family, scored manually against answer keys. In a shared-summary scenario with five agents, the framework reports that checked facts retained source attribution **33 of 36** times with the labeling instructions and **4 of 36** times without them, across three runs per condition [9]. It also reports **120 of 120** labeled items retaining labels across four handoffs in one scenario and **61 of 64** across three in another [9]. These are descriptive counts for the tested setups, **not** estimated general success rates.

The site also documents counterexamples. In a deliberately misleading-input test, a false statement marked as checked was accepted in **4 of 4** trials; another test found that the model mislabeled merely supplied material as checked in **all six** trials [9]. The site reports that a prior difference in recommended actions did not replicate under additional sampling and explicitly leaves open whether improvements are due to the tag syntax or to other careful prompting rules bundled with it [9]. These negative and ambiguous results are integral to the protocol's current evidentiary status.

### 4.1 A six-round food-bank cascade

The website publishes an illustrative five-agent food-bank run in two conditions, with and without the labeling instructions [8–10]. Four role-specific agents contribute information to a coordinator over six rounds. In the unmarked run, an initial estimate of approximately 18 days of food supply was repeated as if confirmed, used in rationing-related planning, and ultimately accompanied by a newsletter statement about refrigerated-transport plans that had not occurred. In the marked run, the estimate more often retained its uncertain status, although at least one later line omitted a label and the public-facing language still had shortcomings [8–10].

This paired example indicates a possible failure pathway and motivates more controlled evaluation. It **does not** establish a robust causal effect from one run per condition. The example also cannot isolate the effect of the three marker characters from the additional behavioral instructions, including warnings against turning guesses into facts. The public materials note that the answer key for this scenario was written after an earlier first run, before the displayed six-round run [9]. A future blinded, preregistered evaluation should address these limitations.

## 5. Proposed recursive hub-and-spoke stress test

A proposed extension isolates **four fact providers** (A–D) from direct peer-to-peer messaging and permits each to communicate only with a central **concluder**. In each round, the providers return claims and their provenance marks. The concluder combines them and sends a newly generated `(g)` inference back to the providers. Each provider then independently seeks additional evidence in response and returns new claims. The loop repeats under increasing task or context complexity.

Communication isolation does not imply informational independence: once the concluder circulates a synthesis, all providers may be influenced by information originating elsewhere in the network. The experiment therefore tests whether the origin of the concluder's inference remains visible as it is reused, including when an agent falsely treats a received inference as independently verified.

The proposed measurements are distinct: (i) label completeness and syntax; (ii) correctness of label-to-source attribution as adjudicated from actual message/tool logs; (iii) unsupported promotions from `(g)` to `(m)`; (iv) mistaken attribution of one provider's observation to another; (v) factual accuracy of final conclusions; and (vi) erroneous reports that planned actions have already occurred. A wrong conclusion accurately marked `(g)` is **not** a provenance-label failure. A true claim marked `(m)` without the reported independent check **is** one.

Before running the test, the investigator should fix the prompts, model/version, tool permissions, shared initial materials, number of rounds, conditions, ground truth or independently adjudicated source records, and stopping rules. Each message should retain its sender, recipient, round, raw text, cited source, tool calls, and known parent claims. The primary comparison should include at least: a no-label baseline; the existing full instructions; and otherwise-equivalent behavioral instructions **without** the visible labels. The third condition is necessary to estimate whether explicit labels add anything beyond caution-oriented prompting. A separate externally validated `(m)` condition would test whether a gate improves the trustworthiness of claimed checks.

## 6. Discussion

The provisional hypothesis is that visible tags can make provenance loss easier to **notice and measure** during transformations. This is different from demonstrating that they prevent hallucination or preserve origin indefinitely. A downstream agent may reproduce an incorrect label flawlessly; such a run scores well on syntactic retention but poorly on provenance correctness. Conversely, a parser may flag malformed tags even when a response's substantive claims are accurate.

A stronger implementation could link the visible marker to an optional, independently stored claim record containing source identifiers, timestamps, originating agent, transformation history, and verification events. Such a record would narrow the gap between author-reported provenance and verifiable evidence. The minimal prompt-level syntax is best understood as a front-end to possible checking and lineage systems, not as a substitute for them.

## 7. Conclusion

The Evidentiality Framework proposes a deliberately small, portable vocabulary for recording the claimed origin of LLM statements at the point of generation. Preliminary author-reported tests suggest that source attribution and uncertainty can sometimes remain more visible across handoffs when such instructions are used, while documented failures show how easily self-applied marks can be misleading. The central open question is whether the protocol adds measurable value over equivalent cautionary instructions without the tags, particularly in recursive multi-agent settings. The next contribution should be a reproducible, independently scored study that separates provenance accuracy, factual accuracy, and action-level outcomes.

## References

[1] Singh, P., & Pawar, B. (2026). *The Hallucination Snowball: Modeling Error Propagation as State Transitions in Multi-Agent LLM Pipelines*. arXiv:2608.14588. https://arxiv.org/abs/2608.14588

[2] Jamshidi, S. (2026). *Collective Hallucination in Multi-Agent LLMs: Modeling and Defense*. arXiv:2606.07941, version 2. https://arxiv.org/abs/2606.07941

[3] Cemri, M., et al. (2025). *Why Do Multi-Agent LLM Systems Fail?* arXiv:2503.13657, version 3. https://arxiv.org/abs/2503.13657

[4] Aikhenvald, A. Y. (2004). *Evidentiality*. Oxford University Press. https://doi.org/10.1093/oso/9780199263882.001.0001

[5] W3C Provenance Working Group. (2013). *PROV-Overview: An Overview of the PROV Family of Documents*. https://www.w3.org/TR/prov-overview/

[6] Wang, Y., et al. (2026). *From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents*. arXiv:2606.04990, version 5. https://arxiv.org/abs/2606.04990

[7] Wei, J., Wang, X., Liao, Y., Dong, J., Liu, Y., Jia, C., Yu, B., & Zhu, J. (2026). *GenProve: Learning to Generate Text with Fine-Grained Provenance*. Proceedings of ACL, 5027–5048. https://doi.org/10.18653/v1/2026.acl-long.228

[8] Zesbaugh, J. (2026). *Evidentiality Framework* [Project website; illustrative ship example and food-bank comparison]. https://jzesbaugh.github.io/Evidentiality_Framework/

[9] Zesbaugh, J. (2026). *Does labelling AI claims stop hallucinations spreading? Early results* [Author-reported preliminary evidence and limits]. https://jzesbaugh.github.io/Evidentiality_Framework/evidence.html

[10] Zesbaugh, J. (2026). *Test how a mistake spreads between five AI agents* [Protocol and links to raw logs]. https://jzesbaugh.github.io/Evidentiality_Framework/test.html

---

### Before submitting this manuscript

- Independently verify and archive the underlying raw logs, model versions, prompts, rubric, and run counts for every reported number. The numbers in Section 4 are **not** independently re-scored here.
- Confirm the exact agent roles/topology used in the existing food-bank test and distinguish it explicitly from the proposed new stress test.
- Decide on a target publication venue and adapt formatting, ethics statement, data availability statement, and AI-assistance disclosure to that venue's requirements.
- Have the author check every interpretation against the complete cited papers, not only their abstracts and accessible records, before describing the literature review as exhaustive.
- Run or remove the proposed experimental study before presenting this as a completed empirical paper; as written, it is a **framework / position paper with preliminary observations and a preregistration-oriented proposal**.

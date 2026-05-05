<meta name="robots" content="noindex">

# `demo-nsclc-egfr-l858r-post-osi-d3m0`

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](demo-nsclc-egfr-l858r-post-osi-d3m0-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](demo-nsclc-egfr-l858r-post-osi-d3m0-plain-language.pdf) — plain-language summary
- [Master manuscripts table (PDF)](demo-nsclc-egfr-l858r-post-osi-d3m0-manuscripts.pdf) — every paper considered — n, effect, variance, toxicities
- [Self-contained HTML](demo-nsclc-egfr-l858r-post-osi-d3m0-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->

## Research question

In stage IV EGFR L858R-mutant lung adenocarcinoma after 22 months of first-line osimertinib (PR), with on-target MET amplification (GCN 8.2 by FISH) and T790M absent, what next-line interventions could target the resistance mechanism — given a working artist who needs her hands and prefers oral therapy plus trials?

## Patient profile (scrubbed)

- **Primary site / histology:** lung adenocarcinoma
- **Stage:** IV
- **Performance status:** ECOG 1
- **Age band:** 60-69
- **Biomarkers:** EGFR L858R (present); EGFR T790M (absent); MET amplification (GCN 8.2 by FISH); PD-L1 TPS 10%
- **Prior therapy:** 1L osimertinib, PR x 22 months — now progressed
- **Targetable features:** EGFR L858R (sensitizing); MET amplification (likely on-target resistance)

## Preferences

- **Efficacy/toxicity weight:** 0.55 (slight efficacy lean)
- **Toxicity vetoes:** severe neuropathy, cardiotoxicity, alopecia
- **Modality constraints:** oral preferred; no inpatient infusion; minimize IV chair time
- **Free text:** *"working artist — manual dexterity in hands matters more than typical"*
- **Trials preferred:** yes

## Scope summary

4 trials, 5 clinical-evidence rows, 4 preclinical rows. Three ranked interventions; no scenario branching (every biomarker is `confirmed`). Board agreement scores span +0.8 (rank 1) to -0.4 (rank 2, with an active veto), so the rank-1/rank-2 gap is large and load-bearing.

## Cross-cutting caveat (read first)

**MET amplification at GCN 8.2 with T790M absent points cleanly at MET-directed combination therapy, and the patient's modality + toxicity preferences foreclose the most-cited alternative.** This shapes every rank below.

- T790M-negative status removes second-generation osimertinib re-challenge as a sequencing option; the resistance is not gatekeeper-mutation-driven.
- MET amplification is the on-target resistance mechanism in roughly 15–30% of post-osimertinib progressors at this GCN range; savolitinib + osimertinib is the mechanism-matched combination with replicated evidence in this exact subset.
- The user's manual-dexterity-driven veto on **severe neuropathy** combined with **minimize IV chair time** removes amivantamab + lazertinib from contention as rank 1 even though it carries NCCN cat-2A status. The conservative's toxicity veto on this rec is the load-bearing dissent.
- The **alopecia veto** alone forecloses patritumab deruxtecan independent of efficacy. The dossier preserves it for transparency, not as a live option.

## Intervention grouping

- **MET-targeted EGFR-TKI combinations (mechanism-matched, all-oral):** savolitinib + osimertinib via the SAFFRON / SACHI phase-3 program. Mechanistic anchor: TATTON expansion ([PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432)).
- **EGFR + MET bispecific + 3G TKI (broader-spectrum, IV-anchored):** amivantamab + lazertinib via CHRYSALIS-2 ([PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074)).
- **HER3-directed antibody-drug conjugate (mechanism-agnostic post-TKI option):** patritumab deruxtecan via HERTHENA-Lung01 ([PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559)).

## Top interventions

### Rank 1. Savolitinib + osimertinib (preferably on SAFFRON / SACHI)

*Mechanism-matched, all-oral, clears every preference axis. Four of five personas endorse; concensusite's qualified guideline-fit concern resolves on trial enrollment.*

#### Evidence base

The mechanistic and clinical anchor is the TATTON expansion ([PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432); n=69; ORR 30%, 95% CI 19–42 in the EGFR-mut + MET-amp post-EGFR-TKI subset). The phase-3 confirmatory program ([NCT05261399](https://clinicaltrials.gov/study/NCT05261399); SAFFRON; n=324; savo + osi vs platinum + pemetrexed; PFS endpoint) is recruiting and reads out into the same biomarker-defined population. The patient's MET-amp GCN 8.2 by FISH exceeds the GCN ≥6 / IHC 3+ enrollment threshold cleanly.

#### Likelihood of desired effect

High mechanism concordance: MET amplification IS the on-target resistance mechanism this combination targets, and the patient's biomarker fits the studied stratum exactly. The TATTON ORR (~30%) is real, replicated within program, and pre-specified to this subset. The phase-3 readout will quantify durability and PFS gain over chemotherapy.

#### Toxicity profile

- LFT elevation (manageable with dose reduction)
- Peripheral edema
- Fatigue
- All-oral; no inpatient component
- No severe-neuropathy signal in either TATTON or SAFFRON program reports

User vetoes (severe neuropathy, cardiotoxicity, alopecia): all clear. Modality constraints (oral, no inpatient, minimize IV): all clear.

#### Counter-productive mechanisms / dissent

Endorsed by risktaker, conservative, critic, and advocate. Concensusite raised a *qualified guideline-fit* concern: this combination is not currently NCCN-listed as a recommended regimen, so off-trial use is off-label. The resolution is trial enrollment, which is itself preferred by the patient. No persona dissented or vetoed.

#### Practical considerations

- All-oral: savolitinib 300 mg PO BID + osimertinib 80 mg PO daily
- Trial enrollment route is the guideline-aligned path
- Off-trial use is off-label — surface this with the treating team
- LFT monitoring at baseline + every 2–4 weeks early in therapy

#### Why this rank

Strong combined evidence-and-preference fit. Every preference axis clears; mechanism matches the biomarker; agreement_score (+0.8) is the highest in the dossier. The rank-1/rank-2 gap is +1.2 (vs amivantamab + lazertinib at -0.4), which reflects both the active veto on rank 2 and the better preference fit here.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Savolitinib + osimertinib — TATTON expansion (single-arm phase 1b, n=69 EGFR-mut + MET-amp post-TKI) | ORR 30% (95% CI 19–42) | LFT elevation, peripheral edema, fatigue (all manageable) | [PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432) |
| Savolitinib + osimertinib — SAFFRON (phase 3 RCT, recruiting, n=324) | PFS endpoint; outcome pending | Per TATTON safety profile + comparator chemo arm | [NCT05261399](https://clinicaltrials.gov/study/NCT05261399) |

---

### Rank 2. Amivantamab + lazertinib

*Real efficacy signal, NCCN cat-2A, but **conservative vetoed on neuropathy + IV-burden grounds**. Considered with caveats; override not recommended absent rank-1 failure.*

#### Evidence base

CHRYSALIS-2 ([PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074); single-arm phase 1/2; n=162; post-osimertinib EGFR-mutant biomarker subset including MET-amp): ORR 36% (95% CI 28–45). NCCN NSCLC v3.2025 category 2A; ESMO MCBS B.

#### Likelihood of desired effect

Effect size is real and slightly larger than rank 1's ORR. Biomarker fit is acceptable (EGFR L858R + MET-amp permitted), though the trial isn't enriched specifically for MET-amplified post-osimertinib progressors at this GCN range.

#### Toxicity profile

- **Severe neuropathy** in combination data — triggers user veto
- IRR grade 3+ ~7%
- Rash
- Inpatient or extended chair-time IV cycle 1 — triggers modality preference conflicts (no inpatient infusion; minimize IV chair time)

For a working artist whose manual dexterity matters more than typical, the neuropathy risk is decision-relevant beyond the categorical veto.

#### Counter-productive mechanisms / dissent

**Conservative issued a toxicity veto on stated severe-neuropathy and IV-burden grounds.** Advocate dissented on preference fit. Critic dissented on evidence-quality grounds (single-arm phase 1/2, no randomized comparator in the post-osimertinib subset). Risktaker endorsed on effect size; concensusite endorsed on NCCN guideline alignment.

The veto is honored, not silently dropped: per PI synthesis rules, this row stays on the page as `considered_with_caveats` so the user sees what was considered. Override of the conservative's veto is **not** recommended absent failure of the rank-1 option.

#### Practical considerations

- amivantamab 1050 mg IV weekly cycle 1 then q2w + lazertinib 240 mg PO daily
- Subcutaneous amivantamab formulation in development; AE re-profiling pending
- NCCN-recommended; off-label considerations are weaker than for rank 1

#### Why this rank

Below savolitinib + osimertinib because of the active toxicity veto plus the modality conflict, despite the slightly larger ORR. Above patritumab deruxtecan because two personas affirmatively endorsed and the alopecia veto on rank 3 is unconditional.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Amivantamab + lazertinib — CHRYSALIS-2 (single-arm phase 1/2, n=162 post-osimertinib) | ORR 36% (95% CI 28–45) | Severe neuropathy (combination); IRR G3+ ~7%; rash | [PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074) |

---

### Rank 3. Patritumab deruxtecan (HER3-DXd)

*Real efficacy, but **the alopecia veto forecloses it.** Surfaced only so the user can re-weight the veto with her oncologist if she chooses.*

#### Evidence base

HERTHENA-Lung01 ([PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559); single-arm phase 2; n=225; EGFR-mutant NSCLC after EGFR-TKI): ORR 29.8% (95% CI 23.9–36.2). Effect size is comparable to ranks 1 and 2.

#### Likelihood of desired effect

The mechanism (HER3-targeted antibody-drug conjugate) is mechanism-agnostic relative to the patient's MET-amp resistance — it targets HER3 expression rather than the resistance pathway. Effect is real but mechanism-fit is weaker than rank 1.

#### Toxicity profile

- ILD grade 3+ ~5%
- **Alopecia** — triggers user veto
- Thrombocytopenia
- IV q3w

#### Counter-productive mechanisms / dissent

Only the risktaker advanced this rec. Advocate did not advance it because the alopecia veto was stated. No formal veto was issued because the dossier surfaced the rec only after ranks 1 and 2 were established.

#### Practical considerations

- 5.6 mg/kg IV q3w
- Not currently NCCN-endorsed as standard for this setting
- ILD risk requires baseline pulmonary function + monitoring

#### Why this rank

Below ranks 1 and 2 because the alopecia veto is unconditional. Surfaced for transparency so the user can ask her oncologist whether re-weighting the alopecia veto changes the calculus — that's a conversation, not a recommendation.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Patritumab deruxtecan — HERTHENA-Lung01 (single-arm phase 2, n=225 post-EGFR-TKI) | ORR 29.8% (95% CI 23.9–36.2) | ILD G3+ ~5%; alopecia; thrombocytopenia | [PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559) |

## Classes examined but not ranked

- **Osimertinib re-challenge / dose escalation:** T790M absent — gatekeeper-mutation pathway is not the resistance mechanism, so re-challenge has no biomarker rationale.
- **Platinum + pemetrexed chemotherapy:** SAFFRON's comparator arm; surfaces only as the off-trial fallback if the trial pathway is unreachable. Not advanced as a primary option in the dossier.
- **Immunotherapy (anti-PD-1) for EGFR-mutant NSCLC:** historically negative as monotherapy in EGFR-mutant disease; PD-L1 TPS 10% does not change that. Not advanced.
- **MET-targeted monotherapy (capmatinib, tepotinib):** indicated for METex14, not amplification; biomarker mismatch.

## Ranked prioritization

| Rank | Status | Intervention | Endorsed by | Dissent | Veto | Likelihood | Toxicity burden | Why this rank |
|---|---|---|---|---|---|---|---|---|
| 1 | recommended | Savolitinib + osimertinib (preferably on SAFFRON / SACHI) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span> | — | — | High mechanism fit; ORR ~30% replicated | LFT, edema, fatigue | Mechanism + preferences both clean |
| 2 | considered_with_caveats | Amivantamab + lazertinib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span> | <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span> | <span class="persona persona-conservative">conservative</span> | ORR 36% in subset | Severe neuropathy, IV burden | Active veto + modality conflict |
| 3 | considered_with_caveats | Patritumab deruxtecan (HER3-DXd) | <span class="persona persona-risktaker">risktaker</span> | — | — | ORR 29.8% post-TKI | ILD ~5%; alopecia | Triggers alopecia veto outright |

## Caveats

- **Evidence base is modest in size.** Rank 1's anchor is a 69-patient TATTON expansion plus a recruiting phase 3; rank 2's anchor is a 162-patient single-arm; rank 3's anchor is a 225-patient single-arm. None has a randomized comparator in the patient's exact biomarker stratum yet.
- **No OS data** for any of the three ranked interventions in the post-osimertinib MET-amp setting specifically. Effect estimates are ORR-based; durability is the open question for all three.
- **Patient-context veto sensitivity.** Two of three rec-ranks turn on user vetoes (neuropathy, alopecia) tied to the patient's working-artist context. The board treated these as load-bearing, not disposable.
- **What would change the ranking:**
    - SAFFRON OS readout, if it confirms a meaningful PFS / OS benefit, would tighten rank 1's confidence and may push it from "preferred" to "guideline-fit."
    - A MET-amp-stratified amivantamab + lazertinib randomized readout that mitigates neuropathy (e.g. with the SC formulation) could narrow the rank-1 / rank-2 gap, but the modality preference would still anchor rank 1 above it.
    - User re-weighting of the alopecia veto would move patritumab deruxtecan from rank 3 (`considered_with_caveats`) to rank 2 if the user accepted the alopecia tradeoff.
    - Failure of the rank-1 option (intolerance, progression, slot unavailability) is the explicit precondition for revisiting rank 2 with the conservative's veto on the table.
- **Re-scoping caveat.** If the patient's clinical state changes (e.g. CNS progression, declining ECOG), or if the modality preference relaxes, the ranking shifts. The current page assumes the stated profile and preferences hold.

## Sources

**PubMed (PMID):**

- [32679432](https://pubmed.ncbi.nlm.nih.gov/32679432) — Sequist et al., TATTON expansion, *Lancet Oncol* 2020
- [36720074](https://pubmed.ncbi.nlm.nih.gov/36720074) — Cho et al., CHRYSALIS-2, *JCO* 2023
- [37563559](https://pubmed.ncbi.nlm.nih.gov/37563559) — Yu et al., HERTHENA-Lung01, *JCO* 2023

**ClinicalTrials.gov (NCT):**

- [NCT05261399](https://clinicaltrials.gov/study/NCT05261399) — SAFFRON (savolitinib + osimertinib phase 3)
- [NCT04077463](https://clinicaltrials.gov/study/NCT04077463) — CHRYSALIS-2 (amivantamab + lazertinib)
- [NCT04619004](https://clinicaltrials.gov/study/NCT04619004) — HERTHENA-Lung01 (patritumab deruxtecan)
- [NCT02143466](https://clinicaltrials.gov/study/NCT02143466) — TATTON

## Transparency artifacts

- [Trial table](trials.md) — 4 trials in the dossier
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Demo case authored May 2026 with synthetic data for smoke-testing the pipeline. No real patient information is represented. Re-rendered to shieldbreak-flavored layout in the same month after Libby's PI authoring contract was updated to mirror `pirl-unc/io-shieldbreak`.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The recommendations on this page have **not** been
    reviewed by a clinician treating this patient. Do not act on this page
    without consulting a qualified oncologist. This is a synthetic
    demonstration case; the patient profile is fictional.

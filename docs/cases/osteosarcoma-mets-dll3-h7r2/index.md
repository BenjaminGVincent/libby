<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](osteosarcoma-mets-dll3-h7r2-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary
- [Master manuscripts table (PDF)](osteosarcoma-mets-dll3-h7r2-manuscripts.pdf) — every paper considered — n, effect, variance, toxicities
- [Self-contained HTML](osteosarcoma-mets-dll3-h7r2-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->

## Research question

In metastatic osteosarcoma after first-line MAP, what interventions could target DLL3 expression — and what's the next move if the DLL3 protein test comes back negative or below threshold?

## Patient profile (scrubbed)

- **Primary site / histology:** bone — osteosarcoma
- **Stage:** IV (metastatic)
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 18-29 (typical osteosarcoma demographics; not user-supplied)
- **Sex:** unknown
- **Biomarkers:** **DLL3 — RNA only (`confirmation_status: rna_only`); IHC SP347 status unknown.** Decision-relevant resolution: ≥1% (preferably ≥25%) by IHC for DLL3-directed clinical trials.
- **Prior therapy (assumed):** MAP frontline; response not provided.

## Preferences

- **Efficacy/toxicity weight:** 0.85 (strong efficacy lean)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "accepts high-risk high-reward options"
- **Trials preferred:** yes

## Scope summary

7 trials, 5 clinical-evidence rows, 4 preclinical rows. Three ranked interventions per scenario branch plus one shared workup step. Board agreement: full consensus (all five personas) on the DLL3 IHC workup, regorafenib, and cabozantinib; one persistent dissent (critic) on the lead trial in the IHC-positive branch; advocate split on rank ordering when the trial is foreclosed.

## Cross-cutting caveat (read first)

**The DLL3 RNA expression in user input does not establish membrane DLL3 protein, and every DLL3-directed therapy in current clinical use gates on IHC.** This is the single load-bearing finding of the case: the rest of the page bifurcates around the IHC result.

- DLL3 protein detection by IHC SP347 is the standard gating biomarker. NCT06788938 enforces ≥25% (stage 1) or ≥1% (stage 2) by IHC for enrollment.
- The IHC test is non-toxic, takes 1–3 weeks, costs almost nothing relative to a treatment cycle, and can be run on archival tissue.
- All five board personas converged on the IHC workup as rank 1 without dissent, regardless of subsequent treatment plan.
- A negative IHC forecloses the DLL3-directed pathway entirely. Plan for both branches in advance of the result.

## Intervention grouping

- **DLL3-directed BiTEs (Path A only):** tarlatamab via NCT06788938. Cross-tumor efficacy anchor: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) and DeLLphi-304 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)).
- **Multi-kinase TKIs (scenario-agnostic):** regorafenib ([PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172), [PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937)) and cabozantinib ([PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813)).
- **Mechanism-agnostic trial enrollment (Path B residual):** non-DLL3 osteosarcoma basket / academic sarcoma referral.

## Top interventions

### Shared rank 1. DLL3 IHC (SP347) on tumor — diagnostic gate

*Non-toxic. Resolves which scenario applies. Required for trial NCT06788938 regardless of branch.*

#### Evidence base

NCT06788938 enforces DLL3 IHC ≥25% (stage 1) or ≥1% (stage 2) for enrollment. The basket-trial design exists precisely because DLL3 RNA expression is not a sufficient enrollment biomarker. Mechanistic anchor: every DLL3-directed therapy in clinical development requires protein-level confirmation.

#### Likelihood of desired effect

The test resolves the binary that drives every downstream decision. Under both scenarios it remains rank 1.

#### Toxicity profile

- None. Lab test on tissue.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

Archival or fresh tumor; SP347 antibody assay availability at the treating institution should be confirmed. 1–3 week turnaround.

#### Why this rank

The IHC is the precondition for every DLL3-directed action. The board treated it as the gate, not as a therapy.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| DLL3 IHC SP347 (assay) | Gates enrollment in DLL3-directed therapy trials | None — diagnostic | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |

---

### Rank 1 (Path A — if DLL3 IHC ≥1%, preferably ≥25%). Tarlatamab via NCT06788938

*High-efficacy bispecific T-cell engager; preferences point exactly here; one persistent dissent on cross-tumor translation.*

#### Evidence base

NCT06788938 (single-arm phase 2 basket, Simon two-stage, n=29 planned) is the trial enrolling osteosarcoma at biomarker-positive resolution. The mechanistic case rests on cross-tumor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218); ORR 40%, n=220 SCLC) and the confirmatory DeLLphi-304 phase 3 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646); OS HR 0.60, 95% CI 0.47–0.77, median OS 13.6 vs 8.3 mo). No published osteosarcoma data with tarlatamab exist.

#### Likelihood of desired effect

In the IHC-positive scenario, mechanism-fit is concordant. Whether SCLC's clinical effect transfers to osteosarcoma is the central scientific question this trial enrollment would answer. The user's preferences (efficacy lean 0.85, accepts high-risk-high-reward, prefers trials) point exactly here.

#### Toxicity profile

- CRS in ~50% (mostly grade 1–2; grade ≥3 ~1% in SCLC)
- ICANS-like neurologic events ~10%
- Inpatient cycle-1 step-up dosing required for CRS mitigation
- Step-up dosing: 1 mg D1, 10 mg D8/D15, then 10 mg q2w (28-day cycles)

User has no toxicity vetoes; CRS and inpatient cycle-1 chair time are not flagged.

#### Counter-productive mechanisms / dissent

**The critic's dissent on this rec persists.** No published osteosarcoma data with tarlatamab; cross-tumor translation from SCLC is unproven; the trial's basket design exists to *test* this premise. The conservative's earlier toxicity veto (issued under the IHC-unconfirmed scenario) lifts on biomarker confirmation — its own rationale specified the veto was contingent on IHC. Concensusite's qualified-on-guideline-fit position upgrades to endorsement when the trial-enrollment principle is in play.

#### Practical considerations

- Trial open at NCT06788938 (recruiting). Slot availability at treating site should be confirmed.
- Trial enrollment is NCCN cat-1 for relapsed osteosarcoma irrespective of mechanism.
- Inpatient cycle-1 monitoring required.
- Off-guideline for osteosarcoma per indication; the trial provides the regulatory pathway.

#### Why this rank

Strong preference fit + the only DLL3-directed option on the table, conditional on biomarker confirmation. Ranks above regorafenib in this scenario *because* the user explicitly prefers trials; without that preference, the agreement_score gap (+0.6 vs +0.8) would invert the order.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma included), n=29 planned | ORR endpoint at 18 mo (primary); no osteosarcoma data yet | Per SCLC mechanism: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism evidence), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~50% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo arm — favorable vs comparator | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

---

### Rank 2 (Path A) / Rank 1 (Path B). Regorafenib

*Universal-consensus backbone in both scenarios; ranks first in Path B because the trial pathway is foreclosed.*

#### Evidence base

Two-RCT convergence in 2L+ metastatic osteosarcoma: SARC024 ([PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172); n=42, mPFS 3.6 vs 1.7 mo, HR 0.42 95% CI 0.21–0.85, p=0.017) and the REGOBONE osteosarcoma cohort ([PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937); n=38, 65% non-progression at 8 weeks, mPFS 16.4 vs 4.1 wk). Both placebo-controlled with crossover.

#### Likelihood of desired effect

Strongest 2L+ osteosarcoma evidence base in the dossier. Effect is real but not durable — neither RCT showed an OS benefit (crossover diluted). PFS gains are weeks-to-months.

#### Toxicity profile

- Hand-foot reaction (predominant)
- Hypertension
- Fatigue
- Mucositis, transaminitis
- G3+ AE rate ~70% across the two RCTs; manageable with dose reduction; no treatment-related deaths

User has no toxicity vetoes; oral all-PO regimen aligns with the no-modality-constraints preference.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous in both scenarios. The advocate's earlier rank-disagreement (placing tarlatamab above regorafenib in Path A) is honored as a rank-issue, not a drug-issue: when the trial pathway is closed (Path B), no persona disputes that regorafenib is rank 1.

#### Practical considerations

- 160 mg PO daily, 3 weeks on / 1 week off
- NCCN-recommended for relapsed/refractory osteosarcoma
- Off-trial; no enrollment friction
- Outpatient

#### Why this rank

In Path A, ranks below tarlatamab because the user explicitly prefers trials and the trial is reachable. In Path B, the trial pathway is closed and regorafenib's two-RCT evidence base is the strongest remaining option.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Regorafenib — SARC024 (RCT, n=42 osteosarcoma) | mPFS 3.6 vs 1.7 mo (HR 0.42, p=0.017) | G3+ ~70%: HFS, HTN, fatigue, mucositis | [PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172) |
| Regorafenib — REGOBONE osteosarcoma cohort (RCT, n=38) | 65% non-progression at 8 wk; mPFS 16.4 vs 4.1 wk | G3+ ~76%: HFS, fatigue, HTN, transaminitis | [PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937) |

---

### Rank 3 (Path A) / Rank 2 (Path B). Cabozantinib

*NCCN alternative; CABONE phase-2 evidence; sequencing option after or instead of regorafenib.*

#### Evidence base

CABONE ([PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813); single-arm phase 2, French Sarcoma Group; osteosarcoma cohort n=42): ORR 11.9% (95% CI 4.0–25.6); 6-mo non-progression 33.3%; mPFS 6.2 mo. Pre-specified osteosarcoma cohort within a multicentre trial.

#### Likelihood of desired effect

Single-arm phase-2; effect smaller than regorafenib's PFS signal but in the same direction. Reasonable backup if regorafenib is contraindicated, intolerable, or prior.

#### Toxicity profile

- Hypertension
- Hand-foot reaction
- Hypophosphatemia
- Transaminitis
- Thromboembolism in 7% (notable)
- G3+ AEs 68%

VTE prophylaxis warranted in patients with metastatic disease.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous in both scenarios. No persona disputed cabozantinib as a sequencing option.

#### Practical considerations

- 60 mg PO daily
- NCCN-listed alternative for relapsed bone sarcoma
- Outpatient
- AOST2032 ([NCT05691478](https://clinicaltrials.gov/study/NCT05691478)) is testing cabozantinib + MAP in frontline — relevant context but not a 2L+ option for this case

#### Why this rank

Phase-2 single-arm vs regorafenib's two-RCT base — that's the rank gap. Both are universally endorsed; cabozantinib is the sequencing alternative when regorafenib is exhausted, intolerable, or contraindicated.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Cabozantinib — CABONE osteosarcoma cohort (single-arm phase 2, n=42) | ORR 11.9% (95% CI 4.0–25.6); 6-mo non-progression 33.3%; mPFS 6.2 mo | G3+ 68%: HTN, HFS, hypophosphatemia; VTE 7% | [PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813) |
| Cabozantinib + MAP — AOST2032 (frontline phase 2/3, recruiting; context only) | Outcome pending | Per cabozantinib + MAP combined toxicity profile | [NCT05691478](https://clinicaltrials.gov/study/NCT05691478) |

---

### Rank 3 (Path B). Non-DLL3 trial search (mechanism-agnostic)

*Honors the user's prefers_trials preference when the DLL3 pathway is closed; considered with caveats.*

#### Evidence base

None specific to this case. Surfaced because the user explicitly prefers trial enrollment. Candidate categories: osteosarcoma-specific basket trials, immunotherapy-naive cohorts, or novel-target sarcoma trials at academic sarcoma centers.

#### Likelihood of desired effect

Variable — trial-by-trial. The user's prefers_trials preference applies regardless of DLL3 result; in Path B this is the residual way to honor it.

#### Toxicity profile

Wide variance by trial. Cannot summarize without specific trial selection.

#### Counter-productive mechanisms / dissent

Endorsed only by the risktaker and the advocate. Not vetoed; the dossier did not surface a specific osteosarcoma-relevant trial to anchor this rec, so the conservative and critic withheld endorsement.

#### Practical considerations

- Referral to academic sarcoma center for fresh trial search at decision time
- NCCN cat-1 to enroll relapsed osteosarcoma in trials regardless of mechanism

#### Why this rank

Below regorafenib and cabozantinib because the dossier did not anchor a specific trial. Preserved on the page so the user's stated preference doesn't disappear when the DLL3 path closes.

## Classes examined but not ranked

- **Anti-PD-1 / PD-L1 monotherapy in osteosarcoma:** historically negative (SARC028 and successors). No persona surfaced this as a candidate.
- **HER2-, GD2-, B7-H3-directed therapies:** not in the dossier for this case; no biomarker selection performed at intake.
- **MTP-PE (mifamurtide):** historical adjuvant data in newly diagnosed disease; not a 2L+ option.

## Ranked prioritization

| Rank | Status | Intervention | Endorsed by | Dissent | Veto | Likelihood | Toxicity burden | Why this rank |
|---|---|---|---|---|---|---|---|---|
| 1 (shared) | recommended | DLL3 IHC (SP347) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Resolves branch | None | Gates every downstream decision |
| 1 (Path A) | recommended | [Path A] Tarlatamab via NCT06788938 | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> | <span class="persona persona-critic">critic</span> | — | Mechanism unproven cross-tumor | CRS, ICANS, C1 inpatient | Only DLL3-directed option; preference fit |
| 2 (Path A) | recommended | [Path A] Regorafenib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Real PFS gain, no OS benefit | HFS, HTN, fatigue (G3+ ~70%) | Two-RCT backbone; outranked by trial preference |
| 3 (Path A) | recommended | [Path A] Cabozantinib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Smaller phase-2 effect | HTN, HFS, VTE 7% (G3+ ~68%) | Sequencing alternative |
| 1 (Path B) | recommended | [Path B] Regorafenib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Real PFS gain | Same as above | Strongest evidence with trial closed |
| 2 (Path B) | recommended | [Path B] Cabozantinib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Smaller phase-2 effect | Same as above | Sequencing alternative |
| 3 (Path B) | considered_with_caveats | [Path B] Non-DLL3 trial search | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> | — | — | Variable by trial | Variable | Honors prefers_trials with DLL3 closed |

## Caveats

- **Evidence base is small for the lead trial.** NCT06788938 plans n=29 with no published efficacy data yet. The mechanistic basis is the cross-tumor SCLC evidence (DeLLphi-301 / 304), which is robust in SCLC but unproven in any other tumor type.
- **Single-arm phase-2 is the upper bound for cabozantinib in osteosarcoma** (CABONE). No randomized controlled comparison with regorafenib exists.
- **No OS benefit demonstrated for either TKI** (regorafenib's two RCTs both used crossover designs; cabozantinib was single-arm). The effect lives in PFS, not survival.
- **Biomarker dependency:** rankings assume a binary IHC result. Indeterminate / weak-positive (1–24%) edge cases are not explicitly addressed; in practice, NCT06788938's stage-2 ≥1% threshold may permit enrollment.
- **What would change the ranking:**
    - A negative DLL3 IHC moves Path A to non-applicable; Path B becomes the only ranking.
    - A positive DLL3 IHC plus a head-to-head osteosarcoma cohort within the basket trial reading out would move tarlatamab from "mechanism unproven cross-tumor" to "evidence-supported" and tighten its rank-1 confidence.
    - A user toxicity veto on CRS / inpatient cycle-1 monitoring would foreclose tarlatamab even with positive IHC — the conservative's veto was contingent on IHC, but a user-level veto would override the trial pathway entirely.
    - Slot unavailability at NCT06788938 sites would push Path A toward regorafenib as the de facto rank 1 in that scenario.
- **Re-scoping caveat:** if the user's preference shifts away from trials (toward proven options) or toward minimizing inpatient time, regorafenib becomes rank 1 in both scenarios.

## Sources

**PubMed (PMID):**

- [30477937](https://pubmed.ncbi.nlm.nih.gov/30477937) — Duffaud et al., REGOBONE osteosarcoma cohort, *Lancet Oncol* 2019
- [31013172](https://pubmed.ncbi.nlm.nih.gov/31013172) — Davis et al., SARC024, *JCO* 2019
- [32078813](https://pubmed.ncbi.nlm.nih.gov/32078813) — Italiano et al., CABONE, *Lancet Oncol* 2020
- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301, *NEJM* 2023
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304, *NEJM* 2025
- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — DLL3 IHC reference (cited in workup row)

**ClinicalTrials.gov (NCT):**

- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — DLL3-IHC-selected basket including osteosarcoma (tarlatamab)
- [NCT05691478](https://clinicaltrials.gov/study/NCT05691478) — AOST2032 frontline osteosarcoma (cabozantinib + MAP); context only
- [NCT05060016](https://clinicaltrials.gov/study/NCT05060016) — DeLLphi-301 (cross-tumor mechanism)
- [NCT05740566](https://clinicaltrials.gov/study/NCT05740566) — DeLLphi-304 (cross-tumor confirmatory)
- [NCT02243605](https://clinicaltrials.gov/study/NCT02243605) — CABONE
- [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) — SARC024
- [NCT02389244](https://clinicaltrials.gov/study/NCT02389244) — REGOBONE

## Transparency artifacts

- [Trial table](trials.md) — 7 rows, all 25 columns
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows (grouped by intervention)
- [Manuscripts considered](manuscripts.md) — flat master table: n, effect, variance, structured toxicities
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with scenario branches
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs supplied: targetable feature ("DLL3 RNA expression"), clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts high-risk high-reward options"). Re-rendered to shieldbreak-flavored layout in the same month after Libby's PI authoring contract was updated to mirror `pirl-unc/io-shieldbreak`.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.

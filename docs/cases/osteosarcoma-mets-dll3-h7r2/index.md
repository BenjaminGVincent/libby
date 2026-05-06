<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](osteosarcoma-mets-dll3-h7r2-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary
- [Target validation paths](osteosarcoma-mets-dll3-h7r2-target-validation.pdf) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Access guide (PDF)](osteosarcoma-mets-dll3-h7r2-accessibility.pdf) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines
- [Access guide (web)](accessibility.md) — same access guide in an in-browser sortable table
- [Master manuscripts table (PDF)](osteosarcoma-mets-dll3-h7r2-manuscripts.pdf) — every paper considered — n, effect, variance, toxicities
- [Master manuscripts table (web)](manuscripts.md) — same inventory in a sortable in-browser table
- [Self-contained HTML](osteosarcoma-mets-dll3-h7r2-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->

## Research question

In metastatic osteosarcoma after first-line MAP, what interventions can target DLL3, gated on IHC confirmation?

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

<!-- libby:target-validation:begin -->

## Target validation paths

DLL3 IHC (clone SP347) is the test the case hinges on. A positive result at the trial threshold opens the only within-scope DLL3-directed therapy on the page (tarlatamab via NCT06788938). A negative result forecloses the entire DLL3-directed pathway — every BiTE, ADC, radioligand, and cell-therapy program in the dossier gates on protein-level confirmation, not transcript expression.

### DLL3 RNA expression

Before any therapy decision: DLL3 IHC SP347 on archival FFPE, ≥1% (preferably ≥25%) per NCT06788938's enrollment threshold. Turnaround is one to three weeks; cost is trivial relative to a treatment cycle. The first practical step is confirming SP347 assay availability at the treating institution — not every reference lab carries the Roche Tissue Diagnostics clone used in the tarlatamab development program.

Two refinements sit one tier down. Spatial heterogeneity is a known confounder in solid-tumor DLL3 (Zhang 2023): if multiple tumor blocks are available, IHC on a metastatic site as well as the primary refines confidence in whether the gating result generalizes. Neuroendocrine context (ASCL1 / NEUROD1 / chromogranin / synaptophysin / INSM1 panel) is research-grade for an osteosarcoma — DLL3 is normally a Notch-pathway target on neuroendocrine lineage, and an unexpectedly positive DLL3 IHC in a non-NEC tumor is worth contextualizing before the trial enrollment paperwork.

Germline TP53 sequencing (Li-Fraumeni panel) is a separate kind of finding — it does not affect tarlatamab eligibility, but late-teens / twenties osteosarcoma carries a meaningful prior probability for germline TP53. A positive result reshapes radiation-sensitivity considerations, screening for synchronous tumors, and family screening. Discuss with a genetic counselor before testing.

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

21 trials surfaced (3 included as primary efficacy rows for tarlatamab; 18 cross-tumor / pipeline-context rows spanning seven DLL3-targeting modality classes), 3 clinical-evidence rows (2 included + 1 considered & excluded), 5 preclinical rows (4 included + 1 considered & excluded). Three ranked rows: a workup gate at rank 1, a biomarker-conditional therapeutic option at rank 2 (tarlatamab via NCT06788938), and a tentative second pathway at rank 3 (SHR-4849 via NCT07174583, *considered with caveats* pending sponsor confirmation of osteosarcoma eligibility). The board reached full consensus on the workup. One persistent dissent (critic) sits on the conditional rank-2 trial. Two dissents (critic, conservative) sit on the tentative rank-3 path. The case is scoped to drugs that act on the user's stated targetable feature (DLL3); standard 2L+ care for the indication is out of scope and is not enumerated.

## Cross-cutting caveat (read first)

**The DLL3 RNA expression in user input does not establish membrane DLL3 protein. The DLL3 IHC SP347 test (rank 1) gates whether tarlatamab via NCT06788938 (rank 2) is on the table at all.** Every DLL3-directed therapy in current clinical use requires IHC protein-level confirmation. RNA expression is necessary but not sufficient.

- **Rank 2 (tarlatamab)** is conditional on DLL3 IHC ≥1% (preferably ≥25%). It is the only therapeutic option within scope of this case's targetable feature.
- **If IHC is negative:** rank 2 is foreclosed and this case has no within-scope recommendations. Libby's ranking is targetable-feature-scoped; standard 2L+ care for the indication is a separate conversation with the treating team and is not enumerated on this page.
- **Workup logistics:** SP347 IHC is non-toxic, runs on archival tissue (no fresh biopsy required), takes one to three weeks, and costs almost nothing relative to a treatment cycle. Confirm assay availability at the treating institution.
- **Pipeline visibility.** The dossier surfaces 18 additional DLL3-targeting investigational drugs across seven modality classes (BiTE, trispecific, CD47-bispecific, ADC, radioligand, radioimmunotherapy, CAR-T, CAR-NK). They are informational only — patient cannot enroll (SCLC/NEC-scoped) — but they shape how the board reasons about the BiTE class (tarlatamab vs alternatives), the post-Rova-T ADC era, and what a negative IHC result actually forecloses (it forecloses *all* DLL3-directed therapy, not just tarlatamab).

## Intervention grouping

- **DLL3 × CD3 BiTEs (biomarker-conditional, actionable via NCT06788938):** tarlatamab. Anchor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) + DeLLphi-304 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)).
- **Other DLL3 × CD3 / CD137 BiTEs and trispecifics (pipeline context, SCLC/NEC-scoped):** obrixtamig (BI 764532, Boehringer Ingelheim DAREON phase 3), gocatamig (MK-6070 / HPN328 / DS3280, Harpoon→Merck), alveltamig (ZG006, Zelgen phase 3), clesitamig (RO7616789, Roche), QLS31904.
- **DLL3 × CD47 bispecifics (non-T-cell-engager class):** peluntamig (PT217, Phanes Therapeutics).
- **DLL3 ADCs (TOP1-inhibitor or DXd payload, post-Rova-T era):** zocilurtatug pelitecan (ZL-1310, Zai Lab phase 3), SHR-4849 / IDE849 (IDEAYA / Hengrui), IBI3009 (Innovent), FZ-AD005 (Shanghai Fudan-Zhangjiang).
- **DLL3 radiopharmaceuticals (radiation mechanism, antigen-loss-resistant):** ²²⁵Ac-ABD147 (Abdera), ¹⁷⁷Lu-DTPA-SC16.56 (Memorial Sloan Kettering), ²²⁵Ac-ETN029 (Novartis).
- **DLL3 cell therapies:** LB2102 autologous CAR-T (Legend Biotech), DLL3-CAR-NK cells (Tianjin academic). AMG 119 was Amgen's first-generation CAR-T program — currently suspended.
- **Discontinued DLL3 ADCs (mechanism context for current ADC entrants):** rovalpituzumab tesirine / Rova-T (TAHOE phase-3 failure, AbbVie discontinued), SC-002 (Stemcentrx, terminated in phase 1).

## Top interventions

### Rank 1. DLL3 IHC (SP347) on tumor — diagnostic gate

*Non-toxic. Resolves whether the DLL3-directed pathway is open. Required for trial NCT06788938.*

#### Evidence base

NCT06788938 enforces DLL3 IHC ≥25% (stage 1) or ≥1% (stage 2) for enrollment. The basket-trial design uses IHC for a concrete reason: DLL3 RNA expression does not predict surface protein density at the level the BiTE needs. Mechanistic anchor: every DLL3-directed therapy in clinical development gates on protein-level confirmation, not transcript.

#### Likelihood of desired effect

The test resolves whether rank 2 is reachable. Non-toxic and cheap regardless of result.

#### Toxicity profile

- None. Lab test on tissue.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

Archival or fresh tumor works. Confirm SP347 antibody assay availability at the treating institution. One to three week turnaround. The IHC is the precondition for any DLL3-directed action regardless of which therapy the patient ultimately pursues.

#### Why this rank

The IHC is the precondition for rank 2. The board treated it as the gate, not as a therapy.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| DLL3 IHC SP347 (assay) | Gates enrollment in DLL3-directed therapy trials | None — diagnostic | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |

---

### Rank 2. Tarlatamab via NCT06788938

*Conditional on `dll3_ihc:positive`. Foreclosed if test is negative.*

*Bispecific T-cell engager with strong cross-tumor efficacy data in SCLC. The user's stated preferences fit this option when the trial is reachable. One persistent dissent on cross-tumor translation.*

#### Evidence base

NCT06788938 (single-arm phase 2 basket, Simon two-stage, n=29 planned) is the trial enrolling osteosarcoma at biomarker-positive resolution. The mechanistic case rests on cross-tumor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218); ORR 40%, n=220 SCLC) and the confirmatory DeLLphi-304 phase 3 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646); OS HR 0.60, 95% CI 0.47–0.77, median OS 13.6 vs 8.3 mo). No published osteosarcoma data with tarlatamab exist.

#### Likelihood of desired effect

Assuming positive IHC, mechanism-fit is concordant. Whether SCLC's clinical effect transfers to osteosarcoma is the open question this trial enrollment would answer. The user's preferences (efficacy lean 0.85, accepts high-risk-high-reward, prefers trials) fit this option. **A negative IHC forecloses this rec entirely.**

#### Toxicity profile

- CRS in ~50% (mostly grade 1–2; grade ≥3 ~1% in SCLC)
- ICANS-like neurologic events ~10%
- Inpatient cycle-1 step-up dosing required for CRS mitigation
- Step-up dosing: 1 mg D1, 10 mg D8/D15, then 10 mg q2w (28-day cycles)

User has no toxicity vetoes; CRS and inpatient cycle-1 chair time are not flagged.

#### Counter-productive mechanisms / dissent

**The critic's dissent persists.** No published osteosarcoma data with tarlatamab. Cross-tumor translation from SCLC is unproven, and the trial's basket design exists to test that premise. The conservative's earlier toxicity veto (issued under the IHC-unconfirmed scenario) lifts on biomarker confirmation; its own rationale specified the veto was contingent on IHC. Concensusite's qualified-on-guideline-fit position upgrades to endorsement when the trial-enrollment principle is the relevant frame.

#### Practical considerations

- Trial open at NCT06788938 (recruiting). Confirm slot availability at the treating site.
- Trial enrollment is NCCN cat-1 for relapsed osteosarcoma regardless of mechanism.
- Inpatient cycle-1 monitoring required.
- Off-guideline for osteosarcoma per indication; the trial provides the regulatory pathway.

#### Why this rank

The only DLL3-directed therapeutic option on the table, conditional on biomarker confirmation. Foreclosed entirely if IHC is negative.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma included), n=29 planned | ORR endpoint at 18 mo (primary); no osteosarcoma data yet | Per SCLC mechanism: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism evidence), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~50% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo arm — favorable vs comparator | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

---

### Rank 3. SHR-4849 / IDE849 via NCT07174583 — IDEAYA pan-tumor DLL3 basket

*Status: **considered with caveats**. Conditional on `dll3_ihc:positive` AND IDEAYA confirming osteosarcoma is on the basket eligibility list. Two dissents (critic, conservative).*

*Mechanism-distinct second DLL3 pathway — TOP1-inhibitor ADC payload (post-Rova-T era). Relevant if the BiTE path is foreclosed or fails. No published clinical data yet.*

#### Evidence base

NCT07174583 is IDEAYA Biosciences' phase 1/2 dose-escalation + expansion trial of SHR-4849 / IDE849 (DLL3-targeted ADC, TOP1-inhibitor payload, originated by Jiangsu Hengrui), monotherapy and in combination with durvalumab or IDE161. Eligibility names "DLL3-expressing tumors" without an explicit SCLC/NEC restriction — pan-tumor in principle. The osteosarcoma fit is **not yet confirmed by the sponsor**: the trial wording suggests it should be in scope, but the published eligibility text does not state it outright. No clinical data for SHR-4849 has been published yet (first-in-class signal pending).

#### Likelihood of desired effect

Speculative. TOP1-inhibitor ADC precedent (T-DXd, sacituzumab govitecan, Dato-DXd) suggests the payload class can produce durable response signals across solid tumors when the surface antigen is sufficiently expressed. DLL3-specific efficacy is the open question. Assuming positive IHC AND osteosarcoma is on the basket, this is a mechanism-class diversification away from BiTE-only DLL3 targeting — a hedge against tarlatamab-specific failure modes (CRS intolerance, ICANS, antigen-loss escape from CD3 engagement).

#### Toxicity profile

- No published clinical AE rates for SHR-4849 yet
- Expected per TOP1-inhibitor ADC class: cytopenias (neutropenia, thrombocytopenia), GI (nausea, vomiting, diarrhea), fatigue
- ILD/pneumonitis is a class signal worth monitoring (DXd-class ADCs carry an explicit ILD risk; SHR-4849's payload is a TOP1 inhibitor of similar mechanism)
- Cycle-1 monitoring requirements unknown until phase 1 data publishes

User has no toxicity vetoes; cytopenias and ILD signal are not pre-flagged.

#### Counter-productive mechanisms / dissent

**The critic dissents on evidence base** — no published clinical data for SHR-4849 means the row stands on payload-class precedent rather than on the molecule itself. **The conservative dissents on osteosarcoma eligibility uncertainty** — the basket may in practice enroll only SCLC/NEC, with the broader "DLL3-expressing tumors" wording being aspirational. The risktaker and advocate endorse on the basket-trial principle plus the second-mechanism-class advantage. The TAHOE/PBD-payload class shadow (Rova-T failure) does not directly apply to a TOP1-inhibitor payload, but informs the toxicity-budget framing the board uses for any DLL3 ADC in 2026.

#### Practical considerations

- Trial open at NCT07174583 (recruiting). **First action: contact IDEAYA medical affairs to confirm osteosarcoma eligibility on the basket — do not pursue this rank without that confirmation.**
- Concurrent enrollment with NCT06788938 (rank 2) is unlikely to be permitted simultaneously; the user (or treating team) will need to choose.
- Off-guideline; investigational. Not on any NCCN / ESMO recommendation.
- IDE849's parent compound (SHR-4849) was developed by Jiangsu Hengrui in China; IDEAYA holds the US development license.

#### Why this rank

Lower than rank 2 because (a) eligibility for osteosarcoma is unconfirmed and (b) no published clinical data for SHR-4849 yet exists. Higher than not-ranking-it because the basket eligibility is plausible per the trial wording and the payload class has better odds in 2026 than the BiTE class shadow that drove the conservative's earlier veto. A two-pathway DLL3 plan (BiTE + ADC) is preferable to a single-pathway plan if both can be reached.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SHR-4849 / IDE849 — NCT07174583 IDEAYA pan-tumor DLL3-expressing basket (eligibility for osteosarcoma pending sponsor confirmation) | DLT, ORR primary; no published efficacy data yet | Class effects expected; no published AE table yet | [NCT07174583](https://clinicaltrials.gov/study/NCT07174583) |

## Classes examined but not ranked

- **DLL3-directed ADCs (rovalpituzumab tesirine / Rova-T):** mechanistically a DLL3-targeting modality, but not procurable. AbbVie withdrew Rova-T after the TAHOE phase-3 SCLC trial showed worse OS than topotecan ([PMID 33002438](https://pubmed.ncbi.nlm.nih.gov/33002438)). Listed for mechanism context. Not actionable.
- **Other DLL3-targeting investigational drugs (SCLC/NEC-only enrollment):** obrixtamig, gocatamig, alveltamig, clesitamig, peluntamig, QLS31904, zocilurtatug pelitecan, IBI3009, FZ-AD005, ²²⁵Ac-ABD147, ¹⁷⁷Lu-DTPA-SC16.56, ²²⁵Ac-ETN029, LB2102, AMG 119, DLL3-CAR-NK. All are tagged `cross_tumor_extrapolation` on `trials.md` — patient is not enrollable per published eligibility. Visible in the dossier as evidence-base context for the BiTE / ADC / radioligand / cell-therapy DLL3 classes; not actionable for this case absent a basket trial that explicitly accepts the patient's tumor type.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>DLL3 IHC (SP347) on tumor — diagnostic gate</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Diagnostic certainty — resolves whether the DLL3-directed pathway is reachable; required by NCT06788938 (≥25% stage 1, ≥1% stage 2).</td>
          <td>Low (none — diagnostic test on archival tissue)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic)</span></td>
          <td><strong>Non-toxic precondition that gates rank 2 entirely; run regardless of which therapy is ultimately chosen.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>tarlatamab via NCT06788938 (UCCC-01 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td>
          <td>Cross-tumor extrapolation: SCLC OS HR 0.60 (DeLLphi-304); ORR ~40% (DeLLphi-301). Osteosarcoma efficacy is the open question NCT06788938 will answer.</td>
          <td>Moderate (CRS ~50% mostly G1-2; CRS G≥3 ~1%; ICANS-like ~10%; inpatient cycle-1 step-up dosing required)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(On-mechanism CNS bystander T-cell activation drives ICANS; possible DLL3 antigen-loss escape on repeated dosing)</span></td>
          <td><strong>The only DLL3-directed option when IHC is positive — preference-aligned but cross-tumor translation untested; foreclosed if IHC negative.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong class="split-glyph">SHR-4849 / IDE849 via NCT07174583 (IDEAYA pan-tumor DLL3 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive + sponsor confirms osteosarcoma)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Speculative. No published clinical data for SHR-4849. TOP1-inhibitor-payload ADC precedent (T-DXd, sacituzumab) suggests the class can produce signals; DLL3-specific efficacy is the open question.</td>
          <td>Unknown — no published clinical data. Class effects expected: cytopenias, GI, possible ILD/pneumonitis (DXd-class ADC signal).</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(ADC bystander toxicity to DLL3-low tissue; antigen-loss escape on repeated dosing; PBD-class TAHOE shadow does not directly apply but informs framing)</span></td>
          <td><strong>Mechanism-distinct second DLL3 pathway pending sponsor confirmation of osteosarcoma eligibility — relevant if the tarlatamab path is foreclosed or fails.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- The evidence base for the conditional trial is small. NCT06788938 plans n=29 with no published efficacy data yet. The mechanistic basis is the cross-tumor SCLC evidence (DeLLphi-301 / 304), which is robust in SCLC but unproven in any other tumor type.
- Biomarker dependency: rank 2's eligibility assumes a binary IHC result. Indeterminate or weak-positive (1–24%) edge cases are not explicitly addressed; in practice, NCT06788938's stage-2 ≥1% threshold may permit enrollment.
- What would change the ranking:
    - A positive DLL3 IHC plus a head-to-head osteosarcoma cohort within the basket trial reading out would move tarlatamab from "mechanism unproven cross-tumor" to "evidence-supported" and tighten its rank-2 confidence.
    - A user toxicity veto on CRS or inpatient cycle-1 monitoring would foreclose tarlatamab even with positive IHC.
    - Slot unavailability at NCT06788938 sites would close the within-scope therapeutic pathway. The patient's residual options would then be the treating team's standard-of-care conversation, which lies outside Libby's targetable-feature scope and is not enumerated here.

## Sources

**PubMed (PMID):**

- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301, *NEJM* 2023
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304, *NEJM* 2025
- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — DLL3 IHC reference (cited in workup row)

**ClinicalTrials.gov (NCT):**

- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — DLL3-IHC-selected basket including osteosarcoma (tarlatamab)
- [NCT05060016](https://clinicaltrials.gov/study/NCT05060016) — DeLLphi-301 (cross-tumor mechanism)
- [NCT05740566](https://clinicaltrials.gov/study/NCT05740566) — DeLLphi-304 (cross-tumor confirmatory)

## Transparency artifacts

- [Trial table](trials.md) — 3 rows, all 25 columns
- [Evidence list](evidence.md) — 3 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques (filtered to in-scope drugs at render time)
- [Recommendations table](recommendations.md) — full ranked detail with biomarker-conditional flag
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs: targetable feature ("DLL3 RNA expression"), clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts high-risk high-reward options"). Re-rendered when Libby's case scope tightened to drugs that act on the user's stated targetable feature; out-of-scope drugs (standard care for the indication that does not act on DLL3) no longer enter the dossier or appear on any case surface. The cross-cutting caveat carries the negative-result foreclosure mapping. The standard-of-care conversation for the indication is the treating team's, not Libby's. Humanizer pass applied May 2026.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.

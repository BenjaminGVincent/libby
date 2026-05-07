<meta name="robots" content="noindex">

# Recommendations — `osteosarcoma-mets-dll3-h7r2`

## Downloads

- [Target validation paths](osteosarcoma-mets-dll3-h7r2-target-validation.pdf) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations Table](osteosarcoma-mets-dll3-h7r2-recommendations.html) — ranked options + pipeline context — self-contained HTML that opens offline
- [Access guide](accessibility.md) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Master manuscripts table](manuscripts.md) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary

_5 rows: 1 workup + 4 ranked options._

## Shared first step

_The confirmatory test gates whether biomarker-conditional recs below apply. Run regardless of which therapy is ultimately chosen._

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
    <tr><td>1</td><td><strong>Dual-biomarker workup: DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing</strong><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td><td>Diagnostic certainty — resolves which of two targetable-feature pathways is open. Both are independent; either or both may confirm.</td><td>Low (none — diagnostic IHC on archival tissue + a single blood draw for HLA typing)</td><td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic)</span></td><td><strong>Non-toxic dual workup that gates ranks 2-5; run all three tests in parallel regardless of which therapy is ultimately chosen.</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>

## Ranked options

_Biomarker-conditional recs are flagged inline. The ranking is scoped to drugs that target the user's stated targetable feature; if the workup test is negative the within-scope options are exhausted, and standard care for the indication lies outside Libby's targetable-feature scope._

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
    <tr><td>2</td><td><strong>tarlatamab via NCT06788938 (UCCC-01 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td><td>Cross-tumor extrapolation: SCLC OS HR 0.60 (DeLLphi-304); ORR ~40% (DeLLphi-301). Osteosarcoma efficacy is the open question NCT06788938 will answer.</td><td>Moderate (CRS ~50% mostly G1-2; CRS G≥3 ~1%; ICANS-like ~10%; inpatient cycle-1 step-up dosing required)</td><td><strong>Moderate</strong> <span class="cpm-desc">(On-mechanism CNS bystander T-cell activation drives ICANS; possible DLL3 antigen-loss escape on repeated dosing)</span></td><td><strong>The only DLL3-directed option when IHC is positive — preference-aligned but cross-tumor translation untested; foreclosed if IHC negative.</strong></td></tr>
    <tr><td>3</td><td><strong>SHR-4849 / IDE849 via NCT07174583 (IDEAYA pan-tumor DLL3 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small></td><td>Speculative. No published clinical data for SHR-4849. TOP1-inhibitor-payload ADC precedent (T-DXd, sacituzumab govitecan) suggests the payload class can produce response signals, but DLL3-specific efficacy is the open question.</td><td>Unknown — no published clinical data. TOP1-inhibitor ADC class effects expected: cytopenias, GI toxicity, possible ILD/pneumonitis (DXd-class ADCs carry an ILD signal worth monitoring).</td><td><strong>Moderate</strong> <span class="cpm-desc">(ADC bystander toxicity to DLL3-low normal tissue; antigen-loss escape on repeated dosing; PBD-payload class shadow (Rova-T TAHOE) does not directly apply but informs the toxicity-budget framing.)</span></td><td><strong>Mechanism-distinct second DLL3 pathway pending sponsor confirmation of osteosarcoma eligibility — relevant if the tarlatamab path is foreclosed or fails.</strong></td></tr>
    <tr><td>4</td><td><strong>IMA203 (PRAME-TCR-T) via NCT03686124 (Immatics ACTengine pan-solid basket)</strong> <span class="scenario-conditional">(conditional on prame_ihc_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-concensusite">concensusite</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small></td><td>Strong. ORR 54% (95% CI 34-73) in pan-solid PRAME+ HLA-A*02:01+ cohort (Wermke 2024 Lancet Oncol, n=28). Sarcoma cohorts on protocol; osteosarcoma fit unconfirmed but eligibility is mechanism-driven, not tumor-restricted.</td><td>High (CRS ~100% — G3-4 ~10%; ICANS-like ~25%; uniform post-Cy/Flu cytopenias; one treatment-related death in published cohort; CAR-T-style infusion infrastructure required)</td><td><strong>Moderate</strong> <span class="cpm-desc">(On-target / off-tumor toxicity to PRAME-expressing normal testis is class-managed (testis is immune-privileged); CRS / neurotoxicity from T-cell activation is the main mechanism-level risk)</span></td><td><strong>Best-evidenced PRAME pathway with pan-solid sarcoma-inclusive basket; conditional on PRAME IHC + HLA-A*02:01 typing both confirming.</strong></td></tr>
    <tr><td>5</td><td><strong>IMC-P115C via NCT07156136 (Immunocore next-gen PRAME ImmTAC pan-tumor)</strong> <span class="scenario-conditional">(conditional on prame_ihc_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small></td><td>Speculative. No published clinical data for IMC-P115C; relies on brenetafusp class precedent (ORR ~9% in heavily pretreated melanoma; durable in subset).</td><td>Moderate (ImmTAC class: CRS ~85% mostly G1-2; rash ~70%; transient hypotension; pre-medication-managed)</td><td><strong>Moderate</strong> <span class="cpm-desc">(ImmTAC on-target / off-tumor signal in PRAME-expressing normal tissue (low; testis-restricted); CRS from T-cell activation)</span></td><td><strong>Mechanism-class alternative to IMA203 in the PRAME space, contingent on PRAME + HLA confirmation and sponsor confirmation osteosarcoma is in scope.</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

[Back to case](index.md) · [Trials](trials.md) · [Evidence](evidence.md) · [Manuscripts](manuscripts.md) · [Target validation](target_validation.md) · [Board](board.md) · [Plain language](plain_language.md)

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. Recommendations on this page have not been
    reviewed by a clinician treating this patient.
    See [PHI policy](../../phi_policy.md).


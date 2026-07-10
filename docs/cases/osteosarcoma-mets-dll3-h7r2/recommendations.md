<meta name="robots" content="noindex">

# Recommendations — `osteosarcoma-mets-dll3-h7r2`

## Downloads

### HTML

- [Target validation paths](target_validation.md) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](osteosarcoma-mets-dll3-h7r2-recommendations.html) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](osteosarcoma-mets-dll3-h7r2-accessibility.html) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](osteosarcoma-mets-dll3-h7r2-manuscripts.html) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](osteosarcoma-mets-dll3-h7r2-target-validation.pdf) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](osteosarcoma-mets-dll3-h7r2-recommendations.pdf) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](osteosarcoma-mets-dll3-h7r2-accessibility.pdf) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](osteosarcoma-mets-dll3-h7r2-manuscripts.pdf) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary

_7 rows: 1 workup + 6 ranked options._

## Shared first step

_The confirmatory test gates whether biomarker-conditional recs below apply. Run regardless of which therapy is ultimately chosen._

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th><th>Key references</th></tr></thead>
      <tbody>
    <tr><td>1</td><td><strong>DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing — diagnostic gate</strong><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td><td>N/A — diagnostic gate. Determines whether any downstream antigen-directed rec applies; PRAME axis more likely than not to hold, DLL3 protein status unknown.</td><td>Low (none — diagnostic test on tissue and blood)</td><td><strong>N/A</strong> <span class="cpm-desc">(Diagnostic gate, no mechanism of action)</span></td><td><strong>The one move that unlocks the whole antigen list — cheap, archival, non-toxic; a negative result on either axis forecloses that half of the ranking.</strong></td><td><a href="https://clinicaltrials.gov/study/NCT06788938">NCT06788938</a><br><a href="https://clinicaltrials.gov/study/NCT03686124">NCT03686124</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/35983951">PMID&nbsp;35983951</a></td></tr>
      </tbody>
    </table>
  </div>
</div>

## Ranked options

_Biomarker-conditional recs are flagged inline. The ranking is scoped to drugs that target the user's stated targetable feature; if the workup test is negative the within-scope options are exhausted, and standard care for the indication lies outside Libby's targetable-feature scope._

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th><th>Key references</th></tr></thead>
      <tbody>
    <tr><td>2</td><td><strong>tarlatamab (DLL3 x CD3 BiTE) via NCT06788938 (DLL3-IHC-gated basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td><td>Moderate if DLL3 IHC confirms — best-validated mechanism (DeLLphi-304 OS HR 0.60) but efficacy is entirely SCLC-derived; no osteosarcoma data.</td><td>Moderate (CRS ~56% mostly G1-2, ICANS-like ~12%, G3+ TRAE 24%)</td><td><strong>Moderate</strong> <span class="cpm-desc">(On-mechanism CNS/neuro bystander activation and antigen-density-dependent escape if DLL3 membrane expression is low or heterogeneous)</span></td><td><strong>The best-validated mechanism on the board and the lighter-toxicity DLL3 route — but every efficacy row is SCLC; osteosarcoma activity is a hypothesis until the IHC confirms surface target.</strong></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/40454646">PMID&nbsp;40454646</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/37861218">PMID&nbsp;37861218</a><br><a href="https://clinicaltrials.gov/study/NCT06788938">NCT06788938</a></td></tr>
    <tr><td>3</td><td><strong>IMA203 (PRAME TCR-T) via NCT03686124 (ACTengine pan-solid basket, sarcoma cohort named)</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td><td>High ceiling if both biomarkers confirm (ORR 54%, Nat Med 2025) but from n=28 with a wide CI and no osteosarcoma-specific responder; unstable point estimate.</td><td>High (1 treatment-related septic death; CRS ~100%/G3+ 11%, ICANS ~25%, universal G3+ cytopenias post-Cy/Flu)</td><td><strong>Moderate</strong> <span class="cpm-desc">(Antigen-loss / HLA-LOH escape and post-lymphodepletion immunosuppression window; durability unproven, responders melanoma-skewed)</span></td><td><strong>The highest-response on-axis option with a named sarcoma cohort, and the one with a fatality on the board — efficacy-first personas lead it, three dissent on the safety tail and n=28 imprecision.</strong></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/40205198">PMID&nbsp;40205198</a><br><a href="https://clinicaltrials.gov/study/NCT03686124">NCT03686124</a></td></tr>
    <tr><td>4</td><td><strong>brenetafusp (IMC-F106C, PRAME x CD3 ImmTAC) via NCT04262466 / successor IMC-P115C</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span></small></td><td>Low-to-moderate: overall ORR 9-11%, benefit concentrated in a PRAME-positive subset (mPFS 4.5 vs 2.1 mo); melanoma-derived, cross-tumor.</td><td>Low (CRS predominantly G1-2, no G3+ CRS in cohort; rash ~70%, G3+ TRAE ~30%)</td><td><strong>Low</strong> <span class="cpm-desc">(On-target/off-tumor rash and antigen-density dependence; dissent is enrollability-flavored, no mechanism-level counter-productive vector)</span></td><td><strong>The best-tolerated PRAME route with an off-the-shelf, no-lymphodepletion trade — but modest single-agent efficacy and a sarcoma enrollment slot that is currently closed.</strong></td><td>doi:10.1200/JCO.2024.42.16_suppl.9507<br><a href="https://clinicaltrials.gov/study/NCT04262466">NCT04262466</a></td></tr>
    <tr><td>5</td><td><strong>IMC-P115C (next-gen PRAME x CD3 ImmTAC) via NCT07156136</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small></td><td>Unknown — first-in-human, no efficacy data; class bet on the ImmTAC platform and PRAME target, inferred from brenetafusp.</td><td>Low (no drug-specific data; class expectation predominantly G1-2 CRS and rash)</td><td><strong>Low</strong> <span class="cpm-desc">(Same on-target/off-tumor and antigen-density dependence as the ImmTAC class; no drug-specific counter-productive signal yet)</span></td><td><strong>The recruiting-today PRAME ImmTAC when brenetafusp&#x27;s sarcoma slot is closed — a platform-and-target bet with no efficacy readout of its own yet.</strong></td><td><a href="https://clinicaltrials.gov/study/NCT07156136">NCT07156136</a><br>doi:10.1200/JCO.2024.42.16_suppl.9507</td></tr>
    <tr><td>6</td><td><strong>tarlatamab + radiation therapy via NCT06814496 (pan-tumor DLL3-IHC basket with RT)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small></td><td>Unknown — no combination data; abscopal benefit over tarlatamab monotherapy is a hypothesis the phase-1 is still measuring.</td><td>Moderate (uncharacterized combination; BiTE CRS ~50% mostly G1-2, ICANS-like ~10%, plus site-specific RT toxicity)</td><td><strong>Moderate</strong> <span class="cpm-desc">(Uncharacterized RT-on-BiTE synergistic toxicity; potential on-mechanism CNS/neuro bystander activation compounded by radiation)</span></td><td><strong>A parallel DLL3 slot with an abscopal rationale — but zero combination data, and the monotherapy basket delivers the same backbone with a written safety algorithm.</strong></td><td><a href="https://clinicaltrials.gov/study/NCT06814496">NCT06814496</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/40454646">PMID&nbsp;40454646</a></td></tr>
    <tr><td>7</td><td><strong>NW-101C (PRAME TCR-T) via NCT07266298 (pan-solid PRAME/HLA-A*02:01 basket)</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small class="persona-line"><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small><br><small class="persona-line"><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td><td>Unknown — no NW-101C data exist; efficacy inferred entirely from the IMA203 PRAME TCR-T class precedent.</td><td>High (no drug-specific data; class expectation is the IMA203 TCR-T profile — CRS, ICANS, post-lymphodepletion cytopenias)</td><td><strong>Moderate</strong> <span class="cpm-desc">(Same antigen-loss / HLA-LOH escape and lymphodepletion immunosuppression risk as the PRAME TCR-T class; no drug-specific data)</span></td><td><strong>A redundant PRAME TCR-T fallback if the IMA203 slot is inaccessible — but zero data under this name; the efficacy expectation is entirely borrowed.</strong></td><td><a href="https://clinicaltrials.gov/study/NCT07266298">NCT07266298</a></td></tr>
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


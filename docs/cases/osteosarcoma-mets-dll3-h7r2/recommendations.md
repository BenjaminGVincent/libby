<meta name="robots" content="noindex">

# Recommendations — `osteosarcoma-mets-dll3-h7r2`

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. Recommendations on this page have not been
    reviewed by a clinician treating this patient.
    See [PHI policy](../../phi_policy.md).

_7 rows across 2 scenario(s) plus 1 shared row(s)._

## Shared first step (applies to every scenario)

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Status</th><th>Intervention</th><th>Endorsed by</th><th>Dissent</th><th>Veto</th><th>Expected benefit</th><th>Key risks</th><th>Preference fit</th><th>Guideline</th><th>Evidence anchor</th><th>Open questions</th></tr></thead>
      <tbody>
    <tr><td>1</td><td class="">recommended</td><td><strong>Confirm DLL3 by IHC (SP347) on tumor — diagnostic gate</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></td><td>—</td><td>—</td><td>Resolves which scenario applies. Trial NCT06788938 enforces ≥25% (stage 1) or ≥1% (stage 2) by IHC.</td><td>1-3 week turnaround; if negative, the DLL3-targeted pathway is foreclosed</td><td>Aligns with all stated preferences — non-toxic, gates the user-preferred trial option.</td><td>Implicit in every modern targeted-therapy guideline; specifically required by NCT06788938.</td><td>pmid:35983951; nct:NCT06788938</td><td>Will the SP347 antibody assay be available at the treating institution?; Is sufficient archival or fresh tumor available?</td></tr>
      </tbody>
    </table>
  </div>
</div>

## Path A — if DLL3 IHC ≥1% (preferably ≥25%)

<small><code>scenario: dll3_ihc:positive</code></small>

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Status</th><th>Intervention</th><th>Endorsed by</th><th>Dissent</th><th>Veto</th><th>Expected benefit</th><th>Key risks</th><th>Preference fit</th><th>Guideline</th><th>Evidence anchor</th><th>Open questions</th></tr></thead>
      <tbody>
    <tr><td>1</td><td class="">recommended</td><td><strong>tarlatamab via NCT06788938 (UCCC-01 basket)</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></td><td><span class="persona persona-critic">critic</span></td><td>—</td><td>If mechanism translates from SCLC: median OS 13.6 vs 8.3 mo (HR 0.60) in DeLLphi-304 SCLC; ORR ~40% in DeLLphi-301. Cross-tumor extrapolation to osteosarcoma is unproven — the trial design exists precisely to test this.</td><td>CRS ~50% (mostly grade 1-2; grade ≥3 ~1% in SCLC); ICANS-like neurologic events ~10%; inpatient cycle-1 monitoring; no prior osteosarcoma data — cross-tumor translation is the open question</td><td>Strong match: high-risk-high-reward + prefers_trials. The biomarker-positive scenario is exactly when this option is on-mechanism.</td><td>Off-guideline for osteosarcoma; trial enrollment is NCCN cat-1 for relapsed disease.</td><td>nct:NCT06788938; pmid:37861218; pmid:40454646</td><td>Slot availability at NCT06788938 enrolling sites; Pre-medication / monitoring logistics for cycle 1; Cross-tumor translatability of DLL3 BiTE mechanism — first osteosarcoma cohort</td></tr>
    <tr><td>2</td><td class="">recommended</td><td><strong>regorafenib</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></td><td><span class="persona persona-advocate">advocate</span></td><td>—</td><td>Median PFS 3.6 vs 1.7 mo (SARC024); 65% non-progression at 8 weeks (REGOBONE). No OS benefit (crossover designs).</td><td>hand-foot reaction; hypertension; fatigue; transaminitis</td><td>Backbone option even when the trial is reachable. User&#x27;s stated preferences point to the trial as rank-1 in the positive scenario; regorafenib is the off-trial fallback or sequencing option.</td><td>NCCN-recommended for relapsed/refractory osteosarcoma.</td><td>pmid:31013172; pmid:30477937</td><td>Has the patient already had regorafenib?</td></tr>
    <tr><td>3</td><td class="">recommended</td><td><strong>cabozantinib</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></td><td>—</td><td>—</td><td>ORR 11.9% (95% CI 4.0-25.6); 6-mo non-progression 33.3% (CABONE).</td><td>thromboembolism; hypertension; diarrhea; hand-foot syndrome</td><td>Reasonable backup. Universal endorsement.</td><td>NCCN-listed alternative for relapsed bone sarcoma.</td><td>pmid:32078813</td><td>Prior regorafenib history; VTE prophylaxis</td></tr>
      </tbody>
    </table>
  </div>
</div>

## Path B — if DLL3 IHC negative or below threshold

<small><code>scenario: dll3_ihc:negative</code></small>

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Status</th><th>Intervention</th><th>Endorsed by</th><th>Dissent</th><th>Veto</th><th>Expected benefit</th><th>Key risks</th><th>Preference fit</th><th>Guideline</th><th>Evidence anchor</th><th>Open questions</th></tr></thead>
      <tbody>
    <tr><td>1</td><td class="">recommended</td><td><strong>regorafenib</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></td><td>—</td><td>—</td><td>Median PFS 3.6 vs 1.7 mo (SARC024); 65% non-progression at 8 weeks (REGOBONE).</td><td>hand-foot reaction; hypertension; fatigue</td><td>User stated high-risk-high-reward but with the trial pathway closed (negative IHC), regorafenib&#x27;s two-RCT evidence base is the highest expected utility option among non-trial choices. Advocate&#x27;s earlier preference-fit dissent does not apply here since the alternative they were championing (the trial) is no longer reachable.</td><td>NCCN-recommended for relapsed/refractory osteosarcoma.</td><td>pmid:31013172; pmid:30477937</td><td>Prior regorafenib status; Tolerance for hand-foot syndrome</td></tr>
    <tr><td>2</td><td class="">recommended</td><td><strong>cabozantinib</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></td><td>—</td><td>—</td><td>ORR 11.9% (95% CI 4.0-25.6); 6-mo non-progression 33.3% (CABONE).</td><td>thromboembolism; hypertension; diarrhea; hand-foot syndrome</td><td>Reasonable backup. Universal endorsement.</td><td>NCCN-listed alternative for relapsed bone sarcoma.</td><td>pmid:32078813</td><td>Prior cabozantinib; VTE prophylaxis</td></tr>
    <tr><td>3</td><td class="split-glyph">considered_with_caveats</td><td><strong>Non-DLL3 trial search (mechanism-agnostic)</strong></td><td><span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></td><td>—</td><td>—</td><td>Variable — trial-by-trial. The user&#x27;s prefers_trials = true preference applies regardless of the DLL3 result. Consider osteosarcoma-specific basket trials, immunotherapy-naive cohorts, or novel-target sarcoma trials.</td><td>wide variance by trial</td><td>Honors prefers_trials = true even when the DLL3 pathway is closed.</td><td>NCCN cat-1 for relapsed osteosarcoma to enroll in trials.</td><td>—</td><td>Specific osteosarcoma-relevant trials at the patient&#x27;s treating center; Referral pathway to academic sarcoma center</td></tr>
      </tbody>
    </table>
  </div>
</div>

[Back to case](index.md) · [Trials](trials.md) · [Evidence](evidence.md) · [Board](board.md) · [Plain language](plain_language.md)


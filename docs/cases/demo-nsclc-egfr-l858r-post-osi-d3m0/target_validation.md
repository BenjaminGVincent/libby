<meta name="robots" content="noindex">

# Target validation — `demo-nsclc-egfr-l858r-post-osi-d3m0`

_6 validation rows across 2 feature(s) — 0 essential, 0 gating an intervention. Sorted within each feature by priority, then by decision relevance._

_Essential / gates-intervention rows are the diagnostic prerequisites the downstream tumor board and PI use to compute the case's rank-1 shared workup. Rows tagged `confirms_target_call` harden the target call without gating a specific therapy; resistance / co-mutation / microenvironment rows refine sequencing and risk._

## EGFR L858R

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Priority</th><th>Test</th><th>Type</th><th>Modality</th><th>Tissue</th><th>Turnaround</th><th>Gates intervention</th><th>Decision relevance</th><th>Rationale</th><th>References</th></tr></thead>
      <tbody>
    <tr><td><span class="fit-badge fit-partial">high</span></td><td><strong>ctDNA panel including EGFR C797S, T790M, and exon 20 insertions</strong></td><td>resistance marker</td><td>ctDNA</td><td>10–20 mL whole blood; archival tissue not required</td><td>2 weeks</td><td>—</td><td>informs resistance</td><td>After osimertinib progression, the resistance landscape divides cleanly between on-target EGFR mutations (C797S, exon-20 inserts, less commonly T790M) and bypass mechanisms. Detecting C797S in cis vs trans changes whether a fourth-generation EGFR-TKI or a combination strategy is the rational next move. Skipping ctDNA at progression risks treating the case as bypass-resistance-only when the biology is mixed.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/31378236">PMID&nbsp;31378236</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/32385236">PMID&nbsp;32385236</a></td></tr>
    <tr><td><span class="fit-badge fit-partial">high</span></td><td><strong>Tumor NGS including TP53 and RB1 status</strong></td><td>co-mutation</td><td>NGS_panel</td><td>archival FFPE; if exhausted, ctDNA broad panel</td><td>2–4 weeks</td><td>—</td><td>informs resistance</td><td>TP53 + RB1 co-loss is the strongest predictor of small-cell histologic transformation as a resistance mechanism in EGFR-mutant NSCLC progressing on osimertinib. The probability of transformation is non-trivial (3–14% across cohorts), and missing it changes the next-line conversation entirely — chemotherapy backbones and platinum-etoposide enter the picture. Pair this with re-biopsy guidance below.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/31257067">PMID&nbsp;31257067</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/33495462">PMID&nbsp;33495462</a></td></tr>
    <tr><td><span class="fit-badge fit-weak">medium</span></td><td><strong>Re-biopsy with neuroendocrine IHC panel (chromogranin, synaptophysin, INSM1, Ki-67) if imaging morphology shifts</strong></td><td>subtyping</td><td>IHC</td><td>fresh biopsy of the most-active site</td><td>1–3 weeks (IHC turnaround); biopsy scheduling adds time</td><td>—</td><td>informs resistance</td><td>Histologic small-cell transformation is the most consequential resistance pattern that no liquid biopsy can confirm. When TP53/RB1 are co-lost or imaging shows new visceral / explosive growth atypical for adenocarcinoma, fresh tissue with a neuroendocrine IHC panel is the only way to confirm. Without this, a transformed case can be treated as adenocarcinoma indefinitely.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/30664509">PMID&nbsp;30664509</a></td></tr>
      </tbody>
    </table>
  </div>
</div>

## MET amplification

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Priority</th><th>Test</th><th>Type</th><th>Modality</th><th>Tissue</th><th>Turnaround</th><th>Gates intervention</th><th>Decision relevance</th><th>Rationale</th><th>References</th></tr></thead>
      <tbody>
    <tr><td><span class="fit-badge fit-partial">high</span></td><td><strong>MET FISH on a second site (metastatic biopsy or matched archival block)</strong></td><td>heterogeneity</td><td>FISH</td><td>second-site archival FFPE if available; not gating</td><td>1–2 weeks</td><td>—</td><td>refines target subtype</td><td>MET amplification can be focal and discordant between primary and metastatic sites in EGFR-resistant NSCLC. The patient&#x27;s GCN 8.2 from a single block clears SAFFRON&#x27;s threshold, but a second-site test rules out the scenario where one biopsy hits a focal amplicon and the dominant disease is unaffected. Without it, a positive trial enrollment can rest on a non-representative result.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/32679432">PMID&nbsp;32679432</a></td></tr>
    <tr><td><span class="fit-badge fit-weak">medium</span></td><td><strong>MET IHC (clone SP44) for orthogonal expression confirmation</strong></td><td>orthogonal validation</td><td>IHC</td><td>archival FFPE; same block as prior testing</td><td>1 week</td><td>—</td><td>confirms target call</td><td>FISH-confirmed MET amplification at GCN 8.2 is the load-bearing finding, and SAFFRON enrollment accepts FISH or IHC 3+. IHC adds an orthogonal modality and surfaces protein-level MET expression; concordance increases confidence that the FISH result reflects active MET signaling. Discordance (FISH-amp without IHC overexpression) is a soft signal worth flagging but does not foreclose the trial.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/32679432">PMID&nbsp;32679432</a><br><a href="https://clinicaltrials.gov/study/NCT05261399">NCT05261399</a></td></tr>
    <tr><td><span class="fit-badge fit-weak">medium</span></td><td><strong>Comprehensive NGS for HER2 amp, BRAF, KRAS, FGFR1-3, and bypass-pathway alterations</strong></td><td>co-mutation</td><td>NGS_panel</td><td>archival FFPE; ctDNA as backup</td><td>2–4 weeks</td><td>—</td><td>informs resistance</td><td>Bypass amplifications co-occur with MET amp in roughly 10–20% of post-osimertinib cases and modify expected response to MET-directed therapy. Detecting co-bypass alterations doesn&#x27;t foreclose savolitinib + osimertinib but reframes the durability expectation and informs subsequent-line planning. Pair this with the TP53 / RB1 panel if running comprehensive NGS — same blood draw / block.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/31257067">PMID&nbsp;31257067</a></td></tr>
      </tbody>
    </table>
  </div>
</div>

[Back to case](index.md) · [Trials](trials.md) · [Evidence](evidence.md) · [Manuscripts](manuscripts.md) · [Board](board.md) · [Recommendations](recommendations.md)

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The validation tests on this page are decision-support;
    confirm assay availability, current standards, and clinical relevance with the
    treating team and the local pathology service.
    See [PHI policy](../../phi_policy.md).


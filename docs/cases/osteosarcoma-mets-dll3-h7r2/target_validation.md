<meta name="robots" content="noindex">

# Target validation — `osteosarcoma-mets-dll3-h7r2`

_4 validation rows across 1 feature(s) — 1 essential, 1 gating an intervention. Sorted within each feature by priority, then by decision relevance._

_Essential / gates-intervention rows are the diagnostic prerequisites the downstream tumor board and PI use to compute the case's rank-1 shared workup. Rows tagged `confirms_target_call` harden the target call without gating a specific therapy; resistance / co-mutation / microenvironment rows refine sequencing and risk._

## DLL3 RNA expression

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Priority</th><th>Test</th><th>Type</th><th>Modality</th><th>Tissue</th><th>Turnaround</th><th>Gates intervention</th><th>Decision relevance</th><th>Rationale</th><th>References</th></tr></thead>
      <tbody>
    <tr><td><span class="fit-badge fit-strong">essential</span></td><td><strong>DLL3 IHC (clone SP347)</strong></td><td>confirmatory</td><td>IHC</td><td>archival FFPE; fresh biopsy not required if stored tissue is adequate</td><td>1–3 weeks</td><td><code>tarlatamab</code>, <a href="https://clinicaltrials.gov/study/NCT06788938">NCT06788938</a></td><td>gates intervention</td><td>RNA expression establishes that the DLL3 gene is being transcribed; it does not establish that DLL3 protein sits on the cell surface where a BiTE can engage. NCT06788938 enforces IHC ≥ 25% (stage 1) or ≥ 1% (stage 2) for enrollment, and every approved DLL3-directed therapy gates on protein-level confirmation. Skipping the test forecloses every DLL3-directed candidate downstream by definition.</td><td><a href="https://clinicaltrials.gov/study/NCT06788938">NCT06788938</a><br><a href="https://pubmed.ncbi.nlm.nih.gov/35983951">PMID&nbsp;35983951</a></td></tr>
    <tr><td><span class="fit-badge fit-partial">high</span></td><td><strong>DLL3 IHC on multiple tumor regions / metastatic biopsy</strong></td><td>heterogeneity</td><td>IHC</td><td>additional archival blocks from a different site if available</td><td>1–4 weeks</td><td>—</td><td>refines target subtype</td><td>Osteosarcoma metastases can diverge from primary tumors in surface-marker expression, and the cross-tumor DLL3 literature in solid tumors (Zhang 2023) flags spatial heterogeneity as a frequent confounder. Testing one site can over- or under-estimate enrollment-grade DLL3 status. If only one block is available the workup proceeds with that block, but the result should be interpreted with this caveat in mind.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/36841456">PMID&nbsp;36841456</a></td></tr>
    <tr><td><span class="fit-badge fit-weak">medium</span></td><td><strong>ASCL1 / NEUROD1 IHC + chromogranin / synaptophysin / INSM1 panel</strong></td><td>subtyping</td><td>IHC</td><td>archival FFPE; same block as the DLL3 IHC</td><td>1–2 weeks</td><td>—</td><td>confirms target call</td><td>DLL3 is a Notch-pathway target normally expressed in neuroendocrine lineage. In a non-NEC tumor like osteosarcoma, surfacing or excluding any neuroendocrine differentiation pattern (Notch-low / ASCL1-high state) provides mechanistic context for whether DLL3 expression is biologically plausible or a stochastic finding. Does not gate enrollment; informs how the rank-2 trial outcome should be interpreted.</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/33288979">PMID&nbsp;33288979</a></td></tr>
    <tr><td><span class="fit-badge fit-weak">medium</span></td><td><strong>Germline TP53 sequencing (Li-Fraumeni panel)</strong></td><td>germline</td><td>germline_panel</td><td>5–10 mL EDTA whole blood</td><td>3–6 weeks</td><td>—</td><td>informs germline implications</td><td>Osteosarcoma in the late-teens to twenties carries a meaningful prior probability of germline TP53 (Li-Fraumeni). A positive germline TP53 result changes radiation-sensitivity considerations, screening for synchronous tumors, and family screening for first-degree relatives. Does not affect tarlatamab eligibility, but is the kind of finding that would change the surrounding care plan.</td><td><em>nccn-bone-cancer</em><br><a href="https://pubmed.ncbi.nlm.nih.gov/32647394">PMID&nbsp;32647394</a></td></tr>
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


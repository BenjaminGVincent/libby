# Trial-table style

Style spec for tables presenting extracted results from clinical-trial
publications, embedded within a running document. Evidence-synthesis-flavored —
the kind of table a reader scans to compare trials at a glance, with full
citation provenance per row.

**Row granularity:** one row per publication (not per trial). When the same
trial has multiple publications in the table, mark sibling publications with a
superscript letter that resolves to a table note.

---

## Columns (canonical order)

| # | Column      | Notes                                                                 |
|---|-------------|-----------------------------------------------------------------------|
| 1 | First author| surname                                                               |
| 2 | Last author | surname (senior / corresponding)                                      |
| 3 | Year        | 4-digit                                                               |
| 4 | Journal     | standard abbreviation (NEJM, Lancet Oncol, …)                         |
| 5 | NCT ID      | superscript marker (`ᵃ`, `ᵇ`, …) when trial has sibling publications  |
| 6 | Phase       | `1`, `1/2`, `2`, `3`, `4`                                             |
| 7 | Indication  | disease (split from Population)                                       |
| 8 | Line        | `1L`, `2L+`, `adj`, `neoadj`                                          |
| 9 | Biomarker   | `PD-L1 ≥1%`, `BRAF V600E`, `unselected`, …                            |
| 10| n           | randomized or enrolled — specify in caption                           |
| 11| Design      | `RCT`, `single-arm`, `basket`, …                                      |
| 12| Intervention| treatment under study                                                 |
| 13| Comparator  | `—` for single-arm                                                    |
| 14| Endpoint    | `OS (HR)`, `PFS (HR)`, `ORR`, …                                       |
| 15| Effect size | point estimate (replaces the loose "variance" notion)                 |
| 16| Lower CI    | 95% CI lower bound                                                    |
| 17| Upper CI    | 95% CI upper bound                                                    |
| 18| p           | `<0.001` convention                                                   |
| 19| Quality     | RoB 2 (RCTs) or ROBINS-I (non-randomized); optional, see below        |
| 20| PMID        | hyperlinked in web formats; dropped in LaTeX manuscript               |
| 21| DOI         | hyperlinked in web formats; dropped in LaTeX manuscript               |

### Per-format column behavior

- **Markdown / HTML (web, author-year prose style).** All 21 columns. PMID and
  DOI rendered as hyperlinks to `pubmed.ncbi.nlm.nih.gov/<id>` and
  `doi.org/<doi>`.
- **LaTeX manuscript (numeric citation style).** 10-column compact primary
  table in the body: First author, Last author, Year, Phase, Indication, n,
  Intervention, Endpoint, Effect, p, Ref. The `Ref` column uses `\cite{}`;
  PMID/DOI live in the `.bib` entries, not the table. A landscape
  supplementary table carries NCT ID, Line, Biomarker, Design, Comparator,
  Lower/Upper CI, Quality, and trial-sibling notes.

---

## Typography

- Table font: same family as body text.
- Size: `0.88em`–`0.9em` (slightly smaller than body so dense rows don't crowd).
- Tabular numerics: `font-variant-numeric: tabular-nums` (CSS) or `siunitx`
  S-columns (LaTeX) so decimals align without explicit padding.
- Header row: semibold (not bold), sentence case, no all-caps.
- Cell padding: vertical `0.5em`, horizontal `0.6em` — rows need breathing
  room more than columns.

---

## Alignment & number formatting

- Text columns: left-aligned.
- Numeric columns (n, Effect, Lower/Upper CI, p): right-aligned,
  decimal-aligned.
- HR / OR / RR values: 2 decimals.
- Percentages / ORR: 1 decimal.
- p-values: 3 decimals or `<0.001`.
- Missing values: em dash `—`. Never blank. Never `N/A`.
- CI: separate Lower CI / Upper CI columns (not merged into parenthetical form
  — the user explicitly requested a split for downstream meta-analysis).

---

## Palette

| Role            | Hex       | Notes                                                    |
|-----------------|-----------|----------------------------------------------------------|
| Body text       | `#1A202C` | near-black                                               |
| Header tint     | `#F4F6F8` | 14.2:1 against body text — WCAG AAA                      |
| Row divider     | `#E2E8F0` | light gray                                               |
| Top/bottom rule | `#1A202C` | 2px                                                      |
| Muted text      | `#4A5568` | for table notes / footnotes                              |

- Zebra striping: **off**. Numeric tables read cleaner without it.
- Vertical rules: **none**. `booktabs` aesthetic: top rule, header rule,
  bottom rule.
- Emphasis color on Effect column: off by default; evidence tables shouldn't
  editorialize. Okabe–Ito blue (`#0072B2`) + vermillion (`#D55E00`) available
  if the user explicitly wants benefit/harm cueing — both colorblind-safe.

---

## Citations

- **Web (Markdown / HTML):** PMID and DOI hyperlinked in their own columns.
  Reads as "author-year prose style" with the table doubling as an inline
  reference block.
- **Manuscript (LaTeX):** drop PMID/DOI columns; add a `Ref` column that uses
  `\cite{}`. PMID/DOI live in the `.bib` entries. Keeps table width sane.

---

## Multi-publication handling (one row per publication)

- When the same trial has multiple publications in the table, mark the NCT ID
  cell with a superscript letter (`ᵃ`, `ᵇ`, …).
- The letter resolves in a table note: *"ᵃ Same trial (…) as Wolchok 2017
  (NEJM; PMID: 28889792) — differing minimum follow-up."*
- Cheaper than a dedicated "See also" column, and only adds visual weight
  when there's actually something to point to.

---

## Quality column

Include by default; most manuscripts that aren't systematic reviews will omit
or loosen this.

- **Formal rubric (systematic review):** RoB 2 {Low, Some concerns, High} for
  RCTs; ROBINS-I {Low, Moderate, Serious, Critical, No info} for
  non-randomized.
- **Informal rubric (narrative review / manuscript):** loosen to {Low, Med,
  High} with caption describing the criteria used.
- **Drop entirely:** if the manuscript has no quality-assessment framing,
  remove column 19.

Caption must state which rubric is used (per row or across the table). No
color badges by default.

---

## Accessibility

- All foreground/background combinations pass WCAG AA (≥4.5:1 body,
  ≥3:1 large).
- No information conveyed by color alone.
- Hyperlinks underlined, not color-only.

---

## Usage

- **Markdown** — copy `examples/table.md`, replace the rows, paste into your
  document. No dependencies.
- **LaTeX** — `\input{examples/table.tex}` in a manuscript using `booktabs`,
  `threeparttable`, `siunitx`, `array`, and (for the supplementary landscape
  table) `rotating`. A self-contained compilable demo is in
  `examples/preview.tex`.
- **HTML** — copy the complete `examples/table.html`; the `<style>` block is
  scoped via `.trial-table-wrap` so it won't leak into the surrounding page.

---

## Dependencies

- **LaTeX:** `booktabs`, `threeparttable`, `siunitx`, `array`, `rotating` — all
  in standard TeX Live.
- **HTML:** Inter (Google Fonts); falls back to `system-ui`.
- **Markdown:** none.

---

## Example data caveat

The worked example in `examples/` uses one real trial (CheckMate 067 / Larkin
2019) with recalled values for demonstration. The numbers have not been
re-verified against the source PMID — do not reuse them in any published
artifact without pulling the values directly from the NEJM paper. The second
example row is fully placeholdered (`[ph]`) to demonstrate the missing-value
convention.

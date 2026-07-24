---
name: reference_checking
version: 1.0.0
description: |
  Verify every reference in a document — PMIDs, DOIs, URLs, arXiv IDs, ISBNs,
  and author/year/title strings — for both existence and contextual
  correctness. Catches hallucinated identifiers, wrong-identifier bugs
  (the identifier exists but points to a different paper than the prose
  claims), citation drift (the paper exists but doesn't support the
  surrounding claim), retracted papers, broken URLs, and duplicate
  citations. Produces a structured audit report; optionally annotates
  the source document.

  Use when reviewing manuscripts, grants, review articles, blog posts,
  reports, or any document where citation accuracy matters. Invoke
  whenever the user says "check the references," "verify the
  citations," "audit the bibliography," or hands over a document and
  asks if the references are correct.
license: MIT
compatibility: claude-code opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - WebFetch
  - WebSearch
  - AskUserQuestion
---

# Reference Checking: Verify Every Citation, Three Ways

You are a citation auditor. Your job is to confirm that every reference in a document is **real**, that the identifier points to **the right work**, and that the cited work actually **supports the claim it's attached to** in the surrounding prose. You catch hallucinated PMIDs, copy-paste errors (right author, wrong PMID), citation drift (the paper exists but doesn't say what the document claims it does), retractions, broken URLs, and duplicates.

The defining principle of this skill is **triangulation**. A single API lookup is not enough — identifiers can be hallucinated convincingly, metadata can be stale, and a "real PMID for a real paper" tells you nothing about whether the surrounding sentence is accurate. You verify each reference three independent ways: existence, identity-to-claim alignment, and cross-source confirmation. Only references that clear all three passes are marked verified.

## Your task

When invoked on a document (path or inline text):

1. **Enumerate every reference** in the document — every identifier of every type.
2. **For each reference, run three verification passes** (existence → claim-match → cross-source).
3. **Produce a structured audit report** with per-reference verdicts: Verified, Wrong-identifier, Hallucinated, Claim-drift, Retracted, Broken-URL, Ambiguous, or Could-not-verify.
4. **Optionally annotate the source document** with inline flags so the author can find issues quickly. Default: report only, ask before editing the source.

---

## Phase 0 — Setup

Before any lookups:

1. **Read the entire document.** Build a flat list of every citation occurrence with: the identifier (or identifier-like text), the file location (line number, or section heading), and the surrounding sentence(s) — at minimum the sentence containing the citation and one sentence on either side. This surrounding context is what you check claims against.
2. **Classify each citation by identifier type.** Common types:
   - **PMID**: `[PMID: 12345678]`, `PMID:12345678`, `(PubMed: 12345678)`.
   - **DOI**: `10.xxxx/...`, `doi.org/10.xxxx/...`, `https://doi.org/10.xxxx/...`.
   - **arXiv**: `arXiv:2401.12345`, `2401.12345 [cs.LG]`.
   - **PMC ID**: `PMC1234567`.
   - **ISBN**: 10- or 13-digit, hyphenated or not.
   - **URL**: any `http(s)://...` not covered above.
   - **Bibliographic string**: "Smith et al., *Nature* 2021" with no identifier.
   - **Bracketed numeric**: `[1]`, `[23]` — needs cross-reference to a bibliography section.
   - **Author-year**: `(Smith et al., 2021)` — needs cross-reference to a bibliography section.
3. **If the document uses numeric `[1]` or author-year citations**, locate the bibliography section. Map each in-text citation to its bibliography entry, then verify the bibliography entries themselves. Flag any in-text citation whose number/key has no bibliography entry, and any bibliography entry never cited.
4. **Deduplicate by identifier**, but keep all occurrences. You verify each identifier once; you check claim-match for every occurrence (a PMID can be cited correctly in one paragraph and wrong in another).
5. **Tell the user what you found before lookups begin.** A one-line summary: `Found 42 references — 30 PMIDs, 5 DOIs, 4 URLs, 3 bibliographic strings. Beginning verification.` This lets them catch scope misunderstandings before you spend lookup budget.

---

## Phase 1 — Existence (Pass 1 of 3)

Confirm each identifier resolves to a real, retrievable record. Use the canonical authority for each type.

### PMID

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<PMID>&retmode=json&tool=claude-reference-checking&email=benjamin.g.vincent@gmail.com
```

Capture from the response: `title`, `authors`, `source` (journal abbreviation), `fulljournalname`, `pubdate`, `elocationid` (often a DOI), and any `pubtype` entries that include "Retracted Publication" or "Retraction of Publication." Save these in your worktable for Pass 2.

If ESummary returns no record for the PMID, flag as **Hallucinated** and stop further checks on that identifier.

### DOI

```
https://api.crossref.org/works/<DOI>
```

Capture: `title`, `author`, `container-title` (journal/publisher), `issued` (publication date), `type`, and any cross-references to a PMID. If CrossRef returns 404, also try the NCBI ID Converter:

```
https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=<DOI>&format=json&tool=claude-reference-checking&email=benjamin.g.vincent@gmail.com
```

If both fail, flag as **Hallucinated**.

### arXiv

```
https://export.arxiv.org/api/query?id_list=<arXiv-ID>
```

Capture: `title`, `author`, `published`, `summary` (abstract), and the primary category. If the API returns an empty `<entry>` block, flag as **Hallucinated**.

### PMC ID

Use the NCBI ID Converter above with `ids=PMC<num>`. PMC records always cross-reference to a PMID — verify the round-trip.

### ISBN

Try the Open Library API:

```
https://openlibrary.org/api/books?bibkeys=ISBN:<ISBN>&format=json&jscmd=data
```

Capture title, authors, publisher, year. If Open Library has nothing, try a Google Books query as a fallback. If both fail, flag as **Could-not-verify** and ask the user (ISBN catalogs are incomplete — absence is not proof of non-existence).

### URL

Use WebFetch to retrieve the page. Capture the HTTP status, the page `<title>`, and the first 500 words of body text. Flag any of:
- non-200 status → **Broken-URL**
- redirect to a generic landing page or login wall → **Broken-URL** (note the redirect target in the report)
- archived-only content (page exists but is empty or stub) → **Broken-URL**

For URLs that should be stable (DOI pages, journal article pages), also check the Wayback Machine for a recent snapshot as a sanity check that the content was the same when the citation was likely written.

### Bibliographic string (no identifier)

Search PubMed first:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<first-author-LastName>[Author]+AND+<year>[DP]+AND+<title-fragment>[Title]&retmode=json
```

If a unique top hit returns, treat as a probable PMID match and proceed to Pass 2. If multiple hits or zero hits, fall back to WebSearch with the author/year/title and the journal name. If still ambiguous, flag as **Ambiguous** and present candidates to the user.

### Bracketed numeric / author-year

These are resolved through the bibliography mapping done in Phase 0. The bibliography entry then becomes the unit you verify (it will have a DOI, PMID, or bibliographic string, which you check via the rules above).

### Rate limiting

NCBI E-utilities: 3 requests/second without an API key. Batch sequentially. CrossRef has no hard limit but asks you to include a `User-Agent` and `mailto` parameter:

```
curl -A 'claude-reference-checking (mailto:benjamin.g.vincent@gmail.com)' 'https://api.crossref.org/works/<DOI>'
```

Do not parallelize lookups beyond ~3 in flight. A 100-reference document should take a couple of minutes; that's the cost of doing this right.

---

## Phase 2 — Claim match (Pass 2 of 3)

This is the pass that catches the most expensive errors: the identifier is real, but it doesn't point to the work the document says it points to, or the work doesn't actually support the claim.

For each reference that cleared Phase 1, do these checks against every in-text occurrence (not just the first):

### Identity match

- **In-text attribution vs. resolved metadata.** If the prose says "Smith and colleagues showed..." the resolved record's first author should be Smith. If the prose says "the 2014 *NEJM* paper by Gragert et al.," the resolved journal should be NEJM and the year 2014. Mismatches at this level usually mean a wrong-identifier bug — a typo or copy-paste error where the citation tag lost track of which paper it belonged to. Flag as **Wrong-identifier**.
- **Topic match.** Fetch the abstract:
  - PMID: ESummary doesn't include the abstract; use EFetch:
    ```
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text
    ```
  - DOI: many CrossRef records include `abstract`; if not, fetch the article landing page via WebFetch and pull the abstract from there.
  - arXiv: the API response already includes `summary`.
  - URL: the WebFetch from Phase 1 already captured the body text.
  Compare the abstract's topic to the topic of the surrounding sentence(s). If a paper about CAR-T manufacturing is cited for a claim about HLA matching, that's claim-drift even if the identifier is real and the authors match. Flag as **Claim-drift**.

### Specific-claim match

If the prose makes a quantitative or factual claim that the cited paper is the named source for ("Smith et al. reported a 73% response rate [PMID: X]"), check whether the abstract contains or implies that number. Abstracts won't always contain every detail of the paper — when the abstract doesn't confirm or deny, mark **Could-not-verify-from-abstract** and note that the full text would be needed. Don't fabricate confirmation.

### Retraction check

In the ESummary response, look for `pubtype` entries containing "Retracted Publication," "Retraction of Publication," or "Expression of Concern." Also check the `history` field for retraction dates. For papers known to be in fields with active retraction concerns (clinical trials, image-heavy biomedical work), consider an additional pass through PubPeer search:

```
https://pubpeer.com/search?q=<PMID>
```

If retracted, flag as **Retracted** and include the retraction notice's PMID in the report.

### Self-consistency in the document

- **Duplicate citations.** If the same identifier appears multiple times, that's fine — but if it's cited for claims that contradict each other, flag it. (Rare, but happens in long documents.)
- **Identifier collisions.** If two different identifiers resolve to the same work (e.g., a PMID and a DOI for the same paper, cited as if they were two papers), flag as **Duplicate-identifier**.

---

## Phase 3 — Cross-source (Pass 3 of 3)

For each reference that cleared Phases 1 and 2, verify by an **independent** path. The goal is to catch errors where the primary source (e.g., PubMed) is itself wrong, stale, or where the identifier happens to be a valid record but for the wrong reason.

### Round-trip via the other identifier

- **PMID → DOI → PMID.** Take the DOI from ESummary's `elocationid` or `articleids`, look it up via CrossRef, and confirm CrossRef's metadata matches what PubMed gave you (same title, same first author). If CrossRef has a different PMID in its cross-references field, flag.
- **DOI → PMID → DOI.** Symmetric to above, via the NCBI ID Converter.
- **arXiv → published version.** If the arXiv record has a `doi` field (papers often deposit the published DOI to arXiv after publication), round-trip through CrossRef.

### Independent metadata source

For high-stakes documents (grants, manuscripts under review), do one of:
- **Google Scholar search** via WebSearch with the title in quotes. Confirm the top hit's authors and year match.
- **Semantic Scholar API**:
  ```
  https://api.semanticscholar.org/graph/v1/paper/PMID:<PMID>?fields=title,authors,year,journal,citationCount,influentialCitationCount
  ```
  Useful as an independent metadata source and as a citation-count check (the original author may have a sense for how widely cited the paper is, which can flag wrong-paper bugs).

### Skip Phase 3 only when

You may skip Phase 3 for routine non-critical documents (a blog post, an internal memo) if Phase 1 and Phase 2 both passed cleanly and the identifier was supplied directly by the author. For anything submitted externally (grant, manuscript, review article, dissertation), always run all three phases.

---

## Phase 4 — Report

Write the audit to `<document-directory>/reference_check_report.md` (or a path the user specifies). Structure:

```markdown
# Reference check: <document name>
Audited: <ISO date>  |  Total references: N (unique: M)  |  Verified: X  |  Flagged: Y  |  Could not verify: Z

## Summary
- Verified (X): list of identifiers
- Flagged (Y): brief one-liners per flag with severity
- Could not verify (Z): one-liners with reason

## Verified references
| ID | Type | Authors | Year | Venue | Cited at (line / section) | Verdict |
|----|------|---------|------|-------|---------------------------|---------|
| ... | PMID | Smith et al. | 2014 | NEJM | line 12, line 47 | OK |

## Flagged — needs author action
For each flag, give:
- **Identifier and document location** (line number or section, plus quoted surrounding text).
- **Issue type** (Wrong-identifier / Hallucinated / Claim-drift / Retracted / Broken-URL / Duplicate-identifier).
- **What the document claims** (one sentence, quoted).
- **What the resolved record actually is** (Authors, Year, Journal, Title).
- **Recommended action** (e.g., "Replace with PMID X (Author Year Journal — Title) which matches the claim," or "Remove citation; claim is not supported by this source").

## Could-not-verify
- Reference, reason (rate-limited, paywalled, ambiguous bibliographic string, etc.), suggested next step.

## Verification method notes
One paragraph: which APIs you used, anything you skipped (and why), any rate-limit interruptions, whether Phase 3 was full or abbreviated.
```

Put the most important section (**Flagged — needs author action**) at the top of the file if there are any flags. The user should not have to scroll past 200 verified references to find the 3 that need attention.

---

## Annotating the source document (optional)

If the user wants inline flags in the source document itself, add tags in a grep-able format adjacent to each problematic citation. Example for a Markdown document:

```
This paper showed X [PMID: 12345678] <!-- REFCHECK-FLAG: Wrong-identifier — resolves to "Y et al. 2019" not Smith et al. as claimed -->
```

For `.tex` documents, use `% REFCHECK-FLAG: ...` comments after the citation. For `.docx`, ask the user — Word comments require a different approach (python-docx with `add_comment`) and may be more disruptive than a separate report.

**Never edit a citation silently.** This skill diagnoses; it does not fix. Fixing is a human or downstream-tool decision (e.g., the scientific-writer agent can apply approved swaps).

---

## Verdict definitions (use these exact terms)

- **Verified** — Phases 1, 2, and 3 all passed.
- **Verified-abbr** — Phases 1 and 2 passed; Phase 3 skipped (low-stakes doc).
- **Wrong-identifier** — Identifier resolves to a real work, but that work is not what the prose claims it is (different authors, different topic). This is the most common citation bug.
- **Hallucinated** — Identifier does not resolve to any record.
- **Claim-drift** — Identifier and authors match the prose, but the cited work doesn't actually support the surrounding claim.
- **Could-not-verify-from-abstract** — Identifier and authors match; the specific claim couldn't be confirmed from the abstract alone, and the full text wasn't checked. Note for human follow-up.
- **Retracted** — Cited work has been retracted or has an expression of concern. Include retraction notice ID.
- **Broken-URL** — URL does not resolve, requires login, or returns generic landing page.
- **Duplicate-identifier** — Two distinct identifiers resolve to the same work; the document treats them as separate citations.
- **Ambiguous** — Bibliographic string or partial citation matched multiple records. Candidates listed in report for user to disambiguate.
- **Could-not-verify** — Lookup failed for reasons other than hallucination (rate-limited, paywalled, API down). Suggest next step.

---

## Discipline (read this carefully)

- **Never guess.** If a lookup is ambiguous, flag it. Do not pick the closest hit and call it verified.
- **Never invent metadata.** If the abstract is unavailable, say so — don't reconstruct what you think it probably says.
- **Surface, don't fix.** This skill produces a report. The author or downstream tool decides what to change.
- **Quote the surrounding prose verbatim** for every flag. The user needs to find it in their document and decide what to do — paraphrasing the claim makes it harder to verify.
- **Distinguish what you checked from what you didn't.** A "Verified" label means all three phases passed for that reference. "Verified-abbr" or "Could-not-verify-from-abstract" are not weaker forms of verified — they mark the boundary of what you actually confirmed, and that boundary matters to the author.
- **Respect the user's known references.** If the document is by an author whose own papers are cited (self-citations), do not flag them as "wrong" just because the resolved metadata feels off — fetch the abstract and compare to the claim like any other citation, but apply equal rigor in both directions.

---

## When to push back

- The user gives you a document with hundreds of references and asks for a thorough check on a tight clock. Tell them how long it will realistically take (≈1–2 seconds per reference under rate limits, so 100 references is several minutes minimum). Offer to scope: "Want me to run Phase 1 on all 300 and Phases 2–3 only on the 20 most-cited claims?"
- The document is a draft with `[CITE]` or `[TK]` placeholders. Skip those and report the count separately so they're not buried in the verification queue.
- The document cites preprints that have since been published. Note the published version in your report; the author may prefer to update.
- A reference points to a paper the author co-authored. Apply the same checks; don't relax rigor for self-citations.

---

## Operating notes

- For long documents, write a checkpoint file (`reference_check_progress.json`) every 25 references so you can resume after a rate-limit pause or interruption without re-doing finished lookups.
- For documents with bibliography sections, parse those first — they're the canonical source of identifier-to-citation-key mapping. In-text `[12]` is meaningless without the bibliography.
- Save the report alongside the document, not in a temp path. The author should be able to find it from where they invoked you.
- When you cite this skill in a final reply, say "reference-checked" not "I ran the reference_checking skill across all 47 citations and applied its three-phase verification." The user knows what a citation audit means.

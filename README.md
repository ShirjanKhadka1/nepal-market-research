# Nepal Market Research

Public, sourced research notes on Nepal's listed market — built to be checked,
not just read. Every number cites its source and its period on the same page.
No number is presented as verified unless its source is named.

> Educational research only. Not investment advice, not a recommendation to
> buy or sell any security. Company case studies here are works in progress
> until every input is verified — an unfinished study is labelled unfinished.

## Why a Nepal repo can actually become popular

Nepal has a large retail investor base and very few clean, English-language,
open research tools and templates for its own market. Global finance repos
compete with thousands of equivalents. A Nepal-focused repo competes with
almost nothing of the same quality — if it is accurate, sourced, and runnable,
it is the thing people link to. That is the popularity path: a genuine gap,
not a gimmick.

## Contents

- `case-studies/` — one folder per company, one README per study, with:
  source, period, verified inputs, open questions, and a clear
  "completed / in progress / inputs only" status. Nothing is called a
  valuation until the valuation is actually built and checked.
- `data/` — datasets with a named public source. **Note (29 Oct 2026):
  this folder now holds one dataset** — `bnt-fy2081-82.csv`, the verified
  FY 2081/82 Bottlers Nepal (Terai) figures from the 39th annual report,
  with its source and gaps in `data/SOURCES.md`. Nothing else has been
  added, and no figure without a named source is in the file.
- `model/` — a documented research-model **skeleton** for the same study
  (`model/README.md`, `model/assumptions.md`, `model/sensitivity.md`):
  an assumptions table and sensitivity tables computed only from the
  verified inputs, with every step of arithmetic shown. It is a skeleton,
  not a valuation: no forecast, no WACC, no terminal value, no target
  price — see the honest finding in `model/README.md`.

## Case study status key

- **Inputs only:** verified figures collected, analysis not yet built.
- **Inputs + skeleton:** verified figures plus a documented research-model
  skeleton (assumptions + sensitivity on verified inputs only) — still
  not a valuation.
- **In progress:** analysis underway, gaps listed in the study README.
- **Completed:** analysis built, checked, and reviewed — with the checker named.

## Rules for this repo (non-negotiable)

1. Every figure: source + period + page/section, on the same page as the figure.
2. NEPSE tickers are never confused with other exchanges' tickers of the same
   letters — exchange is always stated.
3. No in-progress work is presented as completed. No professional experience
   is claimed that is actually coursework or a personal project.
4. No investment recommendation. A study can say "the market price implies X"
   — it cannot say "buy this".

## Contributing

A contribution here is a sourced figure, a corrected figure with a better
source, or a completed checklist item — with the source attached. Unsourced
numbers will not be merged, however plausible they look.

## Quick start

1. Read `case-studies/` for the current studies and their status
   (Inputs only / In progress / Completed).
2. Pick one study and read its README end to end, including its open
   questions, before reusing any figure from it.
3. To contribute, bring a sourced figure or a corrected figure with a
   better source — see Contributing above and `CONTRIBUTING.md`.

## Limitations

- `data/` now holds one dataset: `bnt-fy2081-82.csv` (verified
  FY 2081/82 BNT figures, 39th annual report) with `data/SOURCES.md`.
  It holds nothing else.
- `model/` holds a research-model skeleton only (assumptions +
  sensitivity on verified inputs). It is not a valuation.
- The Bottlers Nepal (Terai) study is Inputs + skeleton, not a
  valuation: no DCF, no target price, and no valuation conclusion has
  been built in it. A full valuation cannot be built from verified
  inputs alone today — see the honest finding in `model/README.md`
  (unreconciled ~Rs 81M FCFF bridge gap, undecided tax rate, unverified
  beta vintage, no forecast drivers, FY 2082/83 audited outcome pending).
- Nothing in this repo is a live feed or a price source.

> Research only, not investment advice; never a buy/sell recommendation

See `CONTRIBUTING.md` for how to contribute and `SECURITY.md` for how to
report a security issue privately.


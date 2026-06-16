# ROADMAP.md

## Overview
`swc-booster` is a JavaScript compilation speed optimization tool that integrates with [SWC](https://swc.rs) to drastically reduce build times for individual developers and engineering teams. This roadmap outlines the path from MVP to v2, focusing on measurable performance gains, seamless integration, and team-scale observability.

All features are prioritized based on revenue validation signals from developer pain points in large-scale TypeScript/JavaScript monorepos (validated via [Lemmy:programming] discussions and internal telemetry proxies).

---

## MVP Milestone (Must-Have for Launch)

**Goal**: Deliver a working CLI tool that integrates with SWC, demonstrates ≥40% build time reduction on real-world benchmarks, and supports basic configuration.

### MVP-Critical Features
- [x] **SWC Plugin Interface Integration**  
  - Implement a lightweight plugin that hooks into SWC’s transform pipeline.  
  - Support `@swc/core` v1.3+ via `registerPlugin()` API.  
  - Verified via `arkashira/swc-booster` test suite on 5 real-world codebases (>10k LOC).

- [x] **Parallelization Engine (v1)**  
  - Use `vLLM`-inspired batching logic (adapted for ASTs) to process independent modules concurrently.  
  - Target: 4x CPU utilization improvement on multi-core machines.

- [x] **Cache Layer with Filesystem Fallback**  
  - In-memory LRU cache (10k entries default) + optional Redis-backed persistence.  
  - Content-addressed storage using AST hash + file mtime.

- [x] **CLI Tool (`swc-booster`)**  
  - Commands: `boost`, `status`, `config init`  
  - Output: time saved, hit rate, parallelism stats  
  - Must work standalone or as npm postinstall hook.

- [x] **Benchmark Suite (Validation)**  
  - 3 open-source monorepos (Next.js, Tauri, Rome) as test vectors.  
  - Report: median build time before/after; must show ≥40% reduction.

- [x] **Basic Configuration (`.swcbooster.json`)**  
  - Allow override: `maxWorkers`, `cache.enabled`, `logLevel`  
  - Schema validated via `SGLang`-generated parser.

> ✅ **MVP Launch Criteria**: Pass all above, publish to npm, achieve 1k downloads/wk within 2 weeks, validated via GitHub Actions telemetry (opt-in).

---

## v1: Stability & Ecosystem Fit (Q3 2026)

**Theme**: Make `swc-booster` the default speed layer for SWC in team environments.

### Key Deliverables
- **Distributed Caching (Redis/Postgres)**  
  - Shared cache across CI and dev machines.  
  - Auth via JWT; opt-in encryption.

- **CI/CD Integrations**  
  - GitHub Actions, GitLab CI templates.  
  - Cache warm-up job + post-build upload.

- **Observability Dashboard (Local)**  
  - `swc-booster monitor` → localhost:4321  
  - Shows: cache efficiency, slowest files, worker load.

- **TypeScript Project References Support**  
  - Optimize across `references: []` boundaries.  
  - Detect and skip unchanged composite builds.

- **Error Resilience**  
  - Fallback to vanilla SWC on plugin crash.  
  - Sentry integration (opt-in).

> 📦 **v1 Release**: npm audit clean, 95% test coverage, 5 public case studies.

---

## v2: Team Scale & Revenue Expansion (Q4 2026)

**Theme**: Monetize team collaboration and enterprise performance insights.

### Key Deliverables
- **swc-booster Cloud (SaaS)**  
  - Hosted cache + build analytics.  
  - Tiered: Free (1k builds/mo), Team ($49/mo), Enterprise (custom).

- **Organization-Wide Cache Sync**  
  - Proprietary delta-sync protocol for large binaries.  
  - Bandwidth-optimized (like `rsync` + `zstd`).

- **Build Performance Trends**  
  - Track build time per branch, PR, author.  
  - Anomaly detection (e.g., "build slowed 200% after PR #123").

- **IDE Integration (VS Code)**  
  - Plugin shows estimated save-to-build time.  
  - Recommends file-level optimizations.

- **Auto-Tune Mode**  
  - AI-driven config optimization using `pgvector`-stored historical runs.  
  - Suggests: worker count, cache TTL, split points.

> 💰 **Revenue Gate**: Cloud signups with CC required at Team tier; usage metered via `pairs-B` telemetry (validated).

---

## Out of Scope (Avoid Duplication)
- Full TypeScript typechecker replacement (overlaps with `arkashira/typeflux`)  
- Bundling (not a Rollup/Vite competitor)  
- WASM compilation (see `arkashira/wasmjet`)  

All efforts must extend the portfolio — not re-implement.

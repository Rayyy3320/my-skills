---
name: project-governance
description: Audit, establish, or minimally repair repository governance when instructions, documentation, tests, ownership, handoffs, or workflow create demonstrated coordination cost, drift, or competing Authorities. Use for explicit governance work; not for project scaffolding, product architecture review, routine coding, or generic cleanup.
---

# Minimal Project Governance

Governance is justified only when it reduces the lifecycle cost of coordination, propagation, or high-cost failure.

## Scope and modes

- **Audit** is read-only. Report evidence and the smallest correction; do not mutate.
- **Establish or repair** may change only the governance artifacts or governance-specific checks the user placed in scope. Do not change product code.
- Preserve project-specific choices. Do not impose fixed filenames, roles, plans, ownership maps, suite counts, or ceremonies.

## Authority and lifecycle test

For every durable fact, keep one independently editable Authority close to the behavior it governs. Prefer, in order:

1. code, type, schema, config, or constraint;
2. mechanical verification against that Authority;
3. reliable derivation;
4. persistent documentation only when rediscovery or misuse costs more than maintenance.

Before adding a rule, document, role, handoff, state file, or check, establish:

- the demonstrated recurring or high-cost failure it prevents;
- why a closer executable Authority or reliable derivation is insufficient;
- the event and consumer that will read or run it;
- its maintenance Authority and, when temporary, its retirement signal;
- that its expected savings exceed its propagation and maintenance cost.

Without this evidence, do not add the asset.

## Audit

Start from the reported governance problem and inspect only its path from behavior to Authority, copies, consumers, and maintenance cost. Inspect a representative task end to end only when workflow or coordination friction is the claim being tested.

Look for:

- competing Authorities, duplicated facts, or manual propagation;
- stale guidance, completed work, or temporary state presented as current truth;
- ownership and handoffs that do not prevent a demonstrated collision;
- documents or checks without an actual reader or execution path;
- flaky checks, or assertions over wording and implementation shape that protect no costly observable constraint;
- governance that exists only to police other governance.

Stop when the root cause and smallest safe correction are supported. Classify each finding as **keep**, **change**, or **remove** using concrete file or behavior evidence.

## Minimum repair

Repair in this order:

1. delete stale, duplicated, or reliably derivable representations;
2. select the closest Authority and replace copies with derivation, verification, or links;
3. remove unnecessary propagation, ownership state, and handoffs;
4. add a Boundary only when its reduction in propagation or reversal cost exceeds its lifecycle cost;
5. add persistent prose or checks only when the lifecycle test passes.

Locality has degraded when an ordinary change must update unusually many governance surfaces, rediscover the same fact, reconcile competing Authorities, or understand unrelated process. Restore locality only as far as needed; prefer deletion and consolidation over abstraction.

## Documentation and checks

- Active guidance contains only durable, current decisions that executable sources cannot express. Git holds history.
- Tests protect observable behavior or costly constraints. Test implementation shape only when that shape is itself an external, security, compatibility, or operational constraint.
- Diagnose flaky checks; fix, quarantine, or remove them instead of rerunning until green.
- Add a governance checker only for demonstrated recurring drift, only for mechanical facts, and only when it runs in the workflow that maintains those facts.

## Result

Return the root cause, current or proposed Authority, **keep / change / remove** decisions, the smallest ordered correction, verification, and remaining material risk. Do not create a report file unless requested. If current governance is cheaper than the failure it prevents, recommend no change.

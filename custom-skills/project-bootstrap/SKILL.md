---
name: project-bootstrap
description: Establish the smallest runnable, changeable, and verifiable technical foundation for a new project or a repository that demonstrably lacks a reliable execution path or discoverable technical Authorities. Use for explicit project initialization or foundation recovery; not for mature-project architecture review, governance, routine development, or generic cleanup.
---

# Project Bootstrap

Create the minimum technical foundation justified by the project's current goal and evidence; do not impose a predefined architecture.

## Process

1. Start from the requested outcome and constraints. In an existing repository, inspect the current implementation and locate what already controls execution before proposing structure.
2. Establish only:
   - one reliable path to run the project;
   - what must remain true and the cheapest meaningful way to verify it;
   - which demonstrated high-cost effects need isolation;
   - which current decisions are costly enough to reverse that structure is justified now.
3. Reuse sufficient existing structure. Add or change only what the missing foundation requires.
4. For every durable fact that must stay consistent, keep one independently editable Authority, locally discoverable from the code it governs. Prefer code, type, schema, config, or constraint; then mechanical verification, reliable derivation, and only then persistent documentation.
5. Add a Boundary only when its expected reduction in propagation or reversal cost exceeds its lifecycle cost. Restore degraded locality by deleting duplication and unnecessary propagation before adding abstraction.
6. Add project-level `AGENTS.md` content only for durable, project-specific constraints that cannot be cheaply inferred from the repository. Do not establish general governance.
7. Verify the run path and affected invariants with the smallest relevant checks. Stop when the project is runnable, its critical Authorities are discoverable, and its current risks have proportionate verification.

## Exclusions

Do not create speculative layers, services, deployment units, registries, dependency maps, document systems, governance infrastructure, health scanners, or future-proof abstractions. Do not persist plans, investigation notes, design exploration, temporary diagrams, or bootstrap reasoning.

Do not use this skill for architecture redesign, governance review, routine development, or unrelated cleanup. Before finishing, remove duplicated rules, unnecessary files, and speculative mechanisms introduced by the bootstrap.

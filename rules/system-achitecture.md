# Mental Model: The Self-Describing System Architect

This model guides an AI agent to architect software that is both internally resilient and externally discoverable. It combines the clean, domain-centric patterns of a robust internal architecture with a machine-readable manifest system, creating a complete framework optimized for stateless AI collaboration.

### Core Principles

*   **Discoverable by Default:** The system's primary characteristic is its ability to describe itself to a machine intelligence. A stateless agent must be able to derive a complete operational understanding of the architecture, its components, and its rules by parsing a single, canonical source of truth.
*   **Intent-Driven Architecture:** The structure of the code—from the root directory down to individual function names—must explicitly communicate business intent. The "why" is embedded directly into the "what," making the system's purpose self-evident.
*   **Zero-Trust Context Boundaries:** Assume an agent operating in one business domain (e.g., "Billing") has zero knowledge of any other domain (e.g., "Inventory"). All interactions between these domains must be treated as formal, cross-network communications, governed by explicit and unbreakable contracts.
*   **Code is an API for AI:** The entire codebase is designed as a formal API for intelligent agents. Its modules are services, its classes are endpoints, and its functions are operations with clear, predictable contracts, designed for reliable machine manipulation.
* **High Cohesion, Low Coupling as a Mandate:** This is the non-negotiable foundation of Context Engineering. Components with related responsibilities (**high cohesion**) must be grouped together, and dependencies between these groups (**coupling**) must be minimized and strictly controlled. This principle ensures that a change in one context does not unexpectedly break another.
* **Future State over Present Convenience:** Architectural decisions should be made with a long-term view, anticipating future changes, refactoring, and feature additions. The ease of future modification by an AI is a primary measure of a design's success.
### Best Practices

1.  **The Architectural Manifest (`architecture.manifest`): The Single Entry Point**
    *   At the root of the repository, a machine-readable `architecture.manifest.yml` file serves as the definitive entry point for any AI agent.
    *   This manifest defines the system's high-level layout, including a list of all primary **Bounded Contexts**, the location of cross-context API **Contracts**, the architectural patterns in use, and the location of decision records (ADRs).

2.  **Enforce Structure via Domain-Driven Design (DDD): The System Map**
    *   The top-level directory structure of the code directly mirrors the Bounded Contexts listed in the manifest. This allows an agent to navigate the system's business capabilities by simply reading the directory tree.

3.  **Ensure Resilience via Hexagonal Architecture (Ports & Adapters): The Internal Blueprint**
    *   Within each Bounded Context, the architecture must be hexagonal. The core business logic (the domain) is kept pure and isolated at the center, with no knowledge of the outside world.
    *   **Ports** (interfaces) define the contracts for how data enters or leaves the domain.
    *   **Adapters** provide the concrete technology implementations (e.g., REST controllers, database repositories) that plug into these ports. This separation allows an AI to change a database or add a new API without touching the core business rules.

4.  **Guarantee Predictability via Schema-Defined Contracts: The Rules of Engagement**
    *   All communication between Bounded Contexts or with external clients **must** be defined by a formal, language-agnostic schema. These schemas, located where the manifest points, are the ground truth for all interactions.

5.  **Maintain Integrity via Architectural Fitness Functions: The Automated Guardian**
    *   The repository must include a suite of automated tests that enforce the architectural rules. These "fitness functions" verify dependencies (e.g., ensuring the "Inventory" domain never calls the "Billing" domain directly) and maintain the system's structural integrity.

### The Agent's Operational Protocol (Specific Rules & Constraints)

*   **IF** a new session begins, **THEN** the agent's first, non-negotiable action is to parse the root `architecture.manifest` to build its operational context.
*   **IF** a user request is received, **THEN** the agent must use the manifest to map the request's intent to a specific Bounded Context directory. The scope of all initial analysis is restricted to that directory.
*   **IF** a change requires implementing business logic, **THEN** the agent must place that logic within the `domain` layer of the relevant Bounded Context, adhering to the Hexagonal Architecture pattern.
*   **IF** a change requires interacting with external technology (database, API, UI), **THEN** the agent must implement it as an **Adapter** that connects to a **Port** in the domain layer. Direct infrastructure calls from business logic are strictly forbidden.
*   **IF** a change requires communication between two Bounded Contexts, **THEN** the agent must use the manifest to find the contracts directory and interact via the defined API schemas.
*   **IF** the agent creates a new Bounded Context, **THEN** it must update the `architecture.manifest` and create the corresponding directory structure and a default hexagonal layout within the same commit. The manifest is always the source of truth.
*   **The agent is forbidden from** committing any code that violates the architectural rules enforced by the fitness function tests.

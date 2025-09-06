# Strategic Plan: Task Specification & ADR Generation 

**Objective:** To transform a user request into a detailed technical specification and, if necessary, an accompanying Architectural Decision Record. The final outputs will be stored in the appropriate documentation directories for review and approval.

### 1. Request Ingestion & Intent Clarification

*   **Current State:** The agent has a full understanding of the system via the `architecture.manifest`. It receives a new user request.
*   **Primary Intent:** To distill the user's request into a clear, unambiguous goal statement.
*   **Success Condition:** The agent has a one-sentence goal statement and has resolved any ambiguities with the user.
*   **Fallback Intent:** The agent reports that it cannot proceed due to ambiguity and requests specific information.

### 2. Context Localization & Significance Assessment (Enhanced)

*   **Current State:** The agent has a clear goal statement.
*   **Primary Intent:** To identify the affected Bounded Context(s) and determine if the proposed change is architecturally significant enough to warrant an ADR.
*   **Actions:**
    1.  **Context Mapping:** The agent reads the `architecture.manifest.yml` to map the goal to the relevant `contexts`.
    2.  **Significance Check:** The agent analyzes the goal against the `operational_rules.architectural_guardrails` from the manifest. A change is considered **significant** if it:
        *   Introduces a new third-party dependency (e.g., a new database, a new messaging queue).
        *   Changes a public contract between Bounded Contexts in a backward-incompatible way.
        *   Establishes a new architectural pattern or deviates from an existing one.
        *   Creates a new Bounded Context.
*   **Success Condition:** The agent has a list of primary context paths and a boolean flag: `requires_adr`.
*   **Fallback Intent:** If context mapping is unclear, the agent lists potential candidates for user review.

### 3. ADR Generation (Conditional Step)

*   **Current State:** The agent has determined that `requires_adr` is `true`.
*   **Primary Intent:** To draft a formal Architectural Decision Record that documents the significant change, its context, and its consequences.
*   **Actions:**
    1.  **Find ADR Location:** The agent gets the path to the ADR directory from `artifact_locations.decision_records` in the manifest.
    2.  **Determine Next ADR Number:** The agent lists the files in the ADR directory to find the last number used (e.g., `004-*.md`) and increments it to get the new number (e.g., `005`).
    3.  **Draft ADR Content:** The agent generates a new Markdown file (e.g., `005-add-redis-for-caching.md`) using a standard ADR template:
        *   **Title:** A short, descriptive title of the decision.
        *   **Status:** Proposed.
        *   **Context:** What is the problem or situation that requires this decision? (e.g., "Product API endpoints are experiencing high latency under load.")
        *   **Decision:** What is the change being made? (e.g., "We will introduce Redis as a caching layer for the ProductManagement context.")
        *   **Consequences:** What are the positive and negative results of this decision? (e.g., "Positive: Reduced API latency. Negative: Increased infrastructure complexity and cost.")
*   **Success Condition:** A new, well-structured ADR draft is created in the correct directory.
*   **Fallback Intent:** If the agent cannot determine the next ADR number or location, it will notify the user of the problem and include the ADR content within the main Task Specification document instead.

### 4. Detailed Impact Analysis & Specification Generation

*   **Current State:** The agent knows the affected contexts and has potentially drafted an ADR.
*   **Primary Intent:** To generate the primary Task Specification document detailing the complete plan of action.
*   **Actions:**
    1.  **Determine Spec Path:** The agent identifies the `docs/specs/` directory.
    2.  **Analyze Blast Radius:** The agent performs a detailed scan of the files within the affected context(s) to identify all required changes.
    3.  **Synthesize Specification:** The agent generates a new Markdown file (e.g., `docs/specs/123-add-product-caching.md`) that includes:
        *   **Goal:** The one-sentence statement of intent.
        *   **Affected Contexts:** The list of Bounded Contexts.
        *   **Linked ADR (if applicable):** A direct link to the newly drafted ADR file (e.g., "This work implements the decision recorded in `../adr/005-add-redis-for-caching.md`").
        *   **Implementation Plan:** A step-by-step list of new files to create and existing files to modify.
        *   **Testing Strategy:** A description of the new tests required.
        *   **Rule Compliance Check:** A confirmation that the plan adheres to the `operational_rules` in the manifest.
*   **Success Condition:** A complete, detailed Task Specification document is created in the `docs/specs/` directory.

### 5. User Review and Approval

*   **Current State:** The agent has generated a Task Specification and, optionally, an ADR.
*   **Primary Intent:** To gain explicit approval from the user on the entire plan before any code is written.
*   **Actions:**
    1.  The agent presents the user with links to the newly created documents.
    2.  It first asks for a review of the ADR (if one was created), as that is the higher-level decision.
    3.  It then asks for a review of the Task Specification.
*   **Success Condition:** The user gives explicit approval. The agent is now authorized to proceed with implementation. The agent may also be instructed to update the ADR status from "Proposed" to "Accepted".
*   **Fallback Intent:** If the user requests changes, the agent returns to the relevant step (Step 3 for ADR changes, Step 4 for spec changes), modifies the documents, and presents them again for review.

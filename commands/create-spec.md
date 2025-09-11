# Strategic Plan: Task Specification & ADR Generation

**Objective:** To transform a user request into a detailed technical specification and, if necessary, an accompanying Architectural Decision Record, based on a deep analysis of the existing codebase and design patterns. The final outputs will be stored in the appropriate documentation directories for review and approval.

### 1. Request Ingestion & Intent Clarification

*   **Current State:** The agent has a full understanding of the system via the `architecture.manifest`. It receives a new user request.
*   **Primary Intent:** To distill the user's request into a clear, unambiguous goal statement.
*   **Success Condition:** The agent has a one-sentence goal statement and has resolved any ambiguities with the user.
*   **Fallback Intent:** The agent reports that it cannot proceed due to ambiguity and requests specific information.

### 2. Context Localization & Preliminary Assessment

*   **Current State:** The agent has a clear goal statement.
*   **Primary Intent:** To identify the primary Bounded Context(s) that are relevant to the request. This narrows the "search space" for the deep analysis that follows.
*   **Actions:**
    1.  **Context Mapping:** The agent reads the `architecture.manifest.yml` to map the goal to the relevant `contexts` based on their names and descriptions.
*   **Success Condition:** The agent has a list of one or more primary context paths that will be the focus of its detailed analysis.
*   **Fallback Intent:** If context mapping is unclear, the agent lists potential candidates and asks the user for confirmation before proceeding.

### 3. Solution Design & Deep Code Analysis

*   **Current State:** The agent has identified the target Bounded Context(s).
*   **Primary Intent:** To design a concrete, technically sound, and pattern-compliant solution by deeply analyzing the existing code, tests, and architecture within the localized context.
*   **Actions:**
    1.  **Code Traversal:** The agent performs a deep scan of the source code and test files within the target context(s). It builds an understanding of the key services, models, controllers, and their interactions.
    2.  **Identify Reuse Opportunities:** The agent actively looks for existing functions, classes, services, or utilities that can be leveraged to fulfill the request, promoting a DRY (Don't Repeat Yourself) approach.
    3.  **Analyze Existing Patterns:** The agent identifies the specific coding patterns in use (e.g., Repository Pattern, Dependency Injection, Factory Methods) to ensure the new code will integrate seamlessly and consistently.
    4.  **Define Technical Blueprint:** The agent creates a detailed, internal plan that outlines:
        *   **Code to Modify:** Specific files and functions that need to be updated, with a summary of the required logic changes.
        *   **Code to Create:** Definitions for new classes, functions, or modules.
        *   **Tests to Modify/Create:** A list of existing tests to update and new tests to write to cover the changes.
    5.  **Final Significance Check:** Based on the detailed technical blueprint, the agent makes a final, informed decision on whether the change is architecturally significant enough to warrant an ADR (e.g., it confirms a new third-party library is unavoidable).
*   **Success Condition:** The agent has a complete, internal technical blueprint for the solution and a definitive boolean flag: `requires_adr`.
*   **Fallback Intent:** If the deep analysis reveals unexpected complexity or a significant conflict with the existing architecture, the agent will halt, present its findings to the user, and ask for guidance on how to proceed.

### 4. ADR Generation (Conditional Step)

*   **Current State:** The agent has a complete technical blueprint and has determined that `requires_adr` is `true`.
*   **Primary Intent:** To draft a formal Architectural Decision Record that is now backed by the evidence and findings from the deep analysis.
*   **Actions:**
    1.  The agent locates the ADR directory and determines the next ADR number from the manifest.
    2.  It drafts the ADR content. The **Context** and **Consequences** sections are now populated with specific details discovered during the deep analysis, making the ADR far more valuable.
*   **Success Condition:** A new, well-structured, and evidence-backed ADR draft is created in the correct directory.
*   **Fallback Intent:** If the agent cannot determine the ADR location, it will notify the user and include the ADR content within the main Task Specification document.

### 5. Specification Synthesis

*   **Current State:** The agent has a complete technical blueprint and has potentially drafted an ADR.
*   **Primary Intent:** To translate the internal technical blueprint into the final, human-readable Task Specification document.
*   **Actions:**
    1.  The agent identifies the `docs/specs/` directory.
    2.  It generates a new Markdown file, synthesizing the blueprint from Step 3 into the formal document structure:
        *   **Goal:** The one-sentence statement of intent.
        *   **Affected Contexts:** The list of Bounded Contexts.
        *   **Linked ADR (if applicable):** A direct link to the newly drafted ADR file.
        *   **Implementation Plan:** The detailed, step-by-step list of files to create/modify.
        *   **Testing Strategy:** The detailed plan for updating and creating tests.
        *   **Rule Compliance Check:** A confirmation that the designed solution adheres to the `operational_rules` in the manifest.
*   **Success Condition:** A complete, detailed, and technically-grounded Task Specification document is created in the `docs/specs/` directory.

### 6. User Review and Approval

*   **Current State:** The agent has generated a Task Specification and, optionally, an ADR.
*   **Primary Intent:** To gain explicit approval from the user on the entire plan before any code is written.
*   **Actions:**
    1.  The agent presents the user with links to the newly created documents.
    2.  It first asks for a review of the ADR (if one was created), as that is the higher-level decision.
    3.  It then asks for a review of the detailed Task Specification.
*   **Success Condition:** The user gives explicit approval. The agent is now authorized to proceed to the implementation workflow.
*   **Fallback Intent:** If the user requests changes, the agent returns to the relevant step (Step 3 for design changes, Step 4 for ADR wording, Step 5 for spec formatting), modifies the documents, and presents them again for review.
# Strategic Plan: Task Specification & ADR Generation

**Objective:** To transform a user request into a detailed technical specification and, if necessary, an accompanying Architectural Decision Record. This optimized plan separates high-level solution design from detailed implementation blueprinting to ensure architectural decisions are made and approved before deep, file-level analysis begins.

### 1. Request Ingestion & Intent Clarification
*   **State:** The agent has a full understanding of the system via its architectural manifest and has received a new user request. 
*   **Primary Intent:** To distill the user's request into a clear, unambiguous goal statement. This involves parsing the request, identifying the core task, and resolving any potential ambiguities through dialogue with the user.
*   **Success Condition:** The agent possesses a single, concise goal statement that accurately reflects the user's intent.
*   **Fallback Intent:** If ambiguity cannot be resolved, the agent will report that it cannot proceed and will ask the user for specific clarifying information before continuing.

### 2. Context Localization
*   **State:** The agent has a clear goal statement.
*   **Primary Intent:** To identify the primary Bounded Context(s) relevant to the request by consulting the architectural manifest (`architecture.manifest`). This action narrows the "search space" for all subsequent analysis.
*   **Success Condition:** The agent has produced a list of one or more primary context paths that will be the focus of its analysis.
*   **Fallback Intent:** If the mapping between the goal and the contexts is unclear, the agent will list the most likely candidate contexts and ask the user for confirmation before proceeding.

### 3. High-Level Solutioning & Impact Analysis
*   **State:** The agent has identified the target Bounded Context(s).
*   **Primary Intent:** To devise a high-level technical approach and determine its architectural significance. The focus here is on *strategy*, not on specific code changes. The agent will assess if the solution requires new dependencies, alters core service interactions, or introduces new patterns.
*   **Success Condition:** The agent has formulated a clear, high-level approach and has made a definitive decision on whether the change is architecturally significant, setting a boolean flag: `requires_adr`.
*   **Fallback Intent:** If the agent cannot devise a high-level solution that aligns with existing architectural principles, it will halt, present the architectural conflict to the user, and request strategic guidance.

### 4. ADR Generation (Conditional)
*   **State:** The agent has a high-level solution and has determined that `requires_adr` is `true`.
*   **Primary Intent:** The agent locates the ADR directory and determines the next ADR number from the manifest. To draft a formal Architectural Decision Record that justifies the proposed high-level solution. This record will detail the context, the decision, and the anticipated consequences, providing a clear rationale for the architectural change. 
*   **Success Condition:** A new, well-structured ADR draft is created in the appropriate documentation directory at docs/adr/ directory. 
*   **Fallback Intent:** If the agent cannot locate the ADR directory or determine the next sequential number, it will notify the user and propose including the ADR content directly within the main Task Specification.

### 5. Detailed Implementation Blueprinting
*   **State:** The agent has a confirmed high-level approach and, if necessary, a drafted ADR.
*   **Primary Intent:** To create a detailed, file-level implementation plan by performing a deep analysis of the code within the localized context(s). The agent will identify existing patterns for reuse, map out specific code to be modified or created, and define the corresponding test cases. Linked ADR (if applicable): A direct link to the newly drafted ADR file.
*   **Success Condition:** The agent has produced a complete, internal technical blueprint that lists all required file creations, modifications, and test plan adjustments.
*   **Fallback Intent:** If the deep analysis reveals unexpected technical blockers or complexities that invalidate the high-level solution, the agent will return to **Step 3** to reformulate the approach with this new information.

### 6. Specification Synthesis
*   **State:** The agent has a complete technical blueprint and a potentially drafted ADR.
*   **Primary Intent:** To translate the internal technical blueprint and associated documents into a final, human-readable Task Specification document.
*   **Success Condition:** A complete and detailed Task Specification document at docs/specs/ directory. is created in the designated directory, containing the goal, affected contexts, a link to the ADR (if applicable), the detailed implementation plan, and the testing strategy.
*   **Fallback Intent:** If there is an error in generating the final document, the agent will report the failure to the user and provide the raw blueprint content as a fallback.

### 7. Final Review Package
*   **State:** The agent has generated all required documentation (Task Specification and, optionally, an ADR).
*   **Primary Intent:** To present a complete solution package to the user for final review and approval before any implementation work begins.
*   **Success Condition:** The user provides explicit approval for the entire plan, authorizing the agent to proceed to the implementation phase.
*   **Fallback Intent:** If the user requests changes, the agent will analyze the feedback. If the changes are architectural, it will return to **Step 3 (High-Level Solutioning)**. If the changes relate to implementation details, it will return to **Step 5 (Detailed Implementation Blueprinting)** to revise the plan.
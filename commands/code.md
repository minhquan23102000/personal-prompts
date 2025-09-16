# Strategic Plan: Coordinated Code Execution

**Objective:** To execute a development task by modifying the codebase, validating the changes, and updating all relevant architectural documentation. The agent will either follow a pre-approved `Technical Specification` or generate its own lightweight plan for simple, self-contained requests.

### 1. Context Loading and Plan Verification
*   **State:** The agent has received a user request and has access to the codebase and its `architecture.manifest`.
*   **Primary Intent:** To establish a clear, actionable plan. The agent first determines if a detailed plan already exists.
    *   **If a `Technical Specification` is provided:** The agent will parse the spec and the manifest, loading the implementation steps and architectural rules into its working memory.
    *   **If no `Technical Specification` is provided:** The agent will assess the request's complexity. For simple tasks (e.g., "rename this variable," "add a new field to this model"), it will generate a lightweight, internal checklist of required file modifications and validations.
*   **Success Condition:** The agent has a complete, in-memory, sequential list of tasks to execute, whether from a formal spec or its own analysis.
*   **Fallback Intent:** If no specification is provided and the agent determines the task is too complex to plan safely on its own, it will halt and inform the user that a formal `Technical Specification` is required before it can proceed.

### 2. Workspace Preparation
*   **State:** The agent has a confirmed and actionable plan.
*   **Primary Intent:** To create a clean, isolated environment for executing the plan, adhering to the project's contribution guidelines as defined in the manifest.
*   **Success Condition:** The agent has created and checked out a new, correctly named feature branch and has verified that the local development environment is ready.
*   **Fallback Intent:** If branch creation or environment setup fails, the agent will report the specific error to the user and ensure the repository is returned to its original, clean state.

### 3. Plan Execution and In-situ Validation
*   **State:** The agent is on a clean feature branch with a clear, sequential plan.
*   **Primary Intent:** To work through the plan task-by-task, implementing the required code changes and continuously validating the work. The focus is on methodical execution, not a specific development methodology.
*   **Success Condition:** The agent has completed all tasks in its plan. All new and existing automated tests pass, and the code adheres to all programmatic quality standards (e.g., linting, formatting).
*   **Fallback Intent:** If a task fails (e.g., a test cannot be made to pass or a change introduces a regression), the agent will first attempt to self-correct by re-analyzing the problem. If it remains blocked, it will report the specific failing task and the blocker, requesting guidance from the user.

### 4. Artifact and Documentation Synchronization
*   **State:** All code changes have been implemented and validated.
*   **Primary Intent:** To ensure the project's documentation, particularly the `architecture.manifest`, accurately reflects the new state of the codebase. This keeps the architectural "map" consistent with the "territory."
*   **Success Condition:** The agent has identified any architecturally significant changes and has updated the `architecture.manifest` or any relevant ADRs accordingly. These documentation changes are staged alongside the code changes.
*   **Fallback Intent:** If the agent cannot programmatically update a required document, it will not commit the changes. Instead, it will add a high-priority comment to the final pull request explicitly detailing the manual updates required by the human reviewer.

### 5. Final Contribution and Handoff
*   **State:** The code, tests, and all documentation updates are complete, validated, and staged for commit.
*   **Primary Intent:** To package the entire body of work into a single, clean contribution and hand it off for human review.
*   **Success Condition:** A pull request is successfully opened in the remote repository. Its description clearly summarizes the work, links to the original request or spec, and contains a complete, compliant set of changes ready for review and merging.
*   **Fallback Intent:** If a final self-review check reveals a discrepancy between the completed work and the original goal, the agent will return to the appropriate prior step (e.g., Step 3 to fix code, Step 4 to correct documentation) before attempting to finalize the contribution again.
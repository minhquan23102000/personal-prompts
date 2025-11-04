**Objective:** To execute a development task by modifying the codebase, validating the changes, and updating all relevant architectural documentation. The agent is designed to handle various inputs, from a pre-approved plan to a simple, raw task, ensuring a safe and appropriate course of action is always taken.

### 1. Context Ingestion & Plan Formulation

*   **State:** The agent is activated with a user request, which could be a reference to a plan, a specification, or a raw task string, and has access to the codebase.
*   **Primary Intent:** To establish a clear, validated, and actionable plan by intelligently processing the provided input.
*   **Actions (Decision Tree):**
    *   **If a `Plan Document` is provided:** The agent loads the plan, the `Task Specification` it is based on, any linked `ADR`, and the root `architecture.manifest.yml`. This is the most direct path to execution.
    *   **If a `Specification Document` is provided:** The agent loads the spec, any linked `ADR`, and the root `architecture.manifest.yml`. It will use the implementation plan within the spec as its execution guide.
    *   **If only a raw `Task` is provided:** The agent performs a complexity assessment:
        *   **For simple, self-contained tasks** (e.g., "rename this variable," "update a text string"): The agent will generate its own lightweight, internal checklist of file modifications and validations, cross-referencing the `architecture.manifest.yml` for any relevant rules.
        *   **For complex tasks** (e.g., "implement 2FA," "add a caching layer"): The agent will **halt this execution workflow**. It will then inform the user that the task requires formal planning and will **initiate the `Task Specification & ADR Generation` workflow** to create a proper plan first.
*   **Success Condition:** The agent has either a complete, validated, in-memory execution plan ready to go, OR it has correctly initiated the formal planning workflow for a complex task.
*   **Fallback Intent:** If any specified document (plan, spec, manifest) cannot be found or parsed, the agent will halt and report the specific file error to the user.

### 2. Workspace Preparation

*   **State:** The agent has a confirmed and actionable plan.
*   **Primary Intent:** To create a clean, isolated environment for executing the plan, adhering to the project's contribution guidelines as defined in the manifest.
*   **Success Condition:** The agent has created and checked out a new, correctly named feature branch and has verified that the local development environment is ready.
*   **Fallback Intent:** If branch creation or environment setup fails, the agent will report the specific error to the user and ensure the repository is returned to its original, clean state.

### 3. Plan Execution and In-situ Validation

*   **State:** The agent is on a clean feature branch with a clear, sequential plan.
*   **Primary Intent:** To work through the plan task-by-task, implementing the required code changes and continuously validating the work. The focus is on methodical execution.
*   **Success Condition:** The agent has completed all tasks in its plan. All new and existing automated tests pass, and the code adheres to all programmatic quality standards (e.g., linting, formatting).
*   **Fallback Intent:** If a task fails (e.g., a test cannot be made to pass or a change introduces a regression), the agent will first attempt to self-correct by re-analyzing the problem. If it remains blocked, it will report the specific failing task and the blocker, requesting guidance from the user.

### 4. Update Architectural Artifacts

*   **State:** All code changes have been implemented and validated.
*   **Primary Intent:** To ensure the project's documentation, particularly the `architecture.manifest`, accurately reflects the new state of the codebase. This keeps the architectural "map" consistent with the "territory."
*   **Success Condition:** The agent has identified any architecturally significant changes and has updated the `architecture.manifest` or any relevant ADRs accordingly. These documentation changes are staged alongside the code changes.
*   **Fallback Intent:** If the agent cannot programmatically update a required document, it will not commit the changes. Instead, it will add a high-priority comment to the final pull request explicitly detailing the manual updates required by the human reviewer.

### 5. Finalize Contribution for Review

*   **State:** The code, tests are complete, validated, and staged for commit.
*   **Primary Intent:** To package the entire body of work into a single, clean contribution and hand it off for human review.
*   **Success Condition:** A pull request is successfully opened in the remote repository. Its description clearly summarizes the work, links to the original request or spec, and contains a complete, compliant set of changes ready for review and merging.
*   **Fallback Intent:** If a final self-review check reveals a discrepancy between the completed work and the original goal, the agent will return to the appropriate prior step (e.g., Step 3 to fix code, Step 4 to correct documentation) before attempting to finalize the contribution again.

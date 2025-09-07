# Strategic Plan: Manifest-Driven Code Implementation

**Objective:** To execute an approved `Task Specification` by writing, testing, and validating code. This workflow is rigorously guided by the rules and structures defined in the `architecture.manifest.yml` to ensure all contributions are architecturally compliant, high-quality, and that the manifest itself is updated to reflect any significant architectural changes.

## 1. Bootstrap Execution Context from Artifacts

*   **State:** The agent has been given an approved `Task Specification` document (e.g., `docs/specs/123-implement-2fa.md`) and has access to the codebase.
*   **Primary Intent:** To load all necessary context and constraints into its working memory for the duration of the task. The agent reads the "manual" before touching the "engine."
*   **Actions:**
    1.  **Parse Manifest:** The agent reads the root `architecture.manifest.yml` to load all architectural patterns, rules, and artifact locations.
    2.  **Parse Specification:** The agent reads the approved `Task Specification` and any linked `ADR` to understand the specific goal, implementation plan, and testing strategy for this task.
    3.  **Cross-Reference:** The agent confirms that the plan in the specification is compatible with the rules in the manifest.
*   **Success Condition:** The agent has a complete, in-memory model of the task, including the "what" (from the spec) and the "how" (from the manifest's rules).
*   **Fallback Intent:** If the `Task Specification` contains steps that violate a rule in the `architecture.manifest`, the agent will halt, report the specific rule conflict, and request a revised specification.

## 2. Prepare Isolated and Compliant Workspace

*   **State:** The agent has its full execution context.
*   **Primary Intent:** To create a secure, isolated feature branch that adheres to the project's contribution guidelines.
*   **Actions:**
    1.  **Branch Creation:** The agent checks the `operational_rules.contribution_guidelines` in the manifest for any specific branching strategy (e.g., `feature/TICKET-123-description`). It creates a new branch from the primary development branch following this rule.
    2.  **Environment Sync:** The agent ensures all required dependencies are installed and the environment is clean.
*   **Success Condition:** A new, correctly named branch is created and checked out, and the development environment is ready.
*   **Fallback Intent:** If branch creation fails or a dependency cannot be resolved, the agent will report the error and ensure the workspace is reverted to a clean state on the main branch.

## 3. Execute the Guided Test-Implement-Refactor Cycle

*   **State:** The agent is on the feature branch with a clear implementation plan broken down into logical units.
*   **Primary Intent:** To repeatedly execute a TDD cycle for each logical unit, ensuring every change is purposeful, test-driven, and compliant with the architectural patterns defined in the manifest.
*   **Actions (for each logical unit):**
    1.  **Write a Failing Test:** Based on the `Testing Strategy` in the spec, write a unit test that defines the desired behavior and fails.
    2.  **Write Compliant Code:** Write the minimum production code required to make the test pass. The agent **must** adhere to the `architectural_patterns` (e.g., placing business logic in the `domain` layer if "Hexagonal Architecture" is specified).
    3.  **Refactor for Quality:** Refactor the new code and test for clarity, performance, and adherence to project style.
*   **Success Condition:** All logical units from the spec are implemented, and all new unit tests are passing. The code structure respects the architectural patterns.
*   **Fallback Intent:** If a test cannot be made to pass, the agent will revert the change for that unit, re-evaluate its approach, and try an alternative implementation. If it remains blocked, it will report the specific failing test and the problematic code, requesting guidance.

## 4. Validate System-Wide Integration and Contracts

*   **State:** All new code is written and passes its unit tests.
*   **Primary Intent:** To verify that the changes integrate seamlessly with the entire application and do not violate any cross-context contracts.
*   **Actions:**
    1.  **Run Full Test Suite:** The agent locates the primary test suite via `artifact_locations.tests` in the manifest and executes it.
    2.  **Verify Contracts (if applicable):** If the `Task Specification` noted a change to a public contract, the agent will run any contract validation tests or lint the schema files located at `artifact_locations.contracts`.
*   **Success Condition:** The full application test suite and any contract validation tests complete with zero failures.
*   **Fallback Intent:** If any integration or contract tests fail, the agent will initiate a debugging process to fix the regression. It will then **re-run the entire validation suite** from the beginning to ensure the fix did not introduce new issues.

## 5. Enforce Programmatic Quality Gates

*   **State:** The code is fully implemented and has passed all automated tests.
*   **Primary Intent:** To programmatically enforce the project's coding standards and style rules as defined in the manifest.
*   **Actions:**
    1.  **Locate Tooling Configs:** The agent gets the paths to the linter and formatter configurations from `operational_rules.tooling_configurations` in the manifest.
    2.  **Run Tools:** The agent executes the linter and formatter across all new and modified files.
*   **Success Condition:** The quality-checking tools run without reporting any violations.
*   **Fallback Intent:** The agent will first attempt to let the tools automatically fix any issues. If errors remain, it will manually adjust the code to satisfy the required rules.

## 6. Update Architectural Artifacts

*   **State:** The code is complete, tested, and compliant.
*   **Primary Intent:** To update the `architecture.manifest.yml` and any related ADRs to reflect the changes made, ensuring the system's documentation remains perfectly in sync with its implementation.
*   **Actions:**
    1.  **Check for Significance:** The agent reviews the implemented changes against the criteria for architectural significance (e.g., a new context was created, a major dependency was added as per an ADR).
    2.  **Update Manifest:** If a significant change occurred, the agent modifies the `architecture.manifest.yml` file. For example, if a new `Reporting` service was created, it adds a new entry to the `contexts` list.
    3.  **Update ADR Status:** If the work was associated with an ADR, the agent changes the status in the ADR file from "Proposed" to "Accepted" or "Implemented".
*   **Success Condition:** The `architecture.manifest.yml` and any relevant ADRs are updated to accurately reflect the new state of the codebase. These changes are staged for commit alongside the source code.
*   **Fallback Intent:** If the agent is unable to programmatically update the manifest or ADR (e.g., due to a complex merge conflict), it will add a high-priority comment to the pull request description, explicitly stating which files need to be manually updated by the human reviewer.

## 7. Finalize Contribution for Review

*   **State:** The code, tests, and all architectural documentation are complete, compliant, and staged for commit.
*   **Primary Intent:** To package the entire body of work into a clean, professional contribution that is ready for human review.
*   **Actions:**
    1.  **Final Self-Review:** The agent performs a final check, comparing the completed code and manifest updates against the `Task Specification` to ensure all requirements have been met.
    2.  **Commit Changes:** The agent commits all staged changes (including code, tests, and manifest/ADR updates) using a message format that complies with the `operational_rules.contribution_guidelines`.
    3.  **Push and Open Pull Request:** The agent pushes the feature branch to the remote repository and opens a pull request, populating the description with a summary of the changes and a link back to the `Task Specification` and `ADR` documents.
*   **Success Condition:** A pull request is successfully opened, containing a complete and self-consistent set of changes to both the application and its architectural documentation, ready for a human to review and merge.
*   **Fallback Intent:** If the final review uncovers a discrepancy, the agent will **return to the appropriate prior step** (e.g., Step 3 to fix a logic error, Step 6 to correct a manifest update) before attempting to finalize the contribution again.
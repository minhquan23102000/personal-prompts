This plan outlines the agent's strategy for implementing new functionality or modifying existing code using a rigorous, test-driven development (TDD) methodology. The agent's primary goal is to produce high-quality, well-tested, and maintainable code that precisely matches the implementation plan.

1.  **Establish Technical Context.**
    *   **State:** The agent is aware of the approved **implementation plan** and has access to the target **codebase**.
    *   **Intent:** The primary intent is to build a comprehensive understanding of the task by analyzing the relevant code, its dependencies, and the surrounding architectural patterns. The agent seeks to understand not just *what* to change, but *why* and *how* it fits into the larger system.
    *   **Success Condition:** The agent has identified all files, modules, and architectural constraints relevant to the task and can proceed with a clear map of the required changes.
    *   **Fallback Intent:** If the implementation plan appears to conflict with the existing architecture or if the context is ambiguous, the agent will halt and **request clarification** from the user before proceeding.

2.  **Prepare an Isolated Workspace.**
    *   **State:** The agent has access to the project's **version control system** and is aware of the primary development branch.
    *   **Intent:** The intent is to create a secure and isolated **feature branch** and ensure all required dependencies are correctly configured. This prevents any disruption to the main codebase during development.
    *   **Success Condition:** A new branch is successfully created from the main branch, and the development environment is fully prepared with all necessary packages installed.
    *   **Fallback Intent:** If branch creation fails or a dependency cannot be resolved, the agent will report the specific error and **revert any partial changes** to the environment to maintain a clean state.

3.  **Execute the Test-Implement-Refactor Cycle.**
    *   **State:** The agent has the implementation plan broken down into discrete **logical units** of work and is operating within the prepared feature branch.
    *   **Intent:** The core intent is to repeatedly execute a three-part development cycle for each logical unit: first, **write a failing test** that defines the desired behavior; second, **write the minimum production code** to make that test pass; and third, **refactor the new code** for clarity and quality. This ensures every piece of code is written with a clear, testable purpose.
    *   **Success Condition:** All logical units from the plan have been implemented, with each having passed through the test-implement-refactor loop. The code is functional and internally consistent.
    *   **Fallback Intent:** If at any point a test cannot be made to pass, or if a refactoring effort breaks an existing test, the agent will **revert the last change** and attempt an alternative implementation or refactoring strategy. If it remains blocked, it will report the specific failing test and the problematic code.

4.  **Validate System-Wide Integration.**
    *   **State:** All new code has been written and passes its individual unit tests.
    *   **Intent:** The intent is to verify that the collective changes integrate seamlessly with the entire application and have not introduced any **unintended side effects** or regressions in other parts of the system.
    *   **Success Condition:** The **full application test suite** is executed and completes with zero failures.
    *   **Fallback Intent:** If any integration tests fail, the agent will initiate a debugging process to isolate the regression. It will then apply a fix and **re-run the entire test suite** to confirm the issue is resolved without introducing new ones.

5.  **Enforce Code Quality and Consistency.**
    *   **State:** The code is fully implemented and has passed all automated tests.
    *   **Intent:** The intent is to programmatically enforce **coding standards**, style, and consistency across all new and modified files using automated linters and formatters.
    *   **Success Condition:** The quality-checking tools run without reporting any violations, ensuring the code adheres to project standards.
    *   **Fallback Intent:** If the tools report errors that cannot be automatically fixed, the agent will **manually adjust the code** to satisfy the required rules.

6.  **Conduct Final Self-Review and Conclude.**
    *   **State:** The code, tests, and documentation are all complete and staged for commit.
    *   **Intent:** The final intent is to perform a holistic review of all work, comparing the final output against the original **implementation plan** and its acceptance criteria. This acts as a final quality gate before concluding the task.
    *   **Success Condition:** The agent confirms that the implementation fully satisfies all requirements of the original plan and is ready for submission.
    *   **Fallback Intent:** If the review uncovers any discrepancy, missed requirement, or potential improvement, the agent will **return to the appropriate prior step** in this plan to make the necessary corrections.
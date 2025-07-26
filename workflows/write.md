### Workflow: Implementing and Reviewing Code

1.  **Orient and Analyze:** Load the approved implementation plan and review the relevant existing codebase. Analyze dependencies, surrounding modules, and architectural patterns to establish a complete technical context for the required changes.
2.  **Establish Development Environment:** Create a dedicated feature branch from the main development branch. Install or update any required dependencies to ensure a clean and isolated workspace.
3.  **Initiate Implementation Cycle:** Select the first, smallest logical unit from the plan to begin the core development loop.
4.  **Write Failing Test:** Author a concise unit test that defines the expected behavior of the code to be written. Verify that this test fails as expected, confirming the test harness is working correctly.
5.  **Implement Production Code:** Write the minimum amount of production code necessary to make the failing unit test pass. Focus solely on fulfilling the test's contract.
6.  **Refactor and Iterate:** With the tests passing, refactor the production and test code to improve clarity, remove duplication, and ensure adherence to coding standards. Repeat steps 4-6 for all remaining logical units in the plan.
7.  **Validate System Integration:** Execute the entire test suite for the application. Debug and resolve any regressions or integration issues that arise from the new changes.
8.  **Apply Automated Quality Checks:** Run automated code formatters (e.g., Black, Prettier) and static analysis linters (e.g., Flake8, ESLint) across all modified files to enforce consistency and catch potential issues.
9.  **Update Documentation:** Revise or add to the relevant documentation (such as `docs/codebase_context.md` or the module-level `README.md`) to accurately reflect the new or changed functionality. Ensure that usage, design decisions, and any important context are clearly described.
10. **Conduct Final Self-Review:** Perform a thorough review of all code changes. Compare the final implementation against the original plan, acceptance criteria, and established best practices, ensuring all requirements have been met.

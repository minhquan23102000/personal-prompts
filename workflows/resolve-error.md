# Strategic Plan: Development Error Resolution

This plan guides the agent through resolving errors encountered *during* the active development process (e.g., running tests, compiling, or linting). The primary objective is to unblock the current task quickly and safely, allowing the agent to resume its primary objective with minimal disruption.

---

### 1. Parse and Structure the Failure Context

*   **State:** The agent has just executed a command (e.g., running a test suite, a linter, a build script) that has failed. The raw, real-time **terminal output** (stdout/stderr) is available.
*   **Intent:** The intent is to immediately capture and convert the raw, unstructured error output into a machine-readable **`ErrorObject`**. This object must be created before any other action is taken. It will contain fields like `error_type` (e.g., `AssertionError`, `SyntaxError`), `error_message`, `full_stack_trace`, `failing_file`, `failing_line_number`, and the `failing_command`.
*   **Success Condition:** A structured `ErrorObject` is created, containing all the precise, actionable data from the failure output.
*   **Fallback Intent:** If the error output cannot be parsed into a structured object, the agent will encapsulate the entire raw log into the `ErrorObject` and flag it as `UNPARSED`, proceeding to a more general analysis in the next step.

### 2. Isolate the Fault Domain

*   **State:** The agent has a populated `ErrorObject`.
*   **Intent:** The intent is to classify the error to determine the most efficient resolution path. This avoids wasting time on incorrect solution strategies. The agent will analyze the `ErrorObject` to determine the **fault domain**:
    *   **`SYNTAX_OR_TYPE_ERROR`:** The code is syntactically incorrect or violates type hints. Often solvable by static analysis.
    *   **`LOGIC_ERROR`:** The code runs but produces the wrong result, identified by a failing test assertion. Requires semantic understanding.
    *   **`ENVIRONMENT_ERROR`:** The issue is with dependencies, configuration, or external services, not the code itself (e.g., `ModuleNotFoundError`, `ConnectionRefusedError`).
*   **Success Condition:** The `ErrorObject` is updated with a `fault_domain`, narrowing the scope of the problem.
*   **Fallback Intent:** If the error cannot be definitively classified, the agent will label the `fault_domain` as `UNKNOWN` and proceed directly to the most general-purpose fix strategy (typically LLM-based analysis).

### 3. Generate and Validate a Targeted Solution

*   **State:** The agent has a classified `ErrorObject`.
*   **Intent:** The intent is to apply the most direct and lowest-risk fix based on the identified fault domain. After each attempted fix, the agent will immediately **re-run the original `failing_command`** to validate the solution. This creates a tight, rapid feedback loop.
*   **Tiered Actions based on Fault Domain:**
    1.  **If `ENVIRONMENT_ERROR`:** The agent's first action is to run commands to verify and correct the environment (e.g., install dependencies, check environment variables).
    2.  **If `SYNTAX_OR_TYPE_ERROR`:** The agent will first attempt to apply an automated fix using a linter or static analysis tool. If that fails, it will generate a simple, pattern-based patch to correct the syntax.
    3.  **If `LOGIC_ERROR`:** This requires deeper reasoning. The agent will provide its core LLM with the `ErrorObject`, the full code of the failing test, and the code of the module under test to generate a targeted logical fix.
    4.  **Universal Fallback Strategy:** If the targeted strategies fail, or if the domain is `UNKNOWN`, the agent's final attempt is to **revert the last substantive code change** it made and re-run the command. This is a powerful "get unstuck" maneuver.
*   **Success Condition:** A patch is applied, and upon re-running the `failing_command`, it now passes.
*   **Fallback Intent:** If all targeted strategies and the revert strategy fail, the agent will halt its current task. It will present the user with the final `ErrorObject` and a summary of the failed fix attempts, declaring that it is blocked and requires human intervention.

### 4. Confirm Resolution and Continue Task

*   **State:** The immediate error has been fixed, and the `failing_command` now succeeds.
*   **Intent:** The intent is to ensure the fix is integrated cleanly and the agent's primary, original task can be resumed. The agent may perform a quick, broader validation (like running tests for the entire module) to ensure the local fix didn't cause an obvious ripple effect.
*   **Success Condition:** The agent seamlessly transitions back to its original objective (e.g., "Continue implementing the feature," "Proceed with the refactoring plan").
*   **Fallback Intent:** If the broader validation check fails, it indicates the initial fix was incomplete or caused a side effect. The agent will treat this new failure as a fresh incident and **re-enter this entire workflow at Step 1**, using the new failure's output.
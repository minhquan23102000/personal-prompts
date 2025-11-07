Following the instruction below and execute carefully step by step:
```

### Metadata

*   **Core Intent:** To automatically generate a simple, straightforward integration test script for a given code implementation, enabling quick verification in a real-world staging environment.
*   **Guiding Principles:**
    *   **Simplicity Over Coverage:** The script's primary goal is to be easily understood and executed, not to cover every edge case. Focus on the "happy path."
    *   **Environment-Awareness:** The test must be configured to run against a specific, real environment (e.g., staging), using actual services and data patterns.
    *   **Isolation of Failure:** The script should test a single, core function or method to ensure that any failure can be quickly traced back to that specific component.
*   **Required Context & State:**
    *   The source code of the target function, method, or class.
    *   A description or access to the target deployment environment (e.g., staging API endpoints, database credentials, required headers).
    *   A sample of valid input data required to execute the target function.
*   **Success Metrics:** A complete, executable test script is generated and saved to the `/debug` directory. When run against the target environment, the script executes without errors and successfully validates the primary function's expected outcome.

### Execution Workflow

1.  **Analyze the Implementation Context**
    *   **State:** The agent has the source code for the target implementation.
    *   **Intent:** To identify the primary public-facing function or method that serves as the main entry point for the implementation's logic.
    *   **Success Condition:** The agent has successfully identified and isolated the target function/method signature, including its name and required arguments.
    *   **Fallback Intent:** If multiple public methods exist, request the user to specify which one should be the focus of the debug script.

2.  **Identify Environmental Dependencies**
    *   **State:** The agent knows the target function/method.
    *   **Intent:** To scan the implementation's code to identify all external dependencies, such as API calls, database connections, or environment variables required for execution.
    *   **Success Condition:** A list of all required environmental configurations and external service endpoints is created.
    *   **Fallback Intent:** If dependencies cannot be automatically determined, prompt the user to provide the necessary connection details and credentials for the target environment.

3.  **Construct the Test Harness**
    *   **State:** The agent has the target function, its arguments, and a list of environmental dependencies.
    *   **Intent:** To generate the boilerplate code for the test script, including importing the target function, setting up environment variables, and configuring any required clients (e.g., an HTTP client).
    *   **Success Condition:** A script file is created that successfully initializes the environment and imports the target code without errors.
    *   **Fallback Intent:** If imports or initializations fail, analyze the error and attempt to correct the file path or initialization logic. If unsuccessful, report the error to the user.

4.  **Implement the Core Test Logic**
    *   **State:** The agent has the test harness and a sample of valid input data.
    *   **Intent:** To write the specific lines of code that call the target function with the sample data and then perform a single, simple check to validate the outcome.
    *   **Success Condition:** The script now includes a call to the target function and a basic assertion that confirms a successful execution (e.g., checks for a `200 OK` status code, or verifies that the output is not null).
    *   **Fallback Intent:** If a simple success assertion is not obvious, create a log output of the function's result and add a comment instructing the user on what to manually verify.

5.  **Finalize and Place the Script**
    *   **State:** The agent has a complete and functional test script.
    *   **Intent:** To add comments to the script explaining its purpose and how to run it, and then save the final file into the designated `e2e_tests` folder.
    *   **Success Condition:** The commented script is correctly named and saved in the target directory.
    *   **Fallback Intent:** If the `e2e_tests` directory does not exist, create it first and then save the file. If file permissions fail, notify the user of the failure.
```
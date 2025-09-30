# Strategic Plan: Integration Test Script Generation

This plan outlines the workflow for an agent to autonomously generate a complete, robust, and idempotent Python integration test script based on user-provided requirements.

1.  ### Deconstruct the User Request
    *   **State:** The agent has received the user's prompt containing the goal, requirements, and specific context for the test script.
    *   **Intent:** To meticulously parse the user's input and extract all critical parameters. This includes the **target function/method**, all **dependencies**, the required **environment variables**, and the structure of the **sample data**. The goal is to build a structured understanding of the test's scope.
    *   **Success Condition:** The agent has successfully identified and stored all contextual variables provided by the user. The agent is fully aware of what needs to be tested and the environment it will run in.
    *   **Fallback Intent:** If critical information is missing or ambiguous (e.g., the function name is listed as `[Insert the name of the function or method]`), the agent must prompt the user for the necessary details before proceeding.

2.  ### Generate the Script Foundation and Configuration
    *   **State:** The agent has a complete, structured understanding of the test requirements.
    *   **Intent:** To create the initial Python script structure. This involves generating the necessary **import statements** (e.g., for `os`, `unittest`, and environment variable handling) and writing the code block responsible for loading the specified **environment variables** from a `.env` file.
    *   **Success Condition:** A Python script is created with the basic boilerplate, including imports and a functional configuration section that prepares the environment for the test.
    *   **Fallback Intent:** If a non-standard library is required for a dependency, the agent should add a comment at the top of the script indicating the necessary installation command (e.g., `# Requirement: pip install python-dotenv`).

3.  ### Implement the Test Setup Logic
    *   **State:** The script's foundation is in place. The agent knows the system dependencies and has the sample data structure.
    *   **Intent:** To write the code that programmatically **creates the necessary preconditions** for the test to run in isolation. This could involve connecting to a database, using the sample data to insert a new record, or initializing a client for an external API. The logic should be placed within a dedicated setup function or block.
    *   **Success Condition:** The script contains a clearly defined setup section that reliably creates all required test data and resources, ensuring the test is self-contained.
    *   **Fallback Intent:** If the setup logic for a dependency is highly complex or proprietary, the agent should generate a placeholder function with a clear docstring and comments explaining what the user needs to implement manually (e.g., `def _create_test_user_in_legacy_crm(): # TODO: Implement logic to create a user...`).

4.  ### Implement the Core Execution and Verification
    *   **State:** The setup logic is complete. The agent knows the target function and the expected successful outcome.
    *   **Intent:** To write the central piece of the test. This involves **calling the target function/method** using the data created during the setup phase. Immediately following the execution, the agent will generate one or more **assertion statements** to validate that the outcome was successful.
    *   **Success Condition:** The script contains a test method that executes the specified function and includes clear, meaningful assertions that confirm the function behaved as expected (e.g., checking a response status or querying the database to confirm a change).
    *   **Fallback Intent:** If the exact success criteria are not explicitly defined, the agent should generate the function call and add a commented-out assertion with a placeholder, prompting the user to define the specific condition to check (e.g., `# self.assertEqual(result['status'], 'completed') # TODO: Confirm expected status`).

5.  ### Implement the Cleanup Logic
    *   **State:** The execution and verification steps are defined. The agent is aware of all resources and data created during the setup phase.
    *   **Intent:** To write the code that **reverses all actions taken in the setup phase**, ensuring the test is idempotent and leaves the environment clean. This involves deleting any created database records, closing connections, or removing temporary files.
    *   **Success Condition:** The script contains a clearly defined teardown section that programmatically removes all resources created during the test, leaving the system in its original state.
    *   **Fallback Intent:** If the cleanup action is ambiguous, the agent should generate a placeholder cleanup function with comments detailing which resources should be removed, leaving the specific implementation to the user.

6.  ### Finalize and Save the Script
    *   **State:** All logical components of the script (configuration, setup, execution, verification, cleanup) have been generated.
    *   **Intent:** To assemble all generated code into a single, well-commented, and readable Python file. The agent will then save this file to the specified location (`tests/integration/`) with a descriptive name derived from the target function.
    *   **Success Condition:** A complete, ready-to-run Python script is successfully saved to the correct directory.
    *   **Fallback Intent:** If the agent encounters a permission error or cannot access the specified file path, it will instead output the complete script content in a single block for the user to copy and save manually.
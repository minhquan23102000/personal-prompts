1.  **Establish Foundational Understanding.**
    *   **State:** The agent begins with access to the root directory of the target project.
    *   **Intent:** The primary intent is to **build a complete map** of the project's structure and **absorb any existing high-level documentation** that explains its purpose and conventions. The agent should perform a comprehensive scan to create a file tree and then read the contents of key files like `README`, `CONTRIBUTING`, or any existing context documents.
    *   **Success Condition:** The agent has successfully constructed a file tree and loaded the contents of all top-level markdown or text-based documentation files into its working memory.
    *   **Fallback Intent:** If no primary documentation files are found, the agent should **note their absence** and proceed with the analysis based solely on the file structure and code, flagging that the project's purpose will need to be inferred.

2.  **Identify Core Technology and Developer Operations.**
    *   **State:** The agent possesses the project's file tree and the content of its documentation.
    *   **Intent:** The goal is to **identify the project's essential vitals**: its technology stack and the specific commands a developer needs to work with it. The agent will inspect dependency management files to determine the language and package manager, and then meticulously scan the absorbed documentation for verbatim commands related to installation, execution, and testing.
    *   **Success Condition:** The agent has definitively identified the primary programming language and has a list of exact, copy-paste-ready commands for setup, running the app, and running tests.
    *   **Fallback Intent:** If the documentation does not contain explicit commands, the agent's intent shifts to **inferring the most probable commands** based on the identified package manager (e.g., `npm install` for a `package.json`). These inferred commands must be clearly marked as such in the final report.

3.  **Map the Architectural Blueprint.**
    *   **State:** The agent knows the technology stack and the command used to run the application.
    *   **Intent:** The intent is to **discover the project's high-level architecture** by identifying its main entry point and the conventional locations for source code, tests, and configuration. The agent should use the "run" command to trace the initial file executed and analyze the directory structure for common patterns (`src`, `app`, `tests`, `lib`, `config`).
    *   **Success Condition:** The agent has identified the file path(s) for the application's entry point(s) and has mapped the primary purpose of the key directories in the project.
    *   **Fallback Intent:** If the entry point is not obvious from the run command, the agent should **search for conventional entry point filenames** (e.g., `main.py`, `index.js`). If the directory structure is unconventional, the agent should analyze import/dependency graphs between files to identify the most central and interconnected directories, assuming they represent the core source code.

4.  **Trace the Core Logic and Data Flow.**
    *   **State:** The agent has identified the application's entry point and key source directories.
    *   **Intent:** The goal is to **create a simplified narrative of the application's behavior**. Starting from the entry point, the agent will trace the primary execution path to identify the most critical modules and summarize their single core responsibility. It will also investigate how configuration is loaded and accessed by the application to understand its runtime environment.
    *   **Success Condition:** The agent has produced a brief, high-level summary of a typical request or data lifecycle, a list of critical modules with their one-sentence purpose, and an explanation of the configuration strategy.
    *   **Fallback Intent:** If a full execution trace proves too complex, the agent's intent changes to **summarizing the static roles of key modules**. It will analyze the files in the main source directory, prioritizing those that are most frequently imported by other modules, and summarize their purpose based on their internal code and structure.

5.  **Synthesize and Deliver the Context Document.**
    *   **State:** The agent has gathered and summarized all necessary information about the project's purpose, tech stack, key commands, architecture, and core logic.
    *   **Intent:** The final intent is to **assemble all gathered intelligence into a single, coherent, and well-structured document**. The agent will create or update the `README.md` file, populating it with distinct sections for each category of information it has discovered. The agent should prioritize clarity and conciseness to maximize value for a human reader.
    *   **Success Condition:** The `README.md` file is successfully written or updated in the project's filesystem, and the agent confirms the location and successful completion of the task.
    *   **Fallback Intent:** If writing to the file fails for any reason (e.g., permissions), the agent must **output the full, formatted Markdown content** directly to the user as its final action, ensuring the generated knowledge is not lost.
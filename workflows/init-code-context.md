Goal: Generate a high-level `docs/codebase_context.md` file by analyzing a project's structure and key files.
- 1. Initial Reconnaissance:
  - Perform a recursive scan of the project to get a complete file tree.
  - Read the root `README.md`, `CONTRIBUTING.md`, and any other top-level development guide files.

- 2. Extract Core Project Vitals:
  - Identify the primary programming language and package manager by inspecting dependency files (e.g., `pyproject.toml`, `package.json`, `pom.xml`, `go.mod`, `Gemfile`).
  - From the documentation read in step 1, extract the exact, verbatim commands for these critical operations:
    - How to install dependencies.
    - How to run the main application(s).
    - How to run the test suite.
    - How to run linters or code formatters.

- 3. Discover Architecture and Entry Points:
  - Based on the "run application" command, identify the main entry point file(s).
  - Based on common conventions and the file tree, identify the primary directories for:
    - Application source code (e.g., `src/`, `app/`, `lib/`).
    - Tests (e.g., `tests/`, `spec/`).
    - Public assets or web content (e.g., `public/`, `static/`).
    - Reusable modules or libraries.

- 4. Map Core Logic and Data Flow:
  - Starting from the main entry point(s), trace the primary execution path. Follow imports, requires, or includes to identify the most critical modules that are loaded first.
  - For each critical module, read its code to determine its single core responsibility (e.g., "Handles API routing," "Manages database connections," "Defines core data types").
  - Investigate how configuration is handled. Look for dedicated config files (`.env`, `.yaml`, `.ini`) or modules that load settings, and note how they are accessed by the application.
  - Formulate a brief, high-level summary of a typical request lifecycle or data flow through the application's main components.

- 5. Assemble the Context Document:
  - Create the `docs/codebase_context.md` file.
  - **Project Overview:** Write a short summary of the project's purpose, based on the `README.md`.
  - **Tech Stack:** List the identified language, package manager, and any major frameworks or libraries found in dependency files.
  - **Key Commands:** Create a section with the verbatim commands for installing, running, and testing, as discovered in step 2.
  - **Architecture Summary:** Describe the high-level directory structure and identify the locations of source code, tests, and configuration.
  - **Key Modules & Responsibilities:** Create a bulleted list of the critical modules identified in step 4, each with its one-sentence summary.
  - **Core Workflows:** Briefly describe the configuration loading process and the typical data flow path.

- 6. Final Confirmation:
  - Announce the successful creation of the `docs/codebase_context.md` file.
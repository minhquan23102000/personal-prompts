# Strategic Plan: Project Code Quality Contract Generation

### Plan Metadata

*   **Core Intent:** To perform a deep analysis of a software project's codebase to generate a formal `CODE_QUALITY.md` file that codifies both existing best practices and aspirational technical standards for the project.
*   **Guiding Principles:**
    *   **Infer from Reality, Then Prescribe:** Rules should be based on an analysis of successful patterns already present in the code, while also creating formal standards to correct identified inconsistencies and anti-patterns.
    *   **Context is King:** The generated rules must be directly relevant to the project's specific language, framework, and domain (e.g., front-end, back-end API, data pipeline). Avoid generic, non-applicable advice.
    *   **Prescriptive and Unambiguous:** The document's language must be direct, establishing clear, enforceable rules using terms like "must," "will," and "is required." It is a rulebook, not a list of suggestions.
*   **Required Context & State:**
    *   Read-only access to the entire project codebase.
    *   Identification of the project's primary programming language(s) and framework(s).
    *   Knowledge of the project's archetype (e.g., REST API, Single-Page Application, CLI tool).
*   **Success Metrics:** A complete, well-structured `CODE_QUALITY.md` file is generated in the project's root directory. The rules within are relevant, actionable, and demonstrably derived from an analysis of the actual source code.

### Execution Workflow

1.  **Deconstruct Project Architecture and Technology Stack**
    *   **State:** The agent has access to the project's file system.
    *   **Intent:** To determine the fundamental nature of the project by scanning dependency files (`package.json`, `pom.xml`), identifying key frameworks, and recognizing common architectural patterns in the directory structure.
    *   **Success Condition:** The agent has successfully classified the project (e.g., "Node.js/Express REST API," "React Single-Page Application") and identified the primary language and frameworks.
    *   **Fallback Intent:** If the archetype is ambiguous, prompt the user to select from a list of probable classifications based on the files found.

2.  **Synthesize Implicit Standards from Codebase Analysis**
    *   **State:** The project's technology stack is known.
    *   **Intent:** To deeply analyze the source code to discover the project's *de facto* coding standards. This involves identifying common patterns for variable naming, function declaration, module structure, asynchronous operations, and error handling. This analysis must also parse configuration files (`.eslintrc`, `.prettierrc`) to capture explicitly defined rules.
    *   **Success Condition:** The agent has a synthesized list of coding patterns, both positive (to be enforced) and inconsistent (to be standardized), derived directly from the source code.
    *   **Fallback Intent:** If the codebase is too new or inconsistent to establish clear patterns, select a widely-accepted, strict community standard for the identified language (e.g., Airbnb JavaScript Style Guide) to serve as the baseline.

3.  **Define Testing and Reliability Mandates**
    *   **State:** The project archetype is known.
    *   **Intent:** To establish non-negotiable rules for software testing. The agent must first scan the codebase for existing test files (`*.spec.js`, `*_test.py`) to identify the currently used testing framework and patterns. Based on this, it will define mandatory test types and propose a minimum code coverage threshold.
    *   **Success Condition:** A "Testing & Reliability" section is drafted with specific requirements that align with the project's existing testing culture (e.g., "All API endpoints must have corresponding integration tests," "A minimum of 80% unit test coverage is required for all new logic").
    *   **Fallback Intent:** If no testing framework is present, recommend a standard one for the ecosystem and propose a conservative but reasonable starting coverage target (e.g., 70%).

4.  **Formulate Domain-Specific Guardrails**
    *   **State:** The agent understands the project's purpose.
    *   **Intent:** To generate rules for quality pillars specific to the project's domain by analyzing relevant code. For a back-end API, this means inspecting route handlers, database models, and security middleware to create rules for API design, data integrity, and input validation. For a front-end app, this means analyzing components to create rules for state management, accessibility, and performance.
    *   **Success Condition:** A set of precise, actionable rules covering security, performance, and other domain-specific concerns is created, supported by examples found in the code.
    *   **Fallback Intent:** Generate a list of universal, high-priority best practices for the general category (e.g., "web application security") and add a placeholder note for the development team to add more specific rules.

5.  **Define Document Structure and Assemble the `CODE_QUALITY.md`**
    *   **State:** Content for all quality pillars has been generated.
    *   **Intent:** To structure and assemble the final document according to a formal template. The agent will first define the standard output format and then populate it with the rules generated in the previous steps.
    *   **Success Condition:** A complete `CODE_QUALITY.md` file is saved to the project's root directory, formatted correctly and containing all the derived and defined rules.
    *   **Fallback Intent:** If content for any section could not be confidently generated, create the section header with a placeholder note instructing the user to define the rules for that domain.

    ***

    ### **Output Format Definition**
    The agent must structure the final `CODE_QUALITY.md` file using the following Markdown template:

    ```markdown
    # Code Quality Standards

    This document is the single source of truth for the technical standards and engineering best practices of this project. All code must adhere to these rules before being merged.

    ### Coding Standards & Readability
    *   [Rules for formatting, naming conventions, and style, derived from Step 2]

    ### Testing & Reliability
    *   [Rules for testing frameworks, coverage requirements, and test types, derived from Step 3]

    ### Security
    *   [Rules for secure coding practices, dependency management, and vulnerability prevention, derived from Step 4]

    ### Performance & Efficiency
    *   [Rules for resource management, algorithmic complexity, and asynchronous operations, derived from Step 4]

    ### Maintainability & Documentation
    *   [Rules for code modularity, commenting, error handling, and logging]

    ### Domain-Specific Standards
    *   [Rules specific to the project's archetype, e.g., API Design, Accessibility (A11y), etc., derived from Step 4]
    ```
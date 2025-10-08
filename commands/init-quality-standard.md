# Strategic Plan: Essential Code Quality Contract Generation

### Plan Metadata

*   **Core Intent:** To generate a concise, actionable `CODE_QUALITY.md` file by synthesizing the project's existing code with established, domain-specific engineering best practices.
*   **Guiding Principles:**
    *   **Synthesize, Don't Just Mirror:** The agent must cross-reference internal code patterns with its external knowledge of industry best practices to propose a standard that improves, rather than just codifies, the current state.
    *   **Prioritize Impact over Volume:** Focus on a minimal set of essential rules that provide the most value in preventing bugs, improving security, and ensuring long-term maintainability.
    *   **Clarity and Brevity:** The output must be simple, using only headings and lists. This makes it easy for human developers to read and edit, and efficient for other automated tools to parse.
*   **Required Context & State:**
    *   Read-only access to the entire project codebase.
    *   A knowledge base of architectural patterns and best practices for various domains (e.g., Next.js front-end, Python back-end API, AI/ML pipelines).
*   **Success Metrics:** A `CODE_QUALITY.md` file is generated containing a short, prioritized list of the most critical rules for the project. The document is easy to read and contains no boilerplate or low-impact suggestions.

### Execution Workflow

1.  **Analyze Project Archetype and Technology Stack**
    *   **State:** The agent has access to the project's file system.
    *   **Intent:** To determine the project's specific domain and technology stack (e.g., "Next.js 14 Web Application," "Python FastAPI Microservice," "Go CLI Tool") by analyzing dependency files, project configuration, and directory structure.
    *   **Success Condition:** The agent has successfully classified the project's archetype and can load the corresponding set of best practices from its knowledge base.
    *   **Fallback Intent:** If the archetype is ambiguous, ask the user to clarify by choosing from a list of likely candidates.

2.  **Establish a Baseline from Code and Best Practices**
    *   **State:** The project archetype is known.
    *   **Intent:** To perform a dual analysis. First, scan the codebase to identify existing, recurring patterns for key activities (e.g., state management, data fetching, error handling). Second, compare these internal patterns against the agent's external knowledge base of industry-standard best practices for that specific archetype.
    *   **Success Condition:** The agent has a clear understanding of where the project's current practices align with, and deviate from, established best practices.
    *   **Fallback Intent:** If the codebase is too new or chaotic to identify clear patterns, the agent will rely entirely on its external knowledge base to propose a strong, foundational set of rules.

3.  **Select High-Impact, Essential Rules**
    *   **State:** The agent has compared the project's code to best practices.
    *   **Intent:** To select a small, curated list of the most critical rules for the project. The agent will prioritize rules that address security vulnerabilities, prevent common bugs, ensure performance, and significantly improve code maintainability for that specific domain. It will deliberately ignore minor stylistic preferences or low-impact conventions.
    *   **Success Condition:** A prioritized list of 5-10 essential, non-negotiable rules has been created.
    *   **Fallback Intent:** If no clear high-impact rules can be determined, propose a "starter kit" of 3 fundamental rules for the archetype (e.g., for a back-end: one for security, one for testing, one for logging).

4.  **Generate the Concise `CODE_QUALITY.md` Document**
    *   **State:** The agent has a final, prioritized list of essential rules.
    *   **Intent:** To render the selected rules into the final `CODE_QUALITY.md` file using a simple, clean format. The structure will consist only of a main heading, a brief introductory sentence, and a series of section headings followed by bulleted lists.
    *   **Success Condition:** A `CODE_QUALITY.md` file is saved to the project root, adhering strictly to the minimal format below.
    *   **Fallback Intent:** If a rule for a critical section (like Security) cannot be confidently generated, the agent will insert a placeholder (`* [TODO: Define the primary rule for X]`) to prompt the team for action.

    ***

    ### **Output Format Definition**
    The agent must structure the final `CODE_QUALITY.md` file using the following minimal Markdown template:

    ```markdown
    # Code Quality Standards

    This document defines the essential, non-negotiable technical standards for this project.

    ### Readability & Style
    * [The single most important rule for naming or formatting, e.g., "Follow the official Go formatting standards via `gofmt`."]

    ### Testing
    * [The core testing requirement, e.g., "All new business logic must be covered by unit tests with a minimum of 80% coverage."]

    ### Security
    * [The most critical security rule, e.g., "All API endpoints that receive user input must use a validation library to sanitize data."]

    ### Performance
    * [The key performance guideline, e.g., "Avoid synchronous file I/O operations in API request handlers."]

    ### Domain-Specific
    * [A critical rule for the project's archetype, e.g., for Next.js: "All data fetching on the server must be done within Server Components."]
    ```
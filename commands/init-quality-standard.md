Following the instruction below and execute carefully step by step:
```

### Plan Metadata

*   **Core Intent:** To generate a `CODE_QUALITY.md` file that establishes a robust and forward-looking technical standard by synthesizing project-specific code analysis with established, domain-aware industry best practices.
*   **Guiding Principles:**
    *   **Best Practice as the North Star:** The agent's primary goal is to align the project with proven, high-quality standards for its specific technology stack and domain. The existing code is a starting point for analysis, not the final authority on quality.
    *   **Balance Aspiration with Pragmatism:** The proposed standards should be ambitious yet achievable. The agent will identify where the current code aligns with best practices and formalize those rules, while prescriptively introducing better patterns where the code is inconsistent or follows outdated practices.
    *   **Clarity and Simplicity:** The final document must be structured with simple Markdown (headings and lists) to be easily read, edited by developers, and parsed by automated tools, minimizing cognitive and token overhead.
*   **Required Context & State:**
    *   Read-only access to the entire project codebase.
    *   An internal knowledge base of software engineering best practices, design patterns, and common anti-patterns for various domains (e.g., Next.js front-end, Python backend API, AI/ML pipelines).
*   **Success Metrics:** A `CODE_QUALITY.md` file is generated that is both relevant to the project's current state and elevates its standards. The rules are clear, prescriptive, and would be endorsed by an experienced senior developer familiar with the project's domain.

### Execution Workflow

1.  **Deconstruct Project Archetype and Domain**
    *   **State:** The agent has access to the project's file system.
    *   **Intent:** To determine the project's specific domain and technology stack. This involves identifying the primary language, key frameworks (e.g., Next.js, Django, FastAPI), and architectural purpose (e.g., "Server-Side Rendered Web App," "Data Processing Service," "RESTful API").
    *   **Success Condition:** The agent has successfully classified the project's archetype and loaded the corresponding set of industry best practices from its internal knowledge base.
    *   **Fallback Intent:** If the archetype is ambiguous, prompt the user to select from a list of probable classifications to ensure the correct best practices are applied.

2.  **Establish Foundational Standards by Reconciling Code with Best Practices**
    *   **State:** The agent has classified the project and has access to both the source code and its knowledge base of best practices.
    *   **Intent:** To compare the *observed patterns* in the code (e.g., naming conventions, formatting, module structure) against the *known best practices* for that archetype. The agent will then synthesize a prescriptive standard.
        *   If code patterns align with best practices, formalize them as a rule.
        *   If code patterns are inconsistent, establish a single, clear rule based on the best practice.
        *   If code patterns conflict with best practices, the new rule will mandate the best practice.
    *   **Success Condition:** A clear set of foundational rules for readability and coding standards is drafted, representing a high-quality, enforceable standard.
    *   **Fallback Intent:** If the codebase is too new or sparse for meaningful analysis, default entirely to a strict, widely-accepted community style guide for the identified technology.

3.  **Define Domain-Specific Quality Pillars**
    *   **State:** The foundational standards are drafted.
    *   **Intent:** To apply the same reconciliation logic (observed code vs. best practice) to higher-level, domain-specific concepts. For a **Next.js front-end**, this means defining rules for state management, component architecture (e.g., Server vs. Client components), and accessibility. For a **backend API**, this means defining rules for API endpoint design, data validation, security headers, and error handling.
    *   **Success Condition:** Prescriptive rules for the project's most critical quality pillars (e.g., Security, Testing, Performance, Reliability) are drafted, creating a robust contract for new development.
    *   **Fallback Intent:** If the code lacks clear patterns for a specific pillar (e.g., no tests exist), generate a "starter" set of rules based entirely on best practices, effectively creating the initial standard for the team to adopt.

4.  **Assemble the Final Document**
    *   **State:** The content for all quality pillars has been generated.
    *   **Intent:** To structure all generated content into the final `CODE_QUALITY.md` file, adhering strictly to a simple, developer-friendly format of headings and bulleted lists. The introduction will clearly state the document's purpose as the project's technical contract.
    *   **Success Condition:** A complete, clearly formatted `CODE_QUALITY.md` file is saved to the project's root directory.
    *   **Fallback Intent:** If content for any section could not be confidently generated, create the section header with a placeholder note instructing the team to define the rules for that domain (e.g., `*   [Team to define standards for database migrations]`).

***

### **Output Format Definition**
The agent must structure the final `CODE_QUALITY.md` file using the following simple and clean Markdown template:

```markdown
# Code Quality Standards

This document defines the technical standards for this project. All code must adhere to these rules to be merged.

### Coding Standards
*   [Rule for naming convention]
*   [Rule for code formatting and style guide]
*   [Rule for module and function structure]

### Testing & Reliability
*   [Rule for required testing framework]
*   [Rule for minimum test coverage]
*   [Rule for types of tests required (e.g., unit, integration)]

### Security
*   [Rule for input validation]
*   [Rule for handling secrets and credentials]
*   [Rule for dependency scanning]

### Performance
*   [Rule for asynchronous operations]
*   [Rule for resource management or performance budgets]

### [Domain-Specific Pillar: e.g., API Design]
*   [Rule for endpoint naming conventions]
*   [Rule for standard success/error response structures]
```
```
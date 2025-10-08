# Mental Model: The Documentation Custodian 
### Core Principles

*   **Documentation is a Product:** Treat documentation with the same rigor and respect as the agent's code. It has a target audience, specific use cases, and requires a commitment to quality, clarity, and maintenance. Its success is measured by its ability to empower users and developers.
*   **Clarity Over Comprehensiveness:** The primary goal is to be understood, not to document every possible detail. Prioritize clear, concise explanations of the most common and critical paths. Use progressive disclosure to guide readers to more detailed information if they need it.
*   **Empathy for the Reader:** Always consider the reader's context, knowledge level, and goal. What problem are they trying to solve right now? The documentation must bridge the gap between their current understanding and the knowledge they need to succeed.

### Best Practices

*   **Write for Specific Personas:** Before writing, identify the primary audience. Are you writing for a new developer setting up their environment, an experienced contributor designing a new feature, or an end-user trying to accomplish a task? Tailor the tone, terminology, and level of detail accordingly.
*   **Structure for Discoverability:** Organize content based on the reader's intent, not the project's internal architecture. A user looks for "how to add a new skill," not "the `skills_manager` module." Use cross-linking extensively to connect related concepts and guide readers on their learning journey.
*   **Maintain a Single Source of Truth:** Avoid information duplication. If a concept is explained in one place, link to it from other relevant documents rather than repeating it. When information needs to be updated, it should only need to be changed in one location.
*   **Use Visuals and Examples:** A well-placed code snippet, diagram, or screenshot is often more effective than paragraphs of text. Examples should be practical, complete, and easy to copy and adapt.

### Specific Rules & Constraints

*   **Directory Structure:** All documentation must reside within the `docs/` folder and adhere to the following structure:
    *   `docs/tutorials/`: For step-by-step, goal-oriented guides that walk a user through a specific task (e.g., `01-installing-the-agent.md`). Files should be numbered to indicate a suggested reading order.
    *   `docs/how-to-guides/`: For problem-oriented instructions that provide a solution to a specific, common problem (e.g., `connecting-to-a-new-database.md`). These are recipes for experienced users.
    *   `docs/explanation/`: For conceptual, background-level discussions that deepen understanding of a topic (e.g., `our-approach-to-agent-reasoning.md`).
    *   `docs/reference/`: For technical descriptions of the project's implementation. This is the technical encyclopedia, organized into the following sub-groups:
        *   `reference/architecture/`: High-level design documents, component diagrams, and data flow explanations.
        *   `reference/api/`: Detailed API endpoint documentation, request/response schemas, and authentication guides.
        *   `reference/data-models/`: Descriptions of database schemas, core data objects, and state structures.
        *   `reference/configuration/`: Exhaustive lists and explanations of all environment variables and configuration file settings.
        *   `reference/modules/`: In-depth documentation for specific, critical internal modules or services.
*   **Audience and Purpose Mandates:**
    *   **IF** the document's purpose is to teach a beginner how to accomplish a multi-step goal, **THEN** it must be placed in `docs/tutorials/` and written with a direct, encouraging tone.
    *   **IF** the document's purpose is to provide a direct answer to a specific technical question, **THEN** it must be placed in `docs/how-to-guides/` and assume the reader has a baseline understanding of the system.
    *   **IF** the document's purpose is to describe the technical implementation of a component, **THEN** it must be placed in the relevant sub-directory within `docs/reference/` (e.g., API specifications in `api/`, architectural overviews in `architecture/`) and must be objective, precise, and free of opinion.
*   **Content Requirements:** Every tutorial and how-to guide must begin with a "Prerequisites" section outlining the knowledge and system state required to follow the guide successfully. Every reference document must include a "Last Reviewed" date to ensure content freshness.
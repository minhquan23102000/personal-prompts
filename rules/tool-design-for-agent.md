## Mental Model: The Ergonomic Toolwright

### Core Principles

*   **Design for Non-Deterministic Minds:** The primary user is an AI agent, not a deterministic program. Every design choice must prioritize the agent's "ergonomics"—how it perceives, reasons about, and uses a tool—over traditional software engineering conventions.
*   **Context is the Most Valuable Resource:** An agent's context window is its world. Tools must be designed to maximize the signal-to-noise ratio of the information they consume and produce, treating every token as a precious commodity.
*   **Tool Quality Dictates Agent Efficacy:** The agent's success or failure is a direct reflection of the quality of its tools. A well-designed tool offloads cognitive work from the agent, while a poorly designed one creates confusion and leads to mission failure.

### Best Practices

*   **Adopt an Evaluation-Driven Cycle:** Begin by prototyping tools, then immediately create a comprehensive evaluation suite based on real-world tasks. Use an agent to analyze evaluation results, identify friction points, and suggest improvements to the tools. This iterative loop is the primary path to quality.
*   **Consolidate Around Workflows, Not Endpoints:** Instead of creating a tool for every individual API endpoint, build tools that encapsulate common, multi-step workflows. A single, powerful tool should enable an agent to achieve a meaningful sub-goal, reducing the number of intermediate steps and context consumption.
*   **Write Descriptions for a New Hire:** Author all tool and parameter descriptions with the clarity and explicit detail you would use to onboard a new human team member. Define all specialized terminology and clearly articulate the tool's distinct purpose and its relationship to other tools.
*   **Use Namespacing to Create Clarity:** Group related tools under logical, shared prefixes (e.g., by service or resource). This helps the agent delineate boundaries between toolsets and select the correct tool for a given task, especially when many tools are available.
*   **Return Semantically Rich Information:** Tool outputs should favor natural language and human-readable names over cryptic technical identifiers like UUIDs. When technical IDs are necessary for subsequent tool calls, they should be provided alongside their human-readable counterparts.
*   **Offer Controllable Verbosity:** For tools that can return large amounts of data, implement a parameter that allows the calling agent to specify a response format, such as **concise** or **detailed**, to manage token usage effectively.

### Specific Rules & Constraints

*   **If a tool can return a list of items, it must implement pagination, filtering, or truncation with sensible defaults.** The agent must never be flooded with an unbounded amount of information from a single tool call.
*   **If a tool call fails due to invalid input, the error response must be helpful and instructive.** It must clearly explain what was wrong and provide an example of a correctly formatted request, rather than returning an opaque error code.
*   **If a tool parameter name is ambiguous (e.g., `id`, `user`), it must be renamed to be specific and unambiguous (e.g., `customer_id`, `user_name`).** This is a non-negotiable requirement to prevent agent misinterpretation.
*   **If a tool's response is truncated, the response body must explicitly state that the information is incomplete.** It should also provide guidance on how the agent can retrieve the remaining information (e.g., by using pagination or refining search filters).
*   **If two tools have significantly overlapping functionality, they must be consolidated into a single tool.** Redundant or confusingly similar tools are forbidden as they create decision paralysis for the agent.
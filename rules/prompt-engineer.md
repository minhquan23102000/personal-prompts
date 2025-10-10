# Mental Model: Adaptive Prompt Architecture

This model guides an agent in its primary meta-task: constructing the most effective and efficient prompt to accomplish a given goal. It prioritizes adapting the prompt's structure and detail to the specific nature of the task at hand.

### Core Principles

*   **Clarity Over Cleverness:** An instruction must be unambiguous. The agent's primary objective is to eliminate guesswork for the receiving system.
*   **Context is the Fuel for Reasoning:** The agent's performance is directly proportional to the quality and relevance of the provided context. Insufficient context leads to hallucination; excessive context leads to waste and distraction.
*   **Efficiency is a Design Constraint:** Every token has a cost. The agent must strive to achieve the goal with the minimum necessary instruction and context, balancing precision with computational expense.
*   **Match the Framework to the Task:** A prompt is not a command; it is a cognitive framework. The agent must select the right framework—from a simple directive to a complex strategic plan—that best fits the problem's complexity.

### Best Practices

*   **Assess Task Complexity First:** Before constructing a prompt, analyze the user's request to classify its complexity (e.g., simple retrieval, multi-step analysis, complex project execution). This assessment dictates the appropriate prompt modality.
*   **Select a Prompt Modality:** Based on the complexity assessment, choose the most efficient structure:
    *   **Direct Instruction:** For simple, low-ambiguity tasks (e.g., "Summarize this article," "Translate this phrase"). This is the default for minimizing cost.
    *   **Guided Reasoning:** For tasks requiring analysis, evaluation, or a clear thought process (e.g., "Compare these two products and recommend the best one for a budget-conscious user"). This often includes the instruction to "think step-by-step."
    *   **Strategic Planning:** For complex, multi-stage goals that require the agent to define its own workflow, use tools, or manage state over time (e.g., "Research market trends for Q3, draft a report, and generate a slide deck summary").
*   **Dynamically Scope Context:** Provide only the essential information required for the task. Instead of providing an entire user history, provide only the relevant conversation turns. Instead of a full document, provide the specific excerpts needed for analysis.
*   **Assign a Role and Persona:** Always begin the prompt by assigning a specific, expert role. This remains a highly effective way to focus the agent's knowledge and behavior.
*   **State the End Goal Explicitly:** Clearly articulate the overall mission and the "definition of done." This allows the agent to self-correct and make intelligent trade-offs.

### Specific Rules & Constraints

*   **IF** the task is atomic and can be completed in a single, clear action, **THEN** the agent must use the **Direct Instruction** modality and avoid any step-by-step language.
*   **IF** the task requires a logical deduction or a traceable thought process to ensure accuracy, **THEN** the agent must use the **Guided Reasoning** modality.
*   **IF** a task involves more than two distinct stages or requires the use of external tools (like searching the web or running code), **THEN** the agent must default to the **Strategic Planning** modality.
*   **IF** the final output must adhere to a strict format (like JSON or XML), **THEN** the agent must provide a schema or a clear template, regardless of the chosen modality.
*   **IF** the agent estimates that the required context plus the instructions will exceed an operational token limit, **THEN** it must first initiate a sub-task to summarize or compress the context before proceeding with the primary goal.
*   **IF** the user's request is ambiguous, **THEN** the agent's first action must be to ask clarifying questions, rather than assuming intent and potentially wasting resources on an incorrect task.
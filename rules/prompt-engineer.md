# Mental Model: Agent Prompt Architecture

This model provides the guiding philosophy for designing prompts that enable an AI agent to reason effectively, act reliably, and achieve complex goals with precision.

### Core Principles

*   **Clarity Over Cleverness:** The agent is a logical system, not a mind reader. Your primary goal is to eliminate ambiguity. A direct, explicit instruction is always superior to a clever or poetic one.
*   **Context is the Fuel for Reasoning:** An agent's performance is directly proportional to the quality and relevance of the context it is given. A prompt without sufficient context forces the agent to guess, leading to unreliable outcomes.
*   **Guide Reasoning, Don't Just Command Action:** Treat the agent as a cognitive partner. The best prompts don't just tell the agent *what* to do, but also guide *how* it should think, plan, and handle uncertainty.

### Best Practices

*   **Assign a Role and Persona:** Begin the prompt by assigning a specific, expert role (e.g., "You are a senior cybersecurity analyst," "You are an expert financial data auditor"). This focuses the agent's knowledge and sets a professional tone for its output.
*   **Structure the Prompt Logically:** Use clear sections with headers (e.g., `## Goal`, `## Context`, `## Constraints`, `## Steps`) to separate different parts of your instruction. This helps the agent parse the request accurately.
*   **Provide Concrete Examples (Few-Shot Prompting):** For any complex task or specific output format, include 1-2 clear examples of the desired outcome. This is often more effective than describing the format in words alone.
*   **State the End Goal Explicitly:** Clearly articulate the overall mission or "definition of done." This allows the agent to self-correct and make more intelligent decisions if it encounters an unexpected obstacle.
*   **Encourage Step-by-Step Thinking:** Instruct the agent to "think step-by-step" or "create a plan before executing." This forces a more deliberate reasoning process, improving accuracy and making its thought process easier to debug.
*   **Define Constraints and Boundaries:** Clearly state what the agent **should not** do. Define the scope of its authority, the tools it should avoid, or the topics it must not discuss.

### Specific Rules & Constraints

*   **IF** the task is complex and involves multiple stages, **THEN** provide the instructions as a numbered list of sequential steps.
*   **IF** the final output must adhere to a strict format (like JSON, XML, or specific Markdown), **THEN** provide a template or schema within the prompt for the agent to populate.
*   **IF** the agent might require more information to complete the task successfully, **THEN** explicitly grant it permission to ask clarifying questions before proceeding.
*   **IF** there is a possibility of failure or an error state, **THEN** provide a clear fallback intent or error-handling instruction (e.g., "If you cannot access the database, notify the user with error code 'DB-CONN-FAIL' and do not proceed.").
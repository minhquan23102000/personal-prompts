# Requirements Gathering and Documentation

This workflow guides the agent through a structured process of eliciting, clarifying, and documenting requirements from any type of user, ensuring a comprehensive and validated final document.

1.  **Initiate and Establish Context**
    *   **State:** The agent has received an initial request to gather requirements but lacks the high-level project context.
    *   **Intent:** The primary goal is to understand the project's **purpose**, the user's **role**, and the overall **business or technical objective**. The agent must establish a foundational understanding before diving into specifics.
    *   **Success Condition:** The agent can articulate a one-paragraph summary of the project's goal and has identified the primary stakeholder providing the requirements.
    *   **Fallback Intent:** If the initial request is too vague, the agent's intent shifts to **proactively asking clarifying questions** to establish the necessary context before proceeding to the next step.

2.  **Elicit High-Level Needs**
    *   **State:** The agent understands the project's context and is ready to engage the user directly on their needs.
    *   **Intent:** The intent is to prompt the user to describe their desired **outcomes**, **features**, and **goals** in their own words. The focus should be on *what* needs to be accomplished, not *how* it should be implemented.
    *   **Success Condition:** The agent has captured a list of initial, high-level requirements or user stories, and the user has confirmed this list broadly represents their vision.
    *   **Fallback Intent:** If the user is unsure how to begin, the agent should **offer prompts based on the project's context**, such as asking about the main problems to be solved or the most critical tasks the user needs to perform.

3.  **Probe for Detailed Specifications and Constraints**
    *   **State:** The agent has a list of high-level requirements that now need to be detailed.
    *   **Intent:** For each high-level requirement, the intent is to **systematically investigate for specifics**. This includes asking about user interactions, data requirements, business rules, and acceptance criteria that would define success for that feature.
    *   **Success Condition:** Each high-level requirement is supported by a set of detailed, unambiguous statements that describe its behavior and constraints.
    *   **Fallback Intent:** If a user provides a vague answer to a probing question, the agent should **rephrase the question or provide illustrative examples** to guide the user toward a more concrete and specific response.

4.  **Uncover Non-Functional Requirements**
    *   **State:** The agent has a collection of detailed functional requirements but needs to understand the system's quality attributes.
    *   **Intent:** The goal is to inquire about requirements not tied to a specific feature, such as **performance**, **security**, **usability**, **reliability**, and **compliance**.
    *   **Success Condition:** The agent has documented a list of specific, ideally measurable, non-functional requirements (e.g., "The system must be accessible to users with screen readers," "User data must be encrypted at rest").
    *   **Fallback Intent:** If the user is unfamiliar with these concepts, the agent should **explain the categories with simple examples** relevant to the project (e.g., "How fast does this need to feel for the user?" or "Are there any legal or privacy rules we must follow?").

5.  **Synthesize and Structure the Documentation**
    *   **State:** The agent has collected a comprehensive but potentially disorganized set of all requirements.
    *   **Intent:** The intent is to **organize all gathered information** into a logical, clear, and professionally structured document. This involves grouping related items, defining terminology, and assigning priorities if possible.
    *   **Success Condition:** A draft document is created that is easy to navigate and understand by both technical and non-technical stakeholders.
    *   **Fallback Intent:** If the agent identifies any **contradictory or incomplete requirements** during the synthesis process, its intent shifts to flagging these inconsistencies and preparing them for discussion in the final review step.

6.  **Facilitate Review and Final Confirmation**
    *   **State:** A structured draft of the requirements document is ready for validation.
    *   **Intent:** The primary goal is to **present the complete document to the user for final review and approval**. The agent must ensure the user agrees that the document is an accurate and complete representation of their needs. Then create completed document at prd/ folder.
    *   **Success Condition:** The user provides explicit confirmation that the document is correct and complete, formally concluding the gathering process. 
    *   **Fallback Intent:** If the user identifies errors, omissions, or requests changes, the agent must **re-engage in the appropriate prior step** (e.g., Step 3 for clarification, Step 5 for restructuring), amend the document, and then re-initiate this final review step until success is achieved.

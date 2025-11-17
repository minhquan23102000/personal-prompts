Following the instruction below and execute carefully step by step:
```
# Strategic Plan: Generating a Frontend Feature Specification

### 1. Request Ingestion & Intent Clarification
*   **State:** The agent has received a new user request for a frontend feature.
*   **Intent:** To distill the user's request into a clear, unambiguous goal statement focused on the user's needs and the problem to be solved. This involves parsing the request, identifying the core user-facing task, and resolving any ambiguities.
*   **Success Condition:** The agent possesses a single, concise goal statement that accurately reflects the user's intent from an end-user perspective.
*   **Fallback Intent:** If ambiguity cannot be resolved, the agent will report that it cannot proceed and will ask the user for specific clarifying information about the user's objective before continuing.

### 2. Context Localization & Manifest Ingestion
*   **State:** The agent has a clear goal statement.
*   **Intent:** To identify the relevant application views and ingest the project's architectural manifest (`architecture.manifest`). This involves locating and parsing documentation on the existing UI component library, design tokens (colors, fonts, spacing), and established UI patterns to understand the available building blocks.
*   **Success Condition:** The agent has a clear understanding of the existing design language and a list of reusable components that can be leveraged for the new feature.
*   **Fallback Intent:** If a design manifest cannot be found, the agent will inform the user that it will have to infer design standards from the existing codebase, which may result in inconsistencies.

### 3. High-Level UX Solutioning & Flow Mapping
*   **State:** The agent has ingested the design context and understands the user's goal.
*   **Intent:** To devise a high-level user experience solution by mapping the user's journey. The focus is on *interaction*, not visuals. The agent will define the step-by-step flow, key user actions, and system responses, and create low-fidelity wireframes to represent this flow structurally.
*   **Success Condition:** The agent has produced a clear user flow diagram and a set of corresponding wireframes, and has made a definitive decision on whether the feature introduces a new, significant design pattern, setting a boolean flag: `requires_visual_spec`.
*   **Fallback Intent:** If the agent cannot devise a user flow that aligns with existing interaction principles, it will halt, present the UX conflict to the user, and request strategic guidance.

### 4. Visual Design Specification Generation (Conditional)
*   **State:** The agent has an approved user flow and has determined that `requires_visual_spec` is `true`.
*   **Intent:** To create a high-fidelity, shareable design artifact that serves as the visual source of truth. This is the frontend equivalent of an ADR. Instead of a text document, the agent will generate a static HTML file or a structured data format representing a pixel-perfect mockup of the new interface, applying the colors, typography, and components from the design system.
*   **Success Condition:** A new, shareable `Visual Design Specification` (e.g., a self-contained HTML/CSS file) is created in a designated project directory (e.g., `docs/designs/`).
*   **Fallback Intent:** If the agent cannot generate the visual artifact due to missing assets or complex requirements, it will notify the user and include detailed textual descriptions of the visual design within the main Task Specification instead.

### 5. Detailed Implementation Blueprinting
*   **State:** The agent has a confirmed user flow and, if necessary, a generated Visual Design Specification.
*   **Intent:** To create a detailed, component-level implementation plan. The agent will perform a deep analysis of the relevant code, breaking down the UI into a hierarchy of new and existing components. It will define the properties (props), state management requirements, and data-fetching logic for each component.
*   **Success Condition:** The agent has produced a complete technical blueprint that lists all required file creations/modifications, defines component APIs, and outlines a testing plan for the new UI.
*   **Fallback Intent:** If the deep analysis reveals technical blockers (e.g., a required component is not feasible with the current framework), the agent will return to **Step 3** to reformulate the user experience with this new constraint.

### 6. Specification Synthesis
*   **State:** The agent has a complete technical blueprint and a potentially generated Visual Design Specification.
*   **Intent:** To translate the internal blueprint and associated design artifacts into a final, human-readable Frontend Task Specification document.
*   **Success Condition:** A complete and detailed Task Specification document is created, containing the user goal, the user flow, a direct link to the Visual Design Specification (if applicable), and the detailed component implementation plan.
*   **Fallback Intent:** If there is an error in generating the final document, the agent will report the failure to the user and provide the raw blueprint and design content as a fallback.

### 7. Final Review Package
*   **State:** The agent has generated all required documentation (Task Specification and, optionally, a Visual Design Specification).
*   **Intent:** To present a complete solution package to the user for final review and approval before any implementation work begins.
*   **Success Condition:** The user provides explicit approval for the entire plan, authorizing the agent to proceed to the implementation phase.
*   **Fallback Intent:** If the user requests changes, the agent will analyze the feedback. If the changes are related to the core user experience, it will return to **Step 3**. If the changes relate to implementation details, it will return to **Step 5**.
```
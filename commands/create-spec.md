
# Strategic Plan: Task Specification & Impact Analysis

**Objective:** To transform a high-level user request into a detailed, actionable technical specification. This plan must be validated against the `architecture.manifest` to ensure it is safe, efficient, and architecturally sound before any code is written.

### 1. Request Ingestion & Intent Clarification

*   **Current State:** The agent has a complete understanding of the system via the `architecture.manifest`. It has just received a new request from a user (e.g., "Implement two-factor authentication," "Fix the bug where invoices are not sending," "Add caching to the product endpoint").
*   **Primary Intent:** To parse the user's natural language request and distill it into a single, unambiguous statement of intent. The agent must resolve any ambiguity before proceeding.
*   **Success Condition:** The agent has a clear, one-sentence goal statement. If the request is vague, the agent has asked clarifying questions (e.g., "For two-factor authentication, are you referring to SMS, Authenticator App, or both?") and has received a definitive answer.
*   **Fallback Intent:** If the user's request is too ambiguous to form a clear goal and the user is unresponsive, the agent will report that it cannot proceed and will state what specific information it needs.

### 2. Context Localization via Manifest

*   **Current State:** The agent has a clear goal statement.
*   **Primary Intent:** To identify the primary Bounded Context(s) that will be affected by the change. This is the most critical step for efficiency, as it prevents the agent from needing to analyze the entire codebase.
*   **Actions:**
    1.  The agent reads the `architecture.manifest.yml`.
    2.  It analyzes the `contexts` section, comparing the `name` and `description` of each context against the goal statement.
    3.  It identifies the most relevant context(s). For "Implement two-factor authentication," it would likely identify the `UserAuthentication` context. For the invoice bug, it would identify the `Billing` or `Notifications` context.
*   **Success Condition:** The agent has a list of one or more primary context paths (e.g., `./src/contexts/UserAuthentication`) that will be the focus of its detailed analysis.
*   **Fallback Intent:** If no single context is a clear match, the agent will identify a list of potential candidates and inform the user, stating its intention to analyze them in order of probability.

### 3. Detailed Impact Analysis

*   **Current State:** The agent has narrowed its focus to one or more specific Bounded Contexts.
*   **Primary Intent:** To determine the precise "blast radius" of the proposed change within the localized context(s). This involves identifying every file, class, function, and contract that will need to be created, modified, or deleted.
*   **Actions:**
    1.  The agent performs a detailed scan of the files within the identified context path(s).
    2.  It identifies the core business logic (`domain` layer), application services, and infrastructure adapters that are relevant to the goal.
    3.  Crucially, it consults the `artifact_locations.contracts` path in the manifest to see if the change will require a modification to the public API of the context, which would affect other contexts.
*   **Success Condition:** The agent has produced an internal list of specific files and code components that will be impacted by the change.

### 4. Solution Design & Specification Generation

*   **Current State:** The agent knows exactly which parts of the code will be affected.
*   **Primary Intent:** To generate a human-readable technical specification that outlines the complete plan of action. This is the deliverable of this workflow.
*   **Actions:** The agent synthesizes its findings into a structured document (e.g., in Markdown) that includes:
    1.  **Goal:** The clear, one-sentence statement of intent from Step 1.
    2.  **Affected Contexts:** The list of Bounded Contexts from Step 2.
    3.  **Implementation Plan:** A step-by-step description of the changes.
        *   **New Files to Create:** (e.g., `src/.../TwoFactorAuthService.ts`).
        *   **Files to Modify:** With a high-level summary of the changes for each (e.g., "Modify `LoginController.ts` to add a second step for the 2FA code").
        *   **Contract Changes:** A diff of the proposed changes to the OpenAPI or gRPC schema, if any.
    4.  **Testing Strategy:** A description of the new unit, integration, or end-to-end tests that will be created to validate the change.
    5.  **Rule Compliance Check:** A statement confirming the plan adheres to the `operational_rules` defined in the manifest.
*   **Success Condition:** A complete, detailed, and clear technical specification document is generated.

### 5. User Review and Approval

*   **Current State:** The agent has a complete technical specification.
*   **Primary Intent:** To gain explicit approval from the user before proceeding with code generation and implementation. This is the critical human-in-the-loop safety and alignment gate.
*   **Success Condition:** The agent presents the specification to the user, and the user gives their explicit approval (e.g., "Yes, proceed," "Looks good"). The agent is now authorized to move to the "Execution" phase.
*   **Fallback Intent:** If the user requests changes to the plan, the agent returns to Step 4 (Solution Design) to revise the specification and presents it again for approval.

---
description: This workflow focuses exclusively on understanding requirements and creating a comprehensive solution blueprint. No code implementation or detailed test case planning occurs in this workflow. The finalized plan is documented in the `specs/` folder.
---

Goal: Create a detailed solution blueprint without writing implementation code.
- 1-Context-Request: Analyze the user's request to fully understand the goals, requirements, and constraints.
- 2-Context-Codebase: Perform a deep analysis of the existing codebase. Review relevant files in `src/`, `docs/codebase_context.md`, and existing tests to understand the current architecture and implementation.
- 3-Decompose: Break the problem into smaller, logical sub-tasks, respecting the Vertical Slice Architecture.
- 4-Design-Solution: For each sub-task, define the technical approach. List all files to be created or modified. Outline the purpose, parameters, and return values for new or changed functions and classes.
- 5-Design-Tests: For each component in the design, specify the unit and integration tests required to verify its correctness.
- 6-Create-Checklist: Synthesize the design into a detailed, step-by-step implementation checklist using `- []` syntax. Each item must be a concrete, actionable task for the implementer.
- 7-Assemble-Specification: Combine the problem summary, design details, test plan, and implementation checklist into a single, coherent specification document.
- 8-Final-Review: Review the generated specification document to ensure it is complete, logical, and fully addresses the user's request while adhering to all global rules.
- 9-Confirm: Announce completion and state that the detailed plan has been created in the `specs/` directory (e.g., `specs/feature-user-authentication.md`).
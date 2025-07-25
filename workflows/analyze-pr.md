---
description: Analyze PR feedback and create a detailed execution plan to address it.
---

Goal: Analyze PR feedback and create a detailed execution plan to address it.
- 1-Comprehend-All-Feedback: Read and process every single comment from the Pull Request to create a comprehensive list. Do not proceed to the next step until all feedback has been collected.
- 2-Analyze-Context: For each item in the comprehensive list, thoroughly analyze the associated source code to fully understand the context and the reviewer's intent.
- 3-Group-And-Categorize: Group related feedback into logical tasks. Categorize each task as a Required Change, Suggestion, or Question.
- 4-Design-Solution: For each task, create a detailed, step-by-step implementation plan. Specify the files to modify and the exact changes to be made.
- 5-Plan-Tests: Define the testing strategy for each change, including new tests to write or existing tests to update.
- 6-Assemble-Plan: Synthesize the complete analysis, categorized feedback, and the detailed implementation/test plan into a single document.
- 7-Final-Review: Review the entire plan document for clarity, accuracy, and completeness, ensuring all feedback is addressed.
- 8-Confirm-And-Save: Announce completion and save the detailed plan to a new file in the `executions/` directory, for example: `executions/pr-123-feedback-plan.md`.
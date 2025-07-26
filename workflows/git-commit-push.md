This is a step-by-step workflow for an agent tasked with turning a developer's current work-in-progress into a formal pull request.

1.  **Assess the Local Repository State**
    *   **State to Describe:** The agent must be aware of the current branch name, the list of staged and unstaged files, the configured remote repository URL, and the repository's default branch (e.g., `main` or `develop`).
    *   **Primary Intent:** To gather a complete picture of the current Git environment to ensure all preconditions for committing and creating a PR are met.
    *   **Success Condition:** The agent has successfully identified the current branch, confirmed that there are staged changes ready to be committed, and verified the existence of a remote repository.
    *   **Fallback Intent:** If there are no staged changes, the agent should **inform the user** and ask them to stage the files they want to include in the commit. If there is no remote repository configured, it should **notify the user** that it cannot create a pull request and ask if they wish to proceed with a local commit only.

2.  **Analyze Staged Code Changes**
    *   **State to Describe:** The full content difference (`diff`) of all files currently in the staging area.
    *   **Primary Intent:** To understand the semantic meaning of the changes. The agent's goal is to determine if the work constitutes a new feature, a bug fix, a performance improvement, a refactor, or another category of change.
    *   **Success Condition:** The agent has processed the `diff` and has formed a high-level summary of the change's purpose, scope, and potential impact.
    *   **Fallback Intent:** If the `diff` is empty or the changes are too complex to be summarized automatically, the agent should **revert to the user** and ask for a manual, one-sentence summary of the work performed.

3.  **Draft the Commit Message and Pull Request Body**
    *   **State to Describe:** The summary of the code changes from the previous step. The agent should also have its internal `Mental Model` for generating conventional commits available.
    *   **Primary Intent:** To generate a clear, conventional, and descriptive commit message. This message should have a concise subject line and a more detailed body explaining the "why" behind the changes. This same content will be repurposed for the pull request body.
    *   **Success Condition:** A complete, well-formatted commit message and PR body are drafted and stored.
    *   **Fallback Intent:** If the agent cannot confidently generate a full message, it should **create a basic template** based on the file names changed and **ask the user to complete it**.

4.  **Propose and Confirm the Action Plan**
    *   **State to Describe:** The drafted commit message, the source branch, and the target branch for the pull request.
    *   **Primary Intent:** To present the generated commit message and the intended pull request plan (e.g., "merge `feature/new-login` into `main`") to the user for final approval or modification before making any permanent changes.
    *   **Success Condition:** The user has approved the message and the PR plan, either as-is or with their own edits.
    *   **Fallback Intent:** If the user rejects the plan or the message and does not provide an alternative, the agent must **terminate the workflow** gracefully without taking any action.

5.  **Execute the Local Commit**
    *   **State to Describe:** The user-approved commit message.
    *   **Primary Intent:** To apply the staged changes to the local repository's history by executing the commit action with the approved message.
    *   **Success Condition:** The commit operation completes successfully in the local repository.
    *   **Fallback Intent:** If the commit command fails (e.g., due to a pre-commit hook failure), the agent must **report the exact error** from the system to the user and halt the process.

6.  **Synchronize Branch with the Remote Repository**
    *   **State to Describe:** The name of the current local branch and the remote repository's URL.
    *   **Primary Intent:** To push the newly created commit(s) on the current branch to the remote repository, making them available for a pull request.
    *   **Success Condition:** The push operation completes successfully, and the remote branch is now up-to-date with the local branch.
    *   **Fallback Intent:** If the push fails (e.g., due to conflicts, authentication failure, or a protected branch rule), the agent must **report the specific error** and advise the user on potential next steps (e.g., "You may need to pull the latest changes first" or "Please check your credentials").

7.  **Initiate the Pull Request**
    *   **State to Describe:** The source branch name, the target branch name, the approved PR title (from the commit subject), and the PR body (from the commit body).
    *   **Primary Intent:** To formally propose the changes for review and merging by creating a pull request on the code hosting platform (e.g., GitHub, GitLab).
    *   **Success Condition:** The hosting platform confirms that the pull request has been created successfully and returns its URL.
    *   **Fallback Intent:** If the API call to create the PR fails, the agent should **report the error** to the user. It should also **provide a pre-filled URL or a command-line instruction** that the user can use to create the PR manually with the already-pushed branch.

8.  **Report Final Status**
    *   **State to Describe:** The URL of the newly created pull request or an error message from a previous step.
    *   **Primary Intent:** To provide the user with a final, conclusive summary of the outcome.
    *   **Success Condition:** The agent presents the user with a direct, clickable link to the newly created pull request and confirms the workflow is complete.
    *   **Fallback Intent:** The agent clearly communicates at which step the process failed and provides the relevant error message and context, ensuring the user knows the exact state of their repository.
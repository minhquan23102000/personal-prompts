# Strategic Plan: Comprehensive Architectural Manifest Generation 

**Objective:** To empower an AI agent with a step-by-step workflow to analyze any existing codebase, infer its architectural properties and operational rules, and synthesize this information into a single, canonical `architecture.manifest.yml` file.

**Guiding Philosophy:** The process is a systematic investigation, moving from broad project identification to specific rule extraction. The final output must be a complete, machine-readable "owner's manual" for the repository, enabling any future stateless AI agent to operate effectively and safely.

### Step 1: Initial Reconnaissance & Tooling Discovery

*   **Current State:** The agent has access to the root directory of the project but holds no prior knowledge.
*   **Primary Intent:** To establish a foundational understanding of the project's identity, technology stack, and configured development tools. This is the first layer of context.
*   **Actions:**
    1.  **Scan Metadata:** Read and parse root-level files like `README.md`, `package.json` (for Node.js), `pom.xml` (for Java/Maven), `pyproject.toml` (for Python), `go.mod` (for Go), etc.
    2.  **Identify Tooling:** Specifically search for common configuration files for linters, formatters, and style guides (e.g., `.eslintrc.json`, `.prettierrc`, `checkstyle.xml`, `.flake8`, `STYLE_GUIDE.md`).
*   **Manifest Fields Populated:**
    *   `system_name`: Inferred from the project name in a configuration file or the repository's directory name.
    *   `system_purpose`: Extracted from the primary description in the `README.md`.
    *   `primary_language_framework`: Determined from the project's dependency management file.
    *   `operational_rules.tooling_configurations`: Each discovered tooling configuration file is mapped with its key (e.g., `linter`, `formatter`) and its relative path.
*   **Fallback Intent:** If metadata files are missing, the agent will analyze file extensions to determine the language. It will populate text fields with placeholder values like `"[AUTO-GENERATED] Please provide a system purpose."` and set tooling paths to `null`.

### Step 2: Bounded Context Identification & Mapping

*   **Current State:** The agent knows the project's purpose and tech stack.
*   **Primary Intent:** To deconstruct the codebase into its primary, high-level business domains or modules. This step is the core of the architectural discovery.
*   **Actions:**
    1.  **Locate Source Directory:** Identify the main source code directory (commonly `src/`, `app/`, `packages/`, or the project root itself).
    2.  **Analyze Subdirectories:** List the subdirectories within the source directory. The agent will use heuristics and its natural language understanding to identify directories whose names represent business concepts (e.g., `billing`, `user_management`, `inventory_service`, `ticket-api`) rather than generic patterns (e.g., `utils`, `helpers`, `components`).
*   **Manifest Fields Populated:**
    *   `contexts`: A list is created. For each directory identified as a Bounded Context, a new entry is added:
        *   `name`: A PascalCase version of the directory name (e.g., `user_management` becomes `UserManagement`).
        *   `path`: The full relative path to the directory from the root.
        *   `description`: A placeholder is generated for human review, e.g., `"[AUTO-GENERATED] Manages the 'UserManagement' domain. Please refine this description."`
*   **Fallback Intent:** If the structure is monolithic or flat, the agent will identify the single main source directory as the sole context (e.g., `name: Monolith, path: ./src`). It will report to the user that the architecture appears non-modular, which is a critical piece of information in itself.

### Step 3: Architectural Pattern Inference

*   **Current State:** The agent has a map of the identified Bounded Contexts.
*   **Primary Intent:** To infer the architectural pattern(s) that govern the codebase, providing a crucial mental model for how the code is organized and how it should be modified.
*   **Actions:**
    1.  **Analyze Macro-Structure:** Evaluate the relationship between the identified contexts.
    2.  **Analyze Micro-Structure:** For each context, examine its internal subdirectory structure.
*   **Manifest Fields Populated:**
    *   `architectural_patterns`: A list is populated based on evidence:
        *   If multiple contexts were found -> add `"Domain-Driven Design"`.
        *   If a context contains subdirectories like `domain`, `application`, and `infrastructure` -> add `"Hexagonal Architecture"`.
        *   If the root contains a `docker-compose.yml` or Kubernetes manifests referencing multiple context-specific services -> add `"Microservices"`.
        *   If only a single context was found -> add `"Monolith"`.
*   **Fallback Intent:** If the structure is ambiguous, the agent will set the field to `["unclassified"]` and notify the user that it could not confidently identify a standard pattern.

### Step 4: Rule and Guideline Discovery

*   **Current State:** The agent understands the system's structure and patterns.
*   **Primary Intent:** To discover and codify the human-readable rules and processes that govern development within the repository.
*   **Actions:**
    1.  **Targeted File Parsing:** The agent will specifically locate and perform a natural language analysis of files like `CONTRIBUTING.md`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, and any documents within a `/docs` or `/architecture` directory.
    2.  **Rule Extraction:** It will look for imperative statements, keywords ("must", "should", "forbidden"), and section headers ("Testing Policy", "Commit Message Format") to extract rules.
*   **Manifest Fields Populated:**
    *   `operational_rules.architectural_guardrails`: Populated with extracted rules about dependencies, module communication, and design principles.
    *   `operational_rules.code_quality_gates`: Populated with rules about testing requirements, code coverage, and review processes.
    *   `operational_rules.contribution_guidelines`: Populated with rules about commit message formats, branching strategies, and pull request procedures.
*   **Fallback Intent:** If these documentation files do not exist or contain no clear rules, the agent will populate each rule list with a single, placeholder string: `["[AUTO-GENERATED] No explicit rules found. Please define them here."]` This makes the absence of rules explicit and prompts the user for input.

### Step 5: Discovery of Key Artifact Locations

*   **Current State:** The agent has a near-complete picture of the architecture and its rules.
*   **Primary Intent:** To locate the precise paths to important, non-code assets that are critical for development and interaction.
*   **Actions:**
    1.  **Perform Targeted Search:** The agent will search the entire repository for common directory names (`/contracts`, `/schemas`, `/docs/adr`, `/tests`, `/e2e`) and file types (`*.openapi.yml`, `*.proto`, `*.graphql`, `*.md`).
*   **Manifest Fields Populated:**
    *   `artifact_locations`: This object is populated with the discovered relative paths. If a specific artifact type is not found, its value is explicitly set to `null`.

### Step 6: Synthesis and Manifest Generation

*   **Current State:** The agent has gathered all required data points.
*   **Primary Intent:** To assemble all the discovered and inferred information into a single, well-formatted, and syntactically valid `architecture.manifest.yml` file.
*   **Actions:**
    1.  **Construct YAML:** The agent will build a YAML string that conforms precisely to the defined manifest structure.
    2.  **Write to File:** The agent will save this string to a new file named `architecture.manifest.yml` in the project's root directory.
*   **Fallback Intent:** If a critical piece of information (like the Bounded Contexts) could not be determined, the agent will still generate the file but will use placeholder values and add a comment at the top of the file indicating its draft status.

### Step 7: Presentation and User Validation

*   **Current State:** A draft `architecture.manifest.yml` exists in the file system.
*   **Primary Intent:** To present the auto-generated manifest to the user for final validation, refinement, and approval. This human-in-the-loop step is non-negotiable to ensure accuracy.
*   **Actions:**
    1.  **Display Manifest:** The agent will output the file path of the generated manifest to the user.
    2.  **Request Feedback:** The agent will explicitly ask the user to review the inferred sections, such as `contexts`, `architectural_patterns`, and `operational_rules`, as these are most subject to interpretation.
    3.  **Apply Corrections:** The agent will apply any requested changes directly to the `architecture.manifest.yml` file, saving the final, user-approved version.
*   **Fallback Intent:** If the user does not provide feedback, the agent will add a comment to the top of the generated file, such as `# WARNING: This is an auto-generated draft. Please review for accuracy before use.`, to ensure the file is not treated as a definitive source of truth without human validation.

# Mental Model: The In-Code Context Engineer

This model defines the agent's fundamental approach to software creation. The core principle is that code is not something to be documented later; **well-written code *is* the documentation.** Every choice—from a variable name to a log message—is an act of embedding clear, machine-readable, and human-readable context.

### Core Principles

*   **Clarity is the Primary Feature:** The most important function of any code is to be understood. Code that is difficult to understand is broken by default, regardless of whether it executes correctly. Readability is a non-negotiable functional requirement.
*   **The Code is the Ultimate Authority:** Comments and external documents can lie or become stale. The code's structure, types, and logic are the only guaranteed source of truth. Therefore, this truth must be made as explicit and self-evident as possible.
*   **Explicitness Over Implicitness:** The agent must strive to eliminate ambiguity and "magic." The shape of data, the purpose of a function, and the state of the system should be explicitly declared, not inferred by a reader.
*   **Runtime Behavior Must Be Observable:** Static code clarity is insufficient. The agent's work must be transparent in production. The system's execution path, state changes, and errors must be captured in a structured way to provide a clear story of its runtime behavior for human engineers.
*   **Machine Readability and Human Readability are the Same Goal:** Code that is well-structured for a machine—with strong types, clear function signatures, and consistent patterns—is also easier for a human to reason about. By optimizing for one, we achieve the other.

### Best Practices (The Pillars of In-Code Context)

1.  **Naming is Revelation:**
    *   Variable, function, and class names are the most fundamental layer of documentation. They should be descriptive, unambiguous, and complete. A good name makes a comment unnecessary.
    *   **Example:** Prefer `is_ready_for_processing` over `status_flag`. Prefer `calculate_sales_tax_for_region` over `process_data`.

2.  **The Type System is the Contract:**
    *   Static type hints are a formal, machine-enforceable contract that describes the shape of data flowing through the system.
    *   Use specific, modern types (`list[str]`, `dict[str, int]`). For complex data structures, define them explicitly. This makes the data's structure part of the code's explicit definition.

3.  **Structure Reveals Intent:**
    *   The physical layout of the code should tell a story.
    *   **Functions:** A function should do one thing and do it well. Its small size and focused purpose make its intent obvious.
    *   **Modules/Files:** Files should group related functions and classes. A file named `user_authentication.py` clearly communicates its purpose.
    *   **Directories:** The directory structure should mirror the application's domain, separating concerns logically (e.g., `api/`, `data_processing/`, `utils/`).

4.  **Docstrings are the API's User Manual:**
    *   A docstring provides the high-level narrative for a module, class, or function. It explains the "why" and its place in the system. It is the primary guide for other developers on how to use the code correctly.
    *   A complete docstring includes a concise summary of the object's purpose, and a practical, copy-pasteable usage example. Keep the docstring really short, clear, and clean as a summary. The code itself should provide the details.

5.  **Logging is Structured Storytelling:**
    *   Logs are not just error messages; they are a chronological, structured narrative of the application's life. Effective logging allows an engineer to debug production issues by understanding what the system was doing and thinking at a specific point in time.
    *   Logs should be structured (e.g., JSON format) and contain rich context, such as relevant IDs, state information, and the specific operation being performed. Use different log levels to distinguish between routine information, potential warnings, and critical errors.

6.  **Encode State Explicitly:**
    *   Avoid using primitive types like strings or booleans to represent a fixed set of states.
    *   Instead, use `Enums` to define a finite set of possible states (e.g., `class UserStatus(Enum): ACTIVE = "active"; PENDING = "pending"`). This makes invalid states impossible and the code self-documenting.

7.  **Inline Comments are for Explaining the "Why":**
    *   Inline comments are a last resort, used only when the code's structure cannot possibly explain the reason behind a decision.
    *   A good comment explains the business rationale, technical trade-offs, or workarounds for external system bugs. It must never explain *what* the code is doing—the code itself should do that.

### Specific Rules & Constraints

*   **Every public-facing module, class, and function MUST have a docstring** that clearly explains its purpose, its role in the system, and provides a clear usage example.
*   **Every function and method signature MUST have complete and specific type hints** for all arguments and the return value. The use of `Any` is strictly forbidden unless it is the only possible, justifiable type.
*   **If an operation fails or an exception is caught, then a log of level `ERROR` MUST be generated.** This log must include the full exception details and contextual information (e.g., user ID, transaction ID) needed for debugging.
*   **If a significant business process or state transition occurs, then a log of level `INFO` SHOULD be generated** to trace the normal flow of the application.
*   **The agent is forbidden from logging sensitive user data** in plain text, including passwords, API keys, and personally identifiable information (PII).
*   **The agent is forbidden from using "magic values"** (unnamed, hardcoded strings or numbers). Any such value must be defined as a constant with a descriptive, all-caps name (e.g., `MAX_RETRIES = 3`).
*   **The agent is forbidden from writing a function longer than 25 lines of logic.** If a function exceeds this, it is a signal that its purpose is not singular, and it must be refactored into smaller, more focused helper functions.
*   **A function's name MUST be a verb or verb phrase** that describes its action or effect (e.g., `fetch_user_profile`, `validate_input`).

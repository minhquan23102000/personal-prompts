# Mental Model: The In-Code Context Engineer

This model defines the agent's fundamental approach to software creation. The core principle is that code is not something to be documented later; **well-written code *is* the documentation.** Every choice—from a variable name to a directory structure—is an act of embedding clear, machine-readable, and human-readable context.

### Core Principles

*   **Clarity is the Primary Feature:** The most important function of any code is to be understood. Code that is difficult to understand is broken by default, regardless of whether it executes correctly. Readability is a non-negotiable functional requirement.
*   **The Code is the Ultimate Authority:** Comments and external documents can lie or become stale. The code's structure, types, and logic are the only guaranteed source of truth. Therefore, this truth must be made as explicit and self-evident as possible.
*   **Explicitness Over Implicitness:** The agent must strive to eliminate ambiguity and "magic." The shape of data, the purpose of a function, and the state of the system should be explicitly declared, not inferred by a reader.
*   **Machine Readability and Human Readability are the Same Goal:** Code that is well-structured for a machine—with strong types, clear function signatures, and consistent patterns—is also easier for a human to reason about. By optimizing for one, we achieve the other.

### Best Practices (The Five Pillars of Self-Describing Code)

1.  **Naming is Revelation:**
    *   Variable, function, and class names are the most fundamental layer of documentation. They should be descriptive, unambiguous, and complete. A good name makes a comment unnecessary.
    *   **Example:** Prefer `is_ready_for_processing` over `status_flag`. Prefer `calculate_sales_tax_for_region` over `process_data`.

2.  **The Type System is the Contract:**
    *   Static type hints are not suggestions; they are a formal, machine-enforceable contract that describes the shape of data flowing through the system.
    *   Use specific, modern types (`list[str]`, `dict[str, int]`). For complex data structures, define them explicitly using `TypedDict`, `dataclasses`, or Pydantic models. This makes the data's structure part of the code's explicit definition.

3.  **Structure Reveals Intent:**
    *   The physical layout of the code should tell a story.
    *   **Functions:** A function should do one thing and do it well. Its small size and focused purpose make its intent obvious.
    *   **Classes:** A class should represent a single, coherent concept.
    *   **Modules/Files:** Files should group related functions and classes. A file named `user_authentication.py` clearly communicates its purpose.
    *   **Directories:** The directory structure should mirror the application's domain, separating concerns logically (e.g., `api/`, `data_processing/`, `utils/`).

4.  **Encode State Explicitly:**
    *   Avoid using primitive types like strings or booleans to represent a fixed set of states. This is "primitive obsession."
    *   Instead, use `Enums` to define a finite set of possible states (e.g., `class UserStatus(Enum): ACTIVE = "active"; PENDING = "pending"`). This makes invalid states impossible and the code self-documenting.

5.  **Inline Comments are the Rationale (The "Why")**
    *   Inline comments are the final and most surgical layer of communication. They are a last resort, used only when the code's structure cannot possibly explain the reason behind a decision.
    *   **A Good Comment Explains the "Why," Never the "What" or "How."**
    *   **Valid Reasons for a Comment:**
        *   **Business Rationale:** `// Apply a 5% surcharge for international orders, as per Q3 business rules.`
        *   **Technical Trade-offs:** `// Using a less accurate algorithm here for a 10x performance gain.`
        *   **Workarounds:** `// This value is hardcoded to 2 because the legacy API (v1.2) has a bug.`
        *   **Intentional Non-Obviousness:** `// This check seems redundant, but it prevents a race condition during user creation.`

### Specific Rules & Constraints

*   **A function's name MUST be a verb or verb phrase** that describes its action or effect (e.g., `fetch_user_profile`, `validate_input`).
*   **Every function and method signature MUST have complete and specific type hints** for all arguments and the return value. The use of `Any` is strictly forbidden unless it is the only possible, justifiable type.
*   **The agent is forbidden from using "magic values"** (unnamed, hardcoded strings or numbers). Any such value must be defined as a constant with a descriptive, all-caps name (e.g., `MAX_RETRIES = 3`).
*   **The agent is forbidden from writing a function longer than 20 lines of logic.** If a function exceeds this, it is a signal that its purpose is not singular, and it must be refactored into smaller, more focused helper functions.
*   **Docstrings have a specific, limited purpose:** They are to be used ONLY for providing a copy-pasteable **usage example** or for explaining complex, high-level concepts that cannot be captured by the code's structure alone. They are not for explaining what parameters are—the type hints and names do that.
*   **Inline comments are a last resort.** Before writing a comment, the agent must first try to refactor the code to make the comment unnecessary. A comment is only permitted to explain the *why* (e.g., the business rationale or a non-obvious trade-off), never the *how*.
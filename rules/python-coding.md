### Rules & Best Practices: Effective Python Coding (Python 3.12+)

#### 1. Code Correctness & Robustness

*   **Always Use Specific and Modern Type Hints** (This is non-negotiable for robust code. It enables static analysis tools to catch errors before runtime and makes code self-documenting).
    *   Be specific. Instead of `dict` or `list`, define the contents, like `dict[str, int]` or `list[float]`.
    *   Use modern union syntax. Prefer `int | str` over `Union[int, str]`.
*   **Employ Pydantic for Data Validation and Settings** (When data correctness is critical, especially in APIs or data processing, Pydantic is the standard. It uses your type hints to parse, validate, and serialize data at runtime, providing a powerful layer of defense against bad data).
*   **Enforce Clarity with Keyword Arguments** (When calling a function or instantiating a class, use keyword arguments like `my_func(user_id=123, status='active')`. This prevents bugs from incorrect argument order and dramatically improves readability).
    *   In your own functions, define keyword-only arguments to force this behavior: `def process_data(*, user_id: int, records: list): ...`.
*   **Write Comprehensive Tests** (Untested code is broken by default. Use frameworks like `pytest` to write unit, integration, and functional tests to ensure your code behaves as expected and to prevent future regressions). Write meaningful tests for your logic (to verify correctness, prevent regressions, and give you the confidence to refactor aggressively).
*   **Handle Exceptions Explicitly** (Anticipate what can go wrong and use `try...except` blocks to manage errors gracefully. Catch specific exceptions rather than a bare `except:`, which can hide bugs).

#### 2. Structure & Modern Patterns

*   **Leverage Dataclasses for Data-Centric Objects** (When you need a class primarily to hold data, use `@dataclass`. It automatically generates boilerplate methods like `__init__`, `__repr__`, and `__eq__`, resulting in cleaner, more concise code).
*   **Use the `match...case` Statement for Complex Conditionals** (For scenarios with multiple conditions based on an object's structure or value, structural pattern matching is often cleaner and more powerful than a long chain of `if/elif/else` statements).
*   **Keep Functions Small and Focused** (A function should do one thing and do it well. This makes functions easier to understand, test, and reuse).
*   **Don't Repeat Yourself (DRY)** (If you find yourself copying and pasting code, refactor it into a reusable function, class, or module. This improves maintainability and reduces errors).
*   **Organize Imports Logically** (Group imports in this order: 1. Standard library, 2. Third-party libraries, 3. Your own application modules. Use a tool like `isort` or `ruff` to automate this).

#### 3. Readability & Style (The Zen of Python)

*   **Prioritize Readability Above All Else** (Write code for humans first, computers second. Clear, understandable code is easier to maintain and debug for you and your team).
*   **Adhere Strictly to PEP 8** (This is the universal style guide for Python. Consistent formatting is the mark of a professional. Use a formatter like `black` or `ruff format` to enforce it automatically).
*   **Prefer f-Strings for All String Formatting** (They are the most readable, concise, and performant way to format strings in modern Python. Example: `f"Processing user {user_id}."`).
*   **Use Descriptive and Unambiguous Names** (Variable and function names should clearly state their purpose. Avoid single-letter names except for simple, conventional counters like `i` or `j`).
*   **Comment the "Why," Not the "What"** (Your code should explain *what* it is doing through clear naming and structure. Use comments to explain the *reasoning* behind complex logic or design choices).

#### 4. Tooling & Environment

*   **Always Work Within a Virtual Environment** (Use tools like `uv` or `poetry` to create an isolated environment for each project. This prevents dependency conflicts and ensures project reproducibility).
*   **Use a Linter and Formatter** (Integrate tools like `ruff` (which combines linting, formatting, and import sorting) into your workflow. They automatically find errors, enforce style, and keep your codebase clean and consistent).
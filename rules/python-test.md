# Rules & Best Practices: Testing Python with Pytest

## **Structure & Naming**
*   **Mirror Your Application Structure** (to make it intuitive to locate corresponding tests). If you have a `src/main/utils.py`, your test should be in `tests/main/test_utils.py`.
*   **Use a Dedicated `tests/` Directory** (to clearly separate test code from application code). This directory should be at the root of your project, alongside your source directory (e.g., `src/`).
*   **Follow Standard Naming Conventions** (so that `pytest` can automatically discover tests). Test files must be prefixed with `test_` or end with `_test.py`. Test functions and methods must be prefixed with `test_`.
*   **Use Descriptive Names for Tests** (to clearly state what each test is checking). A name like `test_login_with_invalid_password_raises_error` is much clearer than `test_login_2`.

## **Test Design & Philosophy**
*   **Test One Thing at a Time** (to ensure that a failing test points directly to a specific bug). A single test function should focus on one behavior or functionality.
*   **Keep Tests Independent and Isolated** (so they can be run in any order and a failure in one test does not impact another). Each test should set up its own required state and not depend on the outcomes of other tests.
*   **Test Behavior, Not Implementation** (to make tests less brittle and resistant to refactoring). Focus on the inputs and outputs of a function, not on how it internally achieves the result.
*   **Use `assert` for Simple, Readable Checks** (to leverage `pytest`'s detailed failure reporting). Avoid complex logic in your tests; a simple `assert` statement is powerful and clear.
*   **Arrange, Act, Assert (AAA)** (to structure your tests in a clean, predictable pattern).
    *   **Arrange:** Set up the preconditions and inputs.
    *   **Act:** Call the function or method you are testing.
    *   **Assert:** Check that the outcome is what you expected.

## **Fixtures**
*   **Use Fixtures to Manage Dependencies and State** (to promote reusability and reduce code duplication). Fixtures are ideal for setting up resources like database connections, temporary files, or complex object instances.
*   **Keep Fixtures Small and Focused** (to ensure they are simple to understand and manage). A fixture should do one setup task well.
*   **Define Shared Fixtures in `conftest.py`** (to make them automatically available to all tests in that directory and its subdirectories without needing to be imported).
*   **Choose the Right Fixture Scope** (to optimize test performance by avoiding redundant setup and teardown). Use scopes like `function` (default), `class`, `module`, or `session` based on how widely the resource can be shared.

## **Parametrization & Data Management**
*   **Use `@pytest.mark.parametrize` to Avoid Redundant Tests** (to run the same test logic with multiple different inputs). This is highly effective for testing various edge cases with minimal code.
*   **Separate Test Data from Test Logic** (to improve readability and maintainability). Parametrization helps achieve this by clearly listing the test cases (inputs and expected outputs) separate from the test's execution steps.
*   **Give Descriptive IDs to Parametrized Tests** (to make it easier to identify which specific test case failed). Use the `ids` argument in `@pytest.mark.parametrize` for clarity.

## **Advanced Practices**
*   **Use `pytest.raises` to Test for Expected Exceptions** (to write clean, explicit checks for error-handling code). This is far better than a `try...except` block within a test.
*   **Use Mocking to Isolate the Code Under Test** (to prevent external systems like databases or APIs from affecting your unit test results). Libraries like `unittest.mock` (which `pytest` integrates with) are essential for this.
*   **Use Markers (`@pytest.mark`) to Categorize Tests** (to selectively run subsets of your test suite, such as `slow`, `integration`, or `smoke`). This allows for more efficient testing workflows.
*   **Measure Code Coverage** (to identify parts of your codebase that are not being executed during your tests). Use a tool like `pytest-cov` to generate coverage reports and aim for a sensible target (e.g., 80%) to ensure test thoroughness.
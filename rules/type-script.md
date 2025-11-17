# Mental Model for a TypeScript 

### Core Principles

*   **Clarity and Readability are Paramount:** Code is read far more often than it is written. The agent's primary goal is to write code that is self-documenting. TypeScript's features must be used to make the intent, data structures, and contracts between different parts of the code as explicit and unambiguous as possible.
*   **Type Safety is the Foundation of Trust:** The fundamental purpose of using TypeScript is to catch errors during development, not in production. The agent must always prioritize providing the compiler with the maximum amount of information to prevent runtime errors before they can occur. Every decision should favor compile-time safety.
*   **Maintainability is the Ultimate Goal:** Code must be structured for long-term health and collaboration. It should be easy for another developer (or another agent) to understand, refactor, and extend without introducing unintended side effects. This means favoring modularity, consistency, and established patterns.

### Best Practices

*   **Embrace Strong and Explicit Typing:** For all complex data structures, such as API responses, function parameters, and application state, define clear `interface` or `type` aliases. This creates a verifiable contract that the rest of the application can rely on.
*   **Leverage Type Inference for Simplicity:** When a variable's type is obvious from its initial assignment (e.g., `const name = "Alice";`), allow the TypeScript compiler to infer the type. This reduces visual noise and verbosity without sacrificing any type safety.
*   **Prefer Immutability to Prevent Side Effects:** Treat data as immutable wherever possible. Use the `readonly` keyword for properties in interfaces and classes, and use `Readonly<T>` or `as const` for collections. This prevents entire classes of bugs caused by unexpected state mutations.
*   **Organize Logic with Modules:** Keep files small and focused on a single responsibility (e.g., a single component, a specific service). Use ES modules (`import`/`export`) to create a clear dependency graph, encapsulate logic, and improve tree-shaking.
*   **Use Modern Language Features for Safer Code:** Prefer modern ECMAScript features that enhance safety and readability. This includes using optional chaining (`?.`) and nullish coalescing (`??`) to safely handle potentially `null` or `undefined` values.
*   **Document Complex Logic with JSDoc:** For complex functions, types, or modules, provide JSDoc comments. The TypeScript language service uses these comments to provide richer context, better autocompletion, and inline documentation in editors.

### Specific Rules & Constraints

*   **If the TypeScript configuration (`tsconfig.json`) does not have `strict: true` enabled**, then it must be the first thing to be activated. All code must be written to be `strict`-compliant.
*   **The `any` type is forbidden.** If a type is genuinely unknown, the agent must use the `unknown` type and perform explicit type-checking (e.g., using `typeof`, `instanceof`, or type guards) before the value can be used.
*   **If a variable's value will not be reassigned**, then it must be declared with `const`. The `let` keyword should only be used when reassignment is necessary. The `var` keyword must never be used.
*   **If defining the shape of an object or the contract for a class**, then the agent should prefer using an `interface`. If defining a union, intersection, or a function signature, a `type` alias is preferred.
*   **Non-null assertions (the `!` operator) must be avoided.** If a value can be `null` or `undefined`, the code must explicitly handle that possibility with a conditional check or other type-safe mechanism.
*   **If a function does not return a value**, then its return type must be explicitly defined as `void`.
*   **Always use the `===` and `!==` operators** for comparisons. The `==` and `!=` operators, which perform type coercion, are forbidden.
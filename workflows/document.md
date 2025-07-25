Goal: Generate comprehensive documentation for a specific code module.
- 1-Analyze: Read and understand the specified code module(s). Identify all public modules, classes, functions, and methods.
- 2-Add-Docstrings: For every public object lacking a docstring, write one that adheres to the Google Python Style standard.
- 3-Review-Docstrings: Review all existing docstrings for accuracy, clarity, and completeness. Update them as needed to reflect the current code.
- 4-Update-Context: Analyze the module's role in the architecture. If it is a key component, update `docs/codebase_context.md` with its purpose and interactions.
- 5-Update-Readme: Determine if the module's functionality requires changes to any `README.md` files (e.g., new setup, new script to run). Update if necessary.
- 6-Final-Check: Read through all generated and updated documentation to ensure it is clear, consistent, and accurate.
- 7-Confirm: Announce the completion of the documentation task and list all modified documentation files.
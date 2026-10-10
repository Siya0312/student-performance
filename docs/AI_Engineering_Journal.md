
# AI Engineering Journal

## Project Details
Project: Student CGPA Performance Management System
IDE: Visual Studio Code
Language: Python
AI Assistant: Claude Code / Copilot Chat interface shown in VS Code
Version Control: Git and GitHub
Quality Tools: Black, Ruff, Pytest

## Entry 1: Repository Context
**Objective:** Provide project-specific instructions to the AI assistant.

**Prompt:** Read .github/copilot-instructions.md and summarize the coding standards, testing requirements, project structure, and responsible AI rules.

**Observation:** The assistant summarized the source and test directories, coding standards, testing requirements, and responsible AI rules.

**Human Validation:** Compared the response with the instructions file.

**Decision:** Use the instructions as project guidance and review all future AI suggestions before accepting them.


## Entry 2: AI-Assisted Code Generation

**Prompt:** Inspect the CGPA source code and suggest an improvement, showing a diff without modifying files.

**AI Suggestion:** Add summarize_performance() to return the CGPA and performance category together. Use a TypedDict named PerformanceSummary to specify the result structure.

**Human Validation:** Reviewed the proposal and identified the need for explicit field types. Checked that the original public functions remained available.

**Decision:** Accepted the structured summary approach and reviewed the implementation.

## Entry 3: Code Explanation

**Prompt:** Explain how the existing CGPA calculation and performance categorisation work.

**Observation:** The assistant explained the weighted-average CGPA formula,
input validation, typed summary structure, and performance categories.

**Human Validation:** Compared the explanation with the implementation
and verified that the existing tests passed.

## Entry 4: Test Generation

**Prompt:** Generate pytest tests for summarize_performance(), including valid results and invalid inputs.

**AI Suggestion:** Six tests covering normal results, high CGPA, empty inputs, mismatched lengths, invalid grade points, and invalid credits.

**Human Validation:** The initial run exposed a missing import. After correcting it, one test still failed because the expected CGPA was incorrect (9.43 instead of 9.45).

**Decision:** Corrected the expected value after checking the weighted-average calculation. Final result: 14 tests passed.

## Entry 5: Debugging

**Issue:** AI-generated tests initially failed due to a missing import and an incorrect expected CGPA.

**Fix:** Added the required import and corrected the expected CGPA to 9.45.

**Verification:** Pytest completed with 14 passed.

## Entry 6: Refactoring

**Objective:** Improve maintainability by providing a reusable, typed performance summary.

**Change:** Added PerformanceSummary and summarize_performance() while retaining the existing calculation and categorisation functions.

**Validation:** Black reformatted the source file, Ruff reported all checks passed, and pytest reported 14 passed.

## Security and Responsible AI

- Never provide passwords, API keys, access tokens, or confidential data to an AI assistant.
- Review AI-generated code and test expectations before accepting them.
- Run tests and quality checks instead of relying on AI claims.
- Keep a record of meaningful changes and Git commits.

## Final Validation

- Pytest: 14 passed.
- Black: Source file formatted successfully.
- Ruff: All checks passed.
- Git traceability: Changes to be committed after final review.




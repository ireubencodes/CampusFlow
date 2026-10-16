# CampusFlow AI Learning Log

This log records AI-assisted learning and engineering decisions for the project.
Each engineer must complete at least two cycles using their actual work and
evidence. Replace every prompt below with the exact question that was asked.
Do not claim a test, experiment, review, or verification unless it was performed.

## Engineer A: Reuben Israel Ojochegbe

### Cycle 1: Git collaboration and branches

- **Learning gap:** I understood basic Git commands such as committing and pushing, but I needed a clearer understanding of how branches and pull requests support teamwork when working on an existing project.
- **Question asked:** How can I collaborate effectively with a new teammate on an existing GitHub repository that already contains multiple branches?
- **Key learning:** I learned to inspect the current branch and working tree, create a separate branch for a task, make focused commits, push changes, and open a pull request for review. I also learned why feature work should not be committed directly to `main`.
- **Unrelated mini-experiment:** To be completed with an experiment actually performed outside this collaboration task.
- **Verification and evidence:** Confirm the relevant commands, commits, and pull requests in the repository history before submission.
- **Engineering decision:** I will use task-specific branches and pull requests for collaborative work, checking my branch and working-tree status before making changes.

### Cycle 2: Validation and JSON persistence

- **Learning gap:** I needed to understand how ticket validation, structured notes, and JSON storage work together, especially how invalid data should be handled.
- **Question asked:** How can I validate ticket records and structured notes while ensuring that loading and saving JSON data does not silently accept invalid records?
- **Key learning:** I learned that validation should cover required fields, unique identifiers, allowed values, priority consistency, legal statuses, and note structure. The entire collection should be validated before it is accepted or saved.
- **Unrelated mini-experiment:** To be completed with an experiment actually performed outside the main CampusFlow validation and persistence task.
- **Verification and evidence:** The storage implementation was inspected. The integrated test suite previously passed 82 tests; rerun it and record the current result before submission.
- **Engineering decision:** I documented the JSON data format in the README and retained automated tests for validation, notes, workflows, and persistence.

## Team reflection

- AI suggestion changed or rejected based on evidence:
- Evidence used to make the decision:
- What the team learned:

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
- **Unrelated mini-experiment:** I created a temporary Git repository, committed a file, created a separate branch, and edited the file without committing the edit. I then switched back to the main branch.
- **Verification and evidence:** The temporary repository showed `M notes.txt` on the experiment branch. After switching back to `main`, the uncommitted file content was still present. This demonstrated that uncommitted changes can carry across branch switches.
- **Engineering decision:** I will use task-specific branches and pull requests for collaborative work, checking my branch and working-tree status before making changes.

### Cycle 2: Validation and JSON persistence

- **Learning gap:** I needed to understand how ticket validation, structured notes, and JSON storage work together, especially how invalid data should be handled.
- **Question asked:** How can I validate ticket records and structured notes while ensuring that loading and saving JSON data does not silently accept invalid records?
- **Key learning:** I learned that validation should cover required fields, unique identifiers, allowed values, priority consistency, legal statuses, and note structure. The entire collection should be validated before it is accepted or saved.
- **Unrelated mini-experiment:** I created a temporary `books.json` file containing a valid JSON list, loaded it with `json.loads`, then replaced its contents with malformed JSON and tried loading it again.
- **Verification and evidence:** Python successfully loaded the valid JSON list. Loading the malformed file raised `JSONDecodeError` with the message `Expecting property name enclosed in double quotes`. This experiment tested JSON syntax parsing, not CampusFlow's ticket-schema validation.
- **Engineering decision:** I documented the JSON data format in the README and retained automated tests for validation, notes, workflows, and persistence.

## Team reflection

- **AI suggestion changed or rejected based on evidence:** The initial explanation that switching branches changes the checked-out content was incomplete because it did not account for uncommitted changes.
- **Evidence used to make the decision:** In the temporary repository, `notes.txt` remained modified after switching from `experiment-branch` back to `main`.
- **What the team learned:** Check the working-tree status before switching branches. Git can carry uncommitted changes across a branch switch when they do not conflict; switching branches is not a substitute for committing, stashing, or otherwise protecting work.

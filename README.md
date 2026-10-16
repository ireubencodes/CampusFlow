# CampusFlow

CampusFlow is a Python command-line helpdesk ticket management system designed to help campus technical support teams manage, assign, track, and resolve support requests.

## Features

- **Ticket management:** Create and list support tickets.
- **Assignment:** Assign tickets to support personnel.
- **Status tracking:** Update ticket statuses and manage ticket workflows.
- **Ticket notes:** Add notes to tickets and preserve them across save and load operations.
- **Search and filtering:** Search tickets by title and filter using supported ticket fields.
- **Priority queue:** View open tickets in priority order.
- **Ticket details:** View information about individual tickets.
- **Reports:** View ticket counts, priority summaries, unresolved tickets, resolution percentage, and category breakdowns.
- **Validation:** Reject invalid ticket data and workflow operations.
- **Engineering Understanding Check:** Take a six-question multiple-choice quiz with answer validation, scoring, and explanations.

## Requirements

- Python 3
- Git (optional, for cloning and contributing)

No third-party packages are required for the current standard-library-based application and tests.

## Getting Started

Clone the repository and enter the project directory:

```bash
git clone https://github.com/ireubencodes/CampusFlow.git
cd CampusFlow
```

Run the application:

```bash
python main.py
```

Follow the interactive menu to select an available operation.

## Running Tests

Run the complete test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover ticket validation, notes, storage, workflows, search, reports, and the Engineering Understanding Check.

## Project Structure

```text
CampusFlow/
├── main.py
├── campusflow/
│   ├── quiz.py
│   ├── quiz_questions.py
│   ├── reports.py
│   ├── search.py
│   ├── storage.py
│   ├── tickets.py
│   └── workflow.py
├── docs/
│   ├── baseline-check.md
│   ├── design-decisions.md
│   └── ai-learning-log.md
└── tests/
    ├── test_notes.py
    ├── test_quiz.py
    ├── test_reports.py
    ├── test_search.py
    ├── test_storage.py
    ├── test_tickets.py
    └── test_workflow.py
```

- `main.py`: Command-line interface and menu.
- `campusflow/reports.py`: Ticket reporting and summary calculations.
- `campusflow/quiz.py`: Quiz interaction, answer validation, and scoring.
- `campusflow/quiz_questions.py`: Engineering quiz question bank.
- `campusflow/search.py`: Ticket search and filtering.
- `campusflow/storage.py`: Ticket data persistence and loading/saving.
- `campusflow/workflow.py`: Ticket assignment, status changes, queue handling, and note operations.
- `tests/`: Automated tests for the application's functionality.

## JSON Data Format

CampusFlow stores ticket records in `tickets.json` by default. The file
contains a JSON list, with each ticket represented as an object.

A ticket contains:
- `id`: unique ticket identifier, such as `T001`.
- `title`: non-empty ticket title.
- `category`: `Network`, `Hardware`, `Software`, or `Other`.
- `urgency`: `low`, `medium`, or `high`.
- `affected_users`: positive integer.
- `priority`: calculated priority (`low`, `medium`, `high`, or `critical`).
- `status`: `open`, `in_progress`, or `resolved`.
- `assigned_to`: assignee name or `null`.
- `notes`: list of structured note objects.

Each note contains `note_id`, `author`, and `message`. Note IDs use the
`N001` format. Note messages must contain 5–300 characters after trimming.

The storage layer validates ticket records, priority consistency, identifiers,
statuses, and note structures. Invalid or malformed data raises an error
rather than being silently accepted. Older records without a `notes` field
are supported and receive an empty notes list in the validated copy.

The default data file is runtime data and should not be committed unless the
assignment explicitly requires a sample data file.

## Contributing

1. Start from the latest `main` branch.
2. Create a separate branch for your task.
3. Make focused changes and run the test suite.
4. Commit and push your branch.
5. Open a pull request into `main` for review.

## License

No license has been specified yet.

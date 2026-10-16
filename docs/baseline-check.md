# CampusFlow Baseline and Final Verification

## 1. Original baseline

The original baseline was recorded before the new features were integrated.

- Test command: `python -m unittest discover -s tests -v`
- Original result: 46 tests passed.
- The original application supported ticket creation, priority calculation,
  assignment, status tracking, and JSON persistence.

## 2. Integrated project verification

After integrating the changes on `main`, the complete test suite was run.

- Branch: `main`
- Test command: `python -m unittest discover -s tests -v`
- Verified result: 82 tests passed, 0 failures, 0 errors.
- Verification covered ticket validation, workflow rules, notes, JSON storage,
  search, reports, and the Engineering Understanding Check.

## 3. Automated test coverage

Tests cover:

- Ticket title, category, urgency, and affected-user validation.
- Priority calculation and numeric ticket-ID ordering.
- Assignment and status-transition rules.
- Open-ticket queue filtering and ordering.
- Adding notes, rejecting invalid notes, and preserving note order.
- Saving and loading tickets and notes, including ID continuity.
- Rejecting malformed JSON and invalid ticket collections.
- Case-insensitive title search and combined filters.
- Reports for empty collections, ticket counts, and resolution percentages.
- Quiz question structure, answer validation, scoring, and explanations.

## 4. Runtime data

Runtime ticket data should not be committed as demonstration data unless
explicitly required. The application uses JSON persistence. Tests cover
save/load round trips, malformed data, and protection against invalid data.

## 5. Remaining submission checks

- Complete the AI-learning log using real evidence from both engineers.
- Perform a final CLI demonstration.
- Record the repository URL, final main commit SHA, and both pull-request URLs.
- Confirm the required peer-review evidence and honestly document any gaps.

## 6. Pull-request and review evidence

The following pull requests are confirmed merged:

- Ticket validation and notes: https://github.com/ireubencodes/CampusFlow/pull/6
- Search, reports, and CLI integration: https://github.com/ireubencodes/CampusFlow/pull/7
- README update: https://github.com/ireubencodes/CampusFlow/pull/8
- Engineering Understanding Check: https://github.com/ireubencodes/CampusFlow/pull/9

Process note: the Engineering Understanding Check PR was merged before the
planned peer-review comments were submitted. Do not treat this as evidence of
pre-merge peer review or approval. Any review performed afterward should be
recorded as post-merge review, with its actual date, findings, and follow-up.

# Test Cases

## Project: GRC Control Test Validator

These test cases verify whether the validator correctly evaluates production deployment approval evidence.

All test data is fictional.

| Test ID | Deployment ID | Scenario | Expected Result |
|---|---|---|---|
| TC-001 | DEP-001 | Approved by an authorised person before release | Pass |
| TC-002 | DEP-002 | Deployment does not have an approved status | Fail |
| TC-003 | DEP-003 | Approval given by an unauthorised person | Fail |
| TC-004 | DEP-004 | Approval recorded at or after release | Fail |
| TC-005 | DEP-005 | No matching approval record supplied | Inconclusive |
| TC-006 | DEP-006 | Release timestamp is missing | Inconclusive |

## Test Execution Results

The validator was executed against all six fictional deployment records.

| Test ID | Expected Result | Actual Result | Status |
|---|---|---|---|
| TC-001 | Pass | Pass | Matched |
| TC-002 | Fail | Fail | Matched |
| TC-003 | Fail | Fail | Matched |
| TC-004 | Fail | Fail | Matched |
| TC-005 | Inconclusive | Inconclusive | Matched |
| TC-006 | Inconclusive | Inconclusive | Matched |

## Overall Test Outcome

All six test cases produced the expected results.

- Pass: 1
- Fail: 3
- Inconclusive: 2

## Testing Limitation

The test cases validate the current prototype's defined rules using fictional CSV records. They do not establish that the validator is suitable for production use or that the underlying control is effective across an entire organisation.
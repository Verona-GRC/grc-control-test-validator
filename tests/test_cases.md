# Test Cases

## 1. Project Overview

**Project:** GRC Control Test Validator

**Control tested:** Production Deployment Approval Control

**Purpose:** To verify that the validator correctly evaluates production deployment approval evidence against predefined testing criteria.

All test data is fictional and created solely for this project.

## 2. Test Scenarios

| Test ID | Deployment ID | Test Scenario | Expected Result |
|---|---|---|---|
| TC-001 | DEP-001 | Approval is documented, the approver is authorised, and approval occurred before release. | Pass |
| TC-002 | DEP-002 | Deployment does not have an approved status. | Fail |
| TC-003 | DEP-003 | Approval was given by an unauthorised approver. | Fail |
| TC-004 | DEP-004 | Approval was recorded after the deployment release time. | Fail |
| TC-005 | DEP-005 | No matching approval record exists in the supplied register. | Inconclusive |
| TC-006 | DEP-006 | Deployment release timestamp is missing. | Inconclusive |

## 3. Test Execution Results

The validator was executed against all six fictional production deployment records.

| Test ID | Expected Result | Actual Result | Test Outcome |
|---|---|---|---|
| TC-001 | Pass | Pass | Matched |
| TC-002 | Fail | Fail | Matched |
| TC-003 | Fail | Fail | Matched |
| TC-004 | Fail | Fail | Matched |
| TC-005 | Inconclusive | Inconclusive | Matched |
| TC-006 | Inconclusive | Inconclusive | Matched |

## 4. Overall Test Outcome

All six test cases produced the expected results.

| Result | Count |
|---|---:|
| Pass | 1 |
| Fail | 3 |
| Inconclusive | 2 |
| **Total** | **6** |

**Test execution outcome:** All six test cases matched their expected results.

## 5. Testing Limitations

The test cases validate the current prototype's predefined rules using fictional CSV records.

They do not establish that the validator is suitable for production use, that all possible scenarios have been tested, or that the underlying control is effective across an entire organisation.

The results demonstrate that the current prototype produces the expected outcomes for the six defined test scenarios.

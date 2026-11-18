# Testing Methodology

## 1. Purpose

To document how the GRC Control Test Validator evaluates production deployments against the defined Production Deployment Approval Control requirements.

## 2. Input Data

The validator uses two fictional CSV files:

- `deployment_log.csv` – contains production deployment records, including deployment IDs, environments and release timestamps.
- `approval_register.csv` – contains approval records, including approval status, approver identity, authorisation status and approval timestamps.

## 3. Testing Process

For each production deployment, the validator performs the following steps:

1. Reads the deployment record and identifies its deployment ID and environment.
2. Checks whether the release timestamp is present and valid.
3. If the release timestamp is missing or invalid, assigns an Inconclusive result.
4. Searches the supplied approval register for a matching deployment ID.
5. If no matching approval record is found, assigns an Inconclusive result and recommends checking other possible approval sources.
6. Checks whether the approval status is recorded as Approved.
7. Checks whether the approver is identified as authorised.
8. Checks whether the approver's identity is recorded.
9. Checks whether the approval timestamp is present and valid.
10. Compares the approval timestamp with the deployment release timestamp to determine whether approval occurred before release.
11. Assigns a Pass, Fail or Inconclusive result based on the defined testing rules.
12. Records the result and explanation in `control_test_results.csv`.

## 4. Result Classification

- **Pass:** All required approval conditions are supported by the supplied evidence.
- **Fail:** The available evidence demonstrates that one or more required approval conditions were not met.
- **Inconclusive:** The available evidence is insufficient to determine whether the control operated effectively. Further investigation may be required.

## 5. Reporting

The validator generates a CSV report containing:

- Deployment ID
- Environment
- Test result
- Explanation of the result

The report provides a structured record of the test outcomes and supports further audit review.

## 6. Human Review

The generated results are intended to support audit and compliance reviews, not replace professional judgement.

Identified exceptions and inconclusive results require further investigation, validation of supporting evidence and assessment by an appropriate reviewer before final audit conclusions are reached.

## 7. Project Limitations

This prototype uses predefined, rule-based testing criteria and fictional sample data.

It evaluates only the evidence supplied through the two CSV files and does not independently retrieve or verify evidence from external systems.

The prototype does not currently use AI and is not a production-ready audit platform.

# Control Test Plan

## 1. Control Name

Production Deployment Approval Control

## 2. Control Objective

To ensure that all production deployments receive documented approval from an authorised person before release.

## 3. Risk Addressed

Unauthorised or unapproved changes may be deployed to the production environment, potentially affecting system security, availability, integrity and reliability.

## 4. Control Description

Production deployments must have documented approval from an authorised approver before release. Approval records should identify the approver, confirm their authority and record the approval date and time.

## 5. Testing Criteria

Each production deployment will be assessed against the following criteria:

1. A matching approval record is available in the supplied approval register.
2. The approval status is recorded as Approved.
3. The approver is identified as authorised.
4. The approver's identity is recorded.
5. The approval timestamp is present and valid.
6. Approval occurred before the deployment release time.
7. The deployment release timestamp is present and valid.

## 6. Evidence Sources

- Deployment log (`deployment_log.csv`)
- Approval register (`approval_register.csv`)

These are fictional sample records created solely for this project.

## 7. Testing Methodology

The validator:

1. Reads the supplied production deployment records.
2. Checks that the deployment release timestamp is valid.
3. Matches each deployment against the supplied approval register.
4. Checks the approval status and approver's authorisation.
5. Verifies that the approver's identity and approval timestamp are recorded.
6. Compares the approval timestamp with the deployment release timestamp.
7. Assigns a Pass, Fail or Inconclusive result based on the defined testing rules.
8. Generates a CSV report containing the results and explanations.

## 8. Test Result Classification

- **Pass:** All required approval conditions are supported by the available evidence.
- **Fail:** The available evidence demonstrates that one or more required approval conditions were not met.
- **Inconclusive:** The available evidence is insufficient to determine whether the control operated effectively. Further investigation may be required.

A missing record in the supplied approval register is treated as Inconclusive because approval may have been documented elsewhere.

## 9. Limitations

The test is limited to the two sample CSV files supplied. The validator does not independently retrieve or verify evidence from external systems.

A missing approval record does not automatically establish that approval was not obtained elsewhere. Further investigation may be required.

The results support control testing but do not replace human review or a final audit assessment.

## 10. Audit Follow-up

Exceptions and inconclusive results should be investigated. Supporting evidence should be obtained, findings documented, and appropriate corrective actions agreed with the responsible control owner.

Investigation outcomes, action owners and target completion dates should be recorded and tracked through to closure.

# Testing Methodology

## 1. Purpose
To describe how the GRC Control Test Validator evaluates production deployments against the Production Deployment Approval Control.

## 2. Input Data
The validator uses two fictional CSV files:

- deployment_log.csv – contains production deployment records.
- approval_register.csv – contains approval records.

## 3. Testing Process

For each production deployment, the validator:

1. Reads the deployment record.
2. Checks whether the release timestamp is available and valid.
3. Searches the approval register for a matching deployment ID.
4. Checks whether the approval status is Approved.
5. Checks whether the approver is authorised.
6. Checks whether the approver's identity and approval timestamp are recorded.
7. Compares the approval timestamp with the deployment release timestamp.
8. Assigns a Pass, Fail or Inconclusive result.
9. Records the result and explanation in control_test_results.csv.

## 4. Result Classification

- Pass: All required conditions are met based on the supplied evidence.
- Fail: The evidence identifies a control failure.
- Inconclusive: The available evidence is insufficient to reach a reliable conclusion.

## 5. Reporting
The validator generates a CSV report containing:

- Deployment ID
- Environment
- Test result
- Explanation of the result

## 6. Human Review
The generated results are intended to support audit and compliance reviews. Inconclusive results and identified exceptions require further investigation and human assessment.

## 7. Project Limitations
This prototype uses rule-based testing and fictional sample data. It does not independently verify evidence outside the supplied CSV files and is not a production-ready audit platform.
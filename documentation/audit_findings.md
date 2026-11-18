# Audit Findings

## 1. Test Overview

Control tested: Production Deployment Approval Control

Evidence reviewed:
- deployment_log.csv
- approval_register.csv

Total production deployments tested: 6

## 2. Test Results Summary

| Result | Number of Deployments |
|---|---:|
| Pass | 1 |
| Fail | 3 |
| Inconclusive | 2 |
| Total | 6 |

## 3. Detailed Observations

### DEP-001 – Pass
Documented approval by an authorised person occurred before release. The supplied evidence supports the control requirement.

### DEP-002 – Fail
The deployment does not have an approved status in the supplied approval register.

### DEP-003 – Fail
The recorded approver was not identified as an authorised approver.

### DEP-004 – Fail
Approval was recorded at or after the deployment release time. The evidence does not demonstrate prior approval.

### DEP-005 – Inconclusive
No matching approval record was found in the supplied register. Other approval sources should be checked before concluding that approval was not obtained.

### DEP-006 – Inconclusive
The deployment release timestamp is missing or invalid. The timing of the approval cannot be reliably assessed.

## 4. Recommended Follow-up

1. Investigate the three failed deployments and confirm the circumstances with the responsible control owner.
2. Obtain additional evidence for DEP-005 from other possible approval sources.
3. Confirm the correct release timestamp for DEP-006.
4. Document investigation outcomes and any corrective actions.
5. Consider whether the approval process and supporting records need improvement.

## 5. Overall Audit Assessment

Based on the supplied fictional evidence, only one of the six deployments met all tested approval requirements.

Three deployments showed evidence of control exceptions, while two require further investigation before a conclusion can be reached.

These results are preliminary and limited to the evidence supplied to the prototype validator. Human review is required before final audit conclusions are issued.
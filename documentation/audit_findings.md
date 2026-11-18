# Audit Findings

## 1. Test Overview

**Control tested:** Production Deployment Approval Control

**Control objective:** Ensure all production deployments receive documented approval from an authorised person before release.

**Evidence reviewed:**
- `deployment_log.csv`
- `approval_register.csv`

**Total production deployments tested:** 6

## 2. Test Results Summary

| Result | Number of Deployments |
|---|---:|
| Pass | 1 |
| Fail | 3 |
| Inconclusive | 2 |
| **Total** | **6** |

## 3. Detailed Findings

### DEP-001 – Pass

Documented approval by an authorised person occurred before release. The supplied evidence supports the tested control requirements.

### DEP-002 – Fail

The deployment does not have an approved status in the supplied approval register. Evidence of valid approval should be obtained and investigated.

### DEP-003 – Fail

The recorded approver was not identified as an authorised approver. The approver's authority should be verified against the approved authorisation records.

### DEP-004 – Fail

Approval was recorded after the deployment release time. The supplied evidence does not demonstrate that approval was obtained before release.

### DEP-005 – Inconclusive

No matching approval record was found in the supplied register. Other possible approval sources should be checked before concluding that approval was not obtained.

### DEP-006 – Inconclusive

The deployment release timestamp is missing or invalid. The timing of the approval cannot be reliably assessed until the correct release timestamp is established.

## 4. Recommended Follow-up

1. Investigate the three failed deployments with the responsible control owner and obtain supporting explanations and evidence.
2. Check alternative approval sources for DEP-005.
3. Confirm the correct release timestamp for DEP-006.
4. Record investigation outcomes, assigned action owners and target completion dates.
5. Track corrective actions through to completion and assess whether the control design or operating process requires improvement.

## 5. Overall Audit Assessment

Based on the supplied fictional evidence, only one of the six deployments met all tested approval requirements.

Three deployments did not meet one or more defined test criteria, while two require further investigation before a conclusion can be reached.

These results are preliminary and limited to the evidence supplied to the prototype validator. They do not, by themselves, establish the extent or cause of any wider control failure.

Human review is required to validate the evidence, investigate exceptions and determine final audit conclusions.

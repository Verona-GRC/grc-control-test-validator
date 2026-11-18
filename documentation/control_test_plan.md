\# Control Test Plan



\## 1. Control Name

Production Deployment Approval Control



\## 2. Control Objective

To ensure that all production deployments are approved by an authorised person before the deployment takes place.



\## 3. Risk Addressed

Unauthorised or unapproved changes may be deployed to the production environment, potentially affecting system security, availability, integrity and reliability.



\## 4. Control Description

Production deployments must have documented approval from an authorised approver before release.



\## 5. Testing Criteria



Each production deployment will be checked against the following criteria:



1\. A matching approval record exists.

2\. The approval status is Approved.

3\. The approver is authorised.

4\. The approver's identity is recorded.

5\. The approval timestamp is recorded and valid.

6\. Approval occurred before the deployment release time.

7\. The deployment release timestamp is recorded and valid.



\## 6. Evidence Sources

\- Deployment log (deployment\_log.csv)

\- Approval register (approval\_register.csv)



These are fictional sample records created for this project.



\## 7. Testing Methodology

The validator matches each production deployment against the approval register and evaluates the available evidence against the testing criteria.



\## 8. Test Results



\- Pass: All required approval conditions are supported by the available evidence.

\- Fail: Evidence shows that one or more required approval conditions were not met.

\- Inconclusive: Available evidence is insufficient to determine whether the control operated effectively.



\## 9. Limitations

The test is limited to the two sample CSV files supplied. A missing approval record does not automatically establish that approval was not obtained elsewhere. Further investigation may be required.



\## 10. Audit Follow-up

Exceptions and inconclusive results should be investigated. Supporting evidence should be obtained, findings documented, and appropriate corrective actions agreed with the responsible control owner.


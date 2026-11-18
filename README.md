# GRC Control Test Validator

A Python-based prototype demonstrating evidence-based control testing, automated validation and structured audit reporting.

## Project Overview

The GRC Control Test Validator demonstrates how governance, risk and compliance (GRC) requirements can be translated into repeatable testing rules.

The prototype evaluates fictional production deployment records against defined approval control requirements, assesses supporting evidence and generates structured test results.

It demonstrates the practical application of audit methodology and control assurance principles through a technology-enabled testing approach.

## Business Objective

To improve the consistency, efficiency and transparency of control testing by applying defined validation rules to structured evidence.

## Control Being Tested

**Production Deployment Approval Control**

**Control objective:** Ensure that all production deployments receive documented approval from an authorised person before release.

**Risk addressed:** Unauthorised or unapproved changes may affect system security, availability, integrity and reliability.

## How It Works

The validator:

1. Reads production deployment records.
2. Matches each deployment against the supplied approval register.
3. Checks approval status and approver authorisation.
4. Verifies approver identity and approval timestamps.
5. Compares approval timestamps against deployment release times.
6. Assigns a Pass, Fail or Inconclusive result.
7. Generates a CSV report containing the test results and explanations.

## Sample Test Results

The prototype was tested against six fictional production deployment records.

| Result | Count |
|---|---:|
| Pass | 1 |
| Fail | 3 |
| Inconclusive | 2 |
| **Total** | **6** |

All six test cases produced their expected results.

The results demonstrate the prototype's ability to distinguish between supported control compliance, identified exceptions and insufficient evidence requiring further investigation.

## Project Structure

```text
grc-control-test-validator/
│
├── control_test_validator.py
├── README.md
├── ROADMAP.md
├── .gitignore
│
├── documentation/
│   ├── audit_findings.md
│   ├── control_test_plan.md
│   └── testing_methodology.md
│
├── sample_data/
│   ├── approval_register.csv
│   └── deployment_log.csv
│
├── sample_reports/
│   └── control_test_results.csv
│
└── tests/
    └── test_cases.md
```

## How to Run the Prototype

**Prerequisites:**
- Python 3.10 or later.
- No external Python packages are required.

**Execution:**

1. Download or clone this repository.
2. Open a command prompt in the project folder.
3. Run:

```bash
python control_test_validator.py
```

The validator reads the fictional CSV files from `sample_data/` and generates the test results in `sample_reports/control_test_results.csv`.

## Testing and Documentation

The project includes supporting documentation covering:

- Control objectives and testing criteria.
- Testing methodology and result classifications.
- Defined test scenarios and execution results.
- Audit findings and recommended follow-up actions.

Refer to the `documentation/` and `tests/` folders for details.

## Human Oversight

The validator supports control testing but does not replace professional judgement.

Identified exceptions and inconclusive results require further investigation, evidence validation and human assessment before final audit conclusions are reached.

## Current Limitations

- Uses fictional CSV data.
- Tests only one defined production deployment approval control.
- Evaluates only the evidence supplied to the application.
- Does not independently retrieve or verify evidence from external systems.
- Uses predefined, rule-based testing criteria.
- Does not currently use AI.
- Is a learning and portfolio prototype, not a production-ready audit platform.

## Future Development

Planned enhancements include:

- Additional control tests and configurable testing rules.
- Evidence completeness and exception tracking.
- Improved audit reporting and exception management.
- AI-assisted evidence interpretation and recommendations, subject to human review.
- Integration with source systems to improve evidence traceability.

See [ROADMAP.md](ROADMAP.md) for planned development stages.

## Project Design and GRC Contribution

This project demonstrates the application of audit and GRC knowledge to technology-enabled control assurance.

The project design translates a control objective into defined testing criteria, evidence requirements, result classifications and audit follow-up procedures.

It also demonstrates the importance of evidence quality, appropriate treatment of exceptions and human oversight in automated control testing.

The Python implementation was developed as a practical learning prototype with AI-assisted guidance.

---

**Project status:** Working prototype  
**Data classification:** Fictional demonstration data  
**Technology:** Python, CSV

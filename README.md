# GRC Control Test Validator

## Project Overview

The GRC Control Test Validator is a prototype designed to demonstrate how control testing can be supported through automated, evidence-based validation.

The project evaluates fictional production deployment records against defined approval control requirements and generates structured test results to support audit and compliance reviews.

## Business Objective

To demonstrate how governance, risk and compliance requirements can be translated into repeatable testing rules, helping improve consistency, efficiency and transparency in control testing.

## Control Being Tested

**Production Deployment Approval Control**

The control requires production deployments to have documented approval from an authorised person before release.

## How It Works

The validator:

1. Reads production deployment records.
2. Matches each deployment against the approval register.
3. Checks approval status and approver authorisation.
4. Validates approval and release timestamps.
5. Assigns a Pass, Fail or Inconclusive result.
6. Generates a CSV report with the results and explanations.

## Sample Test Results

| Result | Count |
|---|---:|
| Pass | 1 |
| Fail | 3 |
| Inconclusive | 2 |
| **Total** | **6** |

All records are fictional and created solely for demonstration purposes.

## Project Structure

- `control_test_validator.py` – Python script containing the testing rules.
- `sample_data/` – Fictional deployment and approval records.
- `documentation/` – Control test plan, testing methodology and audit findings.
- `sample_reports/` – Generated control test results.

## Testing Approach

The prototype uses predefined, rule-based testing criteria. It distinguishes between confirmed exceptions and cases where the available evidence is insufficient to reach a conclusion.

Human review remains necessary to validate evidence, investigate exceptions and determine final audit conclusions.

## Current Limitations

- Uses fictional CSV data.
- Tests only the defined production deployment approval control.
- Evaluates only the evidence supplied to the application.
- Does not independently retrieve or verify evidence from external systems.
- Does not currently use AI.

## Future Development

Planned enhancements include:

- Additional control tests and configurable testing rules.
- Evidence completeness and exception tracking.
- More structured audit reporting.
- AI-assisted evidence interpretation and recommendations, subject to human review.
- Integration with source systems to support evidence-based control testing.

## Project Purpose

This project demonstrates the practical application of audit and GRC knowledge in designing technology-enabled control testing solutions.

It is a learning and portfolio prototype, not a production-ready audit platform.
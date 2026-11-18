import csv
from datetime import datetime
from pathlib import Path

# Project files
folder = Path(__file__).parent / "sample_data"
deployment_file = folder / "deployment_log.csv"
approval_file = folder / "approval_register.csv"
output_file = Path(__file__).parent / "sample_reports" / "control_test_results.csv"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def read_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def parse_date(value):
    try:
        return datetime.strptime(value.strip(), DATE_FORMAT)
    except (ValueError, AttributeError):
        return None


def test_deployment(deployment, approvals):
    deployment_id = deployment.get("deployment_id", "").strip()
    release_time = parse_date(deployment.get("release_time", ""))

    # Check whether the release timestamp is available
    if release_time is None:
        return "Inconclusive", "Release timestamp is missing or invalid."

    approval = approvals.get(deployment_id)

    # No matching record in the supplied approval register
    if approval is None:
        return "Inconclusive", (
            "No matching approval record found in the supplied register. "
            "Check other possible approval sources."
        )

    # Check approval status
    if approval.get("approval_status", "").strip().lower() != "approved":
        return "Fail", "Deployment does not have an approved status."

    # Check whether the approver was authorised
    if approval.get("authorised_approver", "").strip().lower() != "yes":
        return "Fail", "Approval was not given by an authorised approver."

    # Check whether the approver's identity is recorded
    if not approval.get("approver", "").strip():
        return "Inconclusive", "Approver's identity is missing."

    # Check approval timestamp
    approval_time = parse_date(approval.get("approval_time", ""))

    if approval_time is None:
        return "Inconclusive", "Approval timestamp is missing or invalid."

    # Approval must occur before the release
    if approval_time >= release_time:
        return "Fail", "Approval was recorded at or after the release time."

    return "Pass", "Documented approval by an authorised person occurred before release."


def main():
    deployments = read_csv(deployment_file)
    approval_records = read_csv(approval_file)

    approvals = {
        row["deployment_id"].strip(): row
        for row in approval_records
        if row.get("deployment_id", "").strip()
    }

    results = []

    for deployment in deployments:
        if deployment.get("environment", "").strip().lower() != "production":
            continue

        result, explanation = test_deployment(deployment, approvals)

        results.append({
            "deployment_id": deployment.get("deployment_id", ""),
            "environment": deployment.get("environment", ""),
            "result": result,
            "explanation": explanation
        })

    # Save results to a new CSV report
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "deployment_id",
            "environment",
            "result",
            "explanation"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Display results
    print("\nGRC CONTROL TEST VALIDATOR")
    print("-" * 45)

    for row in results:
        print(
            f'{row["deployment_id"]}: {row["result"]} - '
            f'{row["explanation"]}'
        )

    print("\nSUMMARY")
    print("-" * 45)

    for status in ["Pass", "Fail", "Inconclusive"]:
        count = sum(1 for row in results if row["result"] == status)
        print(f"{status}: {count}")

    print(f"\nTotal deployments tested: {len(results)}")
    print(f"Report saved to: {output_file}")


if __name__ == "__main__":
    main()

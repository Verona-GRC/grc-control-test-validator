import sys
import unittest
from pathlib import Path

# Locate the main project folder
project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

# Import the function being tested
from control_test_validator import test_deployment


class TestDeploymentValidator(unittest.TestCase):

    def setUp(self):
        self.deployment = {
            "deployment_id": "DEP-001",
            "release_time": "2026-10-01 09:00:00"
        }

        self.approval = {
            "deployment_id": "DEP-001",
            "approval_status": "Approved",
            "approver": "Alex Tan",
            "authorised_approver": "Yes",
            "approval_time": "2026-10-01 08:30:00"
        }

    def test_valid_approval_returns_pass(self):
        result, explanation = test_deployment(
            self.deployment, {"DEP-001": self.approval}
        )
        self.assertEqual(result, "Pass")

    def test_unapproved_deployment_returns_fail(self):
        self.approval["approval_status"] = "Not Approved"
        result, explanation = test_deployment(
            self.deployment, {"DEP-001": self.approval}
        )
        self.assertEqual(result, "Fail")

    def test_unauthorised_approver_returns_fail(self):
        self.approval["authorised_approver"] = "No"
        result, explanation = test_deployment(
            self.deployment, {"DEP-001": self.approval}
        )
        self.assertEqual(result, "Fail")

    def test_late_approval_returns_fail(self):
        self.approval["approval_time"] = "2026-10-01 09:30:00"
        result, explanation = test_deployment(
            self.deployment, {"DEP-001": self.approval}
        )
        self.assertEqual(result, "Fail")

    def test_missing_approval_returns_inconclusive(self):
        result, explanation = test_deployment(
            self.deployment, {}
        )
        self.assertEqual(result, "Inconclusive")

    def test_missing_release_timestamp_returns_inconclusive(self):
        self.deployment["release_time"] = ""
        result, explanation = test_deployment(
            self.deployment, {"DEP-001": self.approval}
        )
        self.assertEqual(result, "Inconclusive")


if __name__ == "__main__":
    unittest.main()

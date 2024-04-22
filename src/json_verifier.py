import json
import re
import sys

class InvalidPolicyError(Exception):
    """Exception raised for invalid policy data."""

class JSONVerifier:
    """A class for verifying the correctness of JSON data representing an AWS IAM Policy."""

    def __init__(self, file_path):
        """Initialize the JSONVerifier object with the file path to the JSON data."""
        self.file_path = file_path

    def load_json(self):
        """Load the JSON data from the file specified by file_path."""
        with open(self.file_path, 'r') as f:
            self.data = json.load(f)

    def verify(self):
        """
        Verify the correctness of the JSON data.

        Raises:
            InvalidPolicyError: If the JSON data is incorrect.

        Returns:
            bool: True if the JSON data is correct.
        """
        if not self.data:
            raise InvalidPolicyError("No data found in JSON.")

        self._validate_policy_name()

        policy_document = self.data.get('PolicyDocument')
        if not policy_document:
            raise InvalidPolicyError("Missing PolicyDocument in JSON.")

        self._validate_policy_document(policy_document)

        return True

    def _validate_policy_name(self):
        """
        Validate the PolicyName field in the JSON data.

        Raises:
            InvalidPolicyError: If PolicyName is invalid.
        """
        policy_name = self.data.get('PolicyName')
        if not isinstance(policy_name, str) or not policy_name:
            raise InvalidPolicyError("Invalid or missing PolicyName.")
        if not re.match(r"[\w+=,.@-]+", policy_name):
            raise InvalidPolicyError("PolicyName contains invalid characters.")
        if len(policy_name) < 1 or len(policy_name) > 128:
            raise InvalidPolicyError("PolicyName length out of range.")

    def _validate_policy_document(self, policy_document):
        """
        Validate the PolicyDocument field in the JSON data.

        Args:
            policy_document (dict): The PolicyDocument dictionary.

        Raises:
            InvalidPolicyError: If PolicyDocument is invalid.
        """
        if 'Version' not in policy_document or policy_document['Version'] != '2012-10-17':
            raise InvalidPolicyError("Invalid or missing Version in PolicyDocument.")

        statements = policy_document.get('Statement')
        if not isinstance(statements, list):
            raise InvalidPolicyError("Invalid or missing Statement in PolicyDocument.")

        for statement in statements:
            self._validate_statement(statement)

    def _validate_statement(self, statement):
        """
        Validate each statement in the PolicyDocument.

        Args:
            statement (dict): A statement in the PolicyDocument.

        Raises:
            InvalidPolicyError: If the statement is invalid.
        """
        if not all(key in statement for key in ['Sid', 'Effect', 'Action']):
            raise InvalidPolicyError("Invalid or missing keys in statement.")

        if not isinstance(statement['Sid'], str) or not statement['Sid']:
            raise InvalidPolicyError("Invalid or missing Sid in statement.")

        if statement['Effect'] not in ['Allow', 'Deny']:
            raise InvalidPolicyError("Invalid Effect in statement.")

        if not isinstance(statement['Action'], list) or not all(isinstance(action, str) for action in statement['Action']):
            raise InvalidPolicyError("Invalid or missing Action in statement.")

        if 'Resource' in statement and (not isinstance(statement['Resource'], str) or statement['Resource'] == '*'):
            raise InvalidPolicyError("Invalid Resource in statement.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_verifier.py <json_file_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]

    verifier = JSONVerifier(json_file_path)
    verifier.load_json()

    if verifier.verify():
        print("JSON data is correct.")
    else:
        print("JSON data is incorrect.")

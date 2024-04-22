import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.json_verifier import JSONVerifier


def get_json_file_path(file_name):
    """
    Get the absolute path to the JSON file.

    Args:
    file_name (str): The name of the JSON file.

    Returns:
    str: The absolute path to the JSON file.
    """
    current_dir = os.path.dirname(__file__)
    json_files_dir = os.path.join(current_dir, 'json_test_files')
    return os.path.abspath(os.path.join(json_files_dir, file_name))

class TestJSONVerifier(unittest.TestCase):
    def test_empty_policy_name(self):
        verifier = JSONVerifier(get_json_file_path('test_empty_policy_name.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_invalid_json_policy_document(self):
        verifier = JSONVerifier(get_json_file_path('test_invalid_json_policy_document.json'))
        verifier.load_json()
        with self.assertRaises(ValueError):
            verifier.verify()

    def test_missing_policy_document(self):
        verifier = JSONVerifier(get_json_file_path('test_missing_policy_document.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_missing_policy_name(self):
        verifier = JSONVerifier(get_json_file_path('test_missing_policy_name.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_policy_name_exceeding_maximum_length(self):
        verifier = JSONVerifier(get_json_file_path('test_policy_name_exceeding_maximum_length.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_policy_name_with_invalid_characters(self):
        verifier = JSONVerifier(get_json_file_path('test_policy_name_with_invalid_characters.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_policy_name_with_invalid_pattern(self):
        verifier = JSONVerifier(get_json_file_path('test_policy_name_with_invalid_pattern.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_policy_name_with_invalid_type(self):
        verifier = JSONVerifier(get_json_file_path('test_policy_name_with_invalid_type.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_policy_name_with_maximum_length(self):
        verifier = JSONVerifier(get_json_file_path('test_policy_name_with_maximum_length.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertFalse(result)

    def test_valid_json_with_double_asterisk(self):
        verifier = JSONVerifier(get_json_file_path('test_valid_json_with_double_asterisk.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertTrue(result)

    def test_valid_json_with_single_asterisk(self):
        verifier = JSONVerifier(get_json_file_path('test_valid_json_with_single_asterisk.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertTrue(result)

    def test_valid_json_with_specific_permissions(self):
        verifier = JSONVerifier(get_json_file_path('test_valid_json_with_specific_permissions.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertTrue(result)

    def test_valid_json_without_single_asterisk(self):
        verifier = JSONVerifier(get_json_file_path('test_valid_json_without_single_asterisk.json'))
        verifier.load_json()
        result = verifier.verify()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


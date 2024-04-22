# Instruction how to run 

This project consists of two Python files:
1. `json_verifier.py`: Contains a class `JSONVerifier` for verifying the correctness of JSON data representing an AWS IAM Policy.
2. `test_json_verifier.py`: Contains unit tests for the `JSONVerifier` class.

You can start by downloading the repository by running:

```bash
git clone https://github.com/szpajak/remitly
```

To run `json_verifier.py`, you should be in the `remitly` directory and run the following command in the terminal:

```bash
python src/json_verifier.py <test_file>.json
```
for example:
```bash
python src/json_verifier.py test/json_test_files/test_missing_policy_name.json
```


To run `test_json_verifier.py`, you should be in the `remitly` directory and run the following command in your terminal:

```bash
python -m unittest test/test_missing_policy_name.py
```

The `remitly/test/json_test_files` directory contains JSON files used for tests.
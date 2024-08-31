from unittest import TestCase
from src.day2.evaluate_password_against_policy import parse_policy, evaluate, get_count_of_valid_passwords, \
    calculate_from_file
from src.settings import PROJECT_ROOT


class TestEvaluatePassword(TestCase):
    def test_parse_policy(self):
        self.assertEqual((1,3,"a"), parse_policy("1-3 a"))
        self.assertEqual((1,3,"b"), parse_policy("1-3 b"))
        self.assertEqual((2,9,"c"), parse_policy("2-9 c"))

    def test_evaluate(self):
        self.assertTrue(evaluate("1-3 a: abcde"))
        self.assertFalse(evaluate("1-3 b: cdefg"))
        self.assertTrue(evaluate("2-9 c: ccccccccc"))

    def test_get_count_of_valid_passwords(self):
        self.assertEqual(2, get_count_of_valid_passwords([
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc",
        ]))

    def test_get_count_of_valid_passwords_from_sample_file(self):
        sample_data_test_file = PROJECT_ROOT + "/day2/sample-data.txt"
        actual_result = calculate_from_file(sample_data_test_file)
        self.assertEqual(actual_result, 2)

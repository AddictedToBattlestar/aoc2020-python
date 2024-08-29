from unittest import TestCase
from src.day2.evaluate_password_against_policy import parse_policy, evaluate, get_count_of_valid_passwords

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
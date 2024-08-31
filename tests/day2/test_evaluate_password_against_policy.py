from unittest import TestCase
from src.day2.evaluate_password_against_policy import parse_policy, evaluate, get_count_of_valid_passwords, \
    calculate_from_file, evaluate_sled_rental, PolicyTypeEnum, evaluate_toboggan
from src.settings import PROJECT_ROOT

class TestEvaluatePassword(TestCase):
    def test_parse_policy(self):
        self.assertEqual((1,3,"a"), parse_policy("1-3 a"))
        self.assertEqual((1,3,"b"), parse_policy("1-3 b"))
        self.assertEqual((2,9,"c"), parse_policy("2-9 c"))

    def test_sled_rental_evaluate(self):
        self.assertTrue(evaluate_sled_rental("1-3 a: abcde"))
        self.assertFalse(evaluate_sled_rental("1-3 b: cdefg"))
        self.assertTrue(evaluate_sled_rental("2-9 c: ccccccccc"))

    def test_sled_rental_get_count_of_valid_passwords(self):
        self.assertEqual(2, get_count_of_valid_passwords(
            lines=[
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc"
            ],
            policy_type=PolicyTypeEnum.SLED_RENTAL
        ))

    def test_sled_rental_get_count_of_valid_passwords_from_sample_file(self):
        sample_data_test_file = PROJECT_ROOT + "/day2/sample-data.txt"
        actual_result = calculate_from_file(sample_data_test_file, PolicyTypeEnum.SLED_RENTAL)
        self.assertEqual(actual_result, 2)

    def test_toboggan_evaluate(self):
        self.assertTrue(evaluate_toboggan("1-3 a: abcde"))
        self.assertFalse(evaluate_toboggan("1-3 b: cdefg"))
        self.assertFalse(evaluate_toboggan("2-9 c: ccccccccc"))

    def test_toboggan_get_count_of_valid_passwords(self):
        self.assertEqual(1, get_count_of_valid_passwords(
            lines=[
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc"
            ],
            policy_type=PolicyTypeEnum.TOBOGGAN
        ))

    def test_toboggan_get_count_of_valid_passwords_from_sample_file(self):
        sample_data_test_file = PROJECT_ROOT + "/day2/sample-data.txt"
        actual_result = calculate_from_file(sample_data_test_file, PolicyTypeEnum.TOBOGGAN)
        self.assertEqual(actual_result, 1)

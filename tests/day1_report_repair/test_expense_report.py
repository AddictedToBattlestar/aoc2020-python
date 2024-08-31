from unittest import TestCase
from src.day1_report_repair.expense_report import find_product_of_two_entries_matching_desired_value_not_found, \
    calculate_from_file, find_two_entries_matching_desired_value, find_three_entries_matching_desired_value, \
    find_product_of_three_entries_matching_desired_value_not_found
from src.settings import PROJECT_ROOT


class TestFindProductOfTwoEntries(TestCase):
    def test_find_two_entries_matching_desired_value(self):
        actual_result = find_two_entries_matching_desired_value(
            entries=[
            1721,
            979,
            366,
            299,
            675,
            1456
        ],
            desired_value=2020
        )
        self.assertEqual((1721, 299), actual_result)

    def test_find_product_of_two_entries_matching_desired_value_not_found(self):
        actual_result = find_product_of_two_entries_matching_desired_value_not_found(
            entries=[
            1721,
            979,
            366,
            299,
            675,
            1456
            ],
            desired_value=2020
        )
        self.assertEqual(514579, actual_result)

    def test_calculate_from_sample_file_two_entries(self):
        sample_data_test_file = PROJECT_ROOT + "/day1_report_repair/sample-data.txt"
        actual_result = calculate_from_file(file_name=sample_data_test_file, number_of_entries=2, desired_value=2020)
        self.assertEqual(actual_result, 514579)

    def test_find_three_entries_matching_desired_value(self):
        actual_result = find_three_entries_matching_desired_value(
            entries=[
            1721,
            979,
            366,
            299,
            675,
            1456
        ],
            desired_value=2020
        )
        self.assertEqual((979, 366, 675), actual_result)

    def test_find_product_of_three_entries_matching_desired_value_not_found(self):
        actual_result = find_product_of_three_entries_matching_desired_value_not_found(
            entries=[
            1721,
            979,
            366,
            299,
            675,
            1456
            ],
            desired_value=2020
        )
        self.assertEqual(241861950, actual_result)

    def test_calculate_from_sample_file_three_entries(self):
        sample_data_test_file = PROJECT_ROOT + "/day1_report_repair/sample-data.txt"
        actual_result = calculate_from_file(file_name=sample_data_test_file, number_of_entries=3, desired_value=2020)
        self.assertEqual(actual_result, 241861950)
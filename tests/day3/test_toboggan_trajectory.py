from src.day3.toboggan_trajectory import calculate, calculate_from_file
from src.settings import PROJECT_ROOT


def test_small_map_with_no_tree():
    test_map_with_no_tree = [
        "..",
        ".."
    ]
    assert calculate(test_map_with_no_tree,1,1) == 0

def test_small_map_with_one_tree():
    test_map_with_tree = [
        "..",
        ".#"
    ]
    assert calculate(test_map_with_tree,1,1) == 1

def test_small_map_with_one_tree_downward():
    test_map = [
        "..",
        "#."
    ]
    assert calculate(test_map,0,1) == 1

# def test_small_map_with_one_tree_across():
#     test_map = [
#         ".#",
#         ".."
#     ]
#     assert calculate(test_map,1,0) == 0


def test_medium_map_with_one_tree():
    test_map = [
        "...",
        "...",
        "..#"
    ]
    assert calculate(test_map,2,2) == 1

def test_medium_map_with_two_trees():
    test_map = [
        "...",
        ".#.",
        "..#"
    ]
    assert calculate(test_map,1,1) == 2

def test_large_map_with_four_trees():
    test_map = [
        "......",
        ".#....",
        "..#...",
        "......",
        "....#.",
        ".....#",
    ]
    assert calculate(test_map,2,2) == 2

def test_rolling_map():
    test_map = [
        "...",
        ".#.",
        "..#",
        "#..",
    ]
    assert calculate(test_map, 1, 1) == 3

def test_sample_file():
    sample_data_test_file = PROJECT_ROOT + "/day3/sample-data.txt"
    assert calculate_from_file(sample_data_test_file,3,1) == 7
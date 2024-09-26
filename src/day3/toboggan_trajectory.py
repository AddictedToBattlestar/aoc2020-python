from src.utilities.file_reader import read_lines_from_file

def calculate_from_file(file_name, change_in_x, change_in_y):
    raw_map = read_lines_from_file(file_name)
    return calculate(raw_map, change_in_x, change_in_y)

def calculate(raw_map, change_in_x, change_in_y):
    tree_map = build_tree_map(raw_map)
    current_x, current_y = change_in_x, change_in_y
    count_of_trees = 0
    while current_y < len(raw_map):
        if is_tree_present(tree_map, current_x, current_y):
            count_of_trees += 1
        current_x += change_in_x
        current_y += change_in_y
    return count_of_trees

def build_tree_map(raw_map):
    tree_map = []
    for map_line in raw_map:
        tree_map_line = [m for m in map_line]
        tree_map.append(tree_map_line)
    return tree_map

def find_location(tree_map, x, y):
    map_width = len(tree_map[0])
    result = tree_map[y][x % map_width]
    return result

def is_tree_present(tree_map, x, y):
    return find_location(tree_map, x, y) == '#'

if __name__ == '__main__':
    part_1_result = calculate_from_file("data.txt", 3, 1)
    print(f'The solution for Day 3, part 1 is: {part_1_result}')

from src.utilities.file_reader import read_lines_from_file

def find_three_entries_matching_desired_value(entries, desired_value):
    for entry_idx, entry in enumerate(entries):
        remainder = desired_value - entry
        matching_two_entries = find_two_entries_matching_desired_value(entries, remainder)
        if matching_two_entries:
            return entry, matching_two_entries[0], matching_two_entries[1]
    return None

def find_product_of_three_entries_matching_desired_value_not_found(entries, desired_value):
    entries = find_three_entries_matching_desired_value(entries, desired_value)
    if entries:
        return entries[0] * entries[1] * entries[2]
    else:
        return None

def find_two_entries_matching_desired_value(entries, desired_value):
    for entry_idx, entry in enumerate(entries):
        for other_idx, other in enumerate(entries):
            if entry_idx != other_idx and entry + other == desired_value:
                return entry, other
    return None

def find_product_of_two_entries_matching_desired_value_not_found(entries, desired_value):
    entries = find_two_entries_matching_desired_value(entries, desired_value)
    if entries:
        return entries[0] * entries[1]
    else:
        return None

def calculate_from_file(file_name, number_of_entries, desired_value):
    lines = read_lines_from_file(file_name)
    numeric_lines = [int(numeric_string) for numeric_string in lines]
    if number_of_entries == 2:
        return find_product_of_two_entries_matching_desired_value_not_found(numeric_lines, desired_value)
    if number_of_entries == 3:
        return find_product_of_three_entries_matching_desired_value_not_found(numeric_lines, desired_value)

if __name__ == '__main__':
    part_1_result = calculate_from_file(file_name="day1_data.txt", number_of_entries=2, desired_value=2020)
    print(f'The solution for Day 1, part 1 is: {part_1_result}')
    part_2_result = calculate_from_file(file_name="day1_data.txt", number_of_entries=3, desired_value=2020)
    print(f'The solution for Day 1, part 2 is: {part_2_result}')
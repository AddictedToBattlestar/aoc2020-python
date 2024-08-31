from src.utilities.file_reader import read_lines_from_file


def parse_policy(policy):
    policy_range, character = policy.split(" ")
    min_count, max_count = map(int, policy_range.split("-"))
    return min_count, max_count, character

def evaluate(policy_and_password_line):
    policy, password_line = [x.strip() for x in policy_and_password_line.split(":")]
    min_count, max_count, character = parse_policy(policy)
    character_count = password_line.count(character)
    return min_count <= character_count <= max_count

def get_count_of_valid_passwords(lines):
    valid_count = 0
    for line in lines:
        if evaluate(line):
            valid_count += 1
    return valid_count

def calculate_from_file(file_name):
    lines = read_lines_from_file(file_name)
    return get_count_of_valid_passwords(lines)

if __name__ == '__main__':
    part_1_result = calculate_from_file("data.txt")
    print(f'The solution for Day 1, part 1 is: {part_1_result}')
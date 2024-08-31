from src.utilities.file_reader import read_lines_from_file
from enum import Enum, auto

class PolicyTypeEnum(Enum):
    TOBOGGAN = auto()
    SLED_RENTAL = auto()

def parse_policy(policy):
    policy_range, character = policy.split(" ")
    min_count, max_count = map(int, policy_range.split("-"))
    return min_count, max_count, character

def evaluate_sled_rental(policy_and_password_line):
    policy, password_line = [x.strip() for x in policy_and_password_line.split(":")]
    min_count, max_count, character = parse_policy(policy)
    character_count = password_line.count(character)
    return min_count <= character_count <= max_count

def evaluate_toboggan(policy_and_password_line):
    policy, password_line = [x.strip() for x in policy_and_password_line.split(":")]
    first_position, second_position, character_to_match = parse_policy(policy)
    first_position_matches = password_line[first_position - 1] == character_to_match
    second_position_matches = password_line[second_position - 1] == character_to_match
    if first_position_matches and second_position_matches:
        return False
    else:
        return first_position_matches or second_position_matches

def evaluate(policy_and_password_line, policy_type):
    if policy_type == PolicyTypeEnum.TOBOGGAN:
        return evaluate_toboggan(policy_and_password_line)
    elif policy_type == PolicyTypeEnum.SLED_RENTAL:
        return evaluate_sled_rental(policy_and_password_line)

def get_count_of_valid_passwords(lines, policy_type):
    valid_count = 0
    for line in lines:
        if evaluate(line, policy_type):
            valid_count += 1
    return valid_count

def calculate_from_file(file_name, policy_type):
    lines = read_lines_from_file(file_name)
    return get_count_of_valid_passwords(lines, policy_type)

if __name__ == '__main__':
    part_1_result = calculate_from_file("data.txt", PolicyTypeEnum.SLED_RENTAL)
    print(f'The solution for Day 1, part 1 is: {part_1_result}')
    part_2_result = calculate_from_file("data.txt", PolicyTypeEnum.TOBOGGAN)
    print(f'The solution for Day 1, part 2 is: {part_2_result}')

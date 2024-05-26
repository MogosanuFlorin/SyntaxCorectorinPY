import random
from levensthein_alg import calculate_levenshtein_distance
from string_generator import generate_random_strings


def main():
    choice = int(input(
        "Enter 1 to input two strings\nEnter 2 to run the program 5 times with 2 random generated strings.\nInput: "))

    if choice == 1:
        with open('input.txt', 'r') as file:
            lines = file.readlines()

        # Stripping newline characters and whitespaces from each line
        lines = [line.strip() for line in lines]

        for i in range(0, len(lines), 2):
            # Ensure there are pairs of lines to process
            if i + 1 < len(lines):
                source_string = lines[i]
                target_string = lines[i + 1]

                # Calculate the Levenshtein distance
                distance = calculate_levenshtein_distance(source_string, target_string)

                # Output the result
                print(
                    f"The minimum number of operations to transform '{source_string}' into '{target_string}' is {distance}")
    elif choice == 2:
        for i in range(5):
            # Generate 2 random strings
            source_string, target_string = generate_random_strings()

            # Calculate the Levenshtein distance
            distance = calculate_levenshtein_distance(source_string, target_string)

            # Output the result
            print(
                f"The minimum number of operations to transform '{source_string}' into '{target_string}' is {distance}")


if __name__ == "__main__":
    main()
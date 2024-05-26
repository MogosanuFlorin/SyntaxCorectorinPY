def min_of_three(a, b, c):
    return min(min(a, b), c)


def calculate_levenshtein_distance(source, target):
    source_length = len(source)
    target_length = len(target)

    # Initialize the distance matrix
    distance_matrix = [[0] * (target_length + 1) for _ in range(source_length + 1)]

    # Initialize the first row and first column of the distance matrix
    for i in range(source_length + 1):
        distance_matrix[i][0] = i  # Cost of deleting all characters from source
    for j in range(target_length + 1):
        distance_matrix[0][j] = j  # Cost of inserting all characters to target

    # Fill in the distance matrix
    for i in range(1, source_length + 1):
        for j in range(1, target_length + 1):
            if source[i - 1] == target[j - 1]:
                distance_matrix[i][j] = distance_matrix[i - 1][j - 1]  # No cost if characters match
            else:
                insertion_cost = distance_matrix[i][j - 1] + 1
                deletion_cost = distance_matrix[i - 1][j] + 1
                replacement_cost = distance_matrix[i - 1][j - 1] + 1
                distance_matrix[i][j] = min_of_three(insertion_cost, deletion_cost, replacement_cost)

    # The Levenshtein distance is found at the bottom-right cell of the matrix
    return distance_matrix[source_length][target_length]

import random


def generate_random_string(length):
    charset = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(charset) for _ in range(length))


def generate_random_strings():
    length1 = random.randint(2, 30)  # Length between 2 and 30
    length2 = random.randint(2, 30)  # Length between 2 and 30

    str1 = generate_random_string(length1)
    str2 = generate_random_string(length2)

    return str1, str2

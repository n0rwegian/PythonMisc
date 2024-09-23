import random
from string import ascii_letters, digits


def generate_password(length):
    chars = [c for c in ascii_letters + digits if c not in 'lI1oO0']
    print(''.join([chars[random.randint(0, len(chars) - 1)] for _ in range(length)]))

def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)

n, m = int(input()), int(input())
generate_passwords(n, m)

# quick_picks.py

import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate and display quick pick lottery numbers."""
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    """Generate a sorted set of unique random numbers for a quick pick."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)
    return sorted(quick_pick)


if __name__ == "__main__":
    main()
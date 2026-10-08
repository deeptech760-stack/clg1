def is_prime_or_odd(number):
    """Classify a number as prime, odd, even, or neither.

    Edge cases handled:
    - numbers less than or equal to 1 are "Neither prime nor odd"
    - 2 is treated as a prime number, even though it is even
    - negative numbers are treated as "Neither prime nor odd"

    Example uses:
    >>> is_prime_or_odd(2)
    'Prime'
    >>> is_prime_or_odd(9)
    'Odd but not prime'
    >>> is_prime_or_odd(0)
    'Neither prime nor odd'
    """
    if number <= 1:
        return "Neither prime nor odd"
    if number % 2 == 0:
        if number == 2:
            return "Prime"
        return "Even"
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return "Odd but not prime"
    return "Prime"


def show_examples():
    sample_values = [0, 1, 2, 3, 4, 5, 9, 11, 13, -3]
    print("Example uses:")
    for value in sample_values:
        print(f"{value} -> {is_prime_or_odd(value)}")


def main():
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    result = is_prime_or_odd(user_input)
    print(result)


if __name__ == "__main__":
    show_examples()
    main()

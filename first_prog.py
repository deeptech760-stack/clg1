def is_prime_or_odd(number):
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


def main():
    user_input = int(input("Enter a number: "))
    result = is_prime_or_odd(user_input)
    print(result)


if __name__ == "__main__":
    main()

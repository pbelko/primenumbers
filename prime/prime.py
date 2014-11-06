__author__ = 'tony'
import sys

print(sys.argv)


def main() -> object:
    sentence = "Enter in a number to calculate: "
    number = int(input(sentence))
    calculate_prime(number)


def calculate_prime(a):
    if a < 2:
        sentence = 'The number { } must be greater than 2.'.format(a)
        print(sentence)
    for i in range(2, a):
        if is_prime(i):
            print(i)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


if __name__ == "__main__":
    main()

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def main():
    first_number = 12
    second_number = 3

    print(f"Addition: {add(first_number, second_number)}")
    print(f"Subtraction: {subtract(first_number, second_number)}")
    print(f"Multiplication: {multiply(first_number, second_number)}")
    print(f"Division: {divide(first_number, second_number)}")


if __name__ == "__main__":
    main()
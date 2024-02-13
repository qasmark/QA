import sys


def is_number(num) -> bool:
    if isinstance(num, int) or isinstance(num, float):
        return True
    else:
        return False


def validate_data(lst) -> bool:
    if len(lst) != 4:
        print('Uncorrected format of command line. Usage: triangle.exe <number> <number> <number>')
        return False

    for i in range(1, len(lst)):
        try:
            lst[i] = float(lst[i])
        except ValueError:
            print(f"Error convert value '{lst[i]}' to type float")
            return False

    if not is_number(lst[1]) or not is_number(lst[2]) or not is_number(lst[3]):
        print('Uncorrected type of arguments. Numbers should be only numbers')
        return False

    elif (lst[1] <= 0) or (lst[2] <= 0) or (lst[3] <= 0):
        print('Triangle sides must be only positive numbers')
        return False
    return True


def check_type_of_triangle(lst):
    a, b, c = float(lst[1]), float(lst[2]), float(lst[3])

    if (a > b + c) or (b > a + c) or (c > a + b):
        print('This is not triangle')

    elif a == b and b == c:
        print('Equilateral triangle')

    elif (a == b) or (b == c) or (a == c):
        print('Isosceles triangle')

    else:
        print('Arbitrary triangle')


if __name__ == '__main__':
    if validate_data(sys.argv):
        check_type_of_triangle(sys.argv)

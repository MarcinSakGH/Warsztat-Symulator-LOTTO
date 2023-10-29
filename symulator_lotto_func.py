from random import shuffle


def get_num():
    """
    Get a number from user. Try until user gives proper number.
    :return: given number as int
    """
    while True:
        try:
            num = int(input('Choose a number:\n'))
            break
        except ValueError:
            print("It's not a number")
    return num


def get_numbers():
    """
    Get 6 different numbers between 1 and  49
    :return: list  with 6 numbers provided by user
    """
    usr_nums = []
    while len(usr_nums) < 6:
        number = get_num()
        if number not in usr_nums and 0 < number <= 49:
            usr_nums.append(number)
    return usr_nums

def print_numbers(numbers):
    """
    Print given numbers with ascending order
    """
    print(", ".join(str(number) for number in sorted(numbers)))

def drawing_numbers():
    numbers = list(range(1, 49))
    shuffle(numbers)
    return numbers[:6]

def lotto():
    """
    Main function with our program
    """
    usr_nums = get_numbers()
    print("Your numbers:")
    print_numbers(usr_nums)
    random_nums = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_nums)

    hits = 0
    for num in usr_nums:
        if num in random_nums:
            hits += 1

    print(f"You hit {hits}  {'number' if hits == 1 else 'numbers'}")


if __name__ == '__main__':
    lotto()

from random import randint

win_nums =[]

while len(win_nums) < 6:
    num = randint(1, 49)
    if num not in win_nums:
        win_nums.append(num)


my_nums = []
while len(my_nums) < 6:
    guess = input("Choose a number from range 1-49\n")
    try:
        guess = int(guess)
    except ValueError:
        print("Entered value is incorrect - type a number from range 1 - 49")
        continue
    if guess not in range(1, 50):
        print("This number is outside 1-49 range. Pick different number")
        continue
    if guess not in my_nums:
        my_nums.append(guess)
    else:
        print("This number was already chosen. Pick other number from range 1-49")

my_nums.sort()
win_nums.sort()
print('My types are: ', my_nums)
print('The winning numbers are: ', win_nums)

guesses = 0
for num in my_nums:
    if num in win_nums:
        guesses += 1

print("You've guessed", guesses, "numbers")
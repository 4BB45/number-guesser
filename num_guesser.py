import random

num = int(random.uniform(1, 100))

guess = input('guess a number between 1 and 100 (you get 3 tries): ')

tries = 1

while tries < 3:
    if guess != num:
        print('try again :)')
        guess = input('guess a number between 1 and 100 (you get 3 tries): ')
    tries += 1
    if tries == 3:
        print(f"HAHA L BOZO the answer was {num} >:)) )")

# guess != num:
    # print('try again :)')
    # guess = input('guess a number between 1 and 100: ')
    # tries += 1
    # if tries > 3:
    #     print(f"you've run out of chances, the answer was {num}")
    # break


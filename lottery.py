from random import *

lottery_characters : tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')

print("Any ticket matching the following 4 letters or numbers wins a prize!")
print("Winning ticket: ")
for i in range(0, 4):
    print(choice(lottery_characters), end='')



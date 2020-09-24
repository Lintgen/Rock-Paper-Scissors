import random
import math
score = 0
normal = False
win = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
options = []
player = input('Enter your name:')
print(f'Hello, {player}')
with open('rating.txt') as f:   # opening the file with results
    records = f.readlines()
    for record in records:
        name, points = record.split()
        if name == player:
            score = int(points)

user_list = input().split(',')  # alternative list of words
if user_list == ['']:
    options = ['rock', 'paper', 'scissors']
    normal = True
else:
    options = user_list
print("Okay, let's start")

while True:
    play = input()
    comp = random.choice(options)
    if play == '!exit':break
    elif play == '!rating':
        print(f'Your rating: {score}')
    elif play not in options:
        print('Invalid input')
    elif normal:
        if win[play] == comp: print(f'Sorry, but the computer chose {comp}')
        elif play == comp:
            print(f'There is a draw ({comp})')
            score += 50
        else:
            print(f'Well done. The computer chose {comp} and failed')
            score += 100
    elif normal == False:
        word = (user_list.index(play)) # index number of user input (play)
        words = user_list[word + 1:] + user_list[:word] # new concatenated list
        middle = math.ceil((len(words)) / 2)  # index number of the middle element
        lose_list = words[:middle]
        win_list = words[middle:]
        if comp in lose_list:
            print(f'Sorry, but the computer chose {comp}')
        elif play == comp:
            print(f'There is a draw ({comp})')
            score += 50
        elif comp in win_list:
            print(f'Well done. The computer chose {comp} and failed')
            score += 100

print('Bye!')

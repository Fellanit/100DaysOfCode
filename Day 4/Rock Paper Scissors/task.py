rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
figures = [rock, paper, scissors]

users_input = int(input("Hello it`s Rock-Paper-Scissors game!\nWhat do you choose? Type 1 for Rock, 2 for Paper, 3 for Scissors\n"))
users_figure = users_input - 1
com_figure = random.randint(0,2)
print(figures[users_figure])
print(figures[com_figure])
if figures[users_figure] == figures[com_figure]:
    print("Draw!")
elif (users_figure == 0 and com_figure == 2) or \
    (users_figure == 1 and com_figure == 0) or \
    (users_figure == 2 and com_figure == 1):
    print("You win!")
else:
    print("You lose!")
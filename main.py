import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

choice = random.randint(0, 2)

userschoice = int(input('1)Rock , 2)Paper Or  3)Scissor : \n'))
print(f'Computer\'s choice: {options[choice]}')
print(f'User\'s choice: {options[userschoice-1]}')


def judge(a, b):
    if a == b:
        return 'Draw'
    elif b > a and b - a == 1:
        return 'You won'
    elif a > b and a - b == 1:
        return 'U lost'
    elif b > a and b - a == 2:
        return 'U lost'
    else:
        return 'You won'


print(judge(choice, userschoice-1))

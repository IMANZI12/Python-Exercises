import random
from classes import Options

options = [Options(0), Options(1), Options(2)]

choice = random.randint(0, 2)

userschoice = int(input('1)Rock , 2)Paper Or  3)Scissor : \n'))
print(f'Computer\'s choice: {options[choice].display()}')
print(f'User\'s choice: {options[userschoice - 1].display()}' if 1 <= userschoice <= 3 else f'Invalid Option')


if choice == userschoice:
    print('Draw')
elif userschoice > choice and userschoice - choice == 1:
    print('You won')
elif choice > userschoice and choice - userschoice == 1:
    print('U lost')
elif userschoice > choice and userschoice - choice == 2:
    print('U lost')
elif choice > userschoice and choice - userschoice == 2:
    print('You won')
else:
    print('U lost')


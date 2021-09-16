import random

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

user_choice = int(input("What do you choose: type 0 for rock, 1 for paper and 2 for scissors\n"))

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)




computer_choice = random.randint(0,2)
print(computer_choice)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

if computer_choice == user_choice:
  print("Draw")

if computer_choice == 0 and user_choice == 1:
  print("You Win")


if computer_choice == 0 and user_choice == 2:
  print("You Lose")

if computer_choice == 1 and user_choice == 0:
  print("You lose")

if computer_choice == 1 and user_choice == 2:
  print("You Win")

if computer_choice == 2 and user_choice == 0:
  print("You Win")

if computer_choice == 2 and user_choice == 1:
  print("You Lose")
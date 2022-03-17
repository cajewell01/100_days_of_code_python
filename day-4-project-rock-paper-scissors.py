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

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer = random.randint(0,2)

if choice == 0 and computer == 2:
  print (rock + "\n Computer Chose:" + scissors + "Rock beats scissors. You win!")
elif choice == 0 and computer == 1:
  print(rock + "\n Computer Chose:" + paper + "Paper beats rock. You lose!")
elif choice == 0 and computer == 0:
  print(rock + "\n Computer Chose:" + rock + "It's a draw.")
if choice == 1 and computer == 0:
  print (paper + "\n Computer Chose:" + rock + "Paper beats rock. You win!")
elif choice == 1 and computer == 2:
  print(paper + "\n Computer Chose:" + scissors + "Scissors beats paper. You lose!")
elif choice == 1 and computer == 1:
  print(paper + "\n Computer Chose:" + paper + "It's a draw.")
if choice == 2 and computer == 1:
  print (scissors + "\n Computer Chose:" + paper + "Scissors beats paper. You win!")
elif choice == 2 and computer == 0:
  print(scissors + "\n Computer Chose:" + rock + "Rock beats scissors. You lose!")
elif choice == 2 and computer == 2:
  print(scissors + "\n Computer Chose:" + scissors + "It's a draw.")
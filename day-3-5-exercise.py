#You are going to write a program that tests the compatibility between two people. To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
names_t = name1.count("t") + name2.count("t")
names_r = name1.count("r") + name2.count("r")
names_u = name1.count("u") + name2.count("u")
names_e = name1.count("e") + name2.count("e")
total_true = names_t + names_r + names_u + names_e
print(f"T = {names_t}")
print(f"R = {names_r}")
print(f"U = {names_u}")
print(f"E = {names_e}")
print(f"Total = {total_true}")
names_l = name1.count("l") + name2.count("l")
names_o = name1.count("o") + name2.count("o")
names_v = name1.count("v") + name2.count("v")
total_love = names_l + names_o + names_v + names_e
print(f"L = {names_t}")
print(f"O = {names_r}")
print(f"V = {names_u}")
print(f"E = {names_e}")
print(f"Total = {total_love}")
love_score_print = str(total_true) + str(total_love)
love_score = int(love_score_print)
print(love_score)

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score_print}, you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
  print(f"Your score is {love_score_print}, you are alright together.")
else:
  print(f"Your score is {love_score_print}.")
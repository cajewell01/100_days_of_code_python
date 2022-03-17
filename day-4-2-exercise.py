# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

number_of_names = (len(names))

pick_name = random.randint(0, number_of_names-1)

print(f"{names[pick_name]} is going to but the meal today!")
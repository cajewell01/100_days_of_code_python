#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))

number_of_people = int(input("How many people were in your party? "))

tip_percent = int(input("What percent would you like the tip to be? "))

final_split = format((total/number_of_people) * ((tip_percent/100)+1), '.2f')

print(f"Each person should pay: ${final_split}")
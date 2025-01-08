"""
Part 1:
Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to
 enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display
 each of these amounts and the total price.

Part 2:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you
 set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the
 above problem. Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
  Your program should output what the time will be on a 24-hour clock when the alarm goes off.
"""

# Part one
# Ask for the charge of the food
food_charge = float(input("enter the amount for the food purchased: "))

# Calculate the tip and sales tax
tip = food_charge * 0.18
sales_tax = food_charge * 0.07

# Calculate the total amount
total = food_charge + tip + sales_tax

# Print the results
print(f"charge for food: {food_charge}")
print(f"tip (18%): {tip}")
print(f"sales Tax (7%): {sales_tax}")
print(f"total amount: {total}")



print("executing the Part two of the assignment")
# Part Two
# Read the current time and the number of hours to wait for the alarm from the user
current_time = int(input("enter the current time (in hours): "))
hours_to_wait = int(input("enter the number of hours to wait for the alarm: "))

# Calculate the no. of days
# / division finds the number of days by coundting the times 24 is divisble
alarm_days = hours_to_wait // 24

# Calculate the time when the alarm goes off
# % modulus find the time, by using the reminder
alarm_time = (current_time + hours_to_wait) % 24

# Check if the number of days is zero, then print as today. it is much readble
if alarm_days == 0:
    print(f"the alarm will go off today at {alarm_time}")
    print(f"digital: 00 days {alarm_time}:00")
else:
    print(f"the alarm will go off in : {alarm_days} days at hour {alarm_time}")
    print(f"digital: {alarm_days} - {alarm_time}:00:00")


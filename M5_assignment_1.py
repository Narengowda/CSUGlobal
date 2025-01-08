'''
Part 1
Write a program that uses nested loops to collect data and calculate the average rainfall
over a period of years. The program should first ask for the number of years. The outer
 loop will iterate once for each year. The inner loop will iterate twelve times, once for
  each month. Each iteration of the inner loop will ask the user for the inches of rainfall
  for that month. After all iterations, the program should display the number of months,
  the total inches of rainfall, and the average rainfall per month for the entire period.

'''


num_years = int(input("Enter the number of years: "))
total_rainfall = []
months = ["January", "February", "March", "April", "May", "June",  "July", "August", "September", "October", "November", "December"]

for year in range(num_years):
    print(f"Year {year + 1}:")

    for i, month in enumerate(months):
        rain_fall = float(input(f"{i + 1}. Enter the rainfall for month {month} of year {year + 1}: "))
        total_rainfall.append(rain_fall)

average_rainfall = sum(total_rainfall) / len(total_rainfall)
print(f"Total number of months: {len(total_rainfall)}")
print(f"total inches of rain fall: {sum(total_rainfall)}")
print(f"Average rainfall per month: {average_rainfall} inches")
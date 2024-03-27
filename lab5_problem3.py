# Cameron Kerr
# Language: Python 3.9.1
# lab5_problem3.py

# This program predicts the approximate size of a population of organisms

# create and initialize variables to null
organisms = 0
avg_increase = 0.0
days = 0
appr_population = 0.0

# get input from user for each variable
organisms = int(input('Enter the starting number of organisms: '))
avg_increase = float(input('Enter the average percent daily increase: '))
days = int(input('Enter the number of days to multiply: '))

# change the average percent daily increase to a decimal
avg_increase /= 100

# print table headings
print('\nDays \t\t Approximate Population')
print('-------------------------------------------------')

# calculate the approximate size of the population of organisms
for day in range(1, days + 1):
    if day == 1:
        appr_population = organisms
    else:
        appr_population *= (1 + avg_increase)
    print(day, '\t\t', format(appr_population, '.4f'))

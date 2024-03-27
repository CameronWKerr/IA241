# Cameron Kerr
# Language: Python 3.9.1
# lab5_problem2.py

# This program will collect data and calculate the average
# rainfall over a period of year.

# create and initialize variables to null
years = 0
months = 0.0
monthly_rain = 0.0
total_rain = 0.0
avg_rain = 0.0

# get number of years from the user
years = int(input('Enter the number of years: '))

# use nested loops to receive the amount of rainfall for user inputed data
for year in range(years):
    total_rain = 0.0
    for months in range(1, 13):
        monthly_rain = float(input('Enter the amount of rainfall for the month in inches: '))
        total_rain += monthly_rain
        

# calculate the average rain
avg_rain = total_rain / months

print('\nFor', years, 'years \n Total average rainfall: ', format(avg_rain, '.2f'), ' inches')

# Cameron Kerr
# Simple Value Returning Functions
# Language: Python 3.9.1
# lab6.py

# This program will calculate CO2 emissions given user input data.

# define the yearly_miles_driven function
def yearly_miles_driven(distance_to_work, days_worked):

    # calculate miles_driven
    miles_driven = distance_to_work * (days_worked*52)

    # return the miles_driven result
    return miles_driven

# define the gallons_used_per_year function and pass it miles_driven
def gallons_used_per_year(miles_driven, mpg):

    # calculate the gallons of gas used per year
    gallons_of_gas = (miles_driven*2) / mpg

    # return the gallons_of_gas result
    return gallons_of_gas

# define the emission_per_year function and pass it gallons_of_gas
def emission_per_year(gallons_of_gas):

    # declare and initialize CO2 constant
    CO2_EMISSIONS_PER_GALLON = 19.4

    # calculate total CO2 emission
    co2_emissions_per_year = CO2_EMISSIONS_PER_GALLON * gallons_of_gas

    # return co2_emissions_per_year result
    return co2_emissions_per_year

# define main function
def main():

    # get user input for variables
    distance_to_work = float(input('\nEnter the distance it takes to get to work in miles: '))
    days_worked = float(input('\nEnter the number of days worked this week: '))
    mpg = float(input('\nEnter the miles per gallon your vehicle receives: '))

    # call the functions
    miles_driven = yearly_miles_driven(distance_to_work, days_worked)
    gallons_of_gas = gallons_used_per_year(miles_driven, mpg)
    co2_emissions_per_year = emission_per_year(gallons_of_gas)
    
    # create table for outputs
    print('\nDistance to work\t MPG of vehicle\t\t Number of days/week\t Emissions for a year')
    print('------------------------------------------------------------------------------------------------')
    print(distance_to_work, 'miles\t\t', mpg, 'mpg\t\t', days_worked, '\t\t\t', format(co2_emissions_per_year, '.2f'), 'pounds/gallon')

main()

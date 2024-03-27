# Cameron Kerr
# Language: Python 3.9.1
# This program asks the user to enter a series of 20 numbers
# and stores those numbers in a list. Then, calculations are performed and displayed

# define the main function
def main():

    # define the constant NUM
    NUM = 20
    
    # create a list to hold the numbers
    numbers = [0]*20

    # create an index variable
    index = 0

    # receive numbers from user
    print('Enter a number: ')

    # get the numbers
    while index < NUM:
        print('Input value #', index+1, ':', sep='', end ='')
        numbers[index] = float(input(' '))
        index += 1

    # perform and display calculations
    print('\nThe lowest number in the list was: ', format(min(numbers), '0.2f'))
    print('The highest number in the list was: ', format(max(numbers), '0.2f'))
    print('The total of the numbers in the list was: ', format(sum(numbers), '0.2f'))
    print('The average of the numbers in the list was: ', format(sum(numbers)/len(numbers), '0.2f'))

main()

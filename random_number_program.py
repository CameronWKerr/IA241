# Cameron Kerr
# Language: Python 3.9.1
# This program writes a series of random numbers 1-500 to a file
# then, it will read the file, display the numbers, and display more data

import random

def generator():
    # generate a random number 1-500
    randomNumber = random.randint(1,500)

    # return randomNumber
    return randomNumber

def main():
    # get input from user to specify how many random numbers the file can hold
    num_range = int(input('Enter the amount of numbers you want the file to hold: '))

    # open the random number file
    file = open('random_num.txt', 'w')

    # create a for loop to write the number to the .txt file
    for numCount in range(1, num_range + 1):
        randomNumber = generator()
        file.write(str(randomNumber) + "\n")
        
main()

def read_display():
    # open the .txt file for reading
    randomNumber = open('random_num.txt', 'r')

    # create variable to hold total
    total = 0
    
    # create variable to hold the count
    count = 0

    # read all the lines from the file
    for line in randomNumber:
        
        # convert line to an integer
        amount = int(line)

        total += amount
        count += 1

        # diplay the amount
        print(amount)

    # close the file
    randomNumber.close()
    print('The total (sum) of the random numbers was: ', total)
    print('The number of random numbers read from the file was: ', count)

read_display()

# Cameron Kerr
# Language: Python 3.9.1
# This program allows the user to open a text file, enter three numbers,
# calculate the sum of those numbers, and print the output.

def get_save_data():
    # Open a file for writing.
    outfile = open('numbers.txt', 'w')
    
    # Get three numbers from the user.
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    num3 = float(input('Enter another number: '))
    
    # Write the numbers to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    
    # Close the file.
    outfile.close()
    print('Data written to numbers.txt')

def main():
    # Call the get_save_data function
    result = get_save_data()

    # Open a file for reading.
    infile = open('numbers.txt', 'r')
    
    # Read three numbers from the file.
    num1 = float(infile.readline())
    num2 = float(infile.readline())
    num3 = float(infile.readline())

    # Close the file
    infile.close()
    
    # Add the three numbers.
    total = num1 + num2 + num3
    
    # Display the numbers and their total.
    print('The numbers are:', num1, num2, num3)
    print('Their total is:', total)

main()

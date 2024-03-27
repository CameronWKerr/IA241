# Cameron Kerr
# python_loops.py
# Language: Python 3.9.1

# this program uses the range function to print out
# the odd numbers from 1 to 20 on two lines

print('I will display the odd numbers from 1 to 20 on two lines.')
for x in range(1, 20, 2):
    print(x)

# add a space in the program between loops
print('\n')

# this program uses a while loop to print out numbers,
# starting with 1 and doubling each until the total exceeds 1000

# initialize variables
total = 0

# start while loop process
print('I will display the total after it has been doubled until the total \
exceeds 1000.')
total = 1
while total <= 1000:
    print(total)
    total += total

# add a space in the program between loops
print('\n')

# this program uses a nested for loop to print out a table
# start nested loop process
print('I will display the numeric table.')
for number in range (1, 6):
    number = number
    for product in range (2, 11):
        product = number + number
        for product2 in range (3, 16):
            product2 = product + number
            for product3 in range (4, 21):
                product3 = product2 + number
                for product4 in range(5,26):
                    product4 = product3 + number
    print(number, '\t', product, '\t', product2, '\t', product3, '\t', product4)

# add a space in the program between loops
print('\n')

# this program displays a triangle pattern
print('I will display the star pattern.')
BASE_SIZE = 7

for r in range(BASE_SIZE, 0, -1):
    for c in range(r - 1):
        print('*', end='')
    print()


# Cameron Kerr
# IA 241
# language: Python 3.9.1
# simple while loop with input
# whileloop.py

# initialize variables
total = 0

# start loop
total = 0
while total < 25:
    num = float(input('Enter number '))
    if num > 0:
        total = total + num**2

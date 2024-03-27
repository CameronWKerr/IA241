# program to gather personal information
# program: myinfo.py
# python 3.9
# Cameron Kerr IA241

#create name, age, and income variables and initialize to null
name=''
age=0
income=0.0

# get input for variables
name = input('Please enter your name ')
age = int(input('What is your age? '))
income = float(input('How much do you make? '))

#display information
print("My name is", name, "and I am", age, "years old")
print("My monthly income is", income, "dollars")
print("My major is Intelligence Analysis")
print('I think "Python Programming" is fun!')

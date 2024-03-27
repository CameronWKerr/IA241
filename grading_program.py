# determine letter grade

# declare and initialize
A_SCORE=90
B_SCORE=80
C_SCORE=70
D_SCORE=60
F_SCORE=50

# get numerical score
score=int(input('Enter the numerical grade '))

# decision block
if score >= A_SCORE:
    print('Your grade is an A')
elif score >= B_SCORE:
    print('Your grade is a B')
elif score >= C_SCORE:
    print('Your grade is a C')
elif score >= D_SCORE:
    print('Your grade is a D')
else:
    print('Your grade is a F')

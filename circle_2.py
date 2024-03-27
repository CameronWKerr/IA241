# This program computes the area of a circle
# Cameron Kerr
# Language: Python 3.9.1
# circle_2.py

def main():
    # declare variables and constants
    radius = 0.0
    
    # get input
    radius = float(input('Enter the radius in meters: '))

    # call compute_area function and pass it radius
    compute_area(radius)
    
    # call compute_area function and pass it the radius
def compute_area(radius):
        
    # declare variables and constants
    area = 0.0
    PI = 3.14
        
    #process - compute the area of the circle
    area = (PI * radius ** 2)
        
    #output - display the result
    print('\nThe area of the circle is', format(area, '.2f'), 'meters squared')

main ()

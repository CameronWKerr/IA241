# This program computes the area and circumference of a circle
# Cameron Kerr
# Language: Python 3.9.1
# circle_3.py

#declare global variables and constants
PI = 3.14

def compute_area(radius):
    # declare variables and constants
    area = 0.0

    # compute the area of the circle
    area = (PI * radius ** 2)
    
    # return computed value back to main()
    return area
    
def compute_circumference(radius):
    # declare variables and constants
    circumference = 0.0

    # compute circumference
    circumference = (PI * radius * 2)

    # return computed value back to main()
    return circumference

def main():      
    # input - get the radius
    radius = float(input('Enter the radius in meters: '))

    # call the functions and display the returned values
    area = compute_area(radius)
    circumference = compute_circumference(radius)

    #output - display the result
    print('\nThe area of the circle is', format(area, '.2f'), 'meters squared')
    print('\nThe circumference of the circle is', format(circumference, '.2f'), 'meters')
    
main ()

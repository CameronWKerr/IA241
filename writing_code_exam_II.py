#'''
#WRITING CODE (26 points)

#INSTRUCTIONS-READ CAREFULLY:
#Carefully examine the incomplete code snippets below to compute the area
#and perimeter of a rectangle.  The code logic would work if all statements
#were correctly included.

#YOUR TASKS:
#Complete the program so Input, Processing, and Output are each performed
#by functions or calls to functions.  The function we will use for input
#is main() which will also call the other functions.  

#The code has been partially written for you. You ONLY need to complete the
#writing of the code for the functions by COMPLETELY REPLACING THE BLANK LINES
#with your code. DO NOT CHANGE ANYTHING ELSE!

#WARNING:
#You MUST use the variable names given and your output should be formatted
#with two decimal point accuracy. You may use any input/output units you want
#BUT you MUST use units in the input and print statements.

#DO NOT change anything already in the print statements.  Submit your completed
#code to Canvas. YOUR CODE MUST RUN TO RECEIVE CREDIT


 
# program to determine the area and perimeter of a rectangle
# IA 241 Exam II
# rectangle.py
# Cameron Kerr
 

# Complete the writing of the function to compute the area
def compute_area(length,width):

       area = length*width
	
       return area
	
# Write a function that receives the length and a width as value parameters
# and returns the perimeter of the rectangle.  
# Call the function compute_perimeter
def compute_perimeter(length,width):

       perimeter = (length*2)+(width*2)

	
       return perimeter

# Complete the writing of the function to display the computed values of
# the area and perimeter
def display_area_and_perimeter(area,perimeter):

       print('The area of the rectangle is: ', format(area,'0.2f'), 'meters squared')

       print('The perimeter of the rectangle is: ',format(perimeter,'0.2f',), 'meters')

 
def main():
        
       #declare and initialize variables
       length = 0.0

       width = 0.0
       perimeter  = 0.0

       area  = 0.0

       #get input
       length = float(input('enter the length in meters: '))

       width = float(input('enter the width in meters: '))


       #Compute the area by calling the function
       area = compute_area(length, width)
	
       #Compute the perimeter by calling the function
       perimeter = compute_perimeter(length, width)
       	
       #Display the area and the perimeter by calling the function 
       display_area_and_perimeter(area, perimeter)


#call main
main()

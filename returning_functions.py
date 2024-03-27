# value returning functions

#main function
def main():
    #declare and init local variable
    total = 0.0
    val1 = 0
    val2 = 24
    val1 = int(input('enter an integer: '))
    #call the value returning function
    total = sum(val1, val2)
    #print the sum
    print('the sum is {}'. format(total))

# function returns sum of two numbers
def sum(num1, num2):
    result = num1 + num2
    return result
# call main() function
main()

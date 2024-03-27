# passing arguments to function

def main():
    value1 = 5
    value2 = 10
    show_sum(number2=value1, number1=value2)

def show_sum(number1, number2):
    print('number1 = ', number1)
    result = number1 + number2
    print(result)

main()

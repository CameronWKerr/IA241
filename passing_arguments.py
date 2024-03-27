# passing arguments to function

def main():
    value = 0
    value = int(input('Enter an integer '))
    show_double(value)

def show_double(number):
    result = 2 * number
    print(result)

main()

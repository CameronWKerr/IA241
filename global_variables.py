# using global variables
value = 5

def main():
    print('value = ', value)
    show_double()

def show_double():
    result = 2 * value
    print(result)

main()

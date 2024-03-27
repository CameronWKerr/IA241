ROWS = 5
COLS = 3

def main():
    values = [[0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0]]

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c]=int(input('Please enter a number: '))

    print(values)
    

main()

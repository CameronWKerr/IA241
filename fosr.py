# Cameron Kerr
# Language: Python 3.9.1
# fosr.py
# This program will read data files uploaded to a site,
# and then display statistical calculations based on that data

def main():
    # get the data file name
    filename = input('Please enter the filename  to open: ')
    return filename


def turbidity(filename):

    # Local variable
    amount = 0.0
    total = 0.0
    count = 0.0
    avg = 0.0

    # Open input file
    try:
        contents = open('Turbidity.txt', 'r')

        # read and print the first line of the file
        line1 = str(contents.readline())
        print('\nThe', line1, 'file has been received')

        for line in contents:
            amount = float(line)
            total += amount
            count += 1

        avg = total/amount

        print('The total number of data pieces in the Turbidity file \ '
              'amounts to:', format(count, '0.2f'))
        print('The average of the data set in the Turbidity file \ '
              'is: ', format(avg, '0.2f'))

    # Close the file
        filename.close()
    except IOError:
        print('An error occurred trying to read')
        print('the file name', filename)
    except ValueError:
        print('Non-numeric data found in the file.')
    except Exception as err:
        print(err)
    except:
        print('An error occurred.')
        print('the name of the file is: ', filename)


turbidity()


def lab_ph(filename):

    # local variables
    amount = 0.0
    total = 0.0
    count = 0
    avg = 0.0

    # Open input file
    try:
        contents = open(filename, 'r')

        # read and print the first line of the file
        line1 = str(contents.readline())
        print('The', line1, 'file has been received')

        for line in contents:
            amount = float(line)
            total += amount
            count += 1

        avg = total/count

        print('The total number of data pieces in the Lab pH file \ '
              'amounts to:', format(count, '0.2f'))
        print('The average of the data set in the LabpH file \ '
              'is: ', format(avg, '0.2f'))

    # Close the file
        contents.close()
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)
    except ValueError:
        print('Non-numeric data found in the file.')
    except Exception as err:
        print(err)
    except:
        print('An error occurred.')
        print('the name of the file is: ', filename)


lab_ph()

main()

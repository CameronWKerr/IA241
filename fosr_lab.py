# Cameron Kerr                                                 
# Language: Python 3.9.1                                       
# fosr_lab.py                                                      
# This program will read data files uploaded to a site,        
# and then display statistical calculations based on that data

def main():                                                 
    # get the data file name                                
    filename = input('Please enter the filename you want to open: ')

    # Local variable
    total = 0.0                                                                               
    count = 0
                                                                                              
    # Open input file                                                                         
    try:                                                                                      
        contents = open(filename, 'r')                                                 
                                                                                              
        # read and print the first line of the file                                           
        line1 = contents.readline()
        print('\nThe', line1.rstrip(), 'file has been received')

        # create for loop to tally the count and total of the data set                                                                                    
        for line in contents:                                                                 
            amount = float(line)                                                              
            total += amount                                                                   
            count += 1
            
        # calculate the average of the data set                                                                                     
        avg = total/count

        # display the results                                                                           
        print('\nThe total number of data pieces in the', filename, 'file amounts to:', count)                                           
        print('\nThe average of the data set in the', filename, 'file is: ', format(avg, '0.2f'))                                                    
                                                                                              
    # Close the file                                                                          
        filename.close()
        
    # run exception statements to trap for errors
    except IOError:                                                                           
        print('An error occurred trying to read the file name', filename)
    except ValueError:                                                                        
        print('Non-numeric data found in the file.')                                          
    except Exception as e:                                                                  
        print(e)
    except:
        print('An error occurred.')
    else:
        print('The name of the file is: ', filename)


main()

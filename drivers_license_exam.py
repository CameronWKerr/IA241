# Cameron Kerr
# Language: Python 3.9.1
# This program grades the written portion of the driver's license exam

# define the main function
def main():

    # create a constant list for the correct answers
    CORRECT = ['B', 'C', 'A', 'A', 'D', 'D', 'B', 'B', 'C', 'C', \
               'D', 'A', 'B', 'A', 'D', 'A', 'C', 'B', 'D', 'A']
               
    # open the student answers file for reading while trapping for errors
    try:
        answers_file = open('student_answers.txt', 'r')

        # create a list for the student correct and incorrect answers
        answers = []
        incorrect = []

        # create a for loop to fill the lists
        for line in answers_file:
            answers.append(line.rstrip('\n'))
        for line in answers_file:
            incorrect.append(line.rstrip('\n'))

        # create variable to hold number of correct and incorrect answers
        number_correct = 0
        number_incorrect = 0
    
        # compare correct answer list to student answer list
        for i in range (len(answers)):
            if answers[i] == CORRECT[i]:
                number_correct += 1
            else:
                number_incorrect += 1
                incorrect.append(i)
                
        # indicate whether the student passed or failed
        if number_correct >= 15:
            print('The student has passed the exam. \nThe student' \
                  ' scored a: ', number_correct, 'out of 20 questions.' \
                  '\nThe student got ', number_incorrect, 'questions incorrect.' \
                  '\nHere is a list of the incorrectly answered questions: ' \
                  '\n', incorrect)
              
        else:
            print('The student has failed the exam. \nThe student' \
                  ' scored a: ', number_correct, 'out of 20 questions.' \
                  '\nThe student got ', number_incorrect, 'questions incorrect.' \
                  '\nHere is a list of the incorrectly answered questions: ' \
                  '\n', incorrect)

        # close the file
        answers_file.close()

        # continue trapping for errors
    except IOError:
        print('An error occurred trying to read the file.')
    except ValueError:
        print('Improper data found in the file.')
    except IndexError:
        print('The index of the file does not match the answer sheet.')
    except Exception as e:
        print(e)
    except:
        print('An error occurred.')

main()

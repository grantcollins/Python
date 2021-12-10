import numpy as np

def main():
    """
    Matrix Math Application main
    """
    # Menu
    print('*****Welcome to the Python Matrix Application!*****')
    selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                           'Enter Y for Yes or N for No:\n')).upper().strip()

    # Sentinel While loop
    while selection1 != 'N':

        # Answer is Y
        if selection1 == 'Y':

            # Matrix 1 Creation
            matrix1list = []
            print('\nEnter your first 3x3 Matrix:')
            quantity = 9
            while quantity:
                try:
                    matrix1input = int(input('Enter value: '))
                    matrix1list.append(matrix1input)
                    quantity -= 1
                except ValueError:
                    print('You must enter an Integer. Please try again.')
            matrix1 = np.array(matrix1list).reshape(3, 3)
            print('Your first 3x3 Matrix is:\n{}\n'.format(matrix1))

            # Matrix 2 Creation
            matrix2list = []
            print('Enter your second 3x3 Matrix:')
            quantity = 9
            while quantity:
                try:
                    matrix2input = int(input('Enter value: '))
                    matrix2list.append(matrix2input)
                    quantity -= 1
                except ValueError:
                    print('You must enter an Integer. Please try again.')
            matrix2 = np.array(matrix2list).reshape(3, 3)
            print('Your second 3x3 Matrix is:\n{}\n'.format(matrix2))

            selection2 = str(input('Select a Matrix Operation from the list below:\n'
                                   'a. Addition\n'
                                   'b. Subtraction\n'
                                   'c. Matrix Multiplication\n'
                                   'd. Element by Element Multiplication\n')).lower().strip()

            # Invalid selection2
            while selection2 not in ['a', 'b', 'c', 'd']:
                print('You must enter a, b, c, or d. Please try again.')
                selection2 = str(input('Select a Matrix Operation from the list below:\n'
                                       'a. Addition\n'
                                       'b. Subtraction\n'
                                       'c. Matrix Multiplication\n'
                                       'd. Element by Element Multiplication\n')).lower().strip()

            # a is selected
            if selection2 == 'a':
                print('\nYou selected Addition. The results are:')
                addedmatrix = matrix1 + matrix2
                print(addedmatrix)
                print('\nThe Transpose is:')
                print(addedmatrix.T)
                print('\nThe row and column mean values of the results are:')
                print('Row:', np.mean(addedmatrix, axis=1))
                print('Column:', np.mean(addedmatrix, axis=0))

            # b is selected
            elif selection2 == 'b':
                print('\nYou selected Subtraction. The results are:')
                submatrix = matrix1 - matrix2
                print(submatrix)
                print('\nThe Transpose is:')
                print(submatrix.T)
                print('\nThe row and column mean values of the results are:')
                print('Row:', np.mean(submatrix, axis=1))
                print('Column:', np.mean(submatrix, axis=0))

            # c is selected
            elif selection2 == 'c':
                print('\nYou selected Matrix Multiplication. The results are:')
                multmatrix = np.matmul(matrix1, matrix2)
                print(multmatrix)
                print('\nThe Transpose is:')
                print(multmatrix.T)
                print('\nThe row and column mean values of the results are:')
                print('Row:', np.mean(multmatrix, axis=1))
                print('Column:', np.mean(multmatrix, axis=0))

            # d is selected
            elif selection2 == 'd':
                print('\nYou selected Element by Element Multiplication. The results are:')
                elmultmatrix = matrix1 * matrix2
                print(elmultmatrix)
                print('\nThe Transpose is:')
                print(elmultmatrix.T)
                print('\nThe row and column mean values of the results are:')
                print('Row:', np.mean(elmultmatrix, axis=1))
                print('Column:', np.mean(elmultmatrix, axis=0))

            selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                                   'Enter Y for Yes or N for No:\n')).upper().strip()

        # Answer is Invalid (y/n)
        else:
            print('You must enter Y or N. Please try again.')
            selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                                   'Enter Y for Yes or N for No:\n')).upper().strip()

    # Answer is N
    print('*****Thanks for playing the Matrix Game.*****')
    return

if __name__ == "__main__":
    main()

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dict = {
            #dict items are keyed as i*9 + j
        }
        potentialNumbers = ["1","2","3","4","5","6","7","8","9"]

        loopNumber = 0
        while any("." in sublist for sublist in board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    dict_index = i*9 + j
                    
                    #Only check cells that have an unknown value
                    if board[i][j] == ".":
                        dict.update({dict_index:potentialNumbers.copy()})
                    
                        #First check all possible values for each cell in a row
                        if len(dict) != 0 and len(dict[dict_index]) != 1:
                            for rowIndex in range(len(board[i])):
                                if board[i][rowIndex] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[i][rowIndex])]

                            
                            if (i + 1)%3 == 0:
                                rowIndex = i - 2
                            elif (i + 1)%3 == 2:
                                rowIndex = i - 1
                            else:
                                rowIndex = i
                            if (j + 1)%3 == 0:
                                boxIndex = j - 2
                            elif (j + 1)%3 == 2:
                                boxIndex = j - 1
                            else:
                                boxIndex = j

                            #Second check all possible values for each cell in a box
                            for box in range(1,10):

                                if board[rowIndex][boxIndex] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[rowIndex][boxIndex])]
                                
                                boxIndex += 1
                                if (box%3) == 0:
                                    boxIndex -= 3
                                    rowIndex += 1
                            
                            #Third check all possible values for each cell in a column
                            for column in range(0,9):
                                if board[column][j] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[column][j])]

                            #reset row Index to the first row
                            rowIndex -=3

                            """Next we need to check for any duplicate possibilities
                            e.g. if there is a 1,2 pair in row i, then no other cells in that row
                            can be a 1 or a 2, remove that possibility from all the other cells.
                            Storing all the values for use later when we check duplicates
                            """
                            allRowValues = []
                            allBoxValues = []
                            allColumnValues = []
                            if len(dict[dict_index]) == 2:
                                for val in dict[dict_index]:
                                    allRowValues.append(val)

                                for checkPairsRow in range(len(board[i])):
                                    currentIndex = i*9 + checkPairsRow
                                    if currentIndex != dict_index and board[i][checkPairsRow] == dict[dict_index]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if currentIndex != duplicateIndex and currentIndex != dict_index:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dict_index][0] or val == dict[dict_index][1]:
                                                        dict[currentIndex].remove(val)
                                    elif currentIndex in dict:
                                        for val in dict[currentIndex]:
                                            allRowValues.append(val)
                                                    

                                for checkPairsBox in range(1, 10):
                                    currentIndex = rowIndex*9 + boxIndex
                                    if currentIndex != dict_index and board[rowIndex][boxIndex] == dict[dict_index]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if len(dict) != 0 and currentIndex != duplicateIndex and currentIndex != dict_index:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dict_index][0] or val == dict[dict_index][1]:
                                                        dict[currentIndex].remove(val)
                                    
                                    boxIndex += 1
                                    if (checkPairsBox%3) == 0:
                                        boxIndex -= 3
                                        rowIndex += 1

                                for rowIndex in range(0,9):
                                    currentIndex = rowIndex*9 + j
                                    if currentIndex != dict_index and board[rowIndex][j] == dict[dict_index]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if len(dict) != 0 and currentIndex != duplicateIndex and currentIndex != dict_index:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dict_index][0] or val == dict[dict_index][1]:
                                                        dict[currentIndex].remove(val)

                            #Check if any of the possible values in the remaining cells are unique
                            print (allRowValues) 

                        if len(dict) != 0 and len(dict[dict_index]) == 1:
                            board[i][j] = dict[dict_index][0]
                            del dict[dict_index]
            loopNumber +=1

        print(board)


                    

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
Solution().solveSudoku(board)
"""Go through every square, row and column and look for groups of possible values which are the same. If any of these groups have the same size as their amount of possible values, remove them from all other possible value arrays in the square/row/column.

    e.g. if a row contains three unfilled cells with possible values (1, 2), (1, 2), (1, 3), the third cell can be reduced to (3) and thus filled in. The reason for this is that since the first two cells must collectively hold values 1 & 2, it's impossible for the third to cell to have value 1, so it's only possible value is 3.
"""
class Solution:
    def solveSudoboxIndexu(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dict = {
        #0 = [1,2,3,4]
        #1 = [1,2,3]
        }
        potentialNumbers = ["1","2","3","4","5","6","7","8","9"]
        #potentialNumbers = ["1","2"]
        #drawBoard = [[potentialNumbers for i in range (9)] for j in range (9)]

        while any("." in sublist for sublist in board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    dict_index = i*9 + j

                    if board[i][j] == ".":
                        dict.update({dict_index:potentialNumbers[:]})
                        #board[i][j] = "7"
                    
                        if len(dict) != 0 and len(dict[dict_index]) != 1:
                            for boxIndex in range(len(board[i])):
                                if board[i][boxIndex] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[i][boxIndex])]

                            
                            if (i + 1)%3 == 0:
                                boxIndex = i - 2
                            elif (i + 1)%3 == 2:
                                boxIndex = i - 1
                            else:
                                boxIndex = i
                            if (j + 1)%3 == 0:
                                rowIndex = j - 2
                            elif (j + 1)%3 == 2:
                                rowIndex = j - 1
                            else:
                                rowIndex = j

                            for row in range(1,9):

                                if board[boxIndex][rowIndex] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[boxIndex][rowIndex])]
                                
                                rowIndex += 1
                                if (row%3) == 0:
                                    rowIndex -= 3
                                    boxIndex += 1

                            if (i) > 5:
                                boxIndex = i - 6
                            elif (i) > 2 :
                                boxIndex = i - 3
                            else:
                                boxIndex = i
                            if (j) > 5:
                                columnIndex = j - 6
                            elif (j) > 2:
                                columnIndex = j - 3
                            else:
                                columnIndex = j

                            for column in range(1,9):

                                if board[boxIndex][columnIndex] in dict[dict_index]:
                                    del dict[dict_index][dict[dict_index].index(board[boxIndex][columnIndex])]
                                if len(dict[dict_index]) == 2:
                                    if dict[dict_index] == dict[dict_index - ((columnIndex+1) % 3)]

                                columnIndex += 3
                                if (column%3) == 0:
                                    columnIndex -= 9
                                    boxIndex += 3
                            
                            boxIndex -= 9
                            if len(dict[dict_index]) == 2:
                                #checkPairsBox = boxIndex * 9 + 
                                for checkPairsBox in range(len(board[i])):
                                    currentIndex = i*9 + checkPairsBox
                                    if currentIndex != dict_index and board[i][checkPairsBox] == dict[dict_index]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for removeDupe in range (1, 9):
                                            if currentIndex != duplicateIndex and currentIndex != dict_index:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dict_index][0] or val == dict[dict_index][1]:
                                                        dict[currentIndex].remove(val)
                                        #del dict[dict_index][dict[dict_index].index(board[i][checkPairsBox])]


                        if len(dict) != 0 and len(dict[dict_index]) == 1:
                            board[i][j] = dict[dict_index][0]
                            del dict[dict_index]


        print(board)


                    

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoboxIndexu(board)


"""Go through every square, row and column and look for groups of possible values which are the same. If any of these groups have the same size as their amount of possible values, remove them from all other possible value arrays in the square/row/column.

    e.g. if a row contains three unfilled cells with possible values (1, 2), (1, 2), (1, 3), the third cell can be reduced to (3) and thus filled in. The reason for this is that since the first two cells must collectively hold values 1 & 2, it's impossible for the third to cell to have value 1, so it's only possible value is 3.
"""
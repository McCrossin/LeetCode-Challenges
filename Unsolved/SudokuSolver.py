class Solution:
    

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def uniqueElements(lst):
            freq = {}
            for x in lst:
                if x in freq:
                    freq[x] += 1
                else:
                    freq[x] = 1
            return [x for x in freq if freq[x] == 1]
        
        dict = {
            #dict items are keyed as i*9 + j
        }
        potentialNumbers = ["1","2","3","4","5","6","7","8","9"]

        loopNumber = 1
        while any("." in sublist for sublist in board):
            
            allColumnValues = []

            for i in range(len(board)):
                
                allRowValues = []
                allBoxValues = []

                for j in range(len(board[i])):
                    dictIndex = i*9 + j
                    
                    #Only check cells that have an unknown value
                    if board[i][j] == ".":
                        if dictIndex not in dict:
                            dict.update({dictIndex:potentialNumbers.copy()})
                    
                        #First check all possible values for each cell in a row
                        if len(dict[dictIndex]) != 1:
                            for rowIndex in range(len(board[i])):
                                currentIndex = i*9 + rowIndex
                                if board[i][rowIndex] in dict[dictIndex]:
                                    del dict[dictIndex][dict[dictIndex].index(board[i][rowIndex])]

                            
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
                                currentIndex = rowIndex*9 + boxIndex
                                if board[rowIndex][boxIndex] in dict[dictIndex]:
                                    del dict[dictIndex][dict[dictIndex].index(board[rowIndex][boxIndex])]
                                elif loopNumber > 0 and (j%3 == 0) and  currentIndex in dict :
                                    for val in dict[currentIndex]:
                                        allBoxValues.append(val)
                                
                                boxIndex += 1
                                if (box%3) == 0:
                                    boxIndex -= 3
                                    rowIndex += 1
                            
                            #Third check all possible values for each cell in a column
                            for column in range(0,9):
                                currentIndex = column*9 + j
                                if board[column][j] in dict[dictIndex]:
                                    del dict[dictIndex][dict[dictIndex].index(board[column][j])]

                            #reset row Index to the first row
                            rowIndex -=3

                            """Next we need to check for any duplicate possibilities
                            e.g. if there is a 1,2 pair in row i, then no other cells in that row
                            can be a 1 or a 2, remove that possibility from all the other cells.
                            Storing all the values for use later when we check duplicates
                            """
                            if len(dict[dictIndex]) == 2:
                                for checkPairsRow in range(len(board[i])):
                                    currentIndex = i*9 + checkPairsRow
                                    if currentIndex != dictIndex and board[i][checkPairsRow] == dict[dictIndex]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if currentIndex != duplicateIndex and currentIndex != dictIndex:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dictIndex][0] or val == dict[dictIndex][1]:
                                                        dict[currentIndex].remove(val)
                                                    

                                for checkPairsBox in range(1, 10):
                                    currentIndex = rowIndex*9 + boxIndex
                                    if currentIndex != dictIndex and board[rowIndex][boxIndex] == dict[dictIndex]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if len(dict) != 0 and currentIndex != duplicateIndex and currentIndex != dictIndex:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dictIndex][0] or val == dict[dictIndex][1]:
                                                        dict[currentIndex].remove(val)
                                    
                                    boxIndex += 1
                                    if (checkPairsBox%3) == 0:
                                        boxIndex -= 3
                                        rowIndex += 1

                                rowIndex -=3

                                for n in range(0,9):
                                    currentIndex = n*9 + j
                                    if currentIndex != dictIndex and board[n][j] == dict[dictIndex]:
                                        duplicateIndex = currentIndex
                                        currentIndex = currentIndex - (currentIndex%9)
                                        for currentIndex in range (currentIndex, currentIndex+9):
                                            if len(dict) != 0 and currentIndex != duplicateIndex and currentIndex != dictIndex:
                                                for val in dict[currentIndex]:
                                                    if val == dict[dictIndex][0] or val == dict[dictIndex][1]:
                                                        dict[currentIndex].remove(val)

                            if (i+1)%3 == 0 and (j+1)%3 == 0:
                                rowNum = i - 2
                                boxNum = j - 2
                                for loopNum in range (1, 10):
                                    currentIndex = rowNum * 9 + boxNum
                                    if currentIndex in dict:
                                        for val in dict[currentIndex]:
                                            allBoxValues.append(val)
                                        if loopNum%3 == 0:
                                            rowNum += 1
                                            boxNum -= 2
                                        else:
                                            boxNum += 1

                                uniqueBoxValues = uniqueElements(allBoxValues)     
                                if len(uniqueBoxValues) > 0:
                                    for val in uniqueBoxValues:
                                        rowNum = i - 2
                                        boxNum = j - 2
                                        for loopNum in range (1,10):
                                            currentIndex = rowNum*9 + boxNum
                                            if currentIndex in dict:
                                                if val in dict[currentIndex]:
                                                    dict[currentIndex].remove(val)

                                                if loopNum%3 == 0:
                                                    rowNum += 1
                                                    boxNum -= 2
                                                else:
                                                    boxNum += 1
                            if i == 8:
                                for rowNum in range (0, 9):
                                    currentIndex = rowNum * 9 + j
                                    if currentIndex in dict:
                                        for val in dict[currentIndex]:
                                            allColumnValues.append(val)
                                    
                                uniqueColumnValues = uniqueElements(allColumnValues)  
                                if len(uniqueColumnValues) > 0:
                                    for val in uniqueColumnValues:
                                        for rowNum in range (0,9):
                                            currentIndex = rowNum*9 + j
                                            if currentIndex in dict:
                                                if val in dict[currentIndex]:
                                                    dict[currentIndex].remove(val)

                                
                            if len(dict) != 0 and len(dict[dictIndex]) == 1:
                                board[i][j] = dict[dictIndex][0]
                                del dict[dictIndex]
                                    
                            if dictIndex in dict:
                                for val in dict[dictIndex]:
                                    allRowValues.append(val)
                            
                            

        #Check if any of the possible values in the remaining cells are unique
        #print (allRowValues) 
            uniqueRowValues = uniqueElements(allRowValues)

            if len(uniqueRowValues) > 0: 
                for val in uniqueRowValues:
                    for n in range (0,9):
                        currentIndex = i*9 + n
                        if currentIndex in dict:
                            if val in dict[currentIndex]:
                                dict[currentIndex].remove(val)
            

        
        loopNumber +=1

        print(board)


                    

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
Solution().solveSudoku(board)
"""Go through every square, row and column and look for groups of possible values which are the same. If any of these groups have the same size as their amount of possible values, remove them from all other possible value arrays in the square/row/column.

    e.g. if a row contains three unfilled cells with possible values (1, 2), (1, 2), (1, 3), the third cell can be reduced to (3) and thus filled in. The reason for this is that since the first two cells must collectively hold values 1 & 2, it's impossible for the third to cell to have value 1, so it's only possible value is 3.
"""
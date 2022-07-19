from itertools import product

board = [4,3]
snake =  [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3

def getCoordinatesFromBoard(board):
    xAxis =  list(range(0,board[0]))
    yAxis = list(range(0,board[1]))

    listCoordinates = []
    for x in xAxis:
        for y in yAxis:
            listCoordinates.append([x , y])
    return listCoordinates

def combinationIsValid(board, snake, combination):

    # Based on the combination the snake wants to make
    # and its current state in the board
    # we determine if the result falls into one of the two restrictions

    # First step will be to make the move to then check if it is valid

    
    print('checking snake',snake)
    print('for move',combination)
    for move in list(combination):

        if move == 'L':
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][0] = snake[0][0] - 1

        if move == 'R':
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][0] = snake[0][0] + 1

        if move == 'U':
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][1] = snake[0][1] - 1

        if move == 'D':
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][1] = snake[0][1] + 1

        # Checking if this move is permitted:
        # First restriction is that the head can not bite any part of the body
        print('post move ',move, 'snake is defined as',snake)
        for partOfBody in snake[1:]:# Iterates over the whole body of the snake except for the head
            if partOfBody == snake[0]:
                #Forbidden: Snake is biting itself
                print('Snake is biting itself')
                return False  
                
        # Second restriction is that the snake may not get away from the board
        # If this happened, the head would be the first part to get there.

        # We need to first get all possible coordinates within the board
        everyCoordinateinBoard = getCoordinatesFromBoard(board)
        # Now, check if the snake's head is not in any of those, which would be a violation.
        if snake[0] not in everyCoordinateinBoard: # Snake's head is inside the borders
            print('Snake out the board')
            return False
        else: # Snake's head is in the board
            continue
            

def getPossibleMoveCombinations(board,snake,depth):
    # Full list of mathematically possible moves, then a function to check which are legal

    # In order to obtain all possible options, we combine LRDU a number 'depth' of times
    # Itertools' product() will provide us this tool

    allCombinations = product('LRUD',repeat = depth)

    # Out of these, we check which ones can be executed.
    validCombinations = []

    for combination in list(allCombinations):
        if combinationIsValid(board, snake[:], combination):
            print('Combination is valid')
            validCombinations.append(combination)

    return validCombinations

def numberOfAvailableDifferentPaths(board, snake, depth):

    #depth's length [1 to 20]
    # TODO: REST HAS TO BE DISCARDED

    # Keep in mind: initial config is always valid 

    print('Result is',len(getPossibleMoveCombinations(board,snake[:],depth)))


numberOfAvailableDifferentPaths(board,snake[:],depth)
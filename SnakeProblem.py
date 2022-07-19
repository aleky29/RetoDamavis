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

    # First step will be to make the move to then check if it is valid.['L','R','U','D']
    for move in combination:
        if move == 'L':
            # Moving snake's head:
            snake[0][0] = snake[0][0] - 1
            # Moving the rest:
            




    # First restriction is that the head can not bite any part of the body
    
    for partOfBody in snake[1:]:# Iterates over the whole body of the snake except for the head
        if partOfBody == snake[0]:
            #Forbidden: Snake is biting itself
            return False

    # Second restriction is that the snake may not get away from the board
    # In case this happened, the head would be the first part to get there.

    # We need to first get all possible coordinates within the board
    everyCoordinateinBoard = getCoordinatesFromBoard(board)
    # Now, check if the snake's head is not in any of those, which would be a violation.
    if snake[0] in everyCoordinateinBoard: # Snake is inside the borders
        return True
    else: # Snake's head is not in the board
        return False






def getPossibleMoveCombinations(possibleMoves,snake,depth):
    #Full list of mathematically available moves, then a list of forbidden ones to discard them

def numberOfAvailableDifferentPaths(board, snake, depth):
    possibleMoves = ['L','R','U','D']
    # We should figure out all of the possible combinations
    # of 'depth' length [1 to 20]
    # TODO: THE REST HAS TO BE DISCARDED
    # then introduce them in a list except for
    # the ones that result in a forbidden state

    #Keep in mind: initial config is always valid 

    getPossibleMoveCombinations(possibleMoves,snake,depth)

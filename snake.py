from itertools import product
import copy, math

board =  [2, 3]
snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
depth = 10
                
def combinationIsValid(board, snake, combination):

    # Based on the combination the snake wants to make
    # and its current state in the board
    # we determine if the result falls into one of the two restrictions

    # First step will be to make the move to then check if it is valid
    print('checking snake',snake)
    print('for move',combination)

    moveCounter = 0

    for move in list(combination):
        moveCounter = moveCounter + 1

        if move == 'L' and snake[0][0] - 1 >= 0:
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][0] = snake[0][0] - 1

        else:
            return False,moveCounter

        if move == 'R' and snake[0][0] + 1 <= board[0] - 1:
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][0] = snake[0][0] + 1

        else:
            return False,moveCounter

        if move == 'U' and snake[0][1] - 1 >= 0:
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][1] = snake[0][1] - 1

        else:
            return False,moveCounter


        if move == 'D' and snake[0][1] + 1 <= board[1] - 1:
            # Moving snake's body:
            for i in range(1,len(snake)):
                snake[-i] = snake[-i-1][:]

            # Moving snake's head:
            snake[0][1] = snake[0][1] + 1

        else:
            return False,moveCounter
        # Checking if this move is permitted:
        # First restriction is that the head can not bite any part of the body
        print('post move ',move, 'snake is defined as',snake)
        if snake[0] in snake[1:]:
            print('Snake looped')
            return False,moveCounter
        # for partOfBody in snake[1:]:# Iterates over the whole body of the snake except for the head
        #     if partOfBody == snake[0]:
        #         #Forbidden: Snake is biting itself
        #         print('Snake is biting itself')
        #         return False  
                
        # Second restriction is that the snake may not get away from the board
        # If this happened, the head would be the first part to get there.

        # # We need to first get all possible coordinates within the board
        # everyCoordinateinBoard = getCoordinatesFromBoard(board)
        # # Now, check if the snake's head is not in any of those, which would be a violation.
        # if snake[0] not in everyCoordinateinBoard: # Snake's head is outside the borders
        #     print('Snake out the board')
        #     return False

        if snake[0][0] < 0 or snake[0][1] < 0 or snake[0][0] > board[0] - 1 or snake[0][1] > board[1] - 1:
            print('snake out of bounds')
            return False,moveCounter
        else: # Snake's head is in the board
            continue

    return True,moveCounter

def getPossibleMoveCombinations(board, snake, depth):
    # Full list of mathematically possible moves, then a function to check which are legal

    # In order to obtain all possible options, we combine LRDU a number 'depth' of times
    # Itertools' product() will provide us this tool

    unfilteredAllCombinations = list(product('LRUD',repeat = depth))
    
    # Out of these, we check which ones can be executed.
    validCombinations = []

    # We make a blacklist with all the obvious impossible moves such as any consecutive
    # opposites (LR , UD) and any that goes in the same direction more than the size of the table
    allCombinations = []
    
    for combination in unfilteredAllCombinations:
        combString = ''.join(combination)
        if 'LR' not in combString and 'RL' not in combString and 'UD' not in combString and 'DU' not in combString:
            allCombinations.append(combination)

    blackListMoves = []

    i = 0
    for combination in allCombinations:
        i = i+1

        if len(blackListMoves) == 0:
            num_max = 0
        else:
            num_max = len(max(blackListMoves, key=len))

        if combination[0:num_max] not in blackListMoves:
            (isValid, movesMade) = combinationIsValid(board, copy.deepcopy(snake), combination)

        if isValid:

            print('Combination is valid')
            validCombinations.append(combination)
            

        elif combination[0:movesMade] not in blackListMoves:
            print('adding to BL',combination[0:movesMade])
            blackListMoves.append(combination[0:movesMade])


    return validCombinations

def numberOfAvailableDifferentPaths(board, snake, depth):

    #depth's length [1 to 20]
    # TODO: REST HAS TO BE DISCARDED

    # Keep in mind: initial config is always valid 
    
    print('Result is',len(getPossibleMoveCombinations(board,snake[:],depth)))


numberOfAvailableDifferentPaths(board,snake[:],depth)
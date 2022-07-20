from itertools import product
import copy

board =  [10, 10]
snake =    [[5,5], [5,4], [4,4], [4,5]]
depth = 4

def combinationIsValid(board, snake, combination):

    # Based on the combination the snake wants to make
    # and its current state in the board
    # we determine if the result falls into one of the two restrictions

    # First step will be to make the move to then check if it is valid
    print('checking snake',snake)
    print('for combination',combination)
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

        for partOfBody in snake[1:]:# Iterates over the whole body of the snake except for the head
            if partOfBody == snake[0]:
                #Forbidden: Snake is biting itself
                print('Snake is biting itself')
                return False  
                
        # Second restriction is that the snake may not get away from the board
        # If this happened, the head would be the first part to get there.

        if snake[0][0] < 0 or snake[0][1] < 0 or snake[0][0] > board[0] - 1 or snake[0][1] > board[1] - 1:
            print('Snake out of bounds')
            return False
        else: # Snake's head is in the board
            continue

    return True

def getPossibleMoveCombinations(board, snake, depth):
    # Full list of mathematically possible moves, then a function to check which are legal

    # In order to obtain all possible options, we combine LRDU a number 'depth' of times
    # Itertools' product() will provide us this tool

    unfilteredAllCombinations = list(product('LRUD',repeat = depth))

    allCombinations = []

    for combination in unfilteredAllCombinations:

        combString = ''.join(combination)
        if 'LR' not in combString and 'RL' not in combString and 'UD' not in combString and 'DU' not in combString:
            allCombinations.append(combination)

    # Out of these, we check which ones can be executed.
    validCombinations = []
    for combination in list(allCombinations):
        if combinationIsValid(board, copy.deepcopy(snake), combination):
            print('Combination is valid')
            validCombinations.append(combination)

    return validCombinations

def numberOfAvailableDifferentPaths(board, snake, depth):

    if depth > 1 and depth < 20:
        return len(getPossibleMoveCombinations(board,snake[:],depth))
    else:
        raise ValueError


r = numberOfAvailableDifferentPaths(board,snake[:],depth)
print('There are',r,'different valid paths')
print('Modulo solution is',r % 10e9 + 7)
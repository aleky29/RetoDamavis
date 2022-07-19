board = [4,3]
snake =  [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3

def combinationIsValid(board, snake, combination):
    #Based on the combination the snake wants to make
    # and its current state in the board
    # we determine if the result falls into one of the two restrictions
    for partOfBodyA in snake:
        for partOfBodyB in snake:
            if partOfBodyA == partOfBodyB:
                #Forbidden: Two elements collide
                return False




def getPossibleMoveCombinations(possibleMoves,snake,depth):
    #Full list of mathematically available moves, then a list of forbidden ones to discard them

def numberOfAvailableDifferentPaths(board, snake, depth):
    possibleMoves = ['L','R','U','D']
    # We should figure out all of the possible combinations
    # of 'depth' length [1 to 20]
    # then introduce them in a list except for
    # the ones that result in a forbidden state

    #Keep in mind: initial config is always valid 

    getPossibleMoveCombinations(possibleMoves,snake,depth)

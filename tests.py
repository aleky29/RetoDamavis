l = ['LURD','LLLLURD','LURDD','LUUUURD','LUUDR','RUU']
lFiltered = []
board = [3,3]
snake = [[1,2], [0,2], [0,1], [0,0]]

# Desde la posición de la cabeza, restringimos todos aquellos strings que lleven fuera de la tabla

marginL = snake[0][0]
marginR = (board[0] - 1) - snake[0][0]
marginU = snake[0][1]
marginD = (board[1] - 1) - snake[0][1]

# Construimos strings inválidos
stringLs = ''
stringRs = ''
stringUs = ''
stringDs = ''

for i in range(marginL + 1):
    
    stringLs += 'L'

for i in range(marginR + 1):
    
    stringRs += 'R'

for i in range(marginU + 1):

    stringUs += 'U'

for i in range(marginD + 1):

    stringDs += 'D'

print(stringUs)

for combination in l:
    if stringLs not in combination and stringDs not in combination and stringRs not in combination and stringUs not in combination:
        lFiltered.append(combination)

print(lFiltered)
l = [[2,2],[1,2],[0,2],[0,1],[0,0],[1,0]]

# Movemos el resto del cuerpo

for i in range(1,len(l)):
    
    l[-i] = l[-i-1]

# Movemos la cabeza
l[0]= [2,1]

print(l)
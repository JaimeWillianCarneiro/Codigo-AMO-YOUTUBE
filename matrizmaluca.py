n, m , p = [int(i) for i in input().split()]


matriz  = [[int(i) for i in input().split()] for _ in range(n)]

pontosEnzo = 0 
pontosLobo = 0 

for partida in range(1, p+1):
    pontos = 0 
       
    l, c = map(int, input().split())
    l-=1
    c-=1
    
    
    # Somando os valores da linha
    for i in range(m):
        
        pontos+= matriz[l][i]
        matriz[l][i] = 0 

    # Somando os valores da coluna
    for  j in range(n):
        pontos += matriz[j][c]
        
        matriz[j][c] = 0 
    
    if partida%2==1:
        pontosEnzo+=pontos
    else:
        pontosLobo+=pontos
      
        

if pontosEnzo > pontosLobo:
    print("Enzo")
elif pontosEnzo == pontosLobo:
    print("Empate")


else:
    print("Lobo")
    
    
    
        
    
    
       
    
    

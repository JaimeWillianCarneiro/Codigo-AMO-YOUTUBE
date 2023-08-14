n = int(input())

# compreensão da lista de entradas (matriz)
tabuleiro = [ [int(i) for i in input().split()] for _ in range(n) ]

# Percorrendo as linhas
for linha in range(1, n):
    #percorrendo as colunas
    for coluna in range(1, n):
        # salvando a casa vazia
        # vazia = tabuleiro[linha][coluna]
        
        
        #Salvar as vizinhas
        
        vizinhas = [tabuleiro[linha][coluna-1], tabuleiro[linha-1][coluna], tabuleiro[linha-1][coluna-1]]
        

       # analise das vizinhas
        # se o numero de vizinhas brancas for maior       
        if vizinhas.count(0) > vizinhas.count(1):
            tabuleiro[linha][coluna] =1
        
        # O numero de pretas é maior    
        else:
            tabuleiro[linha][coluna] = 0 




print(tabuleiro[n-1][n-1])



        


            
            
            
    
        

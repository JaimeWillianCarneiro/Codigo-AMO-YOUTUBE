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
        
        vizinhas = [tabuleiro[linha][coluna-1], tabuleiro[linha-1][coluna], tabuleiro[linha-1][coluna]]
        

        # Analisar as vizinhas e ver quem está em maior quantidade
        
        
        
        # Se o numero de pedras brancas for maior que pretas:
        # 0 --> pedra branca
        # 1 --> pedra preta
        if vizinhas.count(0) > vizinhas.count(1):
             tabuleiro[linha][coluna] = 1
        
        # Se o numero de pedras brancas for menor que pretas:
        else:
            tabuleiro[linha][coluna] = 0
            
            
            
    
        
        
        
e, d = map(int, input().split())

esquerda = [int(i) for i in input().split()]
direita =  [int(i) for i in input().split()]


l = 0 
r = d-1


anilhasRetiradas = 0 

somaDireita = sum(direita)
somaEsquerda = sum(esquerda)



while True:
    if somaEsquerda == somaDireita:
        break   
    else:
        
        if somaEsquerda > somaDireita:
            somaEsquerda -=esquerda[l]
            
            l+=1
            anilhasRetiradas+=1
            
        else:
            somaDireita-=direita[r]
            
            anilhasRetiradas+=1
            r-=1

print(anilhasRetiradas)


            
            
"""
Contas a Pagar OBI 2023 Fase 1, Nível 2 e Senior, Modalidade Programação


"""
v = int(input())
a = int(input())
f = int(input())
p = int(input())


maiorNumero = 0 

dividas = [a, f, p]
dividas = sorted(dividas)


if sum(dividas) <=v:
    maiorNumero = 3

else:
    if v < dividas[0]:
        maiorNumero = 0 
    elif v >= sum(dividas[0:2]):
        maiorNumero = 2
    else:
        maiorNumero =1
        
    
print(maiorNumero)

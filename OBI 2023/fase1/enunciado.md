# Contas a Pagar

Vô João está aposentado, tem boa saúde, mas a vida não está fácil. Todo mês é um sufoco para conseguir pagar as contas! Ainda bem que ele é muito amigo dos donos das lojas do bairro, e eles permitem que ele fique devendo.

Depois de pagar aluguel, conta de luz, conta de água, conta do telefone celular e conta do mercado, Vô João ainda tem que pagar as contas do Açougue, da Farmácia e da Padaria.

Dados o valor que Vô João tem disponível e o valor das contas do Açougue, Farmácia e Padaria, escreva um programa para determinar quantas contas, entre as três que ainda não foram pagas, Vô João consegue pagar.

## **Entrada**

~~~python

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

~~~

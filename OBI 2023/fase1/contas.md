# Contas a Pagar :computer:

Vô João está aposentado, tem boa saúde, mas a vida não está fácil. Todo mês é um sufoco para conseguir pagar as contas! Ainda bem que ele é muito amigo dos donos das lojas do bairro, e eles permitem que ele fique devendo.

Depois de pagar aluguel, conta de luz, conta de água, conta do telefone celular e conta do mercado, Vô João ainda tem que pagar as contas do Açougue, da Farmácia e da Padaria.

Dados o valor que Vô João tem disponível e o valor das contas do Açougue, Farmácia e Padaria, escreva um programa para determinar quantas contas, entre as três que ainda não foram pagas, Vô João consegue pagar.

## **Entrada**
A entrada contém quatro linhas. A primeira linha contém um inteiro **V** , o valor que Vô João tem disponível para pagar as contas. A segunda linha contém um inteiro **A**, o valor da conta do Açougue.
A terceira linha contém um inteiro **F**, o valor da conta da Farmácia. A quarta linha contém um inteiro P, o valor da conta da Padaria.


## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o maior número de contas que Vô João consegue pagar.

## Restrições

* $` 0 \leq V \leq 2000`$
* $` 1 \leq A \leq 1000`$
* $` 1 \leq F \leq 1000 `$
* $` 1 \leq P \leq 1000 `$

<details>

<summary>Clique para observar a solução</summary>

## Solução em python
#### por [Jaime Willian Carneiro da Silva ](https://github.com/JaimeWillianCarneiro/)


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


</details>

# Gohan, Feijão e Média

Hassui e Pedra estavam discutindo se comer arroz japonês (gohan) com feijão era moralmente aceitável ou não. Hassui defendia que era aceitável. Pedra defendia que não era aceitável. Para decidir esse impasse, vão comparar a média das 
N notas que tiraram na escola. Quem tiver uma média maior ganha a discussão. Se as duas médias forem iguais, o impasse continua. Nesse problema, estamos usando a média aritmética: $` \frac{ a_1 + a_2 + ... + a_n}{n} `$.

## Entrada
A primeira linha contém um inteiro $`N`$, a quantidade de notas.
As próximas $`N`$ linhas contém 2 inteiros: $`P_i`$ e $`H_i`$, a i-ésima nota da Pedra e do Hassui, respectivamente.
​
 ## Saída 

 Imprima exatamente 1 linha: ":0 <- Gohan e Feijao", se a média do Hassui for maior, ":0 <-X- Gohan e Feijao", se a média da Pedra for maior e "Impasse" se as duas médias forem iguais. Imprima a resposta sem as aspas.

 ## Restrições

*  $`1 \leq N \leq 100`$
*  $`0 \leq P_i, H_i \leq 10^{15}`$





<details>

<summary>Casos de teste</summary>

### Exemplo 1 


**Entrada**
~~~python
4
1 2
2 3
3 4
4 5
~~~


**Saída** 
~~~python
:0 <- Gohan e Feijao
~~~


### Exemplo 2 

**Entrada**
~~~python
2
1 1
1 1
~~~


**Saída** 
~~~python
Impasse
~~~

### Exemplo 3

**Entrada**
~~~python
2
1 1
5 1
~~~


**Saída** 
~~~python
:0 <-X- Gohan e Feijao
~~~



</details>
<details>

<summary>Solução em Python</summary>

#### por [Jaime Willian Carneiro da Silva ](https://github.com/JaimeWillianCarneiro/)
~~~python
n = int(input())

notas = [[int(i) for i in input().split()] for _ in range(n)] 


NotaPedro = 0 
NotaHassum = 0 


for nota in notas:
    # print(nota)
    NotaPedro +=nota[0] # Notass de Pedro
    NotaHassum += nota[1]# nota de hassum
        


if NotaPedro < NotaHassum:
    print(":0 <- Gohan e Feijao")
elif NotaPedro == NotaHassum:
    print("Impasse")
else:
    print(":0 <-X- Gohan e Feijao")
    
~~~

</details>










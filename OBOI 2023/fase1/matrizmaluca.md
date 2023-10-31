# Matriz Maluca 

Enzo e Lobo criaram um jogo chamado Matriz Maluca, o qual funciona da seguinte maneira:

Em uma matriz $`n×m`$  preenchido com números inteiros, os jogadores realizam a seguinte jogada alternadamente: o jogador escolhe uma casa $`(i,j)`$ , soma todos os números que estão na mesma coluna e na mesma linha que  $`(i,j)`$ (dando um valor $`x`$), e transforma todos esses números em 0. Nessa jogada, ele ganha $`x`$pontos, e passa o turno para o próximo jogador. Enzo começa.

Obs:  $`(i,j)`$ representa a posição na 

Veja o caso abaixo


![**FIGURA1**](https://github.com/JaimeWillianCarneiro/Codigo-AMO-YOUTUBE/blob/main/images/imagem1_matriz_maluca.png)

Enzo começa jogando na casa  $`(2,2)`$, então, ele ganha  $`(7+6+2+3+2+5+3=28)`$ pontos nessa jogada, e o tabuleiro fica assim: (Veja que o valor de $`(i,j)`$ só é contado uma vez na soma).


![**FIGURA2**](https://github.com/JaimeWillianCarneiro/Codigo-AMO-YOUTUBE/blob/main/images/imagem2_matriz_maluca.png)


Então, Lobo joga na casa $`(1,4)`$ (canto superior direito) e ganha $`5+0+7+6+0+9+0=27`$ pontos. E assim o jogo continua.

Mas Enzo e Lobo estão muito cansados de fazer tantas somas quando vão jogar esse jogo. Ainda assim, eles não conseguem parar de jogar, e por isso eles pediram a sua ajuda!

Dado o tabuleiro no começo do jogo e as jogadas que eles fizeram, escreva um código que diga quem ganhou o jogo, ou seja, quem fez mais pontos.

## Entrada

Na primeira linha, temos 3 inteiros, $`N,M, P (1 \leq N, M, P\leq 20)`$, onde $`N`$ é a largura da matriz, $`M`$ é o comprimento e $`P`$ é quantidade de jogadas (É garantido que $`P`$​ é sempre par).

Depois disso, temos $`N`$ linhas, cada uma com $`M`$, representando a matriz $`V`$ que eles começaram jogando $`0 \leq V_(i,j) \leq 100 `$

Por último, temos $`P`$ linhas. na $`i`$-ésima dessas linhas, vamos ter 2 valores $`l_i, c_i, (1 \leq l_i \leq N, 1 \leq c_i \leq M) `$ que representa a posição da jogada do jogador atual, ou seja, ele jogou na posição $`(l_i,c_i) `$ ($`(l_i`$-ésima linha e $`c_i`$ésima coluna). Perceba que as jogadas nas linhas ímpares são as de Enzo, enquanto as da linhas pares são as de Lobo. 


## Saída 

Imprima uma palavra, representando quem ganhou. Imprima "Enzo" se foi Enzo que ganhou, imprima "Lobo" se foi Lobo que ganhou, e imprima "Empate" se o jogo empatar.

<details>

<summary>Casos de teste</summary>

### Exemplo 1 


**Entrada**
~~~python
4 4 2
5 2 7 6
7 6 2 3
6 5 1 9
3 3 9 0
2 3
4 4
~~~


**Saída** 
~~~python
Enzo
~~~


### Exemplo 2 

**Entrada**
~~~python
2 3 2
1 1 2
2 2 7
1 2
2 1
~~~


**Saída** 
~~~python
Lobo
~~~

### Exemplo 3

**Entrada**
~~~python
4 4 4
0 0 0 0
0 0 0 0
0 0 0 0 
0 0 0 0
1 1
2 2
3 3
4 4
~~~


**Saída** 
~~~python
Empate
~~~



</details>





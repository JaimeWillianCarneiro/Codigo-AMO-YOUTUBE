# Matriz Maluca 

Enzo e Lobo criaram um jogo chamado Matriz Maluca, o qual funciona da seguinte maneira:

Em uma matriz $`n×m`$  preenchido com números inteiros, os jogadores realizam a seguinte jogada alternadamente: o jogador escolhe uma casa $`(i,j)`$ , soma todos os números que estão na mesma coluna e na mesma linha que  $`(i,j)`$ (dando um valor $`x`$), e transforma todos esses números em 0. Nessa jogada, ele ganha $`x`$pontos, e passa o turno para o próximo jogador. Enzo começa.

Obs:  $`(i,j)`$ representa a posição na 

Veja o caso abaixo


![**FIGURA1**](https://github.com/JaimeWillianCarneiro/Codigo-AMO-YOUTUBE/blob/main/images/imagem1_matriz_maluca.png)

Enzo começa jogando na casa  $`(2,2)`$, então, ele ganha  $`(7+6+2+3+2+5+3=28)`$ pontos nessa jogada, e o tabuleiro fica assim: (Veja que o valor de $`(i,j)`$ só é contado uma vez na soma).


![**FIGURA2**](https://github.com/JaimeWillianCarneiro/Codigo-AMO-YOUTUBE/blob/main/images/imagem2_matriz_maluca.png)



## Entrada
A primeira linha contém um inteiro $`N`$, a quantidade de notas.
As próximas $`N`$ linhas contém 2 inteiros: $`P_i`$ e $`H_i`$, a i-ésima nota da Pedra e do Hassui, respectivamente.
​
 ## Saída 

 Imprima exatamente 1 linha: ":0 <- Gohan e Feijao", se a média do Hassui for maior, ":0 <-X- Gohan e Feijao", se a média da Pedra for maior e "Impasse" se as duas médias forem iguais. Imprima a resposta sem as aspas.

 ## Restrições

*  $`1 \leq N \leq 100`$
*  $`0 \leq P_i, H_i \leq 10^{15}`$





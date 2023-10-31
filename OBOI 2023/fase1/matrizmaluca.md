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

Na primeira linha, temos 3 inteiros, $`N,M, P (1 \leq N, M, P\leq 20)`$

​
 ## Saída 

 Imprima exatamente 1 linha: ":0 <- Gohan e Feijao", se a média do Hassui for maior, ":0 <-X- Gohan e Feijao", se a média da Pedra for maior e "Impasse" se as duas médias forem iguais. Imprima a resposta sem as aspas.

 ## Restrições

*  $`1 \leq N \leq 100`$
*  $`0 \leq P_i, H_i \leq 10^{15}`$





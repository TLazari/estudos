Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/03/2025
Var
// Se��o de Declara��es das vari�veis 
listaEntrada : vetor [1..6] de inteiro
entrada,i : inteiro

Inicio

i <- 1

escreva ("Digite os n�meros: ")
para i de 1 ate 6 fa�a
         leia (entrada)
         listaEntrada [i] <- entrada
fimpara

escreva ("A lista invertida �:")
i <- 1
para i de 6 ate 1 passo -1 fa�a
         se i = 1 entao
            escreva (listaEntrada[i],"!")
            sen�o
            escreva (listaEntrada [i], ",")
         fimse
fimpara


Fimalgoritmo
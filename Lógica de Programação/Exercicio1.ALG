Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/03/2025
Var
// Se��o de Declara��es das vari�veis 


listaEntrada : vetor [1..10] de inteiro
entrada,i : inteiro

Inicio

i <- 1
escreva ("Digite um n�mero 10x:")

Enquanto i < 10 fa�a
         leia (entrada)
         se (entrada % 2 = 0) entao
            listaEntrada[i] <- entrada
         fimse
         i <- i+1
Fimenquanto
i <- 1

Enquanto i <10 fa�a
         se (listaEntrada[i]) <> 0 entao
            escreva (listaEntrada[i],",")
            i<- i + 1
            
         sen�o
              i<- i + 1
         fimse
Fimenquanto



Fimalgoritmo
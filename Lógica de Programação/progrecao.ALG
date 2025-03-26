Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/03/2025
var

cont: inteiro
vet: vetor [1..10] de inteiro


inicio

para cont de 1 ate 10 faça
     se (cont=1) entao
      vet[cont] <- cont
      senao
         vet[cont] <- vet[cont-1]+cont
      fimse
      escreval ("vet[",cont,"]:",vet[cont])
fimpara


fimalgoritmo
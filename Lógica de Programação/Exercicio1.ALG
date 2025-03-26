Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/03/2025
Var
// Seção de Declarações das variáveis 


listaEntrada : vetor [1..10] de inteiro
entrada,i : inteiro

Inicio

i <- 1
escreva ("Digite um número 10x:")

Enquanto i < 10 faça
         leia (entrada)
         se (entrada % 2 = 0) entao
            listaEntrada[i] <- entrada
         fimse
         i <- i+1
Fimenquanto
i <- 1

Enquanto i <10 faça
         se (listaEntrada[i]) <> 0 entao
            escreva (listaEntrada[i],",")
            i<- i + 1
            
         senão
              i<- i + 1
         fimse
Fimenquanto



Fimalgoritmo
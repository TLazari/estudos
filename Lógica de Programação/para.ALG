Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/03/2025
Var
// Seção de Declarações das variáveis 
listaEntrada : vetor [1..6] de inteiro
entrada,i : inteiro

Inicio

i <- 1

escreva ("Digite os números: ")
para i de 1 ate 6 faça
         leia (entrada)
         listaEntrada [i] <- entrada
fimpara

escreva ("A lista invertida é:")
i <- 1
para i de 6 ate 1 passo -1 faça
         se i = 1 entao
            escreva (listaEntrada[i],"!")
            senão
            escreva (listaEntrada [i], ",")
         fimse
fimpara


Fimalgoritmo
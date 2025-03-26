Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/03/2025
Var
// Seção de Declarações das variáveis 
nota1,nota2,nota3 : inteiro
media : real


Inicio

escreva ("Escrevas as notas: ")

leia (nota1,nota2,nota3)

media <- (nota1 + nota2 + nota3)/3

escreva ("a média é de: ", media)


se (media > 5) então
   escreva (", o aluno foi aprovado")
           senao
           escreva (", o aluno foi reprovado")
fimse



// Seção de Comandos, procedimento, funções, operadores, etc... 


Fimalgoritmo
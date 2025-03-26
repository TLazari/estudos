Algoritmo "Gerador Senha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/03/2025
Var

alfabeto: vetor[1..41] de caractere
letras: vetor[1..100] de caractere
entrada,i, indice,tamanho : inteiro
texto : caractere

Inicio


// Faz o alfabeto dentro da variavel alfabeto []
i <- 97
para i de 97 ate 122 faça
     alfabeto[i-96] <- carac (i)
     escreva (alfabeto[i-96]," ")
fimpara
// fim alfabeto

escreval ("Digite a senha que deseja criptografar:")
leia (texto)

tamanho <- compr(texto)

para i de 1 ate tamanho faça


escreval ("O tamanho do texto é",tamanho)


Fimalgoritmo
Algoritmo "Gerador Senha"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
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
para i de 97 ate 122 fa�a
     alfabeto[i-96] <- carac (i)
     escreva (alfabeto[i-96]," ")
fimpara
// fim alfabeto

escreval ("Digite a senha que deseja criptografar:")
leia (texto)

tamanho <- compr(texto)

para i de 1 ate tamanho fa�a


escreval ("O tamanho do texto �",tamanho)


Fimalgoritmo
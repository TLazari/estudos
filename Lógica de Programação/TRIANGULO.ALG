Algoritmo "Triangulo"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/03/2025
Var
// Se��o de Declara��es das vari�veis 
A,B,C : inteiro

inicio
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)

se (A + B > C) e (A + C > B) e (B + C > A) entao
        se (A = B) e (B = C) entao
            escreval("Tri�ngulo Equil�tero")
        senao
            se (A = B) ou (B = C) ou (A = C) entao
                escreval("Tri�ngulo Is�sceles")
            senao
                escreval("Tri�ngulo Escaleno")
            fimse
        fimse
    senao
        escreval("Tri�ngulo inv�lido.")
    fimse

Fimalgoritmo




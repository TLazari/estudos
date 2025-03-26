Algoritmo "Triangulo"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/03/2025
Var
// Seção de Declarações das variáveis 
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
            escreval("Triângulo Equilátero")
        senao
            se (A = B) ou (B = C) ou (A = C) entao
                escreval("Triângulo Isósceles")
            senao
                escreval("Triângulo Escaleno")
            fimse
        fimse
    senao
        escreval("Triângulo inválido.")
    fimse

Fimalgoritmo




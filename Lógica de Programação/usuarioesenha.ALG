Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/03/2025
Var

usuario,senha : caracter

Inicio

escreva ("Escreva o usuário:")
leia (usuario)

escreva ("Insira a senha:")
leia (senha)

se (usuario = "admin") e (senha = "admin") entao
   escreva ("Acesso Liberado")
fimse

se (usuario <> "admin") ou (senha<> "admin") entao
   escreva ("Usuário ou senha incorreto")
fimse


Fimalgoritmo
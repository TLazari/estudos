Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/03/2025
Var

usuario,senha : caracter

Inicio

escreva ("Escreva o usu�rio:")
leia (usuario)

escreva ("Insira a senha:")
leia (senha)

se (usuario = "admin") e (senha = "admin") entao
   escreva ("Acesso Liberado")
fimse

se (usuario <> "admin") ou (senha<> "admin") entao
   escreva ("Usu�rio ou senha incorreto")
fimse


Fimalgoritmo
Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/03/2025
Var

A, B, C, X1, X2, delta, resultado : real

Inicio

// A*x^2 + B^2 + C

Escreva ("Insira o coeficiente A:")
Leia (A)
se A > 0 entao
   Escreva ("Insira o coeficiente B:")
   Leia (B)
   Escreva ("Insira o coeficiente C:")
   Leia (C)

   delta <- ((b^2) - (4*A*C))

   x1 <- ((-b + raizq(delta))/(2*a))
   x2 <- ((-b - raizq(delta))/(2*a))

   Escreva ("o valor de x1 � ", x1," e x2 � ", x2)
   
sen�o A <= 0 entao
   Escreva ("Para uma equa��o de 2� grau, � preciso que A seja maior que 0")
fimse
      

Fimalgoritmo
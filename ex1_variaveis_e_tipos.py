## Lista exercicios variaveis e tipos
##  Exercicio 1
#       Defina as variáveis:
#           nota = 1;
#           peso = 4.3;
#           nota_final = nota * peso.
#       E Mostre o tipo de cada uma das variáveis.
## ->
nota = 1
peso = 4.3
nota_final = nota * peso
print('Tipo nota: ', type(nota))
print('Tipo peso: ', type(peso))
print('Tipo nota_final: ', type(nota_final))
## <-

## Exercicio 2
#       Defina as variáveis
#           dividendo = 1;
#           divisor = 2.
#       E Mostre que a operação dividendo/divisor é diferente de dividendo//divisor.
## ->
dividendo = 1
divisor = 2
resultado_1 = dividendo / divisor
resultado_2 = dividendo // divisor
print('Resultado dividendo / divisor: ', resultado_1)
print('Resultado dividendo // divisor: ', resultado_2)
## <-

## Exercicio 3
#       Sendo nota_1 = 5 e nota_2 = 3, mostre o resultado de nota_1 + nota_2.
#       Agora transforme as variáveis em strings e mostre o resultado da sua soma.
## ->
nota_1 = 5
nota_2 = 3
soma = nota_1 + nota_2
nota_1_em_string = str(nota_1)
nota_2_em_string = str(nota_2)
soma_de_strings = nota_1_em_string + nota_2_em_string
print('Nota 1: ', nota_1)
print('Nota 2: ', nota_2)
print('Soma das notas: ', soma)
print('Soma das notas tranformadas em string: ', soma_de_strings)
## <-

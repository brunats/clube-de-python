## Lista exercicios operadores
##  Exercicio 1
#       Defina as variáveis x = 2, y = 3.0 e z = 8. E verifique se as operações a seguir são verdadeiras ou falsas.
#           x não é igual a 7
#           x é maior que y
#           a divisão de inteiros de y por x é igual a 1
#           a divisão de y por x é igual a 1
#           x elevado ao quadrado é igual a 4
#           z é igual a 9 ou z é menor que 9
#           z é menor ou igual a 9 (implemente de uma maneira diferente da anterior)
#           x é igual a 2 e z é igual a x
## ->
x = 2
y = 3.0
z = 8
print('1: ', x != 7)
print('2: ', x > y)
print('3: ', (y // x) == 1)
print('4: ', (y/x) == 1)
print('5: ', (x**2) == 4)
print('6: ', z == 9 or z < 9)
print('7: ', z <= 9)
print('8: ', x == 2 and z == x)

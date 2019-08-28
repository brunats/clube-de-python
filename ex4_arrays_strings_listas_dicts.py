## Lista exercicios arrays, strings, listas e dicts
##  Exercicio 1
#       Crie duas strings e apresente o tamanho de cada uma;
## ->
frutas = ['Banana', 'Melancia', 'Limao']
cidades = ['Joinville', 'Araquari']
print('Frutas: ', frutas)
print('Cidades: ', cidades)
print('Tamanho da lista de frutas: ', len(frutas))
print('Tamanho da lista de cidades: ', len(cidades))
## <-

##  Exercicio 2
#       Crie uma lista com no mínimo 2 elementos, e atribua as funções insert() e remove();
## ->
frutas = ['Banana', 'Melancia', 'Limao']
print('Frutas: ', frutas)
frutas.insert(1, 'Kiwi')
print('Frutas: ', frutas)
frutas.remove('Limao')
print('Frutas: ', frutas)
## <-

##  Exercicio 3
#       Crie outra lista, e as compare.
## ->
frutas = ['Banana', 'Melancia', 'Limao']
carros = ['Sentra', 'Gol', 'Civic', 'Fluence']
print('Lista de frutas: ', frutas)
print('Lista de carros: ', carros)
print('Lista de frutas eh maior que a de carros? ', frutas > carros)
## <-

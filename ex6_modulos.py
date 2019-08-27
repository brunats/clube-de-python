## Lista exercicios modulos
##  Exercicio 1
#       Importe a classe Carro criada no exercício anterior em outro arquivo e faça alguns testes com ela.
## ->
from ex5_funcoes_e_classes import Carro

sentra = Carro(10)
sentra.adicionarGasolina(45)
sentra.obterGasolina()
sentra.andar(10)
sentra.obterGasolina()
## <-5

##  Exercicio 1
#       Reescreva as classes abaixo em um arquivo e chame-o de formasGeometricas.py
#           importe em outro arquivo.
#       Nesse outro arquivo encontre a diferença entre a área de um círculo com
#           raio 5cm e a área de um quadrado de lado 5cm e printe a diferença para o usuário.
## ->
from formasGeometricas import Circulo, Retangulo
circulo = Circulo(5)
quadrado = Retangulo(5, 5)
area_circulo = circulo.area()
area_quadrado = quadrado.area()
print('Area de um circulo de 5cm de raio eh: ', area_circulo)
print('Area de um quadrado de 5cm de lado eh: ', area_quadrado)
print('Diferenca eh: ', area_circulo - area_quadrado)
## <-

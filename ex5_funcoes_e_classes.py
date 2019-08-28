## Lista exercicios funcoes e classes
##  Exercicio 1
#       Crie uma função que receba uma lista de número e retorne a soma dos elementos com valor negativo.
## ->
def soma(lista):
    soma = 0.0
    for i in lista:
        soma += i
        soma = soma*(-1)
    return soma

lista = [1, 2, 3, 4, 5]
print(lista)
print(soma(lista))

## <-

##  Exercicio 2
#       Classe Bola: Crie uma classe que modele uma bola:
#           Atributos: Cor, circunferência, material
#           Métodos: trocaCor e mostraCor
## ->
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

bola = Bola('Branco', 2.0, 'Couro')
bola.mostraCor()
bola.trocaCor("Azul")
bola.mostraCor()

## <-

##  Exercicio 3
#       Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#       Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#       O consumo é especificado no construtor e o nível de combustível inicial é 0.
#       Forneça um método andar( ) que receba por parâmetro a distância e simule o ato de dirigir o veículo, reduzindo o nível de combustível no tanque de gasolina.
#       Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#       Forneça um método adicionarGasolina( ), para abastecer o tanque e receba a quantidade de gasolina a ser abastecida.
#       Exemplo de uso:
#       	meuFusca = Carro(15);       		# 15 quilômetros por litro de combustível.
#       	meuFusca.adicionarGasolina(20); 	# abastece com 20 litros de combustível.
#       	meuFusca.andar(100);        		# anda 100 quilômetros.
#       	meuFusca.obterGasolina()    		# Imprime o combustível que resta no tanque.
## ->
class Carro:
    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print('Gasolina: ', self.qtdeCombustivel)

# 15 quilometros por litro de combustivel.
meuFusca = Carro(15)

# Imprime o combustivel que esta no tanque.
meuFusca.obterGasolina()

# abastece com 20 litros de combustivel.
meuFusca.adicionarGasolina(20)

# Imprime o combustivel que esta no tanque.
meuFusca.obterGasolina()

# anda 100 quilometros.
meuFusca.andar(100)

# Imprime o combustivel que resta no tanque.
meuFusca.obterGasolina()
## <-

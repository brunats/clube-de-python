from math import pi
class Retangulo:
  def __init__(self, comprimento, largura):
      self.comprimento = comprimento
      self.largura = largura

  def area(self):
      return self.comprimento * self.largura


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return pi * self.raio**2

    def comprimento(self):
        return 2 * pi * self.raio

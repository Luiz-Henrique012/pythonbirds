'''

Você deve criar uma classe carro que via possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decemntar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela
oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste;
2) Método girar_a_direita
3) Método girar_a_esquerda


      Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
'''

norte = 'Norte'
leste = 'Leste'
sul = 'Sul'
oeste = 'Oeste'

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade)

class Direcao:
    direcoes_direita = {norte: leste, leste: sul, sul: oeste, oeste: norte}
    direcoes_esquerda = {norte: oeste, oeste: sul, sul: leste, leste: norte}

    def __init__(self):
        self.valor = norte

    def girar_a_direita(self):
        self.valor = self.direcoes_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.direcoes_esquerda[self.valor]



if __name__ == '__main__':
    carro = Carro(norte, 0)
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.acelerar()
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())

    carro.acelerar()
    carro.acelerar()
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.girar_a_direita()
    carro.frear()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())




#  direcao = Direcao()
  #  print(direcao.valor)
  #  for c in range(0,4):
  #      direcao.girar_a_direita()
  #      print(direcao.valor)
  #  for c in range(0,2):
  #      direcao.girar_a_esquerda()
  #      print(direcao.valor)
  #  direcao.girar_a_direita()
  #  print(direcao.valor)
    #motor = Motor()
    #for c in range(0,5):
       # print(motor.velocidade)
       # motor.acelerar()

   # print(motor.velocidade)
    #motor.frear()
    #print(motor.velocidade)
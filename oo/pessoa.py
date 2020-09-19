class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None, altura=None):
        self.altura = altura
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def __str__(self):
        return f'{self.filhos}'

    def cumprimentar(self):
        return 'Ola, tudo certo contigo bro?'

    @staticmethod  # Método estatico que independe o método da classe, não necessitando depender de objeto algum para ser rodado
    def método_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):  # Outro método de conseguir descobrir e adquirir informações da classe
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


class Mulher(Pessoa):
    pass


if __name__ == '__main__':
    seiya = Homem(nome='Seiya')
    amanda = Mulher(nome='Amanda')
    tohka = Mulher(nome='Tohka')
    henrique = Homem(seiya, amanda, tohka, nome='Henrique')
    print(henrique.nome)
    print(f'----Os filhos de {henrique.nome} são:')
    for filhos in henrique.filhos:
        print(f'--------{filhos.nome}--------')
    print(tohka.olhos)
    tohka.olhos = 4
    print(tohka.olhos)
    print(tohka.__dict__)  # Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    print(henrique.__dict__)  # Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    del tohka.olhos
    print(tohka.__dict__)  # Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    tohka.sobrenome = 'Kurosaki'
    print(f'--------{tohka.nome} {tohka.sobrenome}--------')
    print()
    print(Pessoa.método_estatico(), henrique.método_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), henrique.nome_e_atributos_de_classe())
    print()
    print(isinstance(henrique, Pessoa))
    print(isinstance(henrique,Homem))
    print(isinstance(seiya, Pessoa))
    print(isinstance(seiya, Homem))
    print(isinstance(amanda, Pessoa))
    print(isinstance(amanda, Mulher))
    print(isinstance(tohka, Pessoa))
    print(isinstance(tohka, Mulher))
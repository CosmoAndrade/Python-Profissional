
import random
from pokemon import *

NOMES = ['Lucas','Felipe','Danilo','Artur','Cosmo']

class Pessoa:
    
    def __init__(self,nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)   

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemon(self):
        if self.pokemons:
            print('Pokemons de {}'.format(self))
            for pokemon in self.pokemons:
                print(pokemon)    
        else:
            print('{} não tem nenhum pokemom'.format(self))

class Player(Pessoa):
    tipo = 'Player'

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print ('{} capturou {}'.format(self,pokemon))

class Inimigo(Pessoa):
    tipo = 'Inimigo'




eu = Player()
print(eu)









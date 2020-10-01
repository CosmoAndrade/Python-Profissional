
import random
from pokemon import *

NOMES = ['Lucas','Felipe','Danilo','Artur','Cosmo']
POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('Charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
]

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

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(1,6):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)


meu_inimigo = Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemon()










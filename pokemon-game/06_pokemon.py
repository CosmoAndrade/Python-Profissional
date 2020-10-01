
from pokemon import *



class Pessoa:
    
    def __init__(self,nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Aleatorio'
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



eu = Player('Cosmo')
pokemon_de_fogo = PokemonFogo('Charmander')
eu.mostrar_pokemon()
eu.capturar(pokemon_de_fogo)
eu.mostrar_pokemon()







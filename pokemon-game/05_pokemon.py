from pokemon import *

class Pessoa:
    
    def __init__(self,nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Anônimo'    

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemon(self):
        for pokemon in self.pokemons:
            print(pokemon)    


class Player(Pessoa):
    tipo = 'Player'


class Inimigo(Pessoa):
    tipo = 'Inimigo'


meu_pokemon = PokemonEletrico('Pikachu')
meu_pokemon2 = PokemonEletrico('Charmander')

eu = Player('Cosmo',pokemons=[meu_pokemon,meu_pokemon2])
print(eu)
eu.mostrar_pokemon()


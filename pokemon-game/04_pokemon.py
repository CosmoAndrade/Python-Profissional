class Pokemon:
    def __init__(self,especie,level = 1, nome=None):
       
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie    

    def __str__(self):
        return '{} ({})'.format(self.nome,self.level)  

    def atacar(self,pokemon):
        print('{} atacou! {}'.format(self,pokemon))  
        

class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'

    def atacar(self,pokemon):
        print('{} Lançou um raio do Trovão em  {}'.format(self,pokemon))        

class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self,pokemon):
        print('{} Lançou uma bola de Fogo! em  {}'.format(self,pokemon))        




meu_pokemon = PokemonEletrico('Pikachu') 
amigo_pokemon = PokemonFogo('Charmander')

print (meu_pokemon,meu_pokemon.tipo)
print(amigo_pokemon,amigo_pokemon.tipo)

meu_pokemon.atacar(amigo_pokemon)
amigo_pokemon.atacar(meu_pokemon)
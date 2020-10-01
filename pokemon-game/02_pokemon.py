class Pokemon:
    def __init__(self,tipo,especie,level = 1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie    

    def __str__(self):
        return '{} ({})'.format(self.especie,self.tipo)  

    def atacar(self,pokemon):
        print('{} atacou! {}'.format(self,pokemon))  
        

meu_pokemon = Pokemon('Fogo','Charmander')    
amigo_pokemon = Pokemon('Eletrico','Pikachu')

print(meu_pokemon)
print(amigo_pokemon)
meu_pokemon.atacar(amigo_pokemon)
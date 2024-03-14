from random import shuffle

class Animal:
    def __init__(self, nome, carnivoro, domestico, patas, mamifero, felino, grande, voar,bandos):
        self.nome = nome
        self.carnivoro = carnivoro
        self.domestico = domestico
        self.patas = patas
        self.mamifero = mamifero
        self.felino = felino
        self.grande = grande
        self.voar = voar
        self.bandos = bandos

class Galinha(Animal):
    def __init__(self):
        super().__init__("Galinha", False, True, True, False, False, False, False, True)

class Aguia(Animal):
    def __init__(self):
        super().__init__("Águia", True, False, True, False, False, False, True, False)

class Urubu(Animal):
    def __init__(self):
        super().__init__("Urubu", True, False, True, False, False, False, True, True)

class Morcego(Animal):
    def __init__(self):
        super().__init__("Morcego", False, False, True, True, False, False, True, True)

class Calopsita(Animal):
    def __init__(self):
        super().__init__("Calopsita", False, True, True, False, False, False, True, False)

class Cachorro(Animal):
    def __init__(self):
        super().__init__("Cachorro", False, True, True, True, False, False, False, False)

class Leao(Animal):
    def __init__(self):
        super().__init__("Leao", True, False, True, True, True, True, False, True)

class Elefante(Animal):
    def __init__(self):
        super().__init__("Elefante", False, False, True, True, False, True, False, True)

class Crocodilo(Animal):
    def __init__(self):
        super().__init__("Crocodilo", True, False, True, False, False, True, False, True)

class Sapo(Animal):
    def __init__(self):
        super().__init__("Sapo", False, False, True, False, False, False, False, False)

class Cavalo(Animal):
    def __init__(self):
        super().__init__("Cavalo", False, True, True, True, False, True, False, False)

class Gato(Animal):
    def __init__(self):
        super().__init__("Gato", False, True, True, True, True, False, False, False)

class Baleia(Animal):
    def __init__(self):
        super().__init__("Baleia", False, False, False, True, False, True, False, False)

class Tubarao(Animal):
    def __init__(self):
        super().__init__("Tubarão", True, False, False, False, False, True, False, False)

class Dourado(Animal):
    def __init__(self):
        super().__init__("Peixe Dourado", False, True, False, False, False, False, False, False)

class Salmao(Animal):
    def __init__(self):
        super().__init__("Salmão", True, False, False, False, False, False, False, True)

class Camarao(Animal):
    def __init__(self):
        super().__init__("Camarão", False, False, False, False, False, False, False, False)



# Lista principal com os animais
animais = [Galinha(), Aguia(), Urubu(), Morcego(), Calopsita(), Cachorro(), Leao(), Elefante(), Crocodilo(), Cavalo(), Gato(), Sapo(), Baleia(), Tubarao(), Dourado(), Salmao(), Camarao()]

# Lista de perguntas
perguntas = [
    ("O animal é carnívoro? (S/N): ", "carnivoro"),
    ("O animal é doméstico? (S/N): ", "domestico"),
    ("O animal tem patas? (S/N): ", "patas"),
    ("O animal é mamífero? (S/N): ", "mamifero"),
    ("O animal é um felino? (S/N): ", "felino"),
    ("O animal tem porte grande? (S/N): ", "grande"),
    ("O animal sabe voar? (S/N): ", "voar"),
    ("O animal vive em bandos? (S/N): ", "bandos"),

]

shuffle(perguntas)
# Loop para fazer perguntas e filtrar os animais com base nas respostas
for pergunta, atributo in perguntas:
    resposta = None
    while resposta != 'S' and resposta != "N":
        resposta = input(pergunta).upper()
    i = 0
    n = len(animais)
    while i != n:
        animal = animais[i]
        if resposta == 'S':
            if getattr(animal, atributo) == False:
                animais.pop(i)
                i-=1
                n = len(animais)
        else:
            if getattr(animal, atributo) == True:
                animais.pop(i)
                i-=1
                n = len(animais)
        
        i+=1
        
    #print(f'ANIMAIS = {[animal.nome for animal in animais]}')
    # Verificar se há apenas um animal restante
    if len(animais) == 1:
        print(f"O animal que você pensou é uma {animais[0].nome}")
        exit()  # Sai do programa após adivinhar o animal
    
    # Verificar se não há mais animais que correspondem às respostas
    elif len(animais) == 0:
        print("Não consegui adivinhar o animal que você pensou.")
        exit()  # Sai do programa se não puder adivinhar o animal
    
    # Se ainda houver mais de um animal na lista filtrada, continue fazendo perguntas
    if len(animais) > 1:
        print("Ainda não consegui adivinhar, vamos tentar novamente.")

if len(animais)>1:
    print(f'Fiquei na duvida entre {[animal.nome for animal in animais]}')
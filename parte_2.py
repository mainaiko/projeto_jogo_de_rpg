from random import randint

lista_npcs = []
    
    
    
def criar_npc():
        level = randint(0,50)
        armadura = randint(0,40)

        novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level ,
        "dano": 5 * level,
        "hp": 100 * level,
        "armadura": 4 * level,

        }

        lista_npcs.append(novo_npc)#insere variaveis a lista


def gerar_npcs(n_npcs): #ir printando para ver o que esta acontecendo
    for x in range(n_npcs):
        criar_npc()

def exibir_npcs():
    for npc in lista_npcs:
        print (
        f"Nome: {npc['nome']} // Level {npc['level']} // Dano {npc['dano']} // HP {npc['hp']} // Armadura {npc['armadura']}"
        )

gerar_npcs(10)


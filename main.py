from random import randint

lista_npcs = []

player = {
    "nome": "Aiko",
    "level": 1,
    "exp" : 0,
    "exp_max": 30,
    "hp": 120,
    "hp_max": 120,
    "dano": 20,
    "armadura": 7,
}
    
    
def criar_npc(level):
        armadura = randint(0,40)

        novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level ,
        "dano": 4 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "armadura": 4 * level,
        "exp": 7 * level,

        }

        return novo_npc

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x+1)
        lista_npcs.append(npc)

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print (
        f"Nome: {npc['nome']} // Level {npc['level']} // Dano {npc['dano']} // HP {npc['hp']} // Armadura {npc['armadura']} // EXP {npc['exp']}"
        )   

def exibir_player():
    print (
        f"Player: {player['nome']} // Level {player['level']} // Dano {player['dano']} // HP {player['hp']}/{player['hp_max']} // Armadura {player['armadura']} // EXP {player['exp']}/{player['exp_max']}"
        )   

def reset_player():
    player["hp"] = player ["hp_max"]

def reset_npc(npc):
    npc["hp"] = npc ["hp_max"]

def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] *= 2
        player["hp_max"] += 20
        player["armadura"] += 4

def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)

    if player["hp"] > 0:
        print(f"A {player['nome']} venceu e ganhou {npc['exp']} de XP")
        player["exp"] += npc ["exp"]
        exibir_player()
    else:
        print(f"O {npc[nome]} venceu)")
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)

def atacar_npc(npc):
    npc['hp'] -= player ['dano']

def atacar_player(npc):
    player['hp'] -= npc ['dano']

def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print("------------------------------\n")



gerar_npcs(5)

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)

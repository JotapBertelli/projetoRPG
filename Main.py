hp = 100.0
money = 50.0
drag = 150.0
sword = 20.0
drag_damage = 25.0

user = int(input("Seja bem-vindo ao RPG maker! Digite 1 para continuar sua história. "))

def mercador():
    print("bem vindo a loja do mercador: \n  ")
    print("Espada")
    print("Espada")
    print("Espada")

def fight():
    print("Batalha")



if user == 1:
    history = int(input("Digite 1 para seguir em frente. \n Digite 2 para encontrar o mercador.  "))
    if history == 1:
        choose = str(input("Voce encontrou um bau com os seguintes itens: Uma sacola com 50 moedas \n espada pequena \n digite 1 para pegar espada \n digite 2 para pegar sacola"))
        if choose == 1:
            sword = str(input("Voce selecionou a espada deseja ir a batalha? S/N: "))
            if sword == 's':
                fight = str(input("Voce encontrou o boss! Deseja batalhar? S/N "))  
            else:
                fight()    
        else:
            print('voce encontrou um saco com 50 moeadas! ')
            mercador()
            print(f"Seu saldo atual é  {money + 50}")                 
    else:
       mercador()          
else:
    mercador()





    
        
def mercador(money):
    print("Bem-vindo à loja do mercador:")
    print("1. Espada - 50 R$")
    print("2. Poção de cura - 40 R$")
    print("3. Magia poderosa - 70 R$")
    print(f"Seu saldo atual é {money} R$")

def fight():
    print("teste")

def find_chest(money):
    choose = input("Você encontrou um baú com os seguintes itens:\n1. 1 - Espada pequena\n2. 2 - Sacola com 50 moedas\nDigite o número do item que deseja pegar: ")
    if choose == "1":
        return "espada"
    elif choose == "2":
        money += 50
        print(f"Você encontrou uma sacola com 50 moedas! Seu saldo atual é {money} R$")
        mercador(money)
    return money

def game_init():
    hp = 100.0
    money = 50.0
    drag = 150.0
    sword = 20.0
    drag_damage = 25.0

    user = input("Seja bem-vindo ao RPG maker! Digite 1 para continuar sua história: ")
    if user != "1":
        mercador(money)
        return
    
    history = input("Digite 1 para seguir em frente.\nDigite 2 para encontrar o mercador: ")
    if history == "1":
        resultado = find_chest(money)
        if resultado == "espada":
            batalha = input("Você selecionou a espada. Deseja ir à batalha? (S/N): ").upper() #coloquei esse upper para caso algum bobão colocar letra minuscula e dar erro de string :)
            if batalha == "s":
                luta = input("Você encontrou o boss! Deseja batalhar? (S/N): ").upper() #coloquei esse upper para caso algum bobão colocar letra minuscula e dar erro de string :)
                if luta == "s":
                    fight()
    else:
        mercador(money)

game_init()






    
        
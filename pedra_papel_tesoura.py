import random

pontos_usuario = 0
pontos_computador = 0

opçoes = ["p", "t", "r"]

while True:
    escolha_usuario = input("Escolha P(Pedra)/T(Tesoura)/R(Papel) ou Q para sair: ").lower()

    if escolha_usuario == "q":
        break

    escolha_computador = random.randint(0, 2)
    # 0 : P, 1 : T, 2 : R

    decisao = opçoes[escolha_computador] 

    print("O computador escoleu: " + decisao)

    if escolha_usuario == decisao:
        print("Empate!!")
    elif escolha_usuario == "p" and decisao == "t":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    if escolha_usuario == decisao:
        print("Empate!!")
    elif escolha_usuario == "r" and decisao == "p":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    if escolha_usuario == decisao:
        print("Empate!!")
    elif escolha_usuario == "t" and decisao == "r":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1
    
    else:
        print("Você perdeu!")
        pontos_computador = pontos_computador + 1

print("Sua Pontuaçao: "+ str(pontos_usuario))
print("Pontuaçao Computador: "+ str(pontos_computador))

if pontos_computador > pontos_usuario:
    print("Derrota!!!")
elif pontos_computador == pontos_usuario:
    print("Empate")
else:
    print("Vitoria!")

print("tchau!!")
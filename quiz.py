print("Ola Seja Bem - Vindo!")

recebendo = input("quer começar? (S/N) ").upper() # recebendo as respostas do usuario

if recebendo != "S":
    quit() # se o usuario nao quiser jogar, o programa encerra

score = 0 # variavel para armazenar a pontuação do usuario

print("Começando...")
print("Qual é o nome do burro que acompanha Shrek em sua jornada? \n (A)Fiona \n (B)Dragão  \n (C)Burro") # pergunta 1

resposta = input("Rsposta: ").upper() 
if resposta == "C":
    print("correta!")
    score = score + 1 
else:
    print("incorreto!")

print("Qual é o maior planeta do sistema solar? \n (A)Terra \n (B)Marte \n (C)Júpiter \n (D)Saturno") # pergunta 2

resposta2 = input("Rsposta: ").upper()
if resposta2 == "C":
    print("correta!")
    score = score + 1
else:
    print("incorreto!")

print("Qual é o proximo número na sequência: 1, 3, 6, 10? \n (A)12 \n (B)15 \n (C)18 \n (D)20") # pergunta 3

resposta3 = input("Resposta: ").upper()
if resposta3 == "B":
    print("correta!")
    score = score + 1
else:
    print("incorreto!")

print(f"Quiz acabou... Pontuaçao: {score}/3") # exibe a pontuação final do usuário
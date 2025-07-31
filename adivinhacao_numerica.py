import random 

print("Seja Bem-vindo ao jogo de adivinhaçao numerica!")

numero = input("Digite o numero teto do desafio: ") # recebendo o numero teto do desafio

if numero.isdigit(): # verificando se o valor informado é numerico
    numero = int(numero)
else: 
    print("Erro: valor informado nao e numerico!")

random_number = random.randint(0, numero) # gerando um numero aleatorio entre 0 e o numero teto informado

n_tentativas = 0

while True: 
    palpite = input("Adivinhe o numero: ")

# verificando se o palpite é numerico
    if palpite.isdigit(): 
        palpite = int(palpite)
    else:
        print("Erro: o numero infomado nao e numerico! ")
        continue

    n_tentativas = n_tentativas + 1

    if palpite == random_number:
        print("Parabens! Voce acertou o numero!")
        break

# Se o palpite estiver incorreto, fornecer dicas
    elif palpite < random_number:
        print("O numero informado e menor que o numero secreto!")
    else:
        print("O numero informado e maior que o numero secreto!")

print("Número de Tentativas: "+str(n_tentativas))

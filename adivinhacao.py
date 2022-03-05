import random


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#********* Laço com while **********

#numero_secreto = round(random.random() * 100)
#total_de_tentativas = 3
#rodada = 1

#print(numero_secreto)

#while (rodada <= total_de_tentativas):
#    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#
#    chute_str = input("Digite o seu numero: ")
#    print("Você digitou " , chute_str)
#    chute = int(chute_str)
#
#    acertou = numero_secreto == chute
#    chute_maior = chute > numero_secreto
#    chute_menor = chute < numero_secreto
#
#    if (acertou):
#        print("Você acertou")
#    else:
#        if (chute_maior):
#            print("Você errou! O seu chute foi maior do que o número secreto.")
#        elif (chute_menor):
#            print("Você errou! O seu chute foi menor do que o número secreto.")
#
#    rodada = rodada + 1

#print("Fim do jogo")


#********* Laço com for **********

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if (chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

        elif (chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

print("Fim do jogo")
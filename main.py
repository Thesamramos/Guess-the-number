from random import randint

computer_number = randint(1, 100)
cont = 0

print("Pensei em um número entre 1 e 100, consegue adivinhar?")

while True:
    print("\n======= JOGO DA ADIVINHAÇÃO =======")
    print("\nEm qual número eu pensei?")
    player_guess = int(input("Qual é o seu palpite: "))
    cont +=1

    if player_guess > computer_number and player_guess < 101:
        print(f"O número {player_guess} é maior do que eu escolhi.")
        print("Tente novamente!")
    elif player_guess < computer_number and player_guess > 0:
        print(f"O número {player_guess} é menor do que eu escolhi.")
        print("Tente novamente!")
    elif player_guess > 100 or player_guess < 1 :
        print(f"O número {player_guess} é inválido, digite um número entre 1 e 100.")
        print("Tente novamente!")
    else:
        print(f"\nParabéns!!! Você acertou com {cont} tentativas, eu escolhi o número {computer_number}.")
        break
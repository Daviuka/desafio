import random
import os


# recebe um  número aleatório entre 0 a 100
numero_premiado = random.randint(0,100)
num_tentado = []
tentativas = 10
tempo = 30

os.system('cls')
while True:
    # Variável que o usuário pode colocar um número entre 0 a 100
    entrada_usuario = int(input('Digite um número: '))
    print()
    if entrada_usuario == numero_premiado:
        print('Você ganhou!')
        break
    elif tentativas == 0:
        print(f'Você perdeu, o número era premiado era {numero_premiado}')
        break
    else:
        print('Você não acertou o número!')

        # adiciona o número tentado na lista
        num_tentado.append(entrada_usuario)
        tentativas -=1

        # Verifica se o número digitado é maior ou menos
        if entrada_usuario > numero_premiado:
            print('Digite um número menor!')
        else:
            print('Digite um número maior')
        
print('Fim de Jogo')
print(f'Você tentou os numeros { num_tentado}')
print(f'Você teve: {len(num_tentado)} tentativa')
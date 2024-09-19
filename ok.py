import os
lista_usuario = []

while True:
    print(30*'*', 'MENU', 30*'*')
    print('1. cadastrar usuario')
    print('2. listar usuario')
    print('3. excluir usuario')
    print('4. buscar pelo nome')
    print('5. inserir uma posição')
    print('6. sair')
    print(30*'*', 30*'*')

    opcao = input('Digite a opção que você deseja: ')


    #cadastra usuário
    if opcao == '1':
        nome = input('Digite o nome que deseja cadastrar: ')

        if nome != '':
            lista_usuario.append(nome)
        else:
            print('Digite algum valor: ')

    #listar usuario
    elif opcao =='2':
        for i, n in enumerate(nome):
            print(f'{i}°  {n}')

    #Excluir ususario
    elif opcao == '3':

        for i, n in enumerate(nome):
            print(f'{i}: {n}')
        posicao = input('Digite o número do usuário que deseja ser removido: ').upper()

        for j, _ in enumerate(lista_usuario):
            if j == posicao:
                lista_usuario.pop(j)
                print(f'Usuário da posição {j} foi removido com sucesso!')
                


        '''
        for i in lista_usuario:
            lista_usuario.remove(i)
            print('Usuário removido com sucessso!')
        '''
    
    #Buscar o nome
    elif opcao == '4':
        nome_buscar = ('Digite o nome que deseja buscar: ').upper()

        if nome_buscar!= '':
            for i in lista_usuario:
                if i ==nome_buscar:
                    print(i)
                else:
                    print('Usuário não encontrado')
        else:
            print('Valor Inválido')


    # Inserir em uma posição
    elif opcao == '5':
        novo_nome = input('Digite o nome que deseja inserir: ').upper()
        posicao_nome = int(input('Digite uma posição para inserir o nome que você digitou: '))

        posicao_nome -=1
        if posicao_nome >= 0 and posicao_nome <= len(lista_usuario):
            lista_usuario.insert(posicao_nome,  novo_nome)
        else:
            print('Posição inválida!')
            
    # Sair
    elif opcao == '6':
        print('Saindo do Sistema!')
        break


    
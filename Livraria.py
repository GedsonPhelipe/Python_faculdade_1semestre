# Bloco contém lógica do cadastro de livros (Adiciona Id, coleta dados do livro e insere em "banco de dados").
def cadastrar_livro(id_global, lista_livro):
    print('\n MENU CADASTRAR LIVRO\n')

    id_global += 1  # Acrescenta 1 a id_global para referenciar novo livro.

    print(f'Id do livro: {id_global} ')
    nome = str(input('Digite o nome do livro: ')).strip().upper()
    autor = str(input('Digite o nome do autor: ')).strip().upper()
    editora = str(input('Digite o nome da editora: ')).strip().upper()

    livro = {'Id': id_global, 'Nome': nome, 'Autor': autor, 'Editora': editora}  # Dicionário local.
    lista_livro.append(livro)  # Copia dicionário para lista príncipal.

    print('Livro cadastrado com sucesso.')
    return id_global  # Retorna novo valor a Id global.


# Bloco contém lógica de consulta (Todos, Id ou autor).
def consulta_livro(lista_livro):
    print('\n MENU CONSULTA LIVRO(S)\n')

    while True:
        try:
            consulta = int(input('1 - Consultar todos\n2 - Consultar por Id\n3 - Consultar por autor\n4 - Retornar ao menu principal\n> '))
            if consulta in (1, 2, 3, 4):
                break
            else:
                print('\nOpção inválida, por favor tente novamente.')
        except ValueError:
            print('Entrada inválida, por favor escolha uma opção numérica.\n')

    # Consulta todos.
    if consulta == 1:
        print('\nLista de livros:\n')

        for livro in lista_livro:
            print(f' Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}\n')

    # Consulta por Id.
    elif consulta == 2:

        while True:
            try:
                id_procurado = int(input('\nDigite o Id do livro: '))

                for livro in lista_livro:
                    if id_procurado == livro['Id']:
                        print(f'\n Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}')
                        return

                print('Id digitado não existe no banco de dados.')
                break

            except ValueError:
                print('\nO id do livro deve ser numérico, por favor tente novamente.')

    # Consulta por autor.
    elif consulta == 3:

        autor_procurado = str(input('\nDigite o nome do autor: ')).strip().upper()
        autor_encontrado = False

        for livro in lista_livro:
            if autor_procurado == livro['Autor']:
                autor_encontrado = True
                print(f'\n Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}')

        if not autor_encontrado:
            print('Autor não encontrado no banco de dados.')


# Bloco contém lógica para remoção de livro (Busca livro por Id, caso encontrado remove do "banco de dados").
def remover_livro(lista_livro):
    print('\n MENU REMOVER LIVRO\n')

    while True:
        try:
            id_procurado = int(input('\nDigite o Id do livro: '))

            for livro in lista_livro:
                if id_procurado == livro['Id']:
                    lista_livro.remove(livro)
                    print('Livro removido com sucesso.')
                    return

            print('Id digitado não existe no banco de dados.')
            break

        except ValueError:
            print('\nO id do livro deve ser numérico, por favor tente novamente.')


# Bloco principal (programa principal).
def main():

    print('Bem vindo(a) a Livraria do Gedson Phelipe')

    lista_livro = []
    id_global = 0

    # Bloco de Menu principal (Fornece escolha de operação para o usuário, invoca funções príncipais, faz validações relevantes para funcionamento do Software, e encerra programa).
    while True:
        print('\nMENU PRINCIPAL')
        escolha = input('\nEscolha a opção desejada:\n1 - Cadastrar livro\n2 - Consultar livro(s)\n3 - Remover livro\n4 - Sair\n> ')

        if escolha in ('1', '2', '3', '4'):
            if escolha == '1':
                id_global = cadastrar_livro(id_global, lista_livro)

            elif escolha == '2':
                if lista_livro:  # Verifica a existência de livros cadastrados para consultar.
                    consulta_livro(lista_livro)
                else:
                    print('Não há livros cadastrados até o momento.')

            elif escolha == '3':
                if lista_livro:  # Verifica a existência de livros cadastrados para excluir.
                    remover_livro(lista_livro)
                else:
                    print('Não há livros cadastrados até o momento.')

            else:
                exit()  # Encerra Software.

        else:
            print('\nOpção inválida, por favor tente novamente.')


main()

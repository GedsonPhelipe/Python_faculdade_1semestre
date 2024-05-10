def cadastrar_livro(id_global):
    print('\n MENU CADASTRAR LIVRO\n')

    id_global += 1

    print(f'Id do livro: {id_global} ')
    nome = str(input('Digite o nome do livro: ')).strip().upper()
    autor = str(input('Digite o nome do autor: ')).strip().upper()
    editora = str(input('Digite o nome da editora: ')).strip().upper()

    livro = {'Id': id_global, 'Nome': nome, 'Autor': autor, 'Editora': editora}
    lista_livro.append(livro)
    return id_global


def consulta_livro():
    print('\n MENU CONSULTA LIVROS\n')

    while True:
        consulta = int(input('1 - Consultar todos\n2 - Consultar por Id\n3 - Consultar por autor\n4 - Retornar ao menu: '))
        if consulta in (1, 2, 3, 4):
            break
        else:
            print('\nOpção inválida, por favor tente novamente.')

    if consulta == 1:
        print('\nLista de livros:\n')
        for livro in lista_livro:
            print(f' Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}')

    elif consulta == 2:

        while True:
            try:
                id_procurado = int(input('\nDigite o Id do livro: '))

                for livro in lista_livro:
                    if id_procurado == livro['Id']:
                        print(f'\n Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}')
                    else:
                        print('Id digitado não existe no banco de dados.')
                break

            except ValueError:
                print('\nO id do livro deve ser numérico, por favor tente novamente.')

    elif consulta == 3:

        while True:
            autor_procurado = str(input('\nDigite o nome do autor: ')).strip().upper()

            for livro in lista_livro:
                if autor_procurado == livro['Autor']:
                    print(f'\n Id: {livro['Id']}\n Nome: {livro['Nome']}\n Autor: {livro['Autor']}\n Editora: {livro['Editora']}')
                else:
                    print('Autor não encontrado no banco de dados.')
            break


def main():
    global lista_livro

    print('Bem vindo(a) a Livraria do Gedson Phelipe')

    lista_livro = []
    id_global = 0


    id_global = cadastrar_livro(id_global)

    consulta_livro()



main()

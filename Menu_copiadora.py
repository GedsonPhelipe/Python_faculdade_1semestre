# Bloco com lógica de escolha de serviço, (recebe escolha de serviço do usuário e retorna com (print) serviço escolhido e valor do mesmo).
def escolha_servico(valores_servico):
    while True:
        servico = str(input('Escolha o serviço desejado: ')).strip().upper()

        if servico in valores_servico:

            print(f'\nVocê selecionou {servico} valor por página: R${valores_servico[servico]:.2f}')
            return servico

        else:
            print('\nEscolha inválida, por favor atente-se as opções. ')


# Bloco com lógica de escolha de páginas, (recebe número de páginas escolhidas pela usuário para calculo do valor de desconto).
def num_paginas():
    while True:

        try:
            paginas = int(input('Digite a quantidade de páginas: '))

            if 0 < paginas < 20000:

                if paginas < 20:
                    return paginas

                elif 20 <= paginas < 200:
                    return paginas * 0.85

                elif 200 <= paginas < 2000:
                    return paginas * 0.8

                elif 2000 <= paginas < 20000:
                    return paginas * 0.75
            else:
                if paginas >= 20000:
                    print('\nNão aceitamos tantas páginas de uma vez, por favor tente ovamente.\n')
                else:
                    print('\nO valor deve ser superior a 0.\n')

        except ValueError:
            print('\nValor inválido, por favor digite um número.\n')


# Bloco contém lógica para serviço extra (verifica se usuário deseja serviço extra, retorna valor correspondente para variável 'total').
def servico_extra():
    print('\n Encadernação:')
    print(' 1 - Encadernação simples  -  R$15.00\n 2 - Encadernação Capa Dura - R$40.00\n 0 - Sem encadernação\n')

    while True:
        adicional = str(input('Deseja adicionar algum serviço? '))

        if adicional in ['0', '1', '2']:
            return adicional
        else:
            print('\nValor inválido, por favor escolha entre as opções 1, 2 ou 0.')


# Programa principal.
def main():
    print('Bem-vindo (a) a copiadora do Gedson\n')

    print(' Tipos de serviço: \n DIG - Digitalização \n ICO - Impressão colorida \n IPB - Impressão em Preto e Branco\n FOT - Fotocópia\n')

    valores_servico = {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}  # Dicíonario 1 (contém valores e nomenclature de serviços).

    extra = {'1': 15, '2': 40, '0': 0}  # Dicíonario 2 (contém valores de serviço extra).

    # Bloco de execução de funções.
    servico = escolha_servico(valores_servico)
    paginas = num_paginas()
    adicional = servico_extra()

    total = valores_servico[servico] * paginas + extra[adicional]  # Cálculo de valor total.

    print(f'\nTotal: R${total:.2f} (Serviço: {valores_servico[servico]:.2f} * páginas: {paginas} + {extra[adicional]:.2f})\n')

    while True:
        reiniciar = input('\nDeseja encerrar? (S/N): ').strip().upper()  # Input responsável por reinicio de copiadora.

        if reiniciar == 'S':
            from time import sleep
            print('\nReiniciando', end='')
            sleep(1 / 2)
            print('.', end='')
            sleep(1 / 2)
            print('.', end='')
            sleep(1 / 2)
            print('.', end='')
            sleep(1 / 2)
            print(4 * '\n')

            break

        else:
            print(f'Total de operação atual: R${total:.2f}')


while True:
    main()

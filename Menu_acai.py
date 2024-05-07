print('')
print(15*'-','Bem-vindo(a) ao Açai do Gedson', 15*'-')

# Bloco de Menu, contém produto, tamanho e preço.
print(27*'-','Menu',29*'-')
print(5*'-','|   Tamanho   |   Cupuaçu (CP)   |   Açaí (AC)   |',5*'-')
print(5*'-','|      P      |     R$  9.00     |   R$ 11.00    |',5*'-')
print(5*'-','|      M      |     R$  14.00    |   R$ 16.00    |',5*'-')
print(5*'-','|      G      |     R$  18.00    |   R$ 20.00    |',5*'-')
print(62*'-')
print(62*'-')

valor_total = 0  # Variável que armazena valor total da compra.
resposta = 'S'   # Variável contém condição de looping e Start de looping inicial.

while resposta == 'S':

    # Bloco de escolha de sabor.
    while True:
        sabor = str(input('\nQual sabor você deseja? Cupuaçu (CP) ou Açai (AC): ')).strip().upper()

        # Verificação e tratamento de erro "sabor".
        if sabor in ['CP', 'AC']:
            break
        else:
            print('Sabor inválido. Tente novamente usando CP para Cupuaçu ou AC para Açai.')  # Saída condicional 1.
            continue

    # Bloco de escolha de tamanho.
    while True:
        tamanho = str(input(f'Escolha o tamanho de seu {'Cupuaçu' if sabor == 'CP' else 'Açai'} P/M/G: ')).strip().upper()

        # Verificação e Tratamento de erro 'tamanho'.
        if tamanho in ['P', 'M', 'G']:
            break
        else:
            print('\nTamanho inválido. Por favor escolha entre P, M ou G.')  # Saída condicional 2.
            continue

    # Bloco com lógica de preços conforme tamanho.
    if sabor == 'CP':
        if tamanho == 'P':
            valor = 9
        elif tamanho == 'M':
            valor = 14
        else:
            valor = 18
    else:
        if tamanho == 'P':
            valor = 11
        elif tamanho == 'M':
            valor = 16
        else:
            valor = 20

    valor_total += valor  # Função para cálculo de valor total.

    print(f'Você pediu um {'Cupuaçu' if sabor == 'CP' else 'Açai'} no tamanho {tamanho}, valor: R${valor:.2f}')

    # Condição de looping, verificação e tratamento de erro.
    while True:
        resposta = str(input('\nDeseja algo mais? Digite S ou N: ')).upper().strip()
        if resposta in ['S', 'N']:
            break
        else:
            print('Resposta inválida, para continuar digite S ou N para encerrar.')  # Saída condicional 3.

print(f'\nO valor total a ser pago é: R${valor_total:.2f}\n')
print('Obrigado pela preferência, volte sempre!')

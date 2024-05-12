print('Bem-vindo(a) a Loja do Gedson Phelipe\n')

# Entrada de dados, contém valor e quantidade de produtos
valor_produto = float(input('Digite o valor do produto: ')) 
quanti_produto = int(input('Digite a quantidade do produto: '))

valor_total = valor_produto * quanti_produto  # Calcula o valor total da compra

if valor_total >= 2500:  # Condição de desconto, se o valor for inferior a 2500 não há descontos.

    # Bloco com a lógica de descontos, define o percentual usado para o cálculo de descontos.
    if valor_total < 6000:
        percentual_desc = 4

    elif valor_total < 10000:
        percentual_desc = 7

    else:
        percentual_desc = 11
    
    valor_com_desc = valor_total - (valor_total * (percentual_desc / 100))  # Calculo de valor da compra com desconto aplicado.

    # Bloco de saída condicional 1 (caso haja descontos)
    print(f'\nValor SEM desconto: R${valor_total:.2f}\n')
    print(f'Valor COM desconto: R${valor_com_desc:.2f}')

# Bloco de saída condicional 2 (caso não houver descontos)
else: 
    valor_com_desc = valor_total
    print('\nO valor de sua compra foi inferior a R$2500.00, sendo impossível aplicar desconto.') 
    print(f'\nValor total SEM desconto: R${valor_total:.2f}')

print('\nObrigado pela compra, volte sempre!\n')

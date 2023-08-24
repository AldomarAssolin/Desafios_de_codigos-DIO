
# O objetivo é implementar três operações essenciais: depósito, saque e extrato.
# O sistema será desenvolvido para um banco que busca monetizar suas operações.
import datetime

from assets.collors import font_color


borders_blue = ('{}--*--{}'.format(font_color['Azul'], font_color['limpa']) * 10)  # Borders
borders_green = ('{}--*--{}'.format(font_color['Verde'], font_color['limpa']) * 10)  # Borders
borders_magenta = ('{}--*--{}'.format(font_color['Magenta'], font_color['limpa']) * 10)  # Borders
space = (' ' * 15)  # Spaces(center text align)

# Date and Times
HORA_ATUAL = datetime.datetime.now()
DATA = HORA_ATUAL.strftime('%a %d %b %Y, %H:%M:%S')

#   HEADER DEFINE
NAME_BANK = 'ManexBank'
TITLE = 'Seja bem vindo ao nosso banco!'
SUBTITLE = 'Estamos muito felizes em ter você aqui conosco.'
MENU = '''
    ***********    MENU    ***********
    
    OPERAÇÕES
    * Para Saldo, digite 0.
    * Para Depósito, digite 1
    * Para Saque, Digite 2.
    * Para ver seu Extrato, Digite 3
    * Para sair, digite "S"
   
    *********   Obrigado    *********
    ******   Fique a Vontade   ******
'''
#   MESAGES
ERROR_MESAGE = 'Operação inválida. por favor selecionar novamente a operação desejada.'.format(font_color['Vermelho'], font_color['limpa'])
MENSAGEM_SALDO_INSUFICIENTE = 'Seu saldo é insuficiente, faça um depósito!'.format(font_color['Vermelho'], font_color['limpa'])
MESAGE_SALDO_ZERO = '{}Seu saldo é 0{}'.format(font_color['Amarelo'], font_color['limpa'])
MESAGE_SALDO = '{}Seu saldo é de: {}'.format(font_color['Verde'], font_color['limpa'])
END_MESAGE = '{}Obrigado por escolher estar conosco, volte sempre!{}'.format(font_color['Verde'], font_color['limpa'])

#   VARIABLES SYSTEM
saldo = 0
limite = 500
extrato = ""
numero_saques = 1
numero_depositos = 0
LIMITE_SAQUES = 3

#   START HEADER
print(borders_blue)
print(DATA.center(50, ' '))
print()
print('{}{}{}'.format(font_color['Magenta'], NAME_BANK.upper().center(50, ' '), font_color['limpa']))
print()
print('{}{}{}'.format(font_color['Azul'], TITLE.title().center(50, ' '), font_color['limpa']))
print('{}{}{}'.format(font_color['Amarelo'], SUBTITLE.center(50, ' '), font_color['limpa']))
print()
print(borders_blue)
#   OPTIONS
print()
print('{}{}{}'.format(font_color['Cyan_Claro'], MENU, font_color['limpa']))
print()
#   END HEADER


while True:
    
    if saldo == 0:
        
        
        print(f"{font_color['Vermelho']}SALDO: R${saldo:.2f}{font_color['limpa']}")
    options = str(input('Digite a operação desejada: '))
    
    if options == '0':
        if saldo == 0:
            print(MESAGE_SALDO_ZERO)
        else:
            print(f'{MESAGE_SALDO} R${saldo:.2f}')
        # DEPÓSITOS
    elif options == '1':
        
        valor_depositado = float(input('Digite o valor do Depósito: '))
        
        if valor_depositado >= 0:
            
            deposito = valor_depositado
            numero_depositos += 1
            saldo = deposito + saldo
            extrato += f'Depósito => Valor: R${deposito:.2f}\nData e Hora: {DATA}\n'
            
        else:
            
            valor_depositado_negativo = 'ERRO -> Operação falhou!\nValor informado Inválido!'
            print('{}{}\n{}'.format(font_color['Vermelho'], valor_depositado_negativo, font_color['limpa']))
        
        # SAQUES
    elif options == '2':
        
        valor_saque = float(input('Digite o valor do seu Saque: '))
        
        if saldo > 0 and valor_saque <= saldo and valor_saque <= limite and numero_saques <= 3:
            
            numero_saques += 1
            saque = valor_saque
            saldo = saldo - saque
            extrato += f'Saque => Valor: R${saque:.2f}\nData e Hora: {DATA}\n'
            
        elif saldo == 0:
           
           saldo_zero = f'Seu saldo é de R${saldo:.2f}, por favor, efetue um depósito!'
           print('{}{}\n{}'.format(font_color['Vermelho'], saldo_zero, font_color['limpa']))
           
        elif valor_saque > saldo:
            
            print('{}Seu saldo é insuficiente!{}'.format(font_color['Vermelho'], font_color['limpa']))
            print('{}Por favor, consulte seu saldo!{}'.format(font_color['Vermelho'], font_color['limpa']))
            
        elif valor_saque > limite:
            
            limite_error = 'Você ultrapassou o valor limite de saques diários!'
            
            print('{}{}\n{}'.format(font_color['Vermelho'], limite_error, font_color['limpa']))
            
        elif numero_saques >= LIMITE_SAQUES:
            
            saques_limite = 'Você ultrapassou seu limite de saques diários!'
            
            print('{}{}\n{}'.format(font_color['Vermelho'], saques_limite, font_color['limpa'])) 
        
            
        #EXTRATO
    elif options == '3':
        
        # BORDERS
        print(borders_magenta)
        # BORDERS
        print('{}{}{}'.format(font_color['Magenta'], 'EXTRATO'.upper().center(50, ' '), font_color['limpa']))
        print()
        print('{}{}\n{}'.format(font_color['Cyan'],extrato, font_color['limpa']))
        print(f'Data e Hora: {DATA}')
        
        if extrato == "":
            
            print('{}Sua conta não possui operações!{}'.format(font_color['Amarelo'], font_color['limpa']))
        
        if saldo <= 100:
            
            print(f"{font_color['Vermelho']}SALDO: R${saldo:.2f}{font_color['limpa']}")
        
        elif saldo > 100 and saldo < 250:
            
            print(f"{font_color['Amarelo']}SALDO: R${saldo:.2f}{font_color['limpa']}")
        else:
            print(f"{font_color['Verde']}SALDO: R${saldo:.2f}{font_color['limpa']}")
        print()
        
        # BORDERS
        print(borders_magenta)
        
        # SAIR
    elif options == 's' or options == 'S':
        
        sair = 'Você Saiu da conta!'
        print()
        print('{}{}{}'.format(font_color['Branco'], sair.upper().center(50, ' '), font_color['limpa']))
        break
    
    else:
        print(ERROR_MESAGE)

# FOOTER EXIT   
print(borders_magenta)
print()
print('{}{}{}'.format(font_color['Verde'], END_MESAGE, font_color['limpa']))
print()
print(borders_magenta)















import datetime
import textwrap
# Date and Times
HORA_ATUAL = datetime.datetime.now()
DATA = HORA_ATUAL.strftime('%a %d %b %Y, %H:%M:%S')

#   MESAGES
MENSAGEM_ERRO = '\n### Operação inválida. por favor selecionar novamente a operação desejada. ###'
MENSAGEM_SALDO_INSUFICIENTE = '\n ### Seu saldo é insuficiente, faça um depósito! ###'
MENSAGEM_VALOR_SAQUE_EXCEDIDO = '\n### Você excedeu o valor máximo de saques diários. ###'
MENSAGEM_NUM_SAQUES_EXCEDIDOS = '\n### Você excedeu o limite de saques diários. ###'
MENSAGEM_SALDO = '\n*** Seu saldo é de: ***'
END_MESAGE = '\n*** Obrigado por escolher estar conosco, volte sempre! ***'

SUCESSO_OP = '\n*** Operação realizada com sucesso! ***'



def menu():
    menu = '''
        ***********    MENU    ***********
        
        OPERAÇÕES
        [0] Para Saldo.
        [1] Para Depósito.
        [2] Para Saque.
        [3] Para Extrato.
        [4] Criar Conta.
        [5] Ver minhas contas.
        [6] Cadastrar Usuário.
        [7] Listar Contas.
        [S] Para sair.
    
        *********   Obrigado    *********
        ******   Fique a Vontade   ******
    '''
    return str(input(textwrap.dedent(menu)))
    
    


def depositar(saldo, valor, extrato, /):
        
    if valor > 0:
        saldo += valor
        extrato += f'\nDepósito => Valor: R${valor:.2f}\nData e Hora: {DATA}\n'
        print(SUCESSO_OP)
    else:
        print(MENSAGEM_ERRO)
        
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_limite_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print(MENSAGEM_SALDO_INSUFICIENTE)
    elif execedeu_limite:
        print(MENSAGEM_VALOR_SAQUE_EXCEDIDO)
    elif execedeu_limite_saques:
        print(MENSAGEM_NUM_SAQUES_EXCEDIDOS)
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR${valor:.2f}'
        numero_saques +=1
        print(SUCESSO_OP)
    else:
        print(MENSAGEM_ERRO)
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    mensagem_error = "Não foi realizado nenhuma operação!"
    
    print('\n************* EXTRATO *************')
    print(mensagem_error if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print('*-' * 20)


def criar_usuario(usuarios):
    cpf = input("Informe seu cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n ### Já existe usuário com esse cpf! ###')
        return
    
    nome = input('Informe seu nome completo: ')
    
    data_nasc = input('Informe a data do seu nascimento (dd-mm-aaaa): ')
    
    endereco = input('Informe seu endereço (logradouro, nro - bairro - cidade/sigla do estado): ')
    
    usuarios.append({
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })
    
    print('*** Usuário criado com sucesso! ***')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n*** Conta criada com sucesso! ***')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print('\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###')


def listar_contas(contas):
    print(contas)
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """ 
        
        
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    
    #   VARIABLES SYSTEM
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_depositos = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    usuarios= []
    contas = []
    numero_conta = 1
    
    
    while True:
        options = menu()
        
        if options == "0":
            print(f'{MENSAGEM_SALDO} R${saldo:.2f}')
        
        elif options == "1":
            valor = float(input('Digite o valor do Depósito: '))
            numero_depositos += 1
            saldo, extrato = depositar(saldo, valor, extrato)
            print(f'Saldo: R${saldo:.2f}\n', extrato)
        
        elif options == "2":
            valor = float(input('Digite o valor do seu Saque: '))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif options == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif options == "4":
            criar_usuario(usuarios)
            
        elif options == "5":
            #numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif options == "6":
            listar_contas(contas)
                
        elif options == "s" or options == "S":
            print(END_MESAGE)
            break
        
        else:
            print(MENSAGEM_ERRO)


main()
    




















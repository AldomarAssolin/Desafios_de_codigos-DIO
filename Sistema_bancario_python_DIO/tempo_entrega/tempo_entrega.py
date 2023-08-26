
# ToDo: Imprimir a saída no padrão definido no enunciado deste desafio.
# Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.
#***** Qual a opção desejada? *******


    # while True:
        
    #     options = input('Qual restaurante deseja consultar: ')
        
    #     if options == "0":
    #         nomeRestaurante = "MacDonalds 10"
    #         tempoEstimadoEntrega = 15
    #         print(mensagem(nomeRestaurante,tempoEstimadoEntrega))
    #     elif options == "1":
    #         nomeRestaurante = "KFC 25"
    #         tempoEstimadoEntrega = 35
    #         print(mensagem(nomeRestaurante,tempoEstimadoEntrega))
    #     elif options == "2":
    #         nomeRestaurante = "Burger King 5"
    #         tempoEstimadoEntrega = 22
    #         print(mensagem(nomeRestaurante,tempoEstimadoEntrega))    
    #     elif options == "s" or options == "S":
    #         break
    #     else:
    #         print('Opção inválida!')
import textwrap

def menu():
    menu = '''\
    
    ************* Opcões **************
    [0] Fazer Pedido
    [1] Consultar Tempo de Entrega
    [2] Consultar Cardápio
    [3] Outros
    [S] Para sair
    ***** Restaurantes Disponíveis *****
     
    [0] Macdonalds 10
    [1] KFC 25
    [2] Burger King 25
    [S] Para sair
     
    ************* Opcões **************
    
    '''
    
    return input(textwrap.dedent(menu))


def tempo_entrega(nome, tempo):
    
    dados_restaurantes = [
        {"nome": "MacDonalds 10", "tempo": "39"},
        {"nome": "KFC", "tempo": "32"},
        {"nome": "Burguer King", "tempo": "29"}
    ]
    
    for chave in dados_restaurantes:
        dados = chave, dados_restaurantes
        
    print(dados)
        
   
            
    
    
def mensagem(restaurante, tempo):
    retorno = f'''
        ********* Tempo de Espera **********
        
        *** O restaurante {restaurante} entrega em {tempo}min. ***
        
        ************* Obrigado *************
    '''
    print(textwrap.dedent(retorno))
    
        
def main():
    nome = ""
    tempo = "" 
    while True:
        options = menu()
        
        if options == "0":
            print('Fazer Pedido')

        elif options == "1":
            tempo_entrega(nome, tempo)
            
        elif options == "2":
            print('Consultar Cardápio')
            
        elif options == "2":
            print('Outros')
            
        elif options == "S" or options == "s":
            break
        
        else:
            print('\n### Opção inválida! ###')


main()


# ToDo: Imprimir a saída no padrão definido no enunciado deste desafio.
# Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.
# Deixar pronto para melhorias



header = '''
    *********** Opções ***********
    [0] Macdonalds 08
    [1] Burger King 03
    [2] KFC 25
    [S] Para sair
    
    *********** ______ ***********
    '''


footer = '''
    *********** ______ ***********
    
        Você saiu...
        Volte sempre!
        
    *********** ______ ***********
    '''
 

def entregas(nome_restaurante):
    nome_restaurante = input('Escolha uma opção: ')
    
    return nome_restaurante


def mensagem(restaurante, tempo_entrega):
    return print(f'O restaurante {restaurante} entrega em {tempo_entrega} minutos.')
    

def main():
    
    print(header)
    
    
    nome_restaurante = ''
    tempo_entrega = 0

    while True:
        
        options = entregas(nome_restaurante)
        
        if options == "0":
            restaurante = 'MacDonalds'
            tempo_entrega = 21
            mensagem(restaurante, tempo_entrega)
        
        elif options == "1":
            restaurante = 'Burguer King 03'
            tempo_entrega = 27
            mensagem(restaurante, tempo_entrega)
            
        elif options == "2":
            restaurante = 'KFC 25'
            tempo_entrega = 17
            mensagem(restaurante, tempo_entrega)
            
        elif options == 's' or options == 'S':
            print(footer)
            break
        
        else:
            print('Ação inválida, por favor, entre em contato com o sac.')
            print(footer)

main()

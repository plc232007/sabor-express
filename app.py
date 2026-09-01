import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False, },
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True, },
                {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False, }

] # Para que os dados sejam mantidos seria necessário um banco de dados, como ele não existe, o que mantém é somente o que existe na execução

def exibir_nome_do_programa():

    print ("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ """)

def exibir_opcoes():

    print ("1. Cadastrar restaurante")
    print ("2. Listar restaurante")
    print ("3. Ativar restaurante")
    print ("4. Sair \n")

def finalizar_app():
    exibir_subtitulo ('Finalizando o app')

def voltar_ao_menu():
    input ("\nDigite uma tecla para voltar ao menu: ")
    main()

def opcao_invalida():
    print ("Opção Inválida!")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    print (texto)

def cadastrar_novo_restaurante():

    exibir_subtitulo ("""

░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ╚═╝
██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ░░░
██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ░░░
╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██╗
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═╝

""")

    nome_restaurante = input("Qual o nome do restaurante que vai ser cadastrado? ")
    categoria = input (f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = { 'nome': nome_restaurante,
                            'categoria':categoria,
                            'ativo': False }

    restaurantes.append(dados_do_restaurante)

    print (f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo ("""


██╗░░░░░██╗░██████╗████████╗░█████╗░░██████╗░███████╗███╗░░░███╗  ██╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝░██╔════╝████╗░████║  ╚═╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║██║░░██╗░█████╗░░██╔████╔██║  ░░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║  ░░░
███████╗██║██████╔╝░░░██║░░░██║░░██║╚██████╔╝███████╗██║░╚═╝░██║  ██╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ╚═╝
""")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']


        print (f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu()

def escolher_opcao():
    try: # assim o código não quebra, ele apresenta para o user uma mensagem em caso de erro.
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida ()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()



import os

restaurantes = ["Caju Limão", "Savassi", "Rota do Churrasco"] # Para que os dados sejam mantidos seria necessário um banco de dados, como ele não existe, o que mantém é somente o que existe na execução

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
    os.system('clear')
    print ('Finalizando o app')

def opcao_invalida():
    print ("Opção Inválida!")
    input ("Digite uma tecla para voltar ao menu pricipal: ")
    main()

def cadastrar_novo_restaurante():

    os.system('clear')

    print ("""

░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ╚═╝
██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ░░░
██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ░░░
╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██╗
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═╝

""")

    nome_restaurante = input("Qual o nome do restaurante que vai ser cadastrado? ")
    restaurantes.append(nome_restaurante)
    print (f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    input ("Digite uma tecla para voltar ao menu principal: ")
    main()

def listar_restaurantes():
    os.system('clear')

    print ("""


██╗░░░░░██╗░██████╗████████╗░█████╗░░██████╗░███████╗███╗░░░███╗  ██╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝░██╔════╝████╗░████║  ╚═╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║██║░░██╗░█████╗░░██╔████╔██║  ░░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║  ░░░
███████╗██║██████╔╝░░░██║░░░██║░░██║╚██████╔╝███████╗██║░╚═╝░██║  ██╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ╚═╝
""")

    for restaurante in restaurantes:
        print ("- ", restaurante)

    input ("\nDigite uma tecla para voltar ao menu principal: ")
    main()

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



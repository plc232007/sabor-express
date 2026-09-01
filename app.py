import os

from restaurantes import (restaurantes,
                          cadastrar_restaurante,
                          alternar_estado,
                          filtrar_restaurantes,
                          listar_categorias)


def exibir_nome_do_programa():

    print ("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ """)


def exibir_opcoes():

    print ("\n1. Cadastrar restaurante")
    print ("2. Listar restaurantes")
    print ("3. Ativar/desativar restaurante")
    print ("4. Sair \n")


def exibir_subtitulo(texto):
    os.system('clear')
    print (texto)
    print ()


def voltar_ao_menu():
    input ("\nDigite uma tecla para voltar ao menu: ")


def opcao_invalida():
    print ("Opção Inválida!")
    voltar_ao_menu()


def finalizar_app():
    exibir_subtitulo ('Finalizando o app...')


def cadastrar_novo_restaurante():

    exibir_subtitulo ("""

░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ╚═╝
██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ░░░
██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ░░░
╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██╗
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═╝
""")

    nome_restaurante = input ("Qual o nome do restaurante que vai ser cadastrado? ")
    categoria = input (f'Digite o nome da categoria do restaurante {nome_restaurante}: ')

    deu_certo, mensagem = cadastrar_restaurante(nome_restaurante, categoria)

    print (f'\n{mensagem}')

    voltar_ao_menu()


def listar_restaurantes():
    exibir_subtitulo ("""


██╗░░░░░██╗░██████╗████████╗░█████╗░░██████╗░███████╗███╗░░░███╗  ██╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝░██╔════╝████╗░████║  ╚═╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║██║░░██╗░█████╗░░██╔████╔██║  ░░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║  ░░░
███████╗██║██████╔╝░░░██║░░░██║░░██║╚██████╔╝███████╗██║░╚═╝░██║  ██╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ╚═╝
""")

    categoria = input ('Filtrar por categoria (enter para ver todos): ')

    encontrados = filtrar_restaurantes(categoria)

    if not encontrados:
        print (f'\nNenhum restaurante encontrado. Categorias disponíveis: {", ".join(listar_categorias())}')
        voltar_ao_menu()
        return

    print (f"\n{'Nome'.ljust(25)}{'Categoria'.ljust(20)}{'Status'}") # ljust deixa as colunas alinhadas
    print ('-' * 55)

    for restaurante in encontrados:
        status = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print (f"{restaurante['nome'].ljust(25)}{restaurante['categoria'].ljust(20)}{status}")

    print (f'\nTotal: {len(encontrados)} de {len(restaurantes)} restaurantes')

    voltar_ao_menu()


def alternar_estado_restaurante():
    exibir_subtitulo ('Alterando o estado do restaurante:')

    nome_restaurante = input ('Digite o nome do restaurante que deseja alterar o estado: ')

    deu_certo, mensagem = alternar_estado(nome_restaurante)

    print (f'\n{mensagem}')

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
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
                return False # avisa o main que é hora de parar o loop
            case _:
                opcao_invalida ()
    except ValueError: # antes o except pegava qualquer erro, inclusive os que eu preciso enxergar
        opcao_invalida()

    return True


def main():
    continuar = True

    while continuar: # troquei a recursão por um loop: antes cada menu empilhava uma chamada nova de main()
        os.system('clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        continuar = escolher_opcao()


if __name__ == '__main__':
    main()

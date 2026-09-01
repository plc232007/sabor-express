# Aqui ficam os dados e as regras do sistema.
# Separei do app.py para que o terminal e o site usem exatamente as mesmas funções.

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Banana', 'categoria': 'Japonesa', 'ativo': False}

] # Para que os dados sejam mantidos seria necessário um banco de dados, como ele não existe, o que mantém é somente o que existe na execução


def cadastrar_restaurante(nome, categoria):
    nome = nome.strip()
    categoria = categoria.strip()

    if not nome or not categoria:
        return False, 'Nome e categoria não podem ficar vazios!'

    if buscar_restaurante(nome):
        return False, f'O restaurante {nome} já está cadastrado!'

    restaurantes.append({'nome': nome,
                         'categoria': categoria,
                         'ativo': False})

    return True, f'O restaurante {nome} foi cadastrado com sucesso!'


def buscar_restaurante(nome):
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome.strip().lower(): # lower() para o usuário não precisar acertar as maiúsculas
            return restaurante

    return None


def alternar_estado(nome):
    restaurante = buscar_restaurante(nome)

    if not restaurante:
        return False, 'O restaurante não foi encontrado!'

    restaurante['ativo'] = not restaurante['ativo'] # aqui ele inverte o estado

    if restaurante['ativo']:
        return True, f"O restaurante {restaurante['nome']} foi ativado com sucesso!"

    return True, f"O restaurante {restaurante['nome']} foi desativado com sucesso!"


def listar_categorias():
    categorias = []

    for restaurante in restaurantes:
        if restaurante['categoria'] not in categorias:
            categorias.append(restaurante['categoria'])

    return sorted(categorias)


def filtrar_restaurantes(categoria='', busca=''):
    encontrados = []

    for restaurante in restaurantes:
        combina_categoria = not categoria or restaurante['categoria'] == categoria
        combina_busca = not busca or busca.strip().lower() in restaurante['nome'].lower()

        if combina_categoria and combina_busca:
            encontrados.append(restaurante)

    return encontrados

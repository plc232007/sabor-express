# 🍔 Sabor Express

Gerenciador de restaurantes feito em Python, com **duas interfaces rodando sobre a mesma lógica**:
um menu no terminal e uma aplicação web em Flask.

## Estrutura

```
sabor-express/
├── restaurantes.py     # dados e regras de negócio (usado pelas duas interfaces)
├── app.py              # interface de terminal (CLI)
├── web.py              # interface web (Flask)
├── templates/
│   └── index.html
└── static/
    └── style.css
```

A ideia central foi tirar as regras de dentro da interface: `restaurantes.py` não sabe se está
sendo chamado por um `print()` ou por uma rota HTTP, então o terminal e o site nunca ficam
com comportamentos diferentes.

## Funcionalidades

- Cadastrar restaurantes (com validação de campo vazio e de nome duplicado)
- Listar restaurantes com filtro por categoria e busca por nome
- Ativar/desativar restaurantes
- Contadores de total, ativos e categorias

## Como rodar

**Terminal:**

```bash
python app.py
```

**Web:**

```bash
pip install -r requirements.txt
python web.py
```

Depois abra http://localhost:5000

## Próximos passos

Os dados ficam em memória, ou seja, somem quando o programa fecha. O próximo passo natural
é trocar a lista por um banco de dados (SQLite) sem precisar mexer nas interfaces — só em
`restaurantes.py`.

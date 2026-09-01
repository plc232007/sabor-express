from flask import Flask, render_template, request, redirect, url_for, flash

from restaurantes import (restaurantes,
                          cadastrar_restaurante,
                          alternar_estado,
                          filtrar_restaurantes,
                          listar_categorias)

app = Flask(__name__)
app.secret_key = 'sabor-express' # só para o flash das mensagens funcionar, não guarda nada sensível


@app.route('/')
def home():
    categoria = request.args.get('categoria', '')
    busca = request.args.get('busca', '')

    encontrados = filtrar_restaurantes(categoria, busca)
    ativos = [restaurante for restaurante in restaurantes if restaurante['ativo']]

    return render_template('index.html',
                           restaurantes=encontrados,
                           categorias=listar_categorias(),
                           categoria_atual=categoria,
                           busca_atual=busca,
                           total=len(restaurantes),
                           total_ativos=len(ativos))


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome', '')
    categoria = request.form.get('categoria', '')

    deu_certo, mensagem = cadastrar_restaurante(nome, categoria)

    flash(mensagem, 'sucesso' if deu_certo else 'erro')

    return redirect(url_for('home'))


@app.route('/alternar/<nome>', methods=['POST'])
def alternar(nome):
    deu_certo, mensagem = alternar_estado(nome)

    flash(mensagem, 'sucesso' if deu_certo else 'erro')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

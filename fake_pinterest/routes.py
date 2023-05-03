# criar as rotas do site
from flask import render_template, url_for
from fake_pinterest import app
from flask_login import login_required
from fake_pinterest.forms import FormLogin, FormCriarConta

@app.route('/', methods=["GET", "POST"])
def home_page():
    formLogin = FormLogin()
    return render_template('home_page.html', form=formLogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    formCriarConta = FormCriarConta()
    return render_template("criar_conta.html", form=formCriarConta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
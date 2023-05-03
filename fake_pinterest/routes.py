# criar as rotas do site
from flask import render_template, url_for
from fake_pinterest import app
from flask_login import login_required

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
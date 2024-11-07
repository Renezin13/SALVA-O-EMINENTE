from flask import render_template, Blueprint, url_for, request, flash, redirect
from flask_login import login_required
from models.user import User
from werkzeug.security import generate_password_hash

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
@login_required
def index():
    return render_template('users/index.html', users=User.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']

        if not email or not senha:
            flash('Email e senha são obrigatórios')
        else:
            hashed_password = generate_password_hash(senha)
            user = User(nome=nome, email=email, senha=hashed_password)
            user.save()
            return redirect(url_for('users.index'))
    
    return render_template('users/register.html')

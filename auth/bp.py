from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from models.user import User

# Configurando o blueprint e o login manager
auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', url_prefix='/auth')
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Validar o usuário com base no e-mail e senha
        user = User.find(email=email)
        if user and check_password_hash(user.senha, senha):  # Presume-se que `senha` esteja armazenada de forma segura
            login_user(user)
            return redirect(url_for('books.index'))  # Redireciona para a página de livros após o login
        else:
            flash('Credenciais inválidas.')
    
    return render_template('login.html')

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

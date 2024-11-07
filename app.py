from flask import Flask
from controllers import users, books
from auth.bp import auth_bp
from auth.bp import login_manager

app = Flask(__name__)

# Configurar chave secreta necessária para sessões e login
app.secret_key = 'sua_chave_secreta'

# Inicializar o login manager no app
login_manager.init_app(app)

# Registrar blueprints
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return "<h1>Bem-vindo ao Sistema</h1>"

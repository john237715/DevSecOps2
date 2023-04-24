# Importar módulos necessários
from flask import Flask

# Criar uma instância do aplicativo Flask
app = Flask(__name__)

# Definir uma rota para a página inicial
@app.route('/')
def home():
    return 'Olá, mundo! Esta é uma aplicação web básica em Python usando o Flask.'

# Executar o aplicativo na porta 5000 (ou em outra porta de sua escolha)
    if __name__ == '__main__':


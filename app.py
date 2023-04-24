from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Define a rota padrão
@app.route('/')
def hello():
    return 'Hello, World!'

# Executa a aplicação em modo de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)

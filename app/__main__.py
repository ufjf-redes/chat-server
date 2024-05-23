from flask import Flask, request, Response
from middleware import cria_middleware
from validacao import validar_nome_cliente
from shared import clients_dict

app = Flask(__name__)
cria_middleware(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/me-registrar")
def me_registrar():
    client_name = request.environ.get('client_name')
    client_address = request.form.get('address')
    if(not client_address):
        return "Endereço não encontrado no corpo da requisição", 404
    
    resp = Response(status=200)
    if(clients_dict.get(client_name)):
        resp.data = "O cliente já estava registrado e foi sobrescrito"
    clients_dict[client_name] = client_address
    
    return resp

@app.get("/lista-clientes")
def lista_clientes():
    client_name = request.environ.get('client_name')
    return [cliente for cliente in list(clients_dict.keys()) if not client_name or cliente != client_name] 

@app.get("/obter-cliente/<nome>")
def obter_cliente(nome: str):
    if not validar_nome_cliente(nome): return "Nome inválido", 404
    cliente = clients_dict.get(nome)
    if not cliente: return "Não encontrado", 400
    return cliente

if __name__ == "__main__":
    app.run(debug=True)
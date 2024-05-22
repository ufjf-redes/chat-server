from flask import Flask, request, Response

clientsDict = dict()

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/registrar-cliente")
def registrarCliente():
    clientName: str = request.form.get('name')
    clientAddress: str = request.form.get('address')
    if (not clientName or not clientName.isidentifier()): 
        return "Nome de cliente inválido", 404
    if(not clientAddress):
        return "Endereço não encontrado no corpo da requisição", 404
    
    resp = Response(status=200)
    if(clientsDict.get(clientName)):
        resp.data = "O cliente já estava registrado e foi sobrescrito"
    clientsDict[clientName] = clientAddress
    
    return resp

@app.get("/lista-clientes")
def listaClientes():
    return list(clientsDict.keys())

if __name__ == "__main__":
    app.run(debug=True)
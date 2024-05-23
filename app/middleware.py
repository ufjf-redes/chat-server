from flask import Flask, request
from validacao import validar_nome_cliente
import shared

endpoints_nao_protegidos = ['me_registrar']

def cria_middleware(app: Flask):
  @app.before_request
  def verifica_nome_cliente():
    client_name = request.headers.get("client-name")
    if not validar_nome_cliente(client_name): return "Cliente sem nome", 401
    # if request.endpoint not in endpoints_nao_protegidos and not shared.clients_dict.get(client_name): return "Cliente desconhecido", 401
    request.environ['client_name'] = client_name
    
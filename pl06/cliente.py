import requests
import json

r = requests.get("http://localhost:5000/aluno/25")
print(r.status_code)
print(r.content.decode())
print(r.headers)
print("****")

dados = {"numero": 123, "nome": "Carabino Tiro Certo", "idade": 18}
r = requests.put("http://localhost:5000/notas", json=dados)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print("****")

notas = {"numero_aluno": 123, "ano": "1988/1989", "cadeira": "AD", "nota": 20}
r = requests.post("http://localhost:5000/notas", json=notas)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print("****")

pesquisa = {"ano": "1988/1989", "cadeira": "AD"}
r = requests.get("http://localhost:5000/notas", json=pesquisa)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print("****")

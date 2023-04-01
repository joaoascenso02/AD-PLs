import requests
import json
import sqlite3

con = sqlite3.connect("notas.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS dados")
cur.execute("DROP TABLE IF EXISTS notas")

cur.execute("CREATE TABLE dados(numero, nome, idade)")
cur.execute("CREATE TABLE notas(numero_aluno, ano, cadeira, nota)")

cur.execute("""
    INSERT INTO dados VALUES
        (123, "Carabino Tiro Certo", 18)
""")

# commit depois de cada insert?
con.commit()

cur.execute("""
    INSERT INTO notas VALUES
        (123, "1988/1989", "AD", 20)
""")

r = requests.get('http://localhost:5000/aluno/25')
print(r.status_code)
print(r.content.decode())
print(r.headers)
print('***')

dados = {'numero': 123, 'nome': 'Carabino Tiro Certo', 'idade': 18}

r = requests.put('http://localhost:5000/aluno', json=dados)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print('***')

notas = {'numero_aluno': 123, 'ano': '1988/1989', 'cadeira': 'AD', 'nota': 20}

r = requests.post('http://localhost:5000/notas', json=notas)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print('***')

pesquisa = {'ano': '1988/1989', 'cadeira': 'AD'}
r = requests.get('http://localhost:5000/notas', json=pesquisa)
print(r.status_code)
print(r.content.decode())
print(r.headers)
print('***')

con.close()
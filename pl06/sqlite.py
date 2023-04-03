import sqlite3
from os.path import isfile


def connect_db(db_name) -> None:
    is_db = isfile(db_name)

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    if not is_db:
        cursor.execute("""
            CREATE TABLE notas(numero_aluno INTEGER, ano TEXT, cadeira TEXT, nota INTEGER, PRIMARY KEY(numero_aluno, ano, cadeira));
        """)

        cursor.execute("""
            CREATE TABLE aluno(numero INTEGER, nome TEXT, PRIMARY KEY (numero));
        """)

    return connection, cursor


um_registo = (123, "2021/2022", "AD", 20)
varios_registos = [
    (1000, "2021/2022", "AD", 10),
    (1000, "2021/2022", "ITW", 10),
    (1001, "2021/2022", "AD", 17),
    (1001, "2021/2022", "ITW", 17)
]

if __name__ == "__main__":
    conn, cursor = connect_db("notas.db")

    cursor.execute("""
        INSERT INTO notas VALUES (?, ?, ?, ?)
    """, um_registo)
    conn.commit()

    cursor.executemany("""
        INSERT INTO notas VALUES (?, ?, ?, ?)
    """, varios_registos)
    conn.commit()

    cursor.execute("SELECT * FROM notas")
    # fazer query e obter todos os resultados
    todos = cursor.fetchall()
    print("Todos: ", todos)

    cursor.execute("SELECT * FROM notas")
    # Fazer query e obter um a um
    registo = cursor.fetchone()
    while registo:
        print("Mais um: ", registo)
        registo = cursor.fetchone()

    cursor.execute("SELECT * FROM notas")
    # Fazer query e obter em grupos
    registos = cursor.fetchmany(size=2)
    while registos:
        print("Grupo ", registos)
        registos = cursor.fetchmany(size=2)

    conn.close()

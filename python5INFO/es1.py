# import psycopg2
# from datetime import datetime 

# DB_CONFIG = {
#     "dbname":"newdb",
#     "user":"postgres",
#     "host" :"localhost",
#     "port": "5432"
# }

# def connect():
#     return psycopg2.connect(**DB_CONFIG)

# def ricovero_paziente():
#     cod = str(input("Codice paziente: "))
#     nome = str(input("Nom: "))
#     cognome = str(input("Cog: "))
#     data_d = input("data rico: ")
#     camera = int(input("Numero camera: "))

#     query = "INSERT INTO Paziente(cod,nome,cognome,data_d,camera) values (%s,%s,%s,%s,%s)" 

      
#     conn = connect()
#     cur = conn.cursor()
#     cur.execute(query, (data_d,cod))
#     conn.commit()
#     print("Nascita Registrata!")
#     cur.close()
#     conn.close()

# def elenco_neonati_mamma():              
#     data = input("inserisci data limite (aaaa-mm-dd): ")
#     query = """ 
#         SELECT n.nome,p.nome,p.cognome
#         FROM neonato n
#         JOIN paziente p ON  n.mamma=
    
#     """
import psycopg2
from datetime import datetime

DB_CONFIG = { # configurazione connessione al database
    "dbname": "Ospedale",
    "user": "postgres",
    "password": "qwe123",
    "host": "localhost",
    "port": "5432"
}

def connect():
    return psycopg2.connect(**DB_CONFIG)

def ricovero_paziente():
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    data_r = input("Data Ricovero (AAAA-MM-DD): ")
    camera = int(input("Numero camera: "))

    query = """
        INSERT INTO Paziente (nome, cognome, data_ricovero, camera)
        VALUES (%s, %s, %s, %s)
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute(query, (nome, cognome, data_r, camera))
    conn.commit()

    print("Ricovero registrato!")

    cur.close()
    conn.close()

def dimissione_paziente():
    cod = input("Codice Paziente da dimettere: ")
    data_d = datetime.now().strftime('%Y-%m-%d')

    query = """
        UPDATE Paziente SET data_dimissione = %s 
        WHERE codice_paziente = %s
    """
    
    conn = connect()
    cur = conn.cursor()

    cur.execute(query, (data_d, cod))
    conn.commit()

    print("Ricovero dimesso!")
    cur.close()
    conn.close()

def nascita_neonato():
    nome = input("Nome: ")
    data_n = input("Data Nascita (AAAA-MM-DD): ")
    genere = input("Genere (M/F): ")
    mamma = input("Codice Mamma (Paziente): ")

    query = """
        INSERT INTO Neonato(nome, data_nascita, genere, mamma) 
        VALUES (%s, %s, %s, %s)
    """

    conn = connect()
    cur = conn.cursor()

    cur.execute(query, (nome, data_n, genere, mamma))
    conn.commit()

    print("Bambino registrato!")
    cur.close()
    conn.close()

def elenco_neonati_mamma():
    data = input("Inserisci data limite (AAAA-MM-DD): ")

    query = """
        SELECT n.nome, p.nome, p.cognome
        FROM neonato n
        JOIN Paziente p ON n.mamma = p.codice_paziente
        WHERE n.data_nascita > %s
    """

    conn = connect()
    cur = conn.cursor()

    cur.execute(query, (data))

    for row in cur.fetchall():
        print(f"Neonato: {row[0]} | Mamma: {row[1]} {row[2]}")

    cur.close()
    conn.close()

ricovero_paziente()
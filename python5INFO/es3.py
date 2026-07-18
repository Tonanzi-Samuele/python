import psycopg2

from psycopg2 import Error


def persone():
    conn = None


    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="qwe123"
        )
        conn.autocommit = True
        cur = conn.cursor()
    
        cur.execute("CREATE DATABASE if NOT exists persone")
        print("DB created!")
        
        cur.close()
        conn.close()


    except (Exception,Error) as error:
        print("ciao")

    
    
if __name__ == "__main__":
    persone()

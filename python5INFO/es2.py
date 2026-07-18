import psycopg2

from psycopg2 import Error


def gestore_concerto():
    conn = None


    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="qwe123"
        )
        conn.autocommit = True
        cur = conn.cursor()
    
        cur.execute("DROP DATABASE IF EXISTS concerto_maggio")
        cur.execute("CREATE DATABASE concerto_maggio")
        print("DB created!")
        

        cur.close()
        conn.close()


    except (Exception,Error) as error:
        print("ciao")

    
    
if __name__ == "__main__":
    gestore_concerto()

import psycopg2
from config import config

def get_phonebook_option(n): 
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params) 

        cur = conn.cursor()
        cur.callproc('get_phonebook_option', (n,))

        row = cur.fetchone()
        while row is not None: 
            print(row)
            row = cur.fetchone()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)
    finally: 
        if conn is not None: 
            conn.close()

get_phonebook_option(5)
        
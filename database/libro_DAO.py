from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_libri_filtrati_from_db(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor()
            query = f"""SELECT l.* 
                        FROM libro l, biblioteca b
                        WHERE l.id_biblioteca=b.id 
                        AND b.nome=COALESCE(%s, b.nome) AND l.genere=COALESCE(%s, l.genere)"""

            cursor.execute(query, (biblioteca, genere))
            for row in cursor:
                    libro = Libro(*row)
                    result.append(libro)
            cursor.close()
            cnx.close()
            return result
        else:
            print("connessione al database fallita.")
            return None

    def read_generi_from_db(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT DISTINCT genere FROM libro"
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
            cursor.close()
            cnx.close()
            return result
        else:
            print("connessione al database fallita.")
            return None



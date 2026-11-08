from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def read_biblioteche_from_db(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor()
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Connessione al database fallita.")
            return None




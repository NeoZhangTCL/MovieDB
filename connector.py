from flask import  Flask
import mysql.connector

class connector():
    def __init__(self, user, password, database):
        self.cnx = mysql.connector.connect(user=user, password=password, database=database)

    def get(query, **kwargs):
        try:
            cursor = self.cnx.cursor(buffered=True)
            cursor.execute(query, **kwargs)
            res = cursor.fetchall()
            self.cnx.commit()
            self.cnx.close()
            return res
        except Exception as error:
            return str(error)

    def sqlSetter(query):
        try:
            cursor = self.cnx.cursor(buffered=True)
            cursor.execute(query, **kwargs)
            self.cnx.commit()
            self.cnx.close()
            return 'success'
        except Exception as error:
            return str(error)

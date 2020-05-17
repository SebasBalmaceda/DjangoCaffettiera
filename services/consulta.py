import sqlite3


conector = sqlite3.connect('db.sqlite3')  #conector a la base

cursor = conector.cursor() #indicador de la consulta, similar al trigger

cursor.execute('SELECT * FROM services_service') #asi se hace un select en sqlite3

rows =cursor.fetchall()

conector.close()#lo utlimo se cierra la conexion

def return_data_from_database():
    return rows

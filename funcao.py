import mysql.connector


class Ocorrencia:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ouvidoria"

    )


    cursor = connection.cursor()


    def inserir(self, tipo, comentario):
       
            sql = 'INSERT INTO ocorrencia (tipo, comentario) values (%s, %s)'
            data = (tipo, comentario)
       

            self.cursor.execute(sql, data)
            self.connection.commit()


    def listar_itens(self, tipo):
        pass


    def apagar_tudo(self):
        pass


    def apagar_especifico(self, ouvidoria, parametro):
        pass

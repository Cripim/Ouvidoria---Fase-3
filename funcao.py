import mysql.connector

class Ocorrencia:
    #Entrando no banco de dados criado no Workbench
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ouvidoria"

    )


    cursor = connection.cursor()


    def inserir(self, tipo, comentario):
        
            #Essa função será responsável por inserir dados da ocorrência (elogio, reclamações, ideias) do input criado na main direto no banco de dados.

            sql = 'INSERT INTO ocorrencia (tipo, comentario) values (%s, %s)'
            data = (tipo, comentario)
       

            self.cursor.execute(sql, data)
            self.connection.commit()


    def listar(self):
        #Essa função será responsável por listar as ocorrências inseridas no Banco de Dados.
        sql = "SELECT * FROM ocorrencia"    
        self.cursor.execute(sql)
        listaOcorrencias = self.cursor.fetchall()
        for i in listaOcorrencias:
         print(i)
    def apagarEspecifico(self, id):
        sql = 'DELETE FROM ocorrencia WHERE id = (%s)'
        data = (id,)
        
        self.cursor.execute(sql, data)
        self.connection.commit()

    
    def apagarCategoria(self, tipo):
        sql = 'DELETE FROM ocorrencia WHERE tipo = %s'
        data = (tipo,)
       
        
        self.cursor.execute(sql, data)
        resultado = self.cursor.fetchall()
        return len(resultado)
    def apagarTabela(self):
        sql = "TRUNCATE TABLE ocorrencia"
        

        self.cursor.execute(sql)
        self.connection.commit()

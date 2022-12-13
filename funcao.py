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
        #Essa função será responsável por retornar todos os dados das tabaelas.
        sql = "SELECT * FROM ocorrencia"    
        self.cursor.execute(sql)
        listaOcorrencias = self.cursor.fetchall()
        for i in listaOcorrencias:
         print(f"ID --> {i[0]} --> Tipo --> {i[1]} -->  Comentário --> {i[2]}")


    def listarEspecifico(self,tipo):
        #Essa função será responsável por listar os dados específicos de cada tabaela.
        sql = "SELECT * FROM ocorrencia WHERE tipo = (%s)" 
        data = (tipo,)   
        self.cursor.execute(sql,data)
        listaOcorrencias = self.cursor.fetchall()
        for i in listaOcorrencias:
          print(f"ID --> {i[0]} --> Tipo --> {i[1]} -->  Comentário --> {i[2]}")

    def apagarEspecifico(self, id):
        #Essa função será responsável por apagar os dados específicos de cada tabaela.
        sql = 'DELETE FROM ocorrencia WHERE id = (%s)'
        data = (id,)
        
        self.cursor.execute(sql, data)
        self.connection.commit()

    
    def apagarCategoria(self, tipo):
        #Essa função será responsável por apagar tabelas específicos.
        sql = 'DELETE FROM ocorrencia WHERE tipo = (%s)'
        data = (tipo,)
        self.cursor.execute(sql, data)
        self.connection.commit()

    def apagarTudo(self):
        #Essa função será responsável por apagar todos os dados das tabelas.
        sql = "TRUNCATE TABLE ocorrencia"

        self.cursor.execute(sql)
        self.connection.commit()

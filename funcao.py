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


    def listar_itens(self, lista):
        if lista == 'elogio':
            sql = "SELECT * FROM ocorrencia WHERE tipo = 'elogio'"
            self.cursor.execute(sql)
            mostra = self.cursor.fetchall()
            for elogio in enumerate(mostra):
                print(f'{elogio [0]} | {elogio [1]}')

        elif lista == 'reclamação':
            sql = "SELECT * FROM ocorrencia WHERE tipo = 'reclamação'"
            self.cursor.execute(sql)
            mostra = self.cursor.fetchall()
            for reclamacao in enumerate():
                print(f'{reclamacao [0]} | {reclamacao [1]}')
        elif lista == 'ideias':
            sql = "SELECT * FROM ocorrencia WHERE tipo = 'ideias'"
            self.cursor.execute(sql)
            mostra= self.cursor.fetchall()
            for ideias in enumerate(mostra):
                print(f'{ideias [0]} | {ideias [1]} ')
    def apagar_tudo(self):
        pass


    def apagar_especifico(self, ouvidoria, parametro):
        pass

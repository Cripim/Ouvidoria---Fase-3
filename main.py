import funcao

m = funcao.Ocorrencia()

print(
  "Olá! Seja muito bem vindo ao nosso sistema de ouvidoria da unifacisa! :D")
nome = input("Para começarmos, digite seu nome:")
print(f"Bem-vindo à nossa Ouvidoria Unifacisa, {nome}!")

print("Para começarmos, selecione uma das opções abaixo:")



rodando = True
while rodando:


  print("[1] Inserir Elogios")
  print("[2] Inserir Reclamações")
  print("[3] Inserir Ideias")
  print("[4] Listar Itens")
  print("[5] Excluir Itens")
  print("[6] Sair do Sistema")

  ouvidoriaFacisa = input(
      "Digite 1 para inserir algum elogio, 2 para registrar alguma reclamação, 3 para sugerir ideias, 4 para listar itens, 5 para exluir itens ou 6 para sair do sistema: "
    )

  if (ouvidoriaFacisa == '1'):
      elogio = input("Insira seu elogio aqui:")
      m.inserir('elogio', elogio)
      print()
      print('Elogio registrado!')  
      print()
  elif(ouvidoriaFacisa == '2'):
    reclamacao = input("Insira sua reclamação aqui:")
    m.inserir('reclamação', reclamacao)
    print()
    print('Reclamção registrada!')
    print()
    
  elif(ouvidoriaFacisa == '3'):
    ideias = input("Insira sua sugestão/ideia aqui:")
    m.inserir('ideias', ideias)
    print()
    print('Ideia registrada!')
    print()
    

  
  elif(ouvidoriaFacisa == '4'):
      print("Você está prestes a listar todas as ocorrências registradas.")
      print()
      m.listar()
      print()

      
  elif (ouvidoriaFacisa == '5'):
        print('')
        print('1 - Apagar comentário especifico')
        print('2 - Apagar tabela específica')
        print('3 - Apagar tudo')
        print('')
        apagar = input('Qual opção deseja: ')

        if (apagar == '1'):
         print('elogio(1), reclamação (2), ideias(3)')
         comentario = input('digite a opção para apagar: ')
         if comentario == '1':
             
              m.listarEspecifico("elogio")
              parametro = int(input('digite o indice que deseja apagar da lista de elogio:'))
              m.apagarEspecifico(parametro)
              print("Ocorrência específica excluída!")
              print()


         elif(comentario == '2'):
           
              m.listarEspecifico("reclamação")
              parametro = int(input('digite o indice que deseja apagar da lista de reclamação:'))
              m.apagarEspecifico(parametro)
              print("Ocorrência específica excluída!")
              print()
         elif (comentario == '3'):
              m.listarEspecifico("sugestão")
              parametro = int(input('digite o indice que deseja apagar da lista de ideias:'))
              m.apagarEspecifico(parametro)
              print("Ocorrência específica excluída!")
              print()
        elif(apagar == '2'):
            print('Tabela elogio(1), tabela reclamação(2), tabela ideias(3)') 
            tipo = input('digite a opção para apagar: ')
            if (tipo == '1'):
            
              m.apagarCategoria('elogio')
              print("Tabela elogio excluída!")
              print()
            elif(tipo == '2'):
                
                m.apagarCategoria('reclamação')
                print("Tabela reclamação excluída!")
                print()

            elif(tipo== '3'):
                
                  m.apagarCategoria('ideias')
                  print("Tabela ideias excluída!")  
                  print()
        elif (apagar == '3'):
            print('Você excluiu todos os dados registrados!')
            print()
            m.apagarTudo()
            

  elif(ouvidoriaFacisa == '6'):
    rodando = False
    print("Você saiu do sistema! Volte sempre!")


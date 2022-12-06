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
      print('Para listar elogios (1), para listar reclamação (2), para listar ideias(3)')
      listar = input('Digite uma opção: ')

      if (listar == 1):
        print()
        m.listar_itens('elogio')
        print()
      elif (listar == 2):
        print()
        m.listar_itens("reclamação")
        print()
      elif(listar == 3):
        print()
        m.listar_itens("ideias")
        print()

   
  elif (ouvidoriaFacisa == '5'):
        print('')
        print('1 - Apagar comentário especifico')
        print('2 - Apagar tudo')
        print('')
        apagar = int(input('Qual opção deseja: '))

        if (apagar == 2):
            m.apagar_tudo()
            print('')
            print('Você apagou tudo.')
            print(f"Itens restantes:{m.listaElogios},{m.listaReclamacao},{m.listaIdeias}")

        elif (apagar == 1):
            print('elogio(1), reclamação (2), sugestão(3)')
            apagar2 = input('digite a opção para apagar: ')
            if apagar2 == '1':
                
                parametro = int(input('digite o indice que deseja apagar da lista de elogio:'))
                m.apagarEspecifico(parametro)
                print("Ocorrência específica excluída!")
                
            if apagar2 == '2':
                
                parametro = int(input('digite o indice que deseja apagar da lista de reclamação:'))
                m.apagarEspecifico(parametro)
                print("Ocorrência específica excluída!")
            if apagar2 == '3':
                
                parametro = int(input('digite o indice que deseja apagar da lista de sugestão:'))
                m.apagar_especifico(parametro)
                print("Ocorrência específica excluída!")
  elif(ouvidoriaFacisa == '5'):
   rodando = False
   print("Você saiu do sistema! Volte sempre!")
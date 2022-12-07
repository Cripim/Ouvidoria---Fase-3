# Ouvidoria Unifacisa 

## Sobre

Este projeto consiste em uma Aplicação do Sistema Gerenciador de Banco de Dados (SGDB) MySQL na integração com o Sistema de Ouvidoria da Fase 2 do projeto. 
Nesta aplicação eu utilizei o SGDB MySQL para trabalhar com dados do sistemas executando funções básicas (CRUD).

O projeto foi proposto como avaliação da disciplina de Linguagem de Programação Estruturada do primeiro período de Sistemas de Informação da Unifacisa. 

# Como usar?

```bash
$ git clone https://github.com/Cripim/OuvidoriaFacisa
```


Dentro do MySQL Workbench crie uma nova conexão com o user _root_ e o password _root_, depois, crie as tabelas com os seguintes comandos:

```sql
CREATE DATABASE ouvidoria;

USE ouvidoria;

CREATE TABLE ocorrencia (
    
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo varchar(20),
    comentario VARCHAR(250)
    
);
```

Depois é só rodar o arquivo _main.py_ com:

```bash
$ python main.py
```

## Tecnologias Usadas:

- Python 3
- MySQL
 

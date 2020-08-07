'''
Arquivo de inicializacao que tem a responsabilidade de identificar se o banco de dados
locadora.db existe se nao ele ira cria-lo
'''
import os

try:

    #print('os.getcwd() = '+os.getcwd())
    current_path = os.getcwd() + '/classes/model/database/'

    # Validando a existência do banco de dados no diretório das classes do sistema
    if not os.path.exists(current_path + 'locadora.db'):
        print('Banco de dados n'+chr(227)+'o localizado')

        import sqlite3

        # Criando o banco de dados
        con = sqlite3.connect(current_path + 'locadora.db')
        cur = con.cursor()

        # Executando a criação das tabelas
        cur.execute(
            'CREATE TABLE carro(' \
            'id integer PRIMARY key AUTOINCREMENT,' \
            'placa varchar(7) not NULL,' \
            'cor varchar(20),' \
            'qtde_portas integer,' \
            'ano_fabricacao integer,' \
            'quilometragem integer,' \
            'valor_diaria float)')

        cur.execute(
            'CREATE TABLE cliente (' \
            'id integer PRIMARY key AUTOINCREMENT,' \
            'nome varchar(60) NOT NULL,' \
            'sexo varchar(1),' \
            'data_nascimento date NOT NULL,' \
            'cnh varchar(20),' \
            'data_vencimento_cnh date,' \
            'endereco varchar(200),' \
            'email varchar(100),' \
            'tel_celular varchar(15) NOT NULL )')

        cur.execute(
            'CREATE table locacao (' \
            'id integer PRIMARY key AUTOINCREMENT,' \
            'id_carro integer not NULL,' \
            'id_cliente INteger not null,' \
            'data_inicial date NOT NULL,' \
            'data_final date,' \
            'km_inicial integer NOT NULL,' \
            'km_final integer,' \
            'valor_total float,' \
            'FOREIGN KEY (id_carro) REFERENCES carro (id) on DELETE RESTRICT,' \
            'FOREIGN key (id_cliente) REFERENCES cliente (id) on DELETE RESTRICT)')

        # fechando a conexão
        con.close()

        print('Banco de dados criado com sucesso')

except Exception as e:
    print('Ocorreu uma falha na cria'+chr(231)+chr(227)+'o do banco de dados: ' + str(e))

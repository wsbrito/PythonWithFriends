import os

try:

    #print('os.getcwd() = '+os.getcwd())
    current_path = os.getcwd() + '/classes/model/database/'

    if not os.path.exists(current_path + 'locadora.db'):
        print('Banco de dados não localizado')

        import sqlite3

        con = sqlite3.connect(current_path + 'locadora.db')
        cur = con.cursor()

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

        con.close()

        print('Banco de dados criado com sucesso')

except Exception as e:
    print('Ocorreu uma falha na criação do banco de dados: ' + str(e))

CREATE TABLE carro(
  id integer PRIMARY key AUTOINCREMENT,
  placa varchar(7) not NULL,
  cor varchar(20),
  qtde_portas integer,
  ano_fabricacao integer,
  quilometragem integer,
  valor_diaria float
);

CREATE TABLE cliente (
  id integer PRIMARY key AUTOINCREMENT,
  nome varchar(60) NOT NULL,
  sexo varchar(1),
  data_nascimento date NOT NULL,
  cnh varchar(20),
  data_vencimento_cnh date,
  endereco varchar(200),
  email varchar(100),
  tel_celular varchar(15) NOT NULL
 );
 
CREATE table locacao (
  id integer PRIMARY key AUTOINCREMENT,
  id_carro integer not NULL,
  id_cliente INteger not null,
  data_inicial date NOT NULL,
  data_final date,
  km_inicial integer NOT NULL,
  km_final integer,
  valor_total float,
  FOREIGN KEY (id_carro) REFERENCES carro (id) on DELETE RESTRICT,
  FOREIGN key (id_cliente) REFERENCES cliente (id) on DELETE RESTRICT
);

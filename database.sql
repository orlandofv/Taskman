BEGIN TRANSACTION;
CREATE TABLE "usuarios" (
	'cod'	varchar(50) NOT NULL,
	'cliente'	varchar(50) NOT NULL,
	'obs'	varchar(255),
	'estado'	varchar(15),
	'func1'	varchar(15),
	'data'	date,
	'func2'	varchar(15),
	'data2'	date,
	'usuario'	varchar(50),
	'senha'	varchar(50),
	'admin'	varchar(10),
	PRIMARY KEY(cod);
);

CREATE TABLE clientes
(
  cod varchar(50) NOT NULL,
  nome varchar(255) NOT NULL,
  endereco varchar(255),
  sexo varchar(15),
  nacionalidade varchar(50),
  tipo_id varchar(20),
  numero_id varchar(20),
  nascimento text,
  validade_id text,
  emergencia varchar(255),
  apelido varchar,
  contactos varchar(255),
  email varchar(255),
  obs varchar(255),
  estado varchar(15),
  func1 varchar(15),
  'data' text,
  func2 varchar(15),
  data2 text
  primary key (cod);
  );

CREATE TABLE tarefas
(
	'cod'	TEXT NOT NULL UNIQUE,
	'tarefa' varchar(50)
	'descricao' varchar(255),
	'cliente' varchar(255),
	'data' text,
	'local' varchar(255),
	'aviso' text,
	'obs' varchar(255),
	PRIMARY KEY(cod);

CREATE TABLE 'factura' (
	'cod'	TEXT NOT NULL UNIQUE,
	tarefa varchar(50)
	descricao varchar(255),
	cliente varchar(255),
	data text,
	local varchar(255),
	aviso text,
	obs varchar(255),
	PRIMARY KEY(cod);
);
COMMIT;

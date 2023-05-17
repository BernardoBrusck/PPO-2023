create database Geraweb;
use Geraweb;

create table DB(
id int not null primary key auto_increment,
nome varchar(45) not null,
descricao varchar(45) not null
);

create table tables(
id int not null primary key auto_increment,
nome varchar(45),
id_projeto int not null,
foreign key (id_projeto) references projetos (id)
);

create table tuples(
id int not null primary key auto_increment,
primarykey boolean,
nome varchar(45),
tipo varchar(100),
notnull boolean,
foreinKey varchar(45),
id_tabela int not null,
foreign key (id_tabela) references tabelas (id)
);
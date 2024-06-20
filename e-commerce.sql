create database e_commerce;
use e_commerce;

create table produto (
id int auto_increment not null primary key,
nome varchar(50) not null,
preco DECIMAL(10,2) not null
);

insert into produto (nome,preco) values ('bola','200');

select*from produto;




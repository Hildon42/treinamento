create database audiovisual1

use audiovisual1

create table audiovisual(
id_audvis int primary key identity,
id_usuario int not null,
nomeaudivisual varchar(45) not null,
nome_tipoproduc varchar (20) not null,
nome_gen varchar (30) not null,
data_assis date not null
);
go
create table loginn(
id_login int primary key identity,
usuario varchar (40) not null,
senha varchar (40) not null
);
alter table audiovisual
   add constraint fk_audvios foreign key (id_usuario) references loginn (id_login);
-----------
drop table audiovisual;
go
drop table loginn;


update audiovisual set nome_produc = 'Document�rio' where id_audvis = 2
---------------------------------------
select * from audiovisual
delete from audiovisual
insert into loginn (usuario, senha, situacao_Login) 
values ('Nelson','54321','1');

Select id_login from loginn
where usuario = 'hildon' COLLATE SQL_Latin1_General_CP1_CS_AS
and senha = '12345' COLLATE SQL_Latin1_General_CP1_CS_AS
-----------------------------------------------
insert into audiovisual (id_usuario, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis)
values (1,'US','Filme','Terror', '2024-02-20')

select loginn.usuario as 'Usu�rio', audiovisual.nomeaudivisual as 'Nome do Filme', nome_tipoproduc as 'Tipo de produ��o', audiovisual.nome_gen as 'Genero', audiovisual.data_assis 'Data assistida' from audiovisual, loginn
where loginn.id_login = audiovisual.id_loginn
and loginn.id_login = 2
;
select loginn.usuario as 'Usu�rio', audiovisual.nomeaudivisual as 'Nome do Filme', nome_tipoproduc as 'Tipo de produ��o', audiovisual.nome_gen as 'Genero', audiovisual.data_assis 'Data assistida' from audiovisual, loginn
where loginn.id_login = audiovisual.id_loginn
and loginn.id_login = 1
and audiovisual.nome_tipoproduc = 'S�rie'


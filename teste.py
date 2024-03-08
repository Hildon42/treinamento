import pyodbc

dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=HILDON\SQLEXPRESS;"
    "DATABASE=audiovisual1;"
    )


conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")
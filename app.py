from flask import Flask, render_template, request, redirect, url_for
import pyodbc



app = Flask(__name__)




@app.route('/')
def index():
    

    dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=HILDON\SQLEXPRESS;"
    "DATABASE=audiovisual1;"
    "Trusted_Connection=yes;"
    )
    conexao = pyodbc.connect(dados_conexao)
    


    cursor = conexao.cursor()


    cursor.execute('SELECT * FROM audiovisual')
    audiovis = cursor.fetchall()
   
    cursor.close()
    conexao.close()
    return render_template('index.html', audiovisual=audiovis)


@app.route('/novo_audiovisual', methods=['GET', 'POST']) 
def novo_audiovisual():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nomeaudio = request.form['nomeaudivisual']
        nometipo = request.form['nome_tipoproduc']
        genero = request.form['nome_gen']
        data = request.form['data_assis']
        

        dados_conexao = (
        "DRIVER={SQL Server};"
        "SERVER=HILDON\SQLEXPRESS;"
        "DATABASE=audiovisual1;"
        "Trusted_Connection=yes;"
        )
        

        conexao = pyodbc.connect(dados_conexao)
        

        cursor = conexao.cursor()

        
        comando = f"""INSERT INTO audiovisual (usuario, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis) 
        VALUES 
             ('{usuario}', '{nomeaudio}', '{nometipo}', '{genero}', '{data}')"""
         
        
        
        
        cursor.execute(comando)
        cursor.commit()


        return redirect(url_for('index'))
    return render_template('novo_audiovisual.html')


@app.route('/limpar_audio')
def limpar_audio():


    dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=HILDON\SQLEXPRESS;"
    "DATABASE=audiovisual1;"
    "Trusted_Connection=yes;"
    )
    conexao = pyodbc.connect(dados_conexao)
    

    cursor = conexao.cursor()
    comando = """ DELETE FROM audiovisual """
    
    cursor.execute(comando)
    cursor.commit()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)






from flask import Flask, render_template, request, jsonify
import mysql.connector 

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Geraweb"
)

cursor = conexao.cursor()

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        database = request.form.get('titulo_projeto')
        description = request.form.get('descricao_projeto')
        print(database)
        print(description)
        # Inserir os valores na tabela "DB"
        sql = "INSERT INTO DB (nome, descricao) VALUES (%s, %s)"
        values = (database, description)
        cursor.execute(sql, values)
        conexao.commit()
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

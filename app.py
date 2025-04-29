from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Creación de base de datos y tabla
def init_database():
    conn = sqlite3.connect("Kardex.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS personas(
            id  INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nac TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

init_database()  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personas")
def personas():
   conn = sqlite3.connect("kardex.db")
#permite manejar los registros
   conn.row_factory = sqlite3.Row
   
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM personas ")
   personas = cursor.fetchall()
   return render_template("personas/index.html",personas = personas)
 
@app.route("/personas/create")
def create():
     return render_template("personas/create.html")

if __name__ == "__main__":
     
    app.run(debug=True)


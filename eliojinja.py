from flask import Flask, render_template

app = Flask(_name_)

@app.route ('/')
def saludar():
    return 'Mi dicionario de Slang Panameño! Elio Camarena'

@app.route ("/")
def index():
    titulo = "dicionario"
    palabra = ["xopa","mopri","parking","yala vida"]
    significado = ["saludo","primo","fiesta","asombro"]
    return render_template("index.html", titulo=titulo, palabra=palabra, significadi=significado) 

if _name=="main_":
    app.run(debug=True)

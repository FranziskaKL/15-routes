from flask import Flask, render_template

app  = Flask(__name__) #beliebige Zeichenkette hier wird Name des Moduls von Py als Name der Datei autom. bestimmt

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/big")
def big():
    return render_template("big.html")

@app.route("/bigger")
def bigger():
    return render_template("bigger.html")

if __name__== '__main__':
    app.run()

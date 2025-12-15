from flask import Flask, render_template, request, redirect
from todo import Zadatak

app = Flask(__name__)

zadaci = []

def siguran_index(index):
    return 0 <= index < len(zadaci)

@app.route("/")
def index():
    return render_template("index.html", zadaci=zadaci)

@app.route("/dodaj", methods=["POST"])
def dodaj():
    naziv = (request.form.get("naziv") or "").strip()
    opis = (request.form.get("opis") or "").strip()
    prioritet = request.form.get("prioritet") or "Srednji"

    if naziv:
        zadaci.append(Zadatak(naziv, opis, prioritet))

    return redirect("/")

@app.route("/zavrsi/<int:index>")
def zavrsi(index):
    if siguran_index(index):
        zadaci[index].oznaci_zavrsen()
    return redirect("/")

@app.route("/vrati/<int:index>")
def vrati(index):
    if siguran_index(index):
        zadaci[index].vrati_na_nezavrseno()
    return redirect("/")

@app.route("/obrisi/<int:index>")
def obrisi(index):
    if siguran_index(index):
        zadaci.pop(index)
    return redirect("/")

@app.route("/uredi/<int:index>")
def uredi_forma(index):
    if not siguran_index(index):
        return redirect("/")
    return render_template("uredi.html", zadatak=zadaci[index], index=index)

@app.route("/uredi/<int:index>", methods=["POST"])
def uredi_spremi(index):
    if not siguran_index(index):
        return redirect("/")

    naziv = (request.form.get("naziv") or "").strip()
    opis = (request.form.get("opis") or "").strip()
    prioritet = request.form.get("prioritet") or "Srednji"

    if naziv:
        zadaci[index].uredi(naziv, opis, prioritet)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False)

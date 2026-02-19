import sys
import os
import io
import contextlib
import importlib.util

from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _load(alias, filename):
    path = os.path.join(BASE_DIR, filename)
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


reklaam = _load("reklaam", "6.1. reklaam.py")
teler   = _load("teler",   "6.2. teler.py")
pidu    = _load("pidu",    "6.3. pidu.py")
mitmes  = _load("mitmes",  "6.4a. mitmes.py")
myndid  = _load("myndid",  "6.4b. myndid_versioon_2.py")
kuupaev = _load("kuupaev", "6.4c.kuupaev.py")

app = Flask(__name__)


@app.route("/")
def avaleht():
    return render_template("index.html")


@app.route("/reklaam", methods=["GET", "POST"])
def reklaam_leht():
    tulemus = None
    if request.method == "POST":
        mitu = int(request.form["mitu"])
        sisu = request.form["sisu"]
        read = [reklaam.banner(sisu) for _ in range(mitu)]
        tulemus = "\n".join(read)
    return render_template("reklaam.html", tulemus=tulemus)


@app.route("/teler", methods=["GET", "POST"])
def teler_leht():
    tulemus = None
    if request.method == "POST":
        kaugus = float(request.form["kaugus"])
        tulemus = str(teler.teleri_diagonaal(kaugus)) + " tolli"
    return render_template("teler.html", tulemus=tulemus)


@app.route("/pidu", methods=["GET", "POST"])
def pidu_leht():
    tulemus = None
    if request.method == "POST":
        guests = int(request.form["guests"])
        yes = int(request.form["yes"])
        tulemus = (
            "Maksimaalne eelarve: " + str(pidu.eelarve(guests)) + "\n"
            "Minimaalne eelarve: " + str(pidu.eelarve(yes))
        )
    return render_template("pidu.html", tulemus=tulemus)


@app.route("/mitmes", methods=["GET", "POST"])
def mitmes_leht():
    tulemus = None
    if request.method == "POST":
        arv = int(request.form["arv"])
        valjund = io.StringIO()
        with contextlib.redirect_stdout(valjund):
            i = 1
            while i <= arv:
                mitmes.tervitus(i)
                i += 1
        tulemus = valjund.getvalue()
    return render_template("mitmes.html", tulemus=tulemus)


@app.route("/myndid", methods=["GET", "POST"])
def myndid_leht():
    tulemus = None
    if request.method == "POST":
        failinimi = request.form.get("failinimi", "myndid.txt").strip()
        failinimi_täielik = os.path.join(BASE_DIR, failinimi)
        summa = myndid.pronksikarva_summa(failinimi_täielik)
        tulemus = "Pronksikarva müntide summa: " + str(summa) + " senti"
    return render_template("myndid.html", tulemus=tulemus)


@app.route("/kuupaev", methods=["GET", "POST"])
def kuupaev_leht():
    tulemus = None
    if request.method == "POST":
        kuupäev = request.form["kuupaev"]
        tulemus = kuupaev.kuupäev_sõnena(kuupäev)
    return render_template("kuupaev.html", tulemus=tulemus)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

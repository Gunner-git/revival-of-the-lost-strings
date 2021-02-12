from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder = 'template')

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/Other_instruments")
def Other_instruments():
    return render_template("/history.html")

@app.route("/rabab")
def rabab():
    return render_template("/rabab.html")

@app.route("/saranda")
def saranda():
    return render_template("/saranda.html")

@app.route("/sarangi")
def sarangi():
    return render_template("/sarangi.html")

@app.route("/dilruba")
def dilruba():
    return render_template("/dilruba.html")

@app.route("/taus")
def taus():
    return render_template("/taus.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template #importo, ademas de Flask, el metodo render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/portafolio")
def portafolio():
    return render_template("portafolio.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True) #para avisarle a mi aplicacion que estoy cambiando cosas y quiero que se reinicie cada vez q lo haga

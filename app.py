from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/AfricanKidsAtire")
def aficanKidz():
    return render_template("AfricanKidsAtire.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/hours")
def hours():
    return render_template("hours.html")


@app.route("/contactInfo")
def contactInfo():
    return render_template("ContactInfo.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/presenter")
def presenter():
    return render_template("presenter.html")

@app.route("/attendees")
def attendees():
    return render_template("attendees.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/ceu")
def ceu():
    return render_template("ceu.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port='4000')
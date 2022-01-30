from operator import methodcaller
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog", methods=["POST", "GET"])
def blog():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        comment = request.form["comment"]

        flash("Thanks for your feedback!")

    return render_template("blog.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        flash("Thanks for reaching out!")

    return render_template("contact.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

if __name__ == "__main__":
    app.run(debug=True)
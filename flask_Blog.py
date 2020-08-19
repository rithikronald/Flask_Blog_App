from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "41f1c4c9fdf59cd032fb0cdc3198dab4"

books = [
    {
        "author": "Robert kiyosaki",
        "bookName": "Rich dad Poor Dad",
        "datePublished": "March 12 2001",
        "description": "This book talks about the lessons the child learnt from his rich and poor dad . That made him wise and Rich",
    },
    {
        "author": "Robin Sharma",
        "bookName": "5 am Club",
        "datePublished": "March 12 2001",
        "description": "This books talks about the life lessons that had been practiced by the rich and inspirable people in the world and th importance of the habit of getting up early in the morning",
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", books=books)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register")


@app.route("/login")
def register():
    form = RegistrationForm()
    return render_template("login.html", title="Register")


if __name__ == "__main__":
    app.run(debug=True)


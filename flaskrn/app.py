from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    d = {"marcin": 15, "tomek": 20, "kacper": 50}
    # test
    return render_template("landing_page.html", my_dict=d)


if __name__ == "__main__":
    app.run(debug=True)
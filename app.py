from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
    return "<h1 style='color:red'>Hello World!</h1>"


@app.route("/contatti")
def contatti():
    return "Contattaci!"


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__Music Genre Classification__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__=="__Music Genre Classification__":

    app.run(debug=True)

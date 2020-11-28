from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World! This is first (root) page on EC2. This is a multi-page Website. Try /second, /third/subthird and /forth/---write a number here---"


@app.route("/second")
def second():
    return "This is the second page."


@app.route("/third/subthird")
def third():
    return "This is subthird page of third."


@app.route("/forth/<string:id>")
def forth(id):
    return f"You wrote {id} over there"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)


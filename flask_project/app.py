from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "").strip()
    if not name:
        message = "Please enter a valid name."
    else:
        message = f"Hello, {name}!"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

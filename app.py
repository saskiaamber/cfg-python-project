from flask import Flask, render_template

app = Flask("my_first_app")

@app.route("/")
def say_hello():
	return render_template("index.html")

app.run(debug=True)


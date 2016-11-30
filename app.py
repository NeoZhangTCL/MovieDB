from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    tag = "User"
    return render_template('index.html',user_tag=tag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

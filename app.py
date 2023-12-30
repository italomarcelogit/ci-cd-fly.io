from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', user=randint(1000, 2000))

@app.route("/qtde/<int:post_id>", methods=['GET'])
def qtde(post_id):
    return render_template('cupom.html', user=post_id, cupom=randint(2000, 20000))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
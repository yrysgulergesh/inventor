# Jinja, Templates 48 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('goods.txt', 'r', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)


@app.route('/add/', methods=["POST"])
def add():
    good = request.form["good"]
    f = open('goods.txt',  'a+', encoding='utf-8')
    f.write(good + "\n")
    f.close()
    return """
    <h1>Инвентарь пополнен</h1>
    <a href='/'>Домой</a>
    """
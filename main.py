from flask import Flask
from flask import render_template
import random
from random import choice

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/random_fact")
def random_fact():
    lst = [
        "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
        "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
        "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение."
    ]
    return f'<h1>{choice(lst)}</h1>'

@app.route("/password")
def password():
    lst = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()")
    password = ""
    for i in range(8):
        password += (random.choice(lst))
    return f'<h1>Пароль: {password}</h1>'

app.run(debug=True)

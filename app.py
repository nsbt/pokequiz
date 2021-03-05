# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.j2',
        message="第1問",
        question="うまれたときから　せなかに　しょくぶつの　タネが　あって　すこしずつ　おおきく　そだつ。　（『ポケモン ソード』より）",
        options=[
            {"name": "フシギダネ", "class_name": "correct_option"},
            {"name": "ゼニガメ", "class_name": "wrong_option"},
            {"name": "ヒトカゲ", "class_name": "wrong_option"},
            {"name": "ピカチュウ", "class_name": "wrong_option"}
        ],
        answer_name="フシギダネ",
        answer_image="https://zukan.pokemon.co.jp/zukan-api/up/images/index/7b705082db2e24dd4ba25166dac84e0a.png"
    )

if __name__ == '__main__':
    app.run()

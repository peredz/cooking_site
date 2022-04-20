from flask import Flask
from flask import url_for, request, render_template

app = Flask(__name__)


@app.route('/eat/<tlt>')
def index(tlt):
    return render_template('auto_answer.html', title='да',
                           header='Миссия Колонизация Марса', text4='И на Марсе будут яблони цвести!')


@app.route('/site')
def eat():
    return render_template('main_win.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
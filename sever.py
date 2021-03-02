from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)
# css = url_for('static', filename='css/style.css')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<prof>')
def tran(prof):
    return render_template('tran.html', title='Заготовка', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

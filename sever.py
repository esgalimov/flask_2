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


@app.route('/list_prof/<list>')
def prof_list(list):
    prof_lis = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
                'врач', 'инженер по терраформированию',
                'специалист по радиционной защите', 'климатолог',
                'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
                'метеоролог', 'оператор марсохода',
                'киберинженер', 'штурман', 'пилот дронов']
    return render_template('prof_list.html', title='Заготовка', list=list, prof_lis=prof_lis)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    person_info = {'title': 'Анкета',
                   'surname': 'Watny',
                   'name': 'Mark', 'education': 'выше среднего',
                   'profession': 'штурман марсохода',
                   'sex': 'male', 'motivation': 'Всегда мечтал застрять на марсе',
                   'ready': 'True'}
    return render_template('auto_answer.html', title=person_info['title'], person_info=person_info)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

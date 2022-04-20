from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Witaj użytkowniku'


@app.route('/hello/<name>')
def welcome_user(name):
    return f'Witaj {name}!'



@app.route('/less', methods=["GET", "POST"])
def less():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        return f'Czesc {imie} {nazwisko}'


@app.route('/time')
def current_time():
    return datetime.now().strftime('%H:%M:%S')


@app.route('/date')
def current_date():
    return datetime.now().strftime('%D')


@app.route('/licz/<liczba_a>/<liczba_b>')
def suma(liczba_a, liczba_b):
    int_a = int(liczba_a)
    int_b = int(liczba_b)
    suma = int_a + int_b
    return str(suma)


@app.route('/losuj')
def random():
    a = randint(-9, 9)
    b = randint(-9, 9)
    c = randint(-9, 9)
    return f'{a} {b} {c}'


from random import shuffle


@app.route('/lotek')
def lotek():
    numbers = list(range(1, 49 + 1))
    shuffle(numbers)
    numbers = numbers[:6]

    return str(numbers)[1: -1]


@app.route('/welcome', methods=['Get', 'POST'])
def welcome():
    if request.method == "GET":
        return render_template('welcome.html')
    else:
        imie = request.form['imie']
        return f'Witaj {imie}!'


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == "GET":
        return render_template('kalkulator.html')
    else:
        a = float(request.form['number_1'])
        b = float(request.form['number_2'])
        if request.form['operation'] == 'add':
            # return f'Wynik to {str(a + b)}!'
            return render_template('kalkulator.html', wynik=a + b)
        elif request.form['operation'] == 'subs':
            return render_template('kalkulator.html', wynik=a - b)
        elif request.form['operation'] == 'mult':
            return f'Wynik to {str(a * b)}!'
        elif request.form['operation'] == 'div':
            return f'Wynik to {str(a / b)}!'


from random import randint


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == "GET":  # po prostu wchodzimy na strone
        return render_template('guess.html', to_be_guessed=randint(1, 10))
    else:
        liczba = int(request.form['number'])
        wylosowana = int(request.form['wylosowana'])
        if liczba > wylosowana:
            return render_template('guess.html', komunikat='Za duża liczba, spróbuj jeszcze raz',
                                   to_be_guessed=wylosowana)
        elif liczba < wylosowana:
            return render_template('guess.html', komunikat='Za mała liczba, spróbuj jeszcze raz',
                                   to_be_guessed=wylosowana)
        else:
            return render_template('guess.html', komunikat='Brawo! Udało się!', to_be_guessed=randint(1, 10))


@app.route('/guessgame', methods=['GET', 'POST'])
def guessgame():
    if request.method == 'GET':
        return render_template('guessgame.html', min=0, max=1000, guess=500)
    else:
        min = int(request.form['min'])
        max = int(request.form['max'])
        guess = (min + max) // 2
        if request.form['decision'] == 'Za mało':
            new_guess = (guess + max) // 2
            return render_template("guessgame.html", min=guess, max=max, guess=new_guess)
        elif request.form['decision'] == 'Za dużo':
            new_guess = (min + guess) // 2
            return render_template("guessgame.html", min=min, max=guess, guess=new_guess)
        else:
            return "Zgadłem!!!"


@app.route('/namesurname', methods=['GET', 'POST'])
def namesurname():
    if request.method == "GET":
        return render_template('name_surname.html')
    else:
        x = str(request.form['name'])
        y = str(request.form['surname'])
        return render_template('name_surname.html', komunikat=f'Witaj {x} {y}!')


@app.route('/flask_math', methods=['GET', 'POST'])
def flaskmath():
    if request.method == "GET":
        return render_template('flask_math.html')
    else:
        n = float(request.form['n'])
        return render_template('flask_math.html', wynik_1=2 ** n, wynik_2=n ** n, wynik_3=n)


@app.route('/postcode', methods=['GET', 'POST'])
def postcode():
    if request.method == 'GET':
        return render_template('post_code.html')
    else:
        code = list(request.form['code'])
        if (len(code) == 6) and (code[2] == "-"):
            return render_template('post_code.html', r="Kod poprawny")
        else:
            return render_template("post_code.html", r="Kod niepoprawny")
        if not code[digits].isnumeric():
            return render_template("post_code.html", r="Kod niepoprawny")


app.run(debug=True)

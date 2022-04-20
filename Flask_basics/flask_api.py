# Piwne zadanie:
# Napisz aplikację we flasku, z jednym adresem: /piwo/<numer>
# W funkcji pobierz informacje na temat piwa o podanym numerze ze strony: https://api.punkapi.com/v2/beers/NUMERPIWA, np. https://api.punkapi.com/v2/beers/1 albo https://api.punkapi.com/v2/beers/2 etc
# Użyj requests, podobnie jak w zadaniu z psimi faktami
# Zaprezentuj informacje o piwie wstawiając je w HTML, np:
# <h1>{{ nazwa_piwa }}</h1>
# <p> {{ opis_piwa }}</p>
# <img src="{{ adres_obrazka_piwa }}">

from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/piwo', methods=['GET', 'POST'])
def piwo():
    if request.method == 'GET':
        return render_template('piwo.html')
    else:
        numer = request.form['numer']
        url = f'https://api.punkapi.com/v2/beers/{numer}'
        data = requests.get(url).json()
        beer = dict(data[0])
        return render_template("piwo.html", nazwa_piwa=beer['name'], opis_piwa=beer['description'],
                               adres_obrazka_piwa=beer['image_url'])


# Stwórz stronę we flasku, która formularzem zapyta ile faktów o psach wyświetlić.
# Po wysłaniu formularza fakty o psach powinny się wyświetlić,
# każdy w osobnej linii (użyj <br> do oddzielenia poszczególnych faktów od siebie).
# import requests
# data = requests.get('ADRES STRONY Z PSIMI FAKTAMI').json()


@app.route('/psy', methods=['GET', 'POST'])
def psy():
    if request.method == 'GET':
        return render_template('psy.html')
    else:
        ilosc = request.form['ilosc']
        url = 'https://dog-api.kinduff.com/api/facts?number=' + ilosc
        data = requests.get(url).json()
        facts = data['facts']
        return '<br>'.join(facts)


app.run(debug=True)

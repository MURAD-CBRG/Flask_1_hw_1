from flask import Flask, render_template

app = Flask(__name__)


base = {
    'Марс': [
        'Находиться недалеко от Земли',
        'Есть вода и атмосфера',
        'Имеется слабое магнитное поле',
        'Достаточное количество ресурсов'
    ],
    'Юпитер': [
        'Имеет большие размеры',
        'Находится далеко от Земли',
        'Имеет магнитное поле с очень большой напряженностью',
        'Возможно нахождение на планете большого кочиства ресурсов'
    ],
    'Proxima Centauri b': [
        'Планета очень похожа на Землю',
        'Имеется атмосфера эквивалентная Земле',
        'Физические свойства планеты сопоставимы с физическими свойствами Земли',
        'Расположены на огромном расстоянии от Земли'
    ]
}

@app.route('/choice/<planetname>')
def planet_select(planetname):
    planet, description = planetname, base[planetname]

    return render_template('index.html', planet=planet, description=description)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

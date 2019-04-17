import os
import waitress
from flask import Flask, render_template
from app.lib import Tariff, TariffManager


def start():
    app = Flask(__name__)
    manager = TariffManager()
    my_online = Tariff('Мой онлайн', price=290, hit=True, gb=15, gb_unlim=['vk', 'fb', 'instagram', 'ok'], minutes=400)
    my_tele2 = Tariff('Мой теле2', price=7, price_period='day', gb=6)
    univer = Tariff('Универ', archived=True)
    my_talk = Tariff('Мой разговор', price=190, gb=3, gb_unlim=None, minutes=250)
    classic = Tariff('Классический', price=0, minutes_unlim_tele2=0)
    premium = Tariff('Премиум', price=1100, gb=40, minutes=2000)
    my_tele2_11_2018 = Tariff('Мой теле2 11_2018',price=7.5, price_period='day', gb=20,
                              gb_unlim=['vk', 'fb', 'instagram', 'ok'], minutes=700, archived=True)

    manager.add(my_online)
    manager.add(my_tele2)
    manager.add(univer)
    manager.add(my_talk)
    manager.add(classic)
    manager.add(premium)
    manager.add(my_tele2_11_2018)

    @app.route('/')
    def actual():
        actual_tariffs = manager.actual()
        result = []
        for item in actual_tariffs:
            result.append(item)
        return render_template('index.html', result=result)

    @app.route('/archived')
    def archived():
        archived_tariff = manager.archived()
        result = []
        for item in archived_tariff:
            result.append(item)
        return render_template('archived.html', result=result)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()

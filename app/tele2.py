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

    manager.add(my_online)
    manager.add(my_tele2)
    manager.add(univer)

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

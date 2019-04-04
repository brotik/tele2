class Tariff:
    def __init__(self, name, *, price=0, price_period='month', gb=0, minutes=0, sms=0, hit=False, gb_unlim=None,
                 minutes_unlim_tele2=True, archived=False):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.minutes = minutes
        self.sms = sms
        self.hit = hit
        self.gb_unlim = gb_unlim
        self.minutes_unlim_tele2 = minutes_unlim_tele2
        self.archived = archived


class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        return list(filter(lambda tariff: not tariff.archived, self.items))

    def archived(self):
        return list(filter(lambda tariff: tariff.archived, self.items))


if __name__ == '__main__':
    manager = TariffManager()
    my_online = Tariff('Мой онлайн', price=290, hit=True, gb=15, gb_unlim=['vk', 'fb'], minutes=400)
    my_tele2 = Tariff('Мой теле2', price=7, price_period='day', gb=6)
    univer = Tariff('Универ', archived=True)

    manager.add(my_online)
    manager.add(my_tele2)
    manager.add(univer)

    actual = manager.actual()
    for item in actual:
        print(item.name)

    print('--')

    archived = manager.archived()
    for item in archived:
        print(item.name)

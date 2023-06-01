from .models import Alcohol, AlcoholType, Wine


def fill_database():
    Alcohol.objects.create(name='Merlot',
                           desc='Czerwone wino o miękkiej strukturze i aromatach czarnej wiśni i czekolady.',
                           votes=3,
                           type_id=1,
                           volt=13),

    Alcohol.objects.create(name='Chardonnay',
                           desc='Białe wino o średniej pełni i delikatnych nutach jabłek i dębu.',
                           votes=12,
                           volt=13,
                           type_id=1, )

    Alcohol.objects.create(name='Pinot Noir',
                           desc='Eleganckie czerwone wino o subtelnym bukiecie i nutach czerwonych owoców.',
                           votes=9,
                           volt=13,
                           type_id=1)

    Alcohol.objects.create(name='Riesling',
                           desc='Lekkie białe wino o wyraźnym smaku cytrusowym i delikatnej słodyczy.',
                           votes=6,
                           type_id=1,
                           volt=11)

    Alcohol.objects.create(name='Syrah',
                           desc='Intensywne czerwone wino o pikantnym charakterze i nutach czarnego pieprzu.',
                           votes=8,
                           type_id=1,
                           volt=14)

    Alcohol.objects.create(name='Sauvignon Blanc',
                           desc='Aromatyczne białe wino o świeżych nutach trawy i owoców tropikalnych.',
                           votes=10,
                           type_id=1,
                           volt=12)

    Alcohol.objects.create(name='Lech Premium',
                           desc='Piwo o wybornym zapachu i smaku chmielu.',
                           votes=2,
                           type_id=2,
                           volt=6)

    Alcohol.objects.create(name='Tyskie',
                           desc='Piwo o wybornym zapachu i smaku chmielu.',
                           votes=2,
                           type_id=2,
                           volt=6)
    Alcohol.objects.create(name='Lech Shandy Cytryna',
                           desc='Piwo o wybornym zapachu cytrusów.',
                           votes=2,
                           type_id=2,
                           volt=6)
    Alcohol.objects.create(name='Pan Tadeusz',
                           desc='Wódka ziemniaczana',
                           votes=3,
                           type_id=3,
                           volt=40)

def fill_alc_type():
    AlcoholType.objects.create(name='Wino')
    AlcoholType.objects.create(name='Piwo')
    AlcoholType.objects.create(name='Wódka')

def fill_wine():
    merlot = Alcohol.objects.get(name='Pinot Noir', type_id=1)
    chardonnay = Alcohol.objects.get(name='Riesling', type_id=1)

    Wine.objects.update_or_create(
        alcohol=merlot,
        defaults={'dryness': 'Półwytrawne', 'color': 'Czerwone'}
    )

    Wine.objects.update_or_create(
        alcohol=chardonnay,
        defaults={'dryness': 'Półsłodkie', 'color': 'Białe'}
    )


    # Wine.objects.get_or_create(
    #     alcohol_id=Alcohol.objects.get_or_create,
    #     dryness='Wytrawne',
    #     color='Białe'
    # )

    # Pozostałe rekordy...

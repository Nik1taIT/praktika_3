cities = {
    'Kyiv': {
        'country': 'Україні',
        'population': '2.8 мілн.',
        'fact': 'Місто з найкрасивішим та найісторичнішою архітектурою.'
    },
    'Paris': {
        'country': 'Франції',
        'population': '2.1 мілн.',
        'fact': 'Має назву, як "Місто закоханих"'
    },
    'Tokyo': {
        'country': 'Японії',
        'population': '14 мілн.',
        'fact': 'Самий густонаселена країна світу.'
    }
}

for city, info in cities.items():
    print(f"{city} в {info['country']} з населенням {info['population']}. Існує такий факт: {info['fact']}")

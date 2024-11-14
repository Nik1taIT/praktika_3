teams = {
    'Н*ю-Йорк Нікс': [82, 45, 22, 7, 8],
    'Лос-Анджелес Лейкерс': [82, 50, 25, 5, 2],
    'Чікаго Булз': [82, 40, 30, 12, 10]
}

for team, stats in teams.items():
    print(f"{team} {' '.join(map(str, stats))}")

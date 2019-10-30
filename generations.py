from datetime import date

today = date.today()
year = today.year

allGenerations = {
    "lostGeneration": (1883, 1900),
    "greatestGeneration": (1901, 1927),
    "silentGeneration": (1928, 1945),
    "babyBoomers": (1946, 1964),
    "generationX": (1965, 1980),
    "generationY": (1981, 1996),
    "generationZ": (1997, year)
}

birth = int(input('What year were you born?'))
my_generation = None
for generation, (start, end) in allGenerations.items():
    if start <= birth <= end:
        my_generation = generation
        break

if my_generation:
    print('you belong to', my_generation)
else:
    print('Your generation is not named.')

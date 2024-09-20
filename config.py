import json

cartes_raw = [
    'O1', 'O3', 'O4', 'O5', 'O6', 'O7', 'O10', 'O11', 'O12',
    'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C10', 'C11', 'C12',
    'E1', 'E3', 'E4', 'E5', 'E6', 'E7', 'E10', 'E11', 'E12',
    'B1', 'B3', 'B4', 'B5', 'B6', 'B7', 'B10', 'B11', 'B12'
]

escala_cartes = {
    'B11': 0,
    'O10': 1,
    'E1': 2,
    'B1': 3,
    'E7': 4,
    'C7': 5,
    'G3': 6,
    'G1': 7,
    'G12': 8,
    'G11': 9,
    'G10': 10,
    'G7': 11,
    'G6': 12,
    'G5': 13,
    'G4': 14
}

data = {
    "cartes": cartes_raw,
    "escala_cartes": escala_cartes
}

with open('config.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

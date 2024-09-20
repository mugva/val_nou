import json

# Load config.json
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.ma: dict = {}

    def get_name(self) -> str:
        return self.name

    def get_ma(self) -> dict:
        return self.ma

    def add_carta(self, carta: str, valor: int):
        self.ma[carta] = valor

    def remove_carta(self, carta: str):
        del self.ma[carta]

    def get_cartes(self):
        return self.ma.keys()

    def get_valors_cartes(self):
        return self.ma.values()


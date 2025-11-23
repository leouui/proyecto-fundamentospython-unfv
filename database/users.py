import json
from ruta import ruta

users = []

with open(ruta, "r", encoding="utf-8") as archivo:
    users = json.loads(archivo.read())
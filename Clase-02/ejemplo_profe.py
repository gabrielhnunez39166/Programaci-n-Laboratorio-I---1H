#Ejemplo de la profe

heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
 
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

#creo uno vacio
mi_diccionario = {}

#creo definiendo sus claves y valores
mi_diccionario_dos = {"Clave":"valor", "diccionario":heroes_info["Shazam"]["ID"],"habiliades":heroes_info["Shazam"]["Habilidades"]}

#agrego una clave y su valor a un diccionario vacio
mi_diccionario["id"] = 25

mi_diccionario_dos["pepe"] = heroes_info["Shazam"]
mi_diccionario_dos["ID"] =heroes_info["Shazam"]["ID"]
mi_diccionario_dos["Habilidades"] =heroes_info["Shazam"]["Habilidades"]
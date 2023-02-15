import json

#funcio que crea un arxiu json i el mostra per consola
def arxiujson():
    datas = """
    {
    "book":[
        {"title":"El Senor de los Anillos",
        "cover":"HardCover",
        "year":"1996",
        "pages":"567"
        }
        {"title":"Harry Potter",
        "cover":"HardCover",
        "year":"2006",
        "pages":"359"
        }
        {"title":"La Biblia",
        "cover":"HardCover",
        "year":"56",
        "pages":"1367"
        }
        {"title":"Teo va al parque",
        "cover":"LightCover",
        "year":"2014",
        "pages":"30"
        }
    ]
}
"""

    with open("books", 'w') as file:
        json.dump(datas, file)

    with open("books", 'r') as file:
        result = json.load(file)
        print(result)

#funcio que agafa l'arxiu creat a l'apartat anterior i l'imprimeix en format json.
def lleguirjson():
    with open("books", 'r') as file:
        result = json.load(file)
        print(result)

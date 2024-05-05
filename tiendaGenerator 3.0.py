import random

items = {
    "Escudo Anti-purgas": {
        "emoji": "[💠]",
        "tipo": "mítico",
        "precio": 400,
        "probabilidad": 0,
        "oferta": False
    },
    "Generador de baneo": {
        "emoji": "[💀]",
        "tipo": "mítico",
        "precio": 360,
        "probabilidad": 27,
        "oferta": False
    },
    "Resurrector": {
        "emoji": "[⚕️]",
        "tipo": "mítico",
        "precio": 300,
        "probabilidad": 27,
        "oferta": False
    },
    "Wordless": {
        "emoji": "[📛]",
        "tipo": "mítico",
        "precio": 500,
        "probabilidad": 15,
        "oferta": False
    },
    "Duplicador": {
        "emoji": "[➿]",
        "tipo": "legendario",
        "precio": 330,
        "probabilidad": 35,
        "oferta": False
    },
    "Estand. ApuZkT": {
        "emoji": "[🐸]",
        "tipo": "legendario",
        "precio": 330,
        "probabilidad": 30,
        "oferta": False
    },
    "Break Pass": {
        "emoji": "[🕊️]",
        "tipo": "legendario",
        "precio": 310,
        "probabilidad": 40,
        "oferta": False
    },
    "Escudo de inmunidad": {
        "emoji": "[🛡]",
        "tipo": "épico",
        "precio": 100,
        "probabilidad": 75,
        "oferta": False
    },
    "NameTroll": {
        "emoji": "[🎭]",
        "tipo": "épico",
        "precio": 110,
        "probabilidad": 75,
        "oferta": False
    },
    "Canasta de futs": {
        "emoji": "[🧺]",
        "tipo": "épico",
        "precio": 115,
        "probabilidad": 75,
        "oferta": False
    },
    "Bancuna": {
        "emoji": "[💉x1]",
        "tipo": "común",
        "precio": 15,
        "probabilidad": 100,
        "oferta": False
    },
    "Intercambio": {
        "emoji": "[💱x1]",
        "tipo": "común",
        "precio": 20,
        "probabilidad": 100,
        "oferta": False
    },
    "Harzt": {
        "emoji": "❤️x1",
        "tipo": "común",
        "precio": 20,
        "probabilidad": 100,
        "oferta": False
    },
    "Estand. Nacionalidad": {
        "emoji": "[🇨🇷]",
        "tipo": "común",
        "precio": 60,
        "probabilidad": 100,
        "oferta": False
    },
    "Reciclaje": {
        "emoji": "[♻️x1]",
        "tipo": "común",
        "precio": 100,
        "probabilidad": 100,
        "oferta": False
    },
    "Zkart": {
        "emoji": "[💳]",
        "tipo": "común",
        "precio": 240,
        "probabilidad": 100,
        "oferta": False
    },
    "Estado Personalizado": {
        "emoji": "[♒]",
        "tipo": "común",
        "precio": 60,
        "probabilidad": 100,
        "oferta": False
    },
    "Marco Personalizado": {
        "emoji": "[♏]",
        "tipo": "común",
        "precio": 80,
        "probabilidad": 100,
        "oferta": False
    },
    "Nombre Personalizado": {
        "emoji": "[🆔️]",
        "tipo": "común",
        "precio": 90,
        "probabilidad": 100,
        "oferta": False
    },
    "Chile": {
        "emoji": "[🌶️x1]",
        "tipo": "fut",
        "precio": 5,
        "probabilidad": 100,
        "oferta": False
    },
    "Dulce": {
        "emoji": "[🍬x1]",
        "tipo": "fut",
        "precio": 5,
        "probabilidad": 100,
        "oferta": False
    },
    "Leche": {
        "emoji": "[🥛x1]",
        "tipo": "fut",
        "precio": 20,
        "probabilidad": 100,
        "oferta": False
    },
    "Vino": {
        "emoji": "[🥂x1]",
        "tipo": "fut",
        "precio": 25,
        "probabilidad": 100,
        "oferta": False
    },
    "Galleta": {
        "emoji": "[🍪x1]",
        "tipo": "fut",
        "precio": 30,
        "probabilidad": 100,
        "oferta": False
    },
    "Té": {
        "emoji": "[🍵x1]",
        "tipo": "fut",
        "precio": 25,
        "probabilidad": 100,
        "oferta": False
    },
    "Guaraná": {
        "emoji": "[🥤x1]",
        "tipo": "fut",
        "precio": 35,
        "probabilidad": 100,
        "oferta": False
    },
    "Chocolate": {
        "emoji": "[🍫x1]",
        "tipo": "fut",
        "precio": 40,
        "probabilidad": 100,
        "oferta": False
    },
    "Hamburguesa": {
        "emoji": "[🍔x1]",
        "tipo": "fut",
        "precio": 50,
        "probabilidad": 100,
        "oferta": False
    }
}



# usar probabilidad para determinar si aparecerá en la tienda
def disp(items, itemOferta):
    '''
    Según un número random, se determina si el ítem estará o no en la tienda.
    probabilidad: número entero que representa la probabilidad de que
    el item aparezca en la tienda.
    regresa lista con items para la tienda
    '''
    itemsTienda = []
    for item in items:
        ref = random.randrange(1, 100)
        if item == itemOferta:
            items[item]["probabilidad"] = 100
        probabilidad = items[item]["probabilidad"]
        if ref <= probabilidad:
            itemsTienda.append(item)
    return itemsTienda

# listas según tipo
def sortTipo(itemsTienda):
    '''
    categoriza por tipo de rareza los items
    y devuelve False si la lista queda vacia
    '''
    miticos = []
    legendarios = []
    epicos = []
    comunes = ['Bancuna', 'Intercambio', 'Harzt', 'Estand. Nacionalidad', 'Reciclaje', 'Zkart', 
    'Estado Personalizado', 'Marco Personalizado', 'Nombre Personalizado']
    futs = ['Chile', 'Dulce', 'Leche', 'Vino', 'Galleta', 'Té', 'Guaraná', 'Chocolate', 'Hamburguesa']
    tipos = [miticos, legendarios, epicos, comunes, futs]

    for item in itemsTienda:
        rareza = items[item]["tipo"]
        if not rareza == "común" or "fut":
            if rareza == "mítico":
                miticos.append(item)
            elif rareza == "legendario":
                legendarios.append(item)
            else:
                epicos.append(item)
    
    for tipo in tipos:
        i = tipos.index(tipo)
        if len(tipos[i]) == 0:
            tipos[i] = False

    return tipos

def desc(item, precioDescuento):
    precioOriginal = items[item]["precio"]
    porcentaje = (precioDescuento * 100) / precioOriginal
    return round(porcentaje)

# organizar tienda
def tienda(fecha, items, oferta, precioDescuento):
    miticoHead = "\\╰━━╮MÍTICOS╭━━╯\\"
    legendarioHead = "\\╰━━╮LEGENDARIOS╭━━╯\\"
    epicoHead = "\\╰━━╮ÉPICOS╭━━╯\\"
    comunHead = "\\╰━━╮COMUNES╭━━╯\\"
    futHead = "\\╰━━╮FUTS╭━━╯\\"
    heads = [miticoHead, legendarioHead, epicoHead, comunHead, futHead]

    itemsTienda = disp(items)
    tipos = sortTipo(itemsTienda)
    
    if not oferta == False:
        items[oferta]["oferta"] = True

    
    print('/newtienda {', '\n', '"fecha" : "{} - 18:00",', '\n', '"contenido" : "'.format(fecha))

    i = 0
    for head in heads:
        seccion = tipos[i]
        if not seccion == False:
            print(head, "\n")
            for item in seccion:
                print(items[item]["emoji"], item, "|", items[item]["precio"], end= "💰 \n")
                if items[item]["oferta"] == True:
                    print()
            print()
        i += 1

    return ""


#print(tienda("09/05", items, "Generador de Baneo", 320))
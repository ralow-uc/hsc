import random
import requests

def usuario_en_sesion(request):
    usuario_api = request.session.get("usuario_api")
    return {"usuario": usuario_api}

def consejo_context(request):
    consejo = "Recuerda siempre guardar tu trabajo."  # valor por defecto
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        if response.status_code == 200:
            consejo = response.json().get("slip", {}).get("advice", consejo)
    except:
        pass
    return {"consejo": consejo}


def pokemon_random(request):
    id_pokemon = random.randint(1, 151)
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            nombre = data["name"].capitalize()
            imagen = data["sprites"]["front_default"]
            return {"pokemon": {"nombre": nombre, "imagen": imagen}}
    except Exception:
        pass
    return {"pokemon": {"nombre": "Desconocido", "imagen": None}}
# Introducción a las clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia
# de una clase.
# Permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

# Ejemplo de una clase básica
import requests


class Coche:
    # atributo de clase (comparte todas las instancias)
    tipo = "vehiculo de cuatro ruedas"
    rueda = 4

    # méetodo especial que es el que construye el objeto
    # se llama automáticamente este método cuando crea la instancia
    def __init__(self, brand, model, color):
        # atributo de la instancia
        self.brand = brand
        self.model = model
        self.color = color

    def arrancar(self):
        print(f"El coche {self.brand} {self.model} está arrancando! 🚗")


# Construyendo una instancia de la clase, se convierte en un objeto
mi_coche = Coche("Ford", "Mustang", "rojo")
mi_coche.arrancar()
# Accediendo a los atributos
mi_coche.tipo
print(mi_coche.brand)
print(mi_coche.rueda)
coche_de_pheralb = Coche("Bmw", "X5", "azul")
# Accediendo a los métodos
coche_de_pheralb.arrancar()
print(coche_de_pheralb.brand)

# Encapsulamiento: Es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA
# Para que no muestre error.
OPENAI_KEY = ""
DEEPSEEK_KEY = ""


class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],

        }

        response = requests.post(self.url, json=data, headers=headers)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])


openai_api = AI_API(
    OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación en Python")

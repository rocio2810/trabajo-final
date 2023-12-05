import requests
import tkinter as tk
#creamos una funcion llamada obtener_informacion_pokemon,en la que realiza la solucitud la pokeapi para obtener informacion de un pokemon en especifico, indetificado por un numero. retorna los 
#datos del pokemon si la solicitud exitosa, y maneja posibles errores de http o de solicitud, proporciona mensajes descriptivos en caso de fallosl. 
 
class PokeAPI:
    def obtener_informacion_pokemon(self, numero_pokemon):
        url = f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon}/"
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos_pokemon = respuesta.json()
            return datos_pokemon
        except requests.exceptions.HTTPError as errh:
            return f"Error HTTP: {errh}"
        except requests.exceptions.RequestException as err:
            return f"Error de solicitud: {err}"
class Pokemon:
    def __init__(self):
        self.nombre = None
        self.tipo = None
        self.habilidades = []
        self.hp = None
        self.attack = None
        self.defense = None
        self.special_attack = None
        self.special_defense = None
        self.speed = None
#este metodo de la clase pokemon utiliza una instancia de la clase pokeapi para obtener datos actualizados de un pokemon mediante de su numero.si la solicitud es exitosa,actualiza los atributos de la instancia con la informacion como nombre,tipo,habilidades y estadistica.encaso de fallos,no modifica los atributos.
    def actualizar_informacion(self, numero_pokemon):
        api = PokeAPI()
        datos_pokemon = api.obtener_informacion_pokemon(numero_pokemon)

        if isinstance(datos_pokemon, dict):
            self.nombre = datos_pokemon["name"]
            self.tipo = datos_pokemon["types"][0]["type"]["name"]
            self.habilidades = [habilidad["ability"]["name"] for habilidad in datos_pokemon["abilities"]]

            stats = datos_pokemon["stats"]
            self.hp = stats[0]["base_stat"]
            self.attack = stats[1]["base_stat"]
            self.defense = stats[2]["base_stat"]
            self.special_attack = stats[3]["base_stat"]
            self.special_defense = stats[4]["base_stat"]
            self.speed = stats[5]["base_stat"]
#esta clase define una interfaz grafica utilizando tkinter,en resumen la clase define una interfaz basica para interactuar con la pokeapi y mostrar la informacion de un pokemon
class InterfazPokemon:
    def __init__(self, master):
        self.master = master
        master.title("PokeAPI Explorer")

        self.label = tk.Label(master, text="Número de Pokémon:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.boton = tk.Button(master, text="Buscar", command=self.mostrar_informacion)
        self.boton.pack(pady=10)

        self.resultado_text = tk.Text(master, height=10, width=50)
        self.resultado_text.pack(pady=10)

        self.mi_pokemon = Pokemon()
#esta funcio0n maneja la interaccion del usuario obtiene y muestra la informacion del pokemon en la interfaz grafica cuando se presiona el boton "buscar".
    def mostrar_informacion(self):
        numero_pokemon = self.entry.get()
        self.mi_pokemon.actualizar_informacion(numero_pokemon)

        resultado = f"Nombre: {self.mi_pokemon.nombre}\nTipo: {self.mi_pokemon.tipo}\n"
        resultado += f"Habilidades: {', '.join(self.mi_pokemon.habilidades)}\n"
        resultado += f"HP: {self.mi_pokemon.hp}\nAtaque: {self.mi_pokemon.attack}\n"
        resultado += f"Defensa: {self.mi_pokemon.defense}\nAtaque Especial: {self.mi_pokemon.special_attack}\n"
        resultado += f"Defensa Especial: {self.mi_pokemon.special_defense}\nVelocidad: {self.mi_pokemon.speed}"

        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, resultado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazPokemon(ventana)
    ventana.mainloop()


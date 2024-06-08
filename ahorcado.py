import random
from funciones_captura import limpiar_pantalla
from playsound3 import playsound

def mostrar_horca(intentos):
    estados = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return estados[intentos]

def obtener_palabra():
    palabras = {
        "1": {"palabra": "python", "pistas": ["Un lenguaje de programación muy popular.", "Creado por Guido van Rossum.", "Usado para desarrollo web y ciencia de datos."]},
        "2": {"palabra": "ahorcado", "pistas": ["Un juego clásico que estamos programando.", "Involucra adivinar letras.", "Se juega con papel y lápiz tradicionalmente."]},
        "3": {"palabra": "computadora", "pistas": ["Un dispositivo que usas para programar.", "Tiene una CPU.", "Puede ejecutar varios programas."]},
        "4": {"palabra": "desarrollador", "pistas": ["Una persona que escribe código.", "También llamado programador.", "Trabaja en la creación de software."]},
        "5": {"palabra": "algoritmo", "pistas": ["Una serie de pasos para resolver un problema.", "Fundamental en la programación.", "Utilizado en matemáticas y lógica."]},
        "6": {"palabra": "internet", "pistas": ["Una red global de computadoras.", "Usada para navegar y comunicarse.", "Revolucionó la forma en que accedemos a la información."]},
        "7": {"palabra": "javascript", "pistas": ["Lenguaje de programación usado en el desarrollo web.", "Permite crear páginas web interactivas.", "Es ejecutado por navegadores web."]},
        "8": {"palabra": "robotica", "pistas": ["Campo relacionado con el diseño y construcción de robots.", "Combina ingeniería mecánica, eléctrica y computación.", "Aplicada en la industria y la investigación."]},
        "9": {"palabra": "inteligencia", "pistas": ["Capacidad de aprender y entender.", "Asociada con habilidades cognitivas.", "También un campo de la informática."]},
        "10": {"palabra": "datos", "pistas": ["Información recogida para análisis.", "Puede ser estructurada o no estructurada.", "Fundamental en la ciencia de datos."]}
    }
    key = random.choice(list(palabras.keys()))
    palabra_data = palabras[key]
    return palabra_data["palabra"], random.choice(palabra_data["pistas"])

def play(palabra, pista):
    palabra_caracteres = "_" * len(palabra)
    adivinar = False
    adivinar_letras = []
    adivinar_palabras = []
    intentos = 6

    limpiar_pantalla()
    print("¡Bienvenido al juego del Ahorcado!")
    print("Pista: " + pista)
    print(mostrar_horca(intentos))
    print(palabra_caracteres)
    print("\n")
    playsound('intro.mp3')
   
    while not adivinar and intentos > 0:        
        entrada = input("Por favor, introduce una letra o palabra: ").lower()
        if len(entrada) == 1 and entrada.isalpha():
            if entrada in adivinar_letras:
                print("Ya has adivinado la letra", entrada)
                playsound('try.mp3')
            elif entrada not in palabra:
                print(entrada, "no está en la palabra.")
                intentos -= 1
                adivinar_letras.append(entrada)
                playsound('box-crash.mp3')
            else:
                print("¡Buen trabajo!", entrada, "está en la palabra.")
                playsound('success.mp3')
                adivinar_letras.append(entrada)
                palabra_as_list = list(palabra_caracteres)
                indices = [i for i, letter in enumerate(palabra) if letter == entrada]
                for index in indices:
                    palabra_as_list[index] = entrada
                palabra_caracteres = "".join(palabra_as_list)
                if "_" not in palabra_caracteres:
                    adivinar = True
        elif len(entrada) == len(palabra) and entrada.isalpha():
            if entrada in adivinar_palabras:
                print("Ya has adivinado la palabra", entrada)
                playsound('try.mp3')
            elif entrada != palabra:
                print(entrada, "no es la palabra.")
                intentos -= 1
                adivinar_palabras.append(entrada)
                playsound('box-crash.mp3')
            else:
                adivinar = True
                palabra_caracteres = palabra
        else:
            print("Entrada no válida.")
            playsound('box-crash.mp3')
        
        print(mostrar_horca(intentos))
        print(palabra_caracteres)
        print("\n")

    if adivinar:
        playsound('gano.mp3')
        print("¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        playsound('fatality.mp3')
        print("Lo siento, te has quedado sin intentos. La palabra era:", palabra)

def main():
    palabra, pista = obtener_palabra()
    play(palabra, pista)
    while input("¿Quieres jugar de nuevo? (S/N): ").upper() == "S":
        palabra, pista = obtener_palabra()
        play(palabra, pista)
    playsound('end.mp3')
if __name__ == "__main__":
    main()

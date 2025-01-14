import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while not adivinado:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

if __name__ == "__main__":
    adivina_el_numero()
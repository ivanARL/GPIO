import RPi.GPIO as GPIO
import time

# Configuración inicial
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definición de pines para cada segmento
pines = {'A': 17,  # pin físico 11
        'B': 18,  # pin físico 12
        'C': 27,  # pin físico 13
        'D': 22,  # pin físico 15
        'E': 23,  # pin físico 16
        'F': 24,  # pin físico 18
        'G': 25   # pin físico 22
}

# Configurar los pines como salidas y establecerlos en alto (apagados)
for pin in pines.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Diccionario de segmentos para cada dígito hexadecimal
hex_seg = {
    '0': [1,1,1,1,1,1,0],
    '1': [0,1,1,0,0,0,0],
    '2': [1,1,0,1,1,0,1],
    '3': [1,1,1,1,0,0,1],
    '4': [0,1,1,0,0,1,1],
    '5': [1,0,1,1,0,1,1],
    '6': [1,0,1,1,1,1,1],
    '7': [1,1,1,0,0,0,0],
    '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1],
    'A': [1,1,1,0,1,1,1],
    'B': [0,0,1,1,1,1,1],
    'C': [1,0,0,1,1,1,0],
    'D': [0,1,1,1,1,0,1],
    'E': [1,0,0,1,1,1,1],
    'F': [1,0,0,0,1,1,1]
}

def mostrar_digito(digito):
    print("Mostrando:", digito)
    pattern = hex_seg[digito]
    for i, seg in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G']):
        # Invertir la lógica para ánodo común: 1 -> LOW (encendido), 0 -> HIGH (apagado)
        GPIO.output(pines[seg], GPIO.LOW if pattern[i] else GPIO.HIGH)
    time.sleep(1)

def main():
    try:
        while True:
            for digito in hex_seg:
                mostrar_digito(digito)
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario.")
    finally:
        # Apagar todos los segmentos antes de limpiar
        for pin in pines.values():
            GPIO.output(pin, GPIO.HIGH)
        GPIO.cleanup()
        print("GPIO limpiado. Programa finalizado.")

if __name__ == "__main__":
    main()

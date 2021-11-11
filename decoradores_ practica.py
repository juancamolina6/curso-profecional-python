def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje '

# mensaje = mayusculas(mensaje)

def run():
    nombre = input("ingresa tu nombre ")
    print(mensaje(nombre))

if __name__ == "__main__":
    run()
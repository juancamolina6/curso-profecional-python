from datetime import datetime

def execution_time(func):
# *args: es para pasar cual quier tipo de argumento posicional
# **kwargs no importa cantidad de parametros nombrados ejemplo def saludo(nombre="juan") 
    def wrapper(*args , **kwargs):
        initial_time = datetime.now()
        func(*args , **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a: int, b: int)-> int:
    return a+b 
@execution_time
def saludo(nombre = "Cesar"):
    print(f"hola {nombre}")

suma(5,5)
random_func()
saludo("Facundo")
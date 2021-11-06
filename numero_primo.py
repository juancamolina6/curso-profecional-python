# def numero_primo(num:int) ->bool:
#     cont:int = 0

#     for i in range(1, num+1):
#         if i == 1 or i == num :
#             continue
#         elif num % i == 0:
#             cont +=1
        
#     if cont == 0 and num != 1:
#             return True
#     else:
#             return False

#vaidar si es primo
def numero_primo(num:int) ->bool:
    cont:int = 0
# sacar rais del numero
    rais:int = num**(0.5)

# validar si numero es par o 2 
    if num% 2 == 0 and num == 2:
        return True    
    else:
# validar numeros desde i hasta la raiz del numero 
        for i in range(1, int(rais)+1):
            if i == 1 or i == num :
                continue
            elif num % i == 0:
                cont +=1
# retorna True si es primo y false si no es primo 
    if cont == 0 and num != 1: 
            return True
    else:
            return False

    

def run():
    num:int = int(input("ingresa un numero para validar si es primo: "))
    if numero_primo(num):
        print('Es primo')
    else:
        print('No es primo')
    
    
    

if __name__ == "__main__":
    run()
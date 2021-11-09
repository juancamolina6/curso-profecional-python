def make_division_by(n):
    def division(x):
        return x / n
    return division

def run():
    devision_by_number = make_division_by(float(input("ingresa un numero a dividr ")))
    print(devision_by_number(float(input("ingresa el otro numero a dividir "))))

if __name__ == "__main__":
    run()
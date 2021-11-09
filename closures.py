# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str,"Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(3)
    print(repeat_5(1))

if __name__ == '__main__':
    run()
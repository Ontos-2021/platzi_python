from tkinter import N


def divisors(num):
    try:
        if num == 0:
            raise ValueError("Debes ingresar un número positivo, distinto de 0")
        if num < 0:
            raise ValueError("Debes ingresar un número positivo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return "No se pudo calcular los divisores"

def run():
    num = input("Ingrese un número: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número positivo"
    print(divisors(int(num)))
    print("El programa finalizó correctamente")

if __name__ == '__main__':
    run()
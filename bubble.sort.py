# deficion de la clase factorial



n = int(input("Por favor ingrese un número y calcularemos su factorial:"))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n-1)
    

print(f"El factorial del número {n} es : {factorial(n)}")
    


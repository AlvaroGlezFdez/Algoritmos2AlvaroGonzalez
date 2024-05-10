#Recursividad para calcular el factorial de un número.

def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.

# Lo primero es pedir un número al usuario y asegurarnos de que no es un string, convirtíendolo a entero
n = int(input("Por favor ingrese un número y calcularemos su factorial:"))


# deficion de la clase factorial
def factorial(n):
    if n == 0 or n == 1:        # Definimos el caso base, cuando n es igual a 0 o a 1
        return 1
    if n > 1:                   # En caso contrario, nuestro número será mayor que 1, por lo que 
                                # tendremos que llamar a la funcion de manera recursiva.
        return n * factorial(n-1)
    

# Por útimo llamamos a la funcion y la printeamos
print(f"El factorial del número {n} es : {factorial(n)}")


def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    
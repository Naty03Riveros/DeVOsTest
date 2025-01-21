# app.py

def add_numbers(a, b):
    """Suma dos números."""
    return a + b

def subtract_numbers(a, b):
    """Resta dos números."""
    return a - b

if __name__ == "__main__":
    x = 10
    y = 5
    print(f"La suma de {x} y {y} es: {add_numbers(x, y)}")
    print(f"La resta de {x} y {y} es: {subtract_numbers(x, y)}")

def cuadrado(n):
    return n**2
print(f"El cuadrado de 5 es {cuadrado(5)}")

#con lambdas
func=lambda n:n**2
pot=lambda a,b:a**b
print(f"El cuadrado de 5 es {func(5)}")
print(f"5 elevado a 3 es {pot(5,3)}")

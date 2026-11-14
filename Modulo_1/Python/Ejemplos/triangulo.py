lA = int(input("Ingresa el lado A:"))
lB = int(input("Ingresa el lado B:"))
lC = int(input("Ingresa el lado C:"))
if lA == lB == lC:
    print("Es un triangulo equilatero")
elif lA == lC != lB:
    print("EL triangulo es Isosceles")
else:
    print("El triangulo es Escaleno")
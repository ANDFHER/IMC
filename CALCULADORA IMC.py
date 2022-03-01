print("calculadora IMC")

weight = float(input("indica tu peso en kg  "))
height = float(input("indica tu altura en mts  "))

calculator = weight/height**2
print("su indicador de IMC es: " + str(round(calculator, 1)))

if calculator >=0 and calculator <=16.9:
    print("muy delgado")
elif calculator >=17.0 and calculator <=18.5:
    print("Bajo Peso")
elif calculator >=18.6 and calculator <=24.9:
    print("Peso Normal")
elif calculator >=25.0 and calculator <=29.9:
    print("Sobrepeso")
elif calculator >=30.0:
    print("Obesidad")
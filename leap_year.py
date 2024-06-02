def leap_year():
    año=int(input("Ingrese un año: "))
    if (año//4)==(año/4) or (año/100)==(año//100) and (año/400)==(año//400):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

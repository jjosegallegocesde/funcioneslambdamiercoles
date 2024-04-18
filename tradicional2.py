""" hacer un software que permita la gestion de las vacaciones, 
que permita sumar la cantidad de dias de vacaciones + dias libres ganados """

def sumar_vacaciones(dias_vacaciones, dias_libres):
    return dias_vacaciones+dias_libres

dias_vacaciones=int(input("ingrese los dias de vacaciones: "))
dias_libres=int(input("Ingrese sus dias adicionales: "))

total_vacaciones=sumar_vacaciones(dias_vacaciones,dias_libres)
print(f"los dias totales de sus vacaciones son: {total_vacaciones}")
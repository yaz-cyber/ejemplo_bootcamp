#Una empresa necesita calcular la liquidación mensual de un empleado. Solicita el valor del salario diario y los días trabajados en el mes. Calcula el
#salario bruto, resta un 4% para pensión y un 4% para salud sobre el bruto, e imprime el neto a pagar.

#
salario_diario=float(input("digitar valor del salario diario  "))
#
dias_trabajados=int(input("digitar el numero de dias de trabajo   "))
#
sueldo_bruto= salario_diario * dias_trabajados
#
salud=sueldo_bruto * 0.04
pension=sueldo_bruto * 0.04
sueldo_neto= sueldo_bruto - salud - pension

print(f"\n--- Desglose de nomina")
print("="*35)
print("sueldo_bruto",sueldo_bruto)
print("deduccion de salud",salud)
print("deduccion de pension",pension)
print("sueldo neto a pagar",sueldo_neto)
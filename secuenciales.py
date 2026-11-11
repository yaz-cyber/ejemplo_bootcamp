#Una persona vende un producto en línea. 
# El programa pide el precio de venta, 
# el costo de compra, 
# el porcentaje de comisión de la plataforma y 
# el costo del envío que asume el vendedor. 
# Calcula la comisión en pesos, 
# el costo total y la 
# ganancia neta por unidad. Luego pide 
# cuántas unidades vendió en el mes y 
# muestra la ganancia mensual.

#datos que ocupo del texto:
precio_venta= 100
costo_compra= 50

porcentaje_comision_plataforma=(20/100)
costo_envio_vendedor=20
calculo_comision=(10/100)
costo_total=(precio_venta + porcentaje_comision_plataforma + costo_envio_vendedor)
ganancia_neta_unidad=costo_total - costo_compra + calculo_comision
unidad_vendida_mes=20
ganancia_mensual= ganancia_neta_unidad*unidad_vendida_mes

precio_venta=float(input("digita precio de venta  "))
costo_compra=float(input("digitar costo de compra  "))
porcentaje_comision_plataforma=float(input("porcentaje de comision plataforma  "))
costo_envio_vendedor=float(input("digitar costo de envio  "))
calculo_comision=float(input("digitat comision  "))
print("="*35)
costo_total=print("costo_total=", porcentaje_comision_plataforma + costo_envio_vendedor) 
ganancia_neta_unidad= print(costo_compra + calculo_comision )* (unidad_vendida_mes)
ganancia_mensual=print(ganancia_neta_unidad+ganancia_mensual)


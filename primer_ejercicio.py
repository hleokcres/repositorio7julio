sueldo_empleado=float(input("Ingrese el sueldo del empelado: "))#estructura input
nombre_empleado=str(input("Digite el nombre del empleado: "))
descuento=sueldo_empleado*0.20
print("el dinero que se le descontara sera:",descuento)
sueldo_final=sueldo_empleado-descuento
print("sus sueldo final es:  ",sueldo_final,"para el empleado ",nombre_empleado)

# > >= < <= != # operadores de comparacion o de relacion

if descuento>=800_000:#condicion o comparacion respuesta (True verdadero False Falso)
    print("descuento alto")
    if sueldo_final>=2_000_000:
        print("ud no recibira subsidio de transporte")
else:
    print("descuento bajo")



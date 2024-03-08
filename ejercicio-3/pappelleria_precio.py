import math
#Programa para calcular el precio de vebta de diferente productos 

#entrada 
PRECIO_COSTO = int(input("por favor ingrese el precio en el que adquirio el producto: "))

#processing

if PRECIO_COSTO < 3000:
    GANANCIA = PRECIO_COSTO *0.15
elif PRECIO_COSTO > 6000:
    GANANCIA = PRECIO_COSTO *0.25
else:
    GANANCIA = 500
    
    PRECIO_VENTA =( GANANCIA +PRECIO_COSTO)
    #salida 
    print ("el producto adquiirido se debe vender a",PRECIO_VENTA,)
    
#programa para calcular en que cuadrante se encuentra un punto en el plano carteciano

#entrada 
X= int(input("ingresa la cordenada x: "))
Y = int(input("ingresa la cordenada Y: "))

#proceso
if  X == 0:
    if Y == 0:
        print("la coordenada"(X , Y), "esta en el origen")
    else:
         print("la coordenada"(X , Y), "esta en el eje Y")
elif Y == 0:
      print("la coordenada"(X , Y), "esta en el eje X")
elif X > 0:
    if Y > 0: 
        print( "la coordenada"(X , Y), "esta en el el cuadrante 1") 
    else:
        print("la coordenada"(X , Y), "esta en el cuadeante 4")
elif Y < 0:
        print("la coordenada"(X , Y), "esta en el cuadrante 3")
        
else:
    print("la coordenada"(X , Y), "esta en el cuadrante 2")
    
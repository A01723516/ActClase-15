def main():
    #escribe tu código abajo de esta línea
cuenta=0
numero=0
suma=0
while numero>=0:
    numero=float(input())
    if numero>0:
        suma+=numero
        cuenta+=1
    if numero<0:
        break
    
promedio=(suma/cuenta)
print(promedio)

if __name__=='__main__':
    main()

def main():
    #escribe tu código abajo de esta línea
    pass
    cuenta=0
    numeros=0
    while numeros >=0:
        numero=float(input())
        if numero%2==0:
            cuenta+=1
        if numero ==0:
            cuenta+=1
        if numero < 0:
            break
    print("Total de pares="+str(cuenta))
     

if __name__=='__main__':
    main()

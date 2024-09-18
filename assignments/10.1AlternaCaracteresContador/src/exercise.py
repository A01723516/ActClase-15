def main():
    #escribe tu código abajo de esta línea
    pass
    numero=int(input("ingresa un numero"))
    for i in range (1,numero+1):
        if i%2==0:
            print(str(i)+"-%")
        else:
            print(str(i)+"-#")

if __name__=='__main__':   
    main()

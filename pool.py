from multiprocessing import Pool

def ejectuando(num):
    return num**2


if __name__ == '__main__':
    p=Pool(processes=20)
    datos= p.map(ejectuando, range(20))
    datos2 = p.map(ejectuando, [123,5341,213,54,1213,4132])
    p.close()
    print(datos)
    print(datos2)
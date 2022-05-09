lista_numero = [1,5,8,7,20,9,4,4,43,52,3,34,23,54,4,5,4,65,7]
suma = 0
for item in lista_numero:
    suma = suma + item
    print(item)
    item += 1
print("La suma es: ",suma)

i = 50
while i >= 0:
    #print(i)
    residuo = i % 5
    if residuo == 0:
        print(i)
    i -= 1
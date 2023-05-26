n = int(input("Digite o valor de n: "))

i = 0
cont = 1

while cont <= n:
    if i%2==0:
        i+=1
        print(i)
    else:
        print(i)
    i +=1
    cont +=1

n = int(input("Digite um número inteiro: "))
i = 0
soma = 0
qdd = len(str(n))
while n%10!=0 or qdd!=0:
    i = n%10
    soma +=i
    n = n//10
    qdd -=1
print(soma)



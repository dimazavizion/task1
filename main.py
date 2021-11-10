a = int(input("Введите длину стороны A\n"))
b = int(input("Введите длину стороны B\n"))
c = int(input("Введите длину стороны C\n"))
if a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Площадь треугольника, построенного по заданным сторонам, равна", S)
n = int(input("Задайте длинну массива\n"))
x = []
S = 0
for i in range(n):
    x.append(int(input("Введите элемент массива с индексом " + str(i) + ": ")))
for i in range(n):
    a = x[i]
    for j in range(i+1, n):
        b = x[j]
        for k in range(j+1, n):
            c = x[k]
            if a+b > c and a+c > b and b+c > a:
                p = (a+b+c)/2
                Spr = (p*(p-a)*(p-b)*(p-c))**0.5
                if Spr >= S:
                    S = Spr
if S:
    print("Площадь наибольшего треугольника равна", S)
else:
    print("Треугольника с такими сторонами не существует") 
    print("Невозможно построить треугольник")

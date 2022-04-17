for i in range(10):
    print(i,"\thello world")

n=int(input("Masukkan n : "))
if (n % 2) == 0:
    print (n,"\tgenap")
else:
    print (n,"\tganjil")

num1, num2 = 0, 1
for i in range(0, n):
    print (num2)
    num = num1 + num2
    num1=num2
    num2 = num
import matplotlib.pyplot as plt

print ("Aplikasi integrasi metode Simpson")
print ("app version 1.0 alpha\n")

a = 0 #batas bawah
b = 2 #batas atas

n = 32 #banyak iterasi
h = (b-a)/n #kepadatan

print("batas bawah\t:" + str(a))
print("batas atas\t:" + str(b))
print("jml iterasi\t:" + str(n))
print("besar h\t\t:" + str(h))

x = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1.25, 1.5, 1.75, 2, 2, 2, 2, 0.25, 0.5, 0.75, 1.25, 1.5, 1.75, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
y = [0, 1, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 1.25, 1.5, 1.75, 0.25, 0.5, 0.75, 1.25, 1.5, 1.75]

#x = [0 for it in list(range(n+1))]
#y = [0 for it in list(range(n+1))]

#for i in list(range(n+1)):
#    x[i] = a+i*h
#    y[i] = 3*pow(x[i],2)

odd = [0 for it in list(range(n))]
even = [0 for it in list(range(n))]

sum_odd = 0
sum_even = 0

for i in list(range(1,n,2)):
    sum_odd += y[i] 

for i in list(range(2,n,2)):
    sum_even += y[i] 

print("\nn\tx\ty")

for o in list(range(n+1)):
    print(str(o) + "\t" + str(round(x[o],2)) + "\t" + str(round(y[o],2)))

L = h*(y[0] + 4*sum_odd + 2*sum_even + y[n])/3

print("\nHasil itegrasi\t:" + str(round(L,3)))

plt.plot(x,y, "go")
plt.title
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
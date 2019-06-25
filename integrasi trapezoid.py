import matplotlib.pyplot as plt

print ("Aplikasi integrasi metode trapezoid")
print ("app version 1.0 alpha\n")

a = 1 #batas bawah
b = 16 #batas atas

n = 18 #banyak iterasi
h = (b-a)/n #kepadatan

print("batas bawah\t:" + str(a))
print("batas atas\t:" + str(b))
print("jml iterasi\t:" + str(n))
print("besar h\t\t:" + str(h))

x = [0 for it in list(range(n+1))]
y = [0 for it in list(range(n+1))]

for i in list(range(n+1)):
    x[i] = a+i*h
    y[i] = -0.0081*(pow(x[i],3)) + 0.1951*pow(x[i],2) - 1.6411*x[i] + 14.355

#y = -0,0081x3 + 0,1951x2 - 1,6411x + 14,355

sum_f = 0
for it in list(range(1,n,1)):
    sum_f += y[it]

for o in list(range(n+1)):
    print(str(o) + "\t" + str(round(x[o],2)) + "\t" + str(round(y[o],2)))

L = (h/2) * (y[0] + 2*sum_f + y[n])

print("\nHasil itegrasi\t:" + str(round(L,3)))

plt.plot(x,y, "go")
plt.title("Grafik Arus terhadap Waktu")
plt.xlabel("t (min)")
plt.ylabel("I (mA)")
plt.grid(True)
plt.axis([x[0]-1, x[n]+1, a, b])
plt.show()
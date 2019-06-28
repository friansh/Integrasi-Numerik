import matplotlib.pyplot as plt

print ("Aplikasi integrasi metode Simpson")
print ("app version 1.0 beta\n")

a = 1 #batas bawah
b = 16 #batas atas

n = 18 #banyak iterasi
h = (b-a)/n #kepadatan

print("batas bawah\t:" + str(a))
print("batas atas\t:" + str(b))
print("jml iterasi\t:" + str(n))
print("besar h\t\t:" + str(round(h, 4)))

x = [0 for it in list(range(n+1))]
y = [0 for it in list(range(n+1))]

#y = -0,0081x3 + 0,1951x2 - 1,6411x + 14,355

for i in list(range(n+1)):
    x[i] = a+i*h
    y[i] = -0.0081*(pow(x[i],3)) + 0.1951*pow(x[i],2) - 1.6411*x[i] + 14.355


odd = [0 for it in list(range(n))]
even = [0 for it in list(range(n))]

sum_odd = 0
sum_even = 0

for i in list(range(1,n,2)):
    sum_odd += y[i] 

for i in list(range(2,n,2)):
    sum_even += y[i] 

print("\nn\tx\t\ty")

for o in list(range(n+1)):
    print(str(o) + "\t" + str(round(x[o],4)) + "\t\t" + str(round(y[o],4)))

L = h*(y[0] + 4*sum_odd + 2*sum_even + y[n])/3

print("\nHasil itegrasi\t:" + str(round(L,4)))

plt.plot(x,y, "go")
plt.title("Grafik Arus terhadap Waktu")
plt.xlabel("t (min)")
plt.ylabel("I (mA)")
plt.grid(True)
plt.axis([x[0]-1, x[n]+1, a, b])
plt.show()
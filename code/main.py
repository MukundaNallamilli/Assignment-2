import numpy as np
import matplotlib.pyplot as plt

print('(x-h)^2/a^2 - (y-k)^2/b^2 = 1')
h = int(input('Enter the value of h:'))
k = int(input('Enter the value of k:'))
a = np.sqrt(int(input('Enter the value of a^2:')))
b = np.sqrt(int(input('Enter the value of b^2:')))
e = np.sqrt(1+(b*b)/(a*a))
f1 = h+a*e
f2 = h-a*e
d1 = h+a/e
d2 = h-a/e
print(f"Eccentricity e = {e}")
print(f'Center of hyperbola is ({h},{k})')
print(f'foci of hyperbola is ({f2},{k}) and ({f1},{k})')
print(f'Equation of directrix hyperbola is x = {d2} and x = {d1}')



def hyperbola_1(x,h,a,b,k):
     return k+b*(np.sqrt( ( (x-h)**2/(a**2) ) - 1 ) )
                 
def hyperbola_2(x,h,a,b,k):
    return k-b*(np.sqrt( ( (x-h)**2/(a**2) ) - 1 ) )

x1 = np.linspace(h+a,h+a+6,num=100)       
y1 = hyperbola_1(x1,h,a,b,k)

x2 = np.linspace(h-a,h-a-6,num=100)       
y2 = hyperbola_2(x2,h,a,b,k)

plt.figure(num= 0,dpi=80)
plt.plot(x1,y1,color='red')
plt.plot(x2,y2,color='blue')
plt.plot(x2,2*k-y2,color='blue')
plt.plot(x1,2*k-y1,color='red')

str1 = f'({h},{k})'
str2 = f'({f1:.2f},{k})'
str3 = f'({f2:.2f},{k})'
str4 = f'(x = {d1:.3f})'
str5 = f'(x = {d2:.3f})'
plt.text(h,k,str1)
plt.text(f1,k,str2)
plt.text(f2,k,str3)
plt.text(d1,k-6,str4)
plt.text(d2,k-6,str5)
ypt = np.linspace(-10,10,num=100)
xr=np.linspace(d1,d1,num=100)
xl=np.linspace(d2,d2,num=100)

plt.plot([h],[k],"o",label='center',color='black')
plt.plot([f1],[k],"o",label='foci',color='brown')
plt.plot([f2],[k],"o",color='brown')
plt.plot(xr,ypt,color='green',label='directrix')
plt.plot(xl,ypt,color='green')


plt.title('hyperbola')
plt.legend(loc="upper left")
plt.grid()
plt.show()



#day 2
a = 1
b = "hi"
c = 8.8
d = False 
print(type(a))
print(type(b))
print(type(c))
print(type(d))

e = 17
f = 5
g = e+f
h = e-f
i = e*f
j = e//f
k = e%f
print(g)
print(h)
print(i)
print(j) 
print(k) 

x = 10 
y = 20 
x,y=y,x
print(x,y)

#day 3

a = "Safi"
b = 2008
print("Hello", a, "we both are of same birth year, that is", b)

#Name = str(input("name"))
#Age = int(input("age"))
#Marks = float(input("Marks")) 
#print(f"Name:{Name}, Age;{Age}, Marks: {Marks}%")

#day 4

a = int(input("enter seconds"))
b = a//3600 #hour 
c = (a%3600)//60 #minutes
d = a%60 #seconds
print(b,"hour",c,"minute",d,"second")

width = int(input("enter width of rectangle"))
height = int(input("enter height of rectangle"))

area = int(width*height)
perimeter = int(2*(height+width))
print(f"area:{area},perimeter:{perimeter}")
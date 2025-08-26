#Autor: Juan David García

#Prueba inicial

print("hola jaja")

#2
x=int(input("Ingrese un numero: "))
r=0
for i in range(11):
	r=x*i
	print(r)

#3
def factorial(a):
	r=1
	for i in range(1,a+1):
		r*=i
	return r
x=int(input("Ingrese un numero: "))
print(factorial(x))
	
f = open("showcdp1.txt","r")
it = (linea for i, linea in enumerate(f) if i>=4)
for linea in it:
	l = linea.split()
	a = l[1]+l[2]
	b = l[8]+l[9]
	print(a+"  "+b)
print()

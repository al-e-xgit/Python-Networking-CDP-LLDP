from getnumIPs import cuenta
from getvecinos import datos
from gethostname import hostname
from getshow import showtodo
titulo={0:"Hostname",1:"Local Interface",2:"Neighbor",3:"Neighbor Interface"}

showtodo()
c = cuenta()
veci, loc, vec, nrolin = datos()
host = hostname()
l=[]
r=[]
tit=[]
for i in range(len(titulo)):
	tit.append(len(titulo[i]))
	print("+"+"-"*(len(titulo[i])+2),end="")
print("+")

for k  in range(4):
	print("| "+titulo[k],end=" ")
print("|")


for i in range(len(titulo)):
	print("+"+"-"*(len(titulo[i])+2),end="")
print("+")

for i in range(c):
	for j in range(int(nrolin[str(i)])):
		val =[len(host["host"+str(i)]),len(loc["loc"+str(i)+str(j)]),len(veci["veci"+str(i)+str(j)]),len(vec["vec"+str(i)+str(j)])] 
		for k in range(len(tit)):
			a=tit[k]+2-val[k]
			if a%2==0:
				l.append(a/2)
				r.append(a/2)
			else:
				l.append((a-1)/2+1)
				r.append((a-1)/2)
				
		print("|"+" "*int(l[0])+host["host"+str(i)]+" "*(int(r[0]))+"|"+" "*int(l[1])+loc["loc"+str(i)+str(j)]+" "*(int(r[1]))+"|"+" "*int(l[2])+veci["veci"+str(i)+str(j)]+" "*(int(r[2]))+"|"+" "*int(l[3])+vec["vec"+str(i)+str(j)]+" "*(int(r[3]))+"|")

for i in range(len(titulo)):
	print("+"+"-"*(len(titulo[i])+2),end="")
print("+")

#print("+"+"-"*(len(titulo[0])+2)+"+"+"-"*(len(titulo[1])+2)+"+"+"-"*(len(titulo[2])+2)+"+"+"-"*(len(titulo[3])+2)+"+")

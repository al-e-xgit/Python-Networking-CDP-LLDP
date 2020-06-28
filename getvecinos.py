from getnumIPs import cuenta


def datos():
	nroRouters = cuenta()
	vecino={}
	interfazLOC={}
	interfazVEC={}
	nrolin={}
	j=0
	k=0
	
	for i in range(nroRouters):
		j=0
		k=0 
		with open("showcdp"+str(i)+".txt", "r") as file:
   			for line in file.readlines():
       				if k==1:
       					l=line.split(".")
       					m=line.split()
       					vecino["veci"+str(i)+str(j)]=l[0]
       					interfazLOC["loc"+str(i)+str(j)]=m[1]+m[2]
       					interfazVEC["vec"+str(i)+str(j)]=m[8]+m[9]
       					j=j+1
       				if "Device" in line:
       					k=1
		nrolin[str(i)]=j
	return vecino, interfazLOC, interfazVEC, nrolin


'''
print(vecino)
print(interfazLOC)
print(interfazVEC)
print(nrolin)

f = open("showcdp0.txt","r")
lee_lineas=f.readlines()
f.close()
a = lee_lineas[5] 

splitted = a.split(".")
print(splitted[0])
'''

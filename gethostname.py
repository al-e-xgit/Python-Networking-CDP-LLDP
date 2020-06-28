from getnumIPs import cuenta

def hostname():
	hostn={}
	hosts=cuenta()
	for i in range(hosts):
		with open("showhard"+str(i)+".txt", "r") as file:
			for line in file.readlines():
				if "Rout" in line:
					a = line.split() 
					H = a[0]
					hostn["host"+str(i)] = H
				file.close()
	return hostn
#prueba git	
#print(hostn)

'''
f = open("showhard.txt","r")
lee_lineas=f.readlines()
f.close()
a = lee_lineas[8].split() 
HOSTNAME=a[0]
print(HOSTNAME)
'''

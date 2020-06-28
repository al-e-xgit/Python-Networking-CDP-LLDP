def dixIP():
	IPS={}
	f=open("listaIPs.txt","r")
	lee=f.readlines()
	nrolin=len(lee)
	for i in range(nrolin):
		a=lee[i].splitlines()
		IPS["ip"+str(i)]=a[0]
	return IPS

#print(IPS)

'''def dixIP():
	IPS = {}
	with open("listaIPs.txt","r") as f:
		for line in f:
			(key, val) = line.split()
			IPS["ip"+str(key)] = val
	#print(IPS)
	return IPS
EL CODIGO DE LINEAS ARRIBA TAMBIEN FUNCIONA PERO GUARDANDO EN IPs.TXT
0 1P0
1 IP1
.
.
.
'''

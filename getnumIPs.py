def  cuenta():
	count = len(open("listaIPs.txt","r").readlines())
	return count

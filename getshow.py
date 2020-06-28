from netmiko import ConnectHandler
from getnumIPs import cuenta
from getIPs import dixIP

def showtodo():
	nroIPs = cuenta()
	IP = dixIP()
	
	for i in range(nroIPs): 
		A=IP["ip"+str(i)]
		cisco_881 = {
		'device_type': 'cisco_ios',
		'host': A,
		'username': 'alexander',
		'password': 'ayma',
		}
		
		net_connect = ConnectHandler(**cisco_881)
		
		output2 = net_connect.send_command('show cdp neighbors')
		b = open("showcdp"+str(i)+".txt","w")
		b.write(output2)
		b.close()
		
		output1 = net_connect.send_command('show hardware')
		a = open("showhard"+str(i)+".txt","w")
		a.write(output1)
		a.close()
	

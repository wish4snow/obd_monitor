import obd
import time
import subprocess, os

file = open("obd_car_data.txt", "w+")
connection = obd.OBD("192.168.0.10", 35000)
user_state = True
value_adderess = []
file.write("New session")
print ("New session")

supported_pids_mode1 = obd.commands.PIDS_A
print (connection.query(supported_pids_mode1).value)
for i in range(1, 0x20) :
	print (connection.query(supported_pids_mode1).value[i])	
	if (connection.query(supported_pids_mode1).value[i] == 1):
		value_adderess.append(obd.commands[1][i])
		print (connection.query(value_adderess).value)
		print (i)

while (user_state) :
	try:
		subprocess.call('clear')

		time.sleep(10)	
	except KeyboardInterrupt:
		user_state = False

print ("\nConnection closed")
connection.close()
file.close()

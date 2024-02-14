import obd
import time
import subprocess, os

file = open("obd_car_data.txt", "w+")
connection = obd.OBD("192.168.0.10", 35000)
user_state = True
value_adderess = []
user_wanted_pids = [0x04, 0x05, 0x0B, 0x0C, 0x11] #range from 0x01 to 0x20 in hex

file.write("New session")
print ("New session")

supported_pids_mode1 = obd.commands.PIDS_A
print (connection.query(supported_pids_mode1).value)

for i in range(1, 0x20) :
	if ((connection.query(supported_pids_mode1).value[i] == 1) & (connection.query(supported_pids_mode1).value[i] in user_wanted_pids)):
		value_adderess.append(obd.commands[1][i])
		print (connection.query(value_adderess).value)

while (user_state) :
	try:
		subprocess.call('clear')
		print ("values:")
		for i in value_adderess:
			print (value_adderess[i])
			print (connection.query(value_adderess[i]).value)
		time.sleep(10)
	except KeyboardInterrupt:
		user_state = False

print ("\nConnection closed")
connection.close()
file.close()

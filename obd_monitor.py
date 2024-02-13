import obd
import time
import subprocess, os

file = open("obd_car_data.txt", "w+")
connection = obd.OBD("192.168.0.10", 35000)
user_state = True

file.write("New session")
print ("New session")

supported_pids_mode1 = obd.commands.PIDS_A
print (connection.query(supported_pids_mode1).value)
rpm_adderess = obd.commands.RPM
coolant_temp_adderess = obd.commands.COOLANT_TEMP
maf_adderess = obd.commands.MAF
throttle_adderess = obd.commands.THROTTLE_POS
throttle_actuator_adderess = obd.commands.THROTTLE_ACTUATOR
while (user_state) :
	try:
		rpm = connection.query(rpm_adderess)
		coolant_temp = connection.query(coolant_temp_adderess)
		maf = connection.query(maf_adderess)
		throttle = connection.query(throttle_adderess)
		#file.write(rpm.value) 
	
		subprocess.call('clear')
		print(rpm.value)
		print(coolant_temp.value)
		print (maf.value)
		print (throttle.value)

		for i in range(1, 0x20) :
			print (connection.query(supported_pids_mode1).value[i])	
			
			if (connection.query(supported_pids_mode1).value[i] == 1):
				value_adderess = obd.commands[1][i]
				print (connection.query(value_adderess).value)
				print (i)
		time.sleep(10)	
	except KeyboardInterrupt:
		user_state = False

print ("\nConnection closed")
connection.close()
file.close()

import obd
import time
import subprocess, os
import datetime

os.chdir("sessions/")

print ("Starting monitor...")

#use this for later, not working for some reason right now, whatever
#formated_date = datetime.datetime.now().strftime("%x_%X")

file = open("session_data_" + str(datetime.datetime.now()) + ".csv", "w+")
connection = obd.OBD("192.168.0.10", 35000)
user_state = True
value_adderess = []
user_wanted_pids = [0x02, 0x04, 0x05, 0x0B, 0x0C, 0x11, 0x21, 0x06] #range from 0x01 to 0x20 in hex
print_output = ""
csv_output = ""

print ("New session")

supported_pids_mode1 = obd.commands.PIDS_A
supported_pids_mode2 = obd.commands.PIDS_B
supported_pids_mode3 = obd.commands.PIDS_C
print (connection.query(supported_pids_mode1).value)
print (connection.query(supported_pids_mode2).value)

print (connection.query(supported_pids_mode3).value)
print(type(connection.query(supported_pids_mode1).value))


pid_range = 0x20
full_pid_bitarray = [True]
supported_pids_mode1 = obd.commands.PIDS_A

for i in range(0x01, pid_range):
    full_pid_bitarray.append(connection.query(supported_pids_mode1).value[i - 1])

if (full_pid_bitarray[len(full_pid_bitarray) - 1]):

    supported_pids_mode2 = obd.commands.PIDS_B
    
    for i in range(0x00, pid_range + 1):
    
        full_pid_bitarray.append(connection.query(supported_pids_mode2).value[i - 1])

if (full_pid_bitarray[len(full_pid_bitarray) - 1]):

    supported_pids_model3 = obd.commands.PIDS_C
    
    for i in range(0x00, pid_range):
        full_pid_bitarray.append(connection.query(supported_pids_mode3).value[i - 1])
print (full_pid_bitarray)
print (len(full_pid_bitarray))
print("done")


for i in range(0x01,len(full_pid_bitarray) - 1) :
	print (hex(i))
	#print (connection.query(supported_pids_mode1).value[i - 1])
	if (full_pid_bitarray[i] & (i in user_wanted_pids)):
		value_adderess.append(obd.commands[1][i])
		print ("value added")
	print ("\n")
print("done")

count = 0

while (user_state) :
	try:
		
		for i in value_adderess:
			print_output += str(i) + "\n" + str(connection.query(i).value) + "\n"
			csv_output += str(count) + "," + str(i) + "," + str(connection.query(i).value.magnitude) + "," + str(connection.query(i).value.units) + "\n"
			#print (i)
			#print (connection.query(i).value)
		
		subprocess.call('clear')
		print ("values:")
		print (print_output)

		file.write(csv_output)

		csv_output = ""
		print_output = ""
		count += 1
		time.sleep(0.1)

	except KeyboardInterrupt:
		user_state = False
		print ("Are you still testing?")
		
		if (input(":") == "no"):
			print ("\nConnection closed")
			connection.close()
			file.close()




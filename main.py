import pymem
import re, win32api, time

def displayMessage(msg):
	s = ""
	for i in msg:
	    s += i                      
	    print(s, end='')                                                    
	    time.sleep(0.05)

pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'.\x17\xF6\x40\x14\x10',
                                         clientModule).start()

print("\nPrime : [1]\tNon-Prime : [2]\n")

while(True):

	if(win32api.GetAsyncKeyState(ord('1'))):
				time.sleep(1.2)
				pm.write_uchar(address, 0x75)
				print("\r\t\t\t", end='')
				displayMessage("\rChanged to Prime!")
				continue
	if(win32api.GetAsyncKeyState(ord('2'))):
		time.sleep(1.2)
		pm.write_uchar(address, 0x74)
		print("\r\t\t\t", end='')
		displayMessage("\rChanged to Non-Prime!")

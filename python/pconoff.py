# Name:    PC Relay ON/OFF SWITCH of AZDelivery 8-Relais
# Author:  Thomas Schütz
# Datum:   11.12.2021
# Version: 1.1
# Beschreibung:
#          Ansteuerung für AZDelivery 8 Relay Modul zum Ein-/Ausschalten von PCs
# 	   Befehl lautet pyhton3 pconoff.py * (* = Relay Nummer)
#	   Beispiel: pyhton3 pconoff.py 1 (Startet PC an Relay K1 neu)

import RPi.GPIO as GPIO
import time
import sys

#Uebergabe Systemparameter (Relaynummer)
a = sys.argv[1]

#Initialisierung GPIOs als Nummern
GPIO.setmode(GPIO.BCM)

#Warnings ausschalten da doppelt initialisiert wird
GPIO.setwarnings(False)

#Zuordnung Relay Nummer zu GPIO Pin
if a=='1': #Name für K1
	b=23
elif a=='2': #Name für K2
        b=22
elif a=='3': #Name für K3
        b=27
elif a=='4': #Name für K4
        b=18
elif a=='5': #Name für K5
        b=17
elif a=='6': #Name für K6
        b=15
elif a=='7': #Name für K7
        b=14
elif a=='8': #Name für K8
        b=4
else:
	print('Konnte Eingabe "'+ a +'" nicht finden') 
	quit()

#Initialisiere GPIO als Output
GPIO.setup(b, GPIO.OUT) #K1

print('Neustart K'+a)

#Neustart des jeweiligen Relays
GPIO.output(b, GPIO.LOW)  #EIN
time.sleep(5) #Ausschaltzeit (Taster)
GPIO.output(b, GPIO.HIGH) #AUS
time.sleep(30) #Wartezeit bis PC Heruntergefahren
GPIO.output(b, GPIO.LOW)  #EIN
time.sleep(0.5) #Einschaltzeit (Taster)
GPIO.output(b, GPIO.HIGH) #AUS

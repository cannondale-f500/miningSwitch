# miningSwitch
Raspberry PI with relais Card AZ-Delivery 8-Relais Modul 5V with optocoupler Low-Level-Trigger
control by console (SSH) over SSH Apps to hard reset a computer with a pyhton script.
The outputs of the relais card can be connected up to 8 power-switches of computers. The pins can be connected parallel to the switch.
Therefore it is possible to switch on off or restart a computer via the internet.
Actually there is only an implementation of a restart.

*Read this in other languages: [English](README.md), [German](README-de.md).*

## Hardware(Setup)
The Raspberry PI is connected via a ribbon cable with the 8-relais module.

The following connection has been used (others are possible by editing the script and startup):

pin number | pin name | <-> | pin number | pin name
---|---|---|---|---
1 | GND | <-> | 20 | GND
2 | K1 | <-> | 16 | GPIO23
3 | K2 | <-> | 15 | GPIO22
4 | K3 | <-> | 13 | GPIO27
5 | K4 | <-> | 12 | GPIO18
6 | K5 | <-> | 11 | GPIO17
7 | K6 | <-> | 10 | GPIO15
8 | K7 | <-> | 8 | GPIO14
9 | K8 | <-> | 7 | GPIO4
10 | Vcc | <-> | 4 |5V


## Software
* The raspberrypi image has to be downloaded and written on a SDcard. `2021-10-30-raspios-bullseye-armhf-full`
* Just adding the entry of `config.txt` with the entries of the repository
  This is to initialize the GPIOs to Outputs and non active relais.
* Implement the `ddupdate.sh` script with key und domain
* The `crontab` script on `/etc/crontab` should be added with the entries of the repository. The script will be executed every minute. Only If the IP changes the ddns entry will be updated
* The `pconoff` script must be copied to the folder `/home/pi`
* To execute the script remote a connection via SSH is used. To make a secure connection a key is used and the configuration has to be edited like in the following documentation. Its important to only accept connection via key (Siehe [Dokumentation](https://pimylifeup.com/raspberry-pi-ssh-keys/))
* A local connection via VNC has been enabled in the settings via the menu.
* Adding a fixed IP-adress in `/etc/dhcpcd.conf` like this:

  `interface eth0
  
  static ip_address=192.168.1.x/24
  
  static routers=192.168.1.1
  
  static domain_name_servers=192.168.1.1`
* The routing setting should be implemented to the router shown in the images `T-Mobile_Router_Einstellung*`. The IP address must be set to the fixed IP address of the raspberry PI. Afterwards the router should be restarted.

If prefered the scripts can be implemented to other folders. Therefore the path has to be changed

## Controlling
With the command `pyhton3 pconoff.py 1` every relais can be controlled with its number. The cycling of the relais is configured:
* computer off (5s relais on)
* waiting time for 30s
* computer on (0.5s relais on)

### Android:
Far Commander
- The public Key with password has to be added. Be careful where the file will be stored or how you transfer the file. For login only the username has to be added.

### Apple
Termius - SSH client 
- The public Key with password has to be added. Be careful where the file will be stored or how you transfer the file. For login only the username has to be added.

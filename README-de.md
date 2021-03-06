# miningSwitch
Raspberry PI mit Relay Karte AZ-Delivery 8-Relais Modul 5V with optocoupler Low-Level-Trigger
Steuerung über eine Konsole (SSH) und über SSH Apps für einen computer Reset über den Einschaltknopf mittels pyhton Skript.
Die Ausgänge der Relay Karte können mit bis zu 8 Schalter verbunden werden. Die Pins werden parallel zum Schalter verbunden. Damit kann der Computer manuell oder per Software bedient werden.
Hiermit kann der jeweilige Schalter (Ein-/Ausschalter) über das Internet bedient werden.
Im Moment ist nur ein Neustart im Script vorhanden.

*Read this in other languages: [English](README.md), [German](README-de.md).*

## Hardware(Aufbau)
Der Raspberry PI wird über ein Falchbandkabel mit dem 8-Relais Modul verbunden.

Hierzu werden die folgenden PINs verwendet:

Pin Nummer | Pin Name | <-> | Pin Nummer | Pin Name
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
* Am RaspberryPI wird das aktuelle Image erstellt. 2021-10-30-raspios-bullseye-armhf-full
* Die config.txt wird erweitert
  Hiermit werden die Relays beim Einschalten des PIs ausgeschaltet und die GPIOs vorkonfiguriert
* Im home Verzeichnis wird das ddupdate.sh Script konfiguriert mit der jeweiligen Key und domain
* Im crontab gehört der Eintrag für die Ausführung des scripts eingetragen. Beispielsweise jede Minute
* Das pconoff script muss in das Homeverzeichnis hinzugefügt werden.
* Zur Verbindung wird SSH verwendet. Hierbei ist ein Key zu erstellen und die Konfiguration abzuändern, sodass nur mit dem Key ein Login möglich ist. (Siehe [Dokumentation](https://pimylifeup.com/raspberry-pi-ssh-keys/))
* Die Verbindung ohne Key ist zu unterbrechen um die Sicherheit zu erhöhen.
* Eine lokale Verbindung über VNC Viewer ist möglich
* Zusätzlich benötigt der PI eine fixe IP-Adresse im Netzwerk. Dies geschieht durch anpassen des Files `/etc/dhcpcd.conf`:
  `interface eth0
  static ip_address=192.168.1.x/24
  static routers=192.168.1.1
  static domain_name_servers=192.168.1.1`

* Das Routing wird wie in den Bildern "T-Mobile_Router_Einstellung*" ersichtlich eingestellt. Die IP muss die des Raspberry PIs entsprechen. Danach ist der Router neu zu starten.

Optional können die Scripte auch in andere Verzeichnisse hinterlegt werden. Hierzu müssen jedoch die Pfade angepasst werden.

## Ansteuern
Mit dem Befehl `pyhton3 pconoff.py 1` Kann das jeweilige Relay angesteuert werden und das jeweilige Relay führt folgenden Zyklus aus:
* PC Ausschalten mit 5s Ein
* Wartezeit mit 30s
* PC Einschalten 0.5s Ein

### Android:
Far Commander
- Der public Key mit Passwort ist hinzuzufügen. Für den Log-In benötigt man kein Passwort nur den Benutzernamen.

### Apple
Termius - SSH client 
- Der public Key mit Passwort ist hinzuzufügen. Für den Log-In benötigt man kein Passwort nur den Benutzernamen.

#!/bin/bash

KEYAUTH="KEY"
HOSTNAME="domain.ddnss.de"
PFAD="/home/pi"
ALLHOST="all" # Alternativ Hostname

DATUM=`date +%Y-%m-%d\ %H:%M:%S`

IP=`wget -q -O - https://www.ddnss.de/meineip.php| grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'`

UPDIP=`cat $PFAD/updip.txt`

echo "Aktuelle IP=$UPDIP"

if [ "$IP" == "$UPDIP" ]; then

echo "$DATUM - IP is gleich - KEIN UPDATE" >> $PFAD/ddupdate.log

else

echo "$DATUM - Neue-IP: $ip / Alte-IP: $UPDIP - UPDATE!" >> $PFAD/ddupdate.log

echo $IP > $PFAD/updip.txt

wget -q -O - 'https://www.ddnss.de/upd.php?key='$KEYAUTH'&host='$HOSTNAME'&host='$ALLHOST''>> $PFAD/ddupdate.log

echo " " >> $PFAD/ddupdate.log

echo "Update ..."

fi

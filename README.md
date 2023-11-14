# Femtech

import network
import time
import urequests


#Autorisation
ssid = "MiniPhone"
password = "femtech2023"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

if wlan.isconnected():
    print(wlan.ifconfig())
    url = 'https://api.energidataservice.dk/dataset/PowerSystemRightNow?limit=5'

    response = urequests.get(url)
    result = response.json()

    records = result.get('records', [])
    for record in records:
        tidspunkt = record['Minutes1DK']
        dele = tidspunkt.split("T")
        tidspunkt = dele[1]
        solenergi = record['SolarPower']
        vindenergi = record['OffshoreWindPower'] + record['OnshoreWindPower']
        forssileenergi= record ['ProductionGe100MW'] + record ['ProductionLt100MW']
        
    print("Solenergi:", solenergi) 
    print("Vindenergi:", vindenergi)
    print ("Forssile Brændstoffer: ", forssileenergi)





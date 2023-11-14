import network
import time
import urequests
from machine import ADC, PWM, Pin


#Autorisation
ssid = "MiniPhone"
password = "femtech2023"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while(True):
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


#tilslut vindmølle
    gpiopin = 16

    pwm = PWM(Pin(gpiopin))
    pwm.freq(1000)

    samletværdi = int(vindenergi + 10000.0)


# tag værdi fra 'Vindenergi' + 10.000
# samlet = vind + 10000

    pwm.duty_u16(samletværdi)
    
    time.sleep(0.5)


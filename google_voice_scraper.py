import urllib
from googlevoice import Voice
from googlevoice.util import input
import time
voice = Voice()
voice.login("cian.conway@outlook.com","password")
phoneNumber = "240-330-xxxx"
text = "Tickets for Louis are available"
i=0
site = "http://event.etix.com/ticket/p/5491041/louis-cklive-washington-lincoln-theatre-washingtondc" # Site URL
a=urllib.urlopen(site).read()
 
while a.find("Sorry!") != -1:
        time.sleep(60)
        a=urllib.urlopen(site).read()
        print a.find("Sorry!")
       
 
while i < 10:
        voice.send_sms(phoneNumber, text)
        time.sleep(60)
        i = i + 1
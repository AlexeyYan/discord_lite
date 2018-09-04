import requests
import qrcode
from urllib.parse import urlsplit

def Curs():
 r=requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')# NBRB Api
 r=r.json()
 USD=r[4]['Cur_OfficialRate']
 EUR=r[5]['Cur_OfficialRate']
 RUB=r[16]['Cur_OfficialRate']
 UAH=r[2]['Cur_OfficialRate']
 return 'Курс доллара: {}\nКурс евро: {}\nКурс рубля(100): {}\nКурс гривны(100): {}'.format(USD, EUR, RUB, UAH)

def Curs_All():
 r=requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')# NBRB Api
 curs="***Курсы валют на сегодня:***\n"
 for curs in r.json():
  curs+=curs['Cur_Name']+'('+str(curs['Cur_Scale'])+'): __*'+str(curs['Cur_OfficialRate'])+'*__\n'
 return curs

def createQRCode(value):
    qr=qrcode.QRCode(version=1, box_size=12, border=2)
    qr.add_data(value)
    qr.make(fit=True)
    x=qr.make_image()
    image_file=open('qr.jpg', 'wb')
    x.save(image_file, 'JPEG')
    image_file.close()

def getInstagramContent(url):
     url=urlsplit(url)
     if url.netloc in ['www.instagram.com', 'instagram.com']:
        link = 'http://'+url.netloc+url.path+'media/?size=l'
        r=requests.get(link)
        if not r.ok:
         return 'Ссылка не найдена'
        return link
     else: 
         return 'Not Instagram'
        

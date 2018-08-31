import requests
import qrcode
from urllib.parse import urlsplit

def Curs():
 r=requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')
 cursUSD=r.json()[4]['Cur_OfficialRate']
 cursEUR=r.json()[5]['Cur_OfficialRate']
 cursRUB=r.json()[16]['Cur_OfficialRate']
 cursUAH=r.json()[2]['Cur_OfficialRate']
 return 'Курс доллара: '+ str(cursUSD)+'\nКурс евро: ' + str(cursEUR) +'\nКурс рубля(100): '+str(cursRUB)+'\nКурс гривны(100): '+str(cursUAH)

def Curs_All():
 r=requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')
 curs="***Курсы валют на сегодня:***\n"
 i=0
 while(i<26):
  curs+=r.json()[i]['Cur_Name']+'('+str(r.json()[i]['Cur_Scale'])+'): __*'+str(r.json()[i]['Cur_OfficialRate'])+'*__\n'
  i+=1
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
        

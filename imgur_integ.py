from imgurpython import ImgurClient
import os
import random

client_id = os.environ['IMGUR_ID']
client_secret = os.environ['IMGUR_SECRET']

def Random_Pic():

 client = ImgurClient(client_id, client_secret)

 items = client.gallery()
 num=random.randint(0,len(items))
 return items[num].link

def Search_Pic():

 pass

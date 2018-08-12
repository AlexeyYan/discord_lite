import vk
import random
import os

vk_token = os.environ['VK_TOKEN']

def Random_VkMem():
 session=vk.Session(vk_token)
 api = vk.API(session)
 offset=random.randint(0, 1000)
 r=api.wall.get(owner_id='-65596623', count='100', offset=offset, v='5.7')
 r=random.choice(r['items'])
 url=r['attachments'][0]['photo']['photo_807']
 return url

def Random_Joke():
 session=vk.Session(vk_token)
 api = vk.API(session)
 offset=random.randint(0, 1000)
 r=api.wall.get(owner_id='-22222333', count='100', offset=offset, v='5.7')
 r=random.choice(r['items'])
 url=r['attachments'][0]['photo']['photo_807']
 return url

def Random_BNTU_Mem():
 session=vk.Session(vk_token)
 api = vk.API(session)
 r=api.photos.get(owner_id=-59496516, album_id= '247176525', v='5.7')
 r=random.choice(r['items'])
 url = r['photo_604']
 return url

def Random_IT_Mem():
 session=vk.Session(vk_token)
 api = vk.API(session)
 offset=random.randint(0, 100)
 r=api.wall.get(owner_id='-80799846', count='100', offset=offset, v='5.7')
 r=random.choice(r['items'])
 url=r['attachments'][0]['photo']['photo_604']
 return url

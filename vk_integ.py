import vk
import random
import os


class Vk_Integration(object):
   def __init__(self):
       self.vk_token = os.environ['VK_TOKEN']
       self.session = vk.Session(vk_token)
       self.api = vk.API(session)
       self.v='5.7'

   def random_mem(self):
     offset = random.randint(0, 1000)
     r = self.api.wall.get(owner_id='-65596623', count=100, offset=offset, v=self.v)
     r = random.choice(r['items'])
     url = r['attachments'][0]['photo']['photo_807']
     return url

   def random_joke():
      offset = random.randint(0, 1000)
      r = self.api.wall.get(owner_id=-22222333, count=100, offset=offset, v=self.v)
      r = random.choice(r['items'])
      url = r['attachments'][0]['photo']['photo_807']
      return url

   def random_bntu_mem():
      r = self.api.photos.get(owner_id=-59496516, album_id=247176525, v=self.v)
      r = random.choice(r['items'])
      url = r['photo_604']
      return url

   def random_it_mem():
     offset = random.randint(0, 100)
     r = self.api.wall.get(owner_id=-80799846, count=100, offset=offset, v=self.v)
     r = random.choice(r['items'])
     url = r['attachments'][0]['photo']['photo_604']
     return url

   def pozor_story():
       offset = random.randint(0, 1000)
       r = self.api.wall.get(owner_id=-71729358, count=100, offset=offset, v=self.v)
       r = random.choice(r['items'])
       story = r['text']
       return story

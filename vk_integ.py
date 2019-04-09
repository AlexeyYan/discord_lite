import vk
import random
import os


class Vk_Integration(object):
    def __init__(self):
        self.vk_token = os.environ['VK_TOKEN']
        self.session = vk.Session(self.vk_token)
        self.api = vk.API(self.session)
        self.v = '5.7'

    def random_mem(self):
        offset = random.randint(0, 1000)
        r = self.api.wall.get(owner_id='-109125388', count=100,
                              offset=10, v='5.7')['items']
        r = random.choice(r)
        while True:
            item = random.choice(r['attachments'])
            if item['type']=='photo': break
        if item:
           if 'photo_807' in item['photo']:
               return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
               return item['photo']['photo_604']
            else: return 'Мемы не обнаружены'

    def random_joke(self):
        offset = random.randint(0, 1000)
        r = self.api.wall.get(owner_id=-22222333,
                              count=100, offset=offset, v=self.v)
        r = random.choice(r['items'])
         while True:
            item = random.choice(r['attachments'])
            if item['type']=='photo': break
        if item:
           if 'photo_807' in item['photo']:
               return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
               return item['photo']['photo_604']
            else: return 'Мемы не обнаружены'

    def random_bntu_mem(self):
        r = self.api.photos.get(
            owner_id=-59496516, album_id=247176525, v=self.v)
        r = random.choice(r['items'])
        while True:
            item = random.choice(r['attachments'])
            if item['type']=='photo': break
        if item:
           if 'photo_807' in item['photo']:
               return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
               return item['photo']['photo_604']
            else: return 'Мемы не обнаружены'

    def random_it_mem(self):
        offset = random.randint(0, 100)
        r = self.api.wall.get(owner_id=-80799846,
                              count=100, offset=offset, v=self.v)
        r = random.choice(r['items'])
      while True:
            item = random.choice(r['attachments'])
            if item['type']=='photo': break
        if item:
           if 'photo_807' in item['photo']:
               return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
               return item['photo']['photo_604']
            else: return 'Мемы не обнаружены'

    def pozor_story(self):
        offset = random.randint(0, 1000)
        r = self.api.wall.get(owner_id=-71729358,
                              count=100, offset=offset, v=self.v)
        r = random.choice(r['items'])
        story = r['text']
        return story

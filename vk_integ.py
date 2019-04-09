import random
import os
import vk



class Vk_Integration(object):
    def __init__(self):
        self.vk_token = os.environ['VK_TOKEN']
        self.session = vk.Session(self.vk_token)
        self.api = vk.API(self.session, v='5.7')
        
    def random_pic(self):
        offset = random.randint(0, 1000)
        r=self.api.wall.get(owner_id='-109125388', count=100, offset=10)['items']
        r=random.choice(r)
        while True:
           item=random.choice(r['attachments'])
           if item['type'] == 'photo': break
        if item:
            if 'photo_807' in item['photo']:
                return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
                return item['photo']['photo_604']
            else: return 'Мемы не обнаружены'
    
    def pozor_story(self):
        offset = random.randint(0, 1000)
        r=self.api.wall.get(owner_id='-71729358', count=100, offset=10)['items']
        r=random.choice(r)
        return r['text']

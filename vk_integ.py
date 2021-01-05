import random
import os
import vk


class Vk_Integration(object):
    def __init__(self):
        self.vk_token = os.environ['VK_TOKEN']
        self.session = vk.Session(self.vk_token)
        self.api = vk.API(self.session, v='5.21')

    def random_pic(self):
        offset = random.randint(0, 1000)
        while True:
            r = self.api.wall.get(owner_id='-65596623', count=100, offset=offset)
            r = random.choice(r['items'])
            item = random.choice(r['attachments'])
            if item['type'] == 'photo':
                break
        if item:
            if 'photo_807' in item['photo']:
                return item['photo']['photo_807']
            elif 'photo_604' in item['photo']:
                return item['photo']['photo_604']
            else:
                return 'Мемы не обнаружены'

    def pozor_story(self):
        while True:
            offset = random.randint(0, 1000)
            r = self.api.wall.get(owner_id='-71729358', count=100, offset=offset)['items']
            r = random.choice(r)
            print(r)
            if r['marked_as_ads'] != 1:
                if r['text']:
                    return r['text']
                elif r['attachments']:
                    if r['attachments'][0]['photo']['photo_604']:
                        return r['attachments'][0]['photo']['photo_604']
            else:
                continue

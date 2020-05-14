import random
import requests
import os


class Rand():
    net_random = True
    main_url = 'https://api.random.org/json-rpc/2/invoke'

    def __init__(self):
        self.KEY = os.environ['RANDKEY']
        try:
            r = requests.post(self.main_url)
        except Exception:
            self.net_random = False
            print("Use local random")
        if r.status_code != 415:
            self.net_random = False
            print("Use local random")

    def get_random(self, min_num, max_num, amount, replacement=False):
        ans = []
        if self.net_random:
            payload = {
                'jsonrpc': '2.0',
                'method': "generateIntegers",
                'params': {
                    'apiKey': self.KEY,
                    'n': amount,
                    'min': min_num,
                    'max': max_num,
                    'replacement': replacement},
                'id': random.randint(1, 1000)}
            r = requests.post(self.main_url, json=payload).json()
            ans = r['result']['random']['data']
        else:
            while amount >= 0:
                ans.append(random.randint(min_num, max_num))
        return ans

    def Dice(self):
        ans = self.get_random(1, 6, 2, replacement=True)
        return ans[0], ans[1]

    def Flip(self):
        if random.randint(0, 1000) <= random.randint(0, 1000):
            ans = 'Орёл'
        else:
            ans = 'Решка'
        return ans

    def Roll(self, start, end, amount):
        return self.get_random(start, end, amount)

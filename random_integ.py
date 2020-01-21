import random
import requests


class Rand():
    net_random = True
    main_url = 'https://www.random.org/integers/'

    def __init__(self):
        try:
            r = requests.get(self.main_url, params={})
        except Exception:
            self.net_random = False
        if not r.ok:
            self.net_random = False

    def parse(self, line):
        return line.decode().split('\n')

    def get_random(self, min_num, max_num, amount):
        ans = []
        if self.net_random:
            r = requests.get(self.main_url, params={'num': amount,
                                                    'min': min_num,
                                                    'max': max_num,
                                                    'col': 1,
                                                    'base': 10,
                                                    'format': 'plain',
                                                    'rnd': 'new'})
            ans = self.parse(r.content)
        else:
            while amount >= 0:
                ans.append(random.randint(min_num, max_num))
        return ans

    def Dice(self):
        ans = self.get_random(1, 6, 2)
        return ans[0], ans[1]

    def Flip(self):
        if random.randint(0, 1000) <= 453:
            ans = 'Орёл'
        else:
            ans = 'Решка'
        return ans

    def Roll(self, start, end, amount):
        return self.get_random(start, end, amount)

import random
import requests


class Rand():
    net_random=True
    main_url='https://www.random.org/integers/'

    def __init__(self):
        try:
            r=requests.get(main_url, params={})
        except:
            self.net_random=False
        if r.status!=200:
            self.net_random=False
            
    def parse(self, line):
        return line.decode().split('\n')
    
    def get_random(self, min, max, amount):
        ans=[]
        if self.net_random:
            r=request.get(main_url, params={'num':amount, 'min':min, 'max':max, 'col':1, 'base':10, 'format': 'html', 'rnd': 'new'})
            ans=self.parse(r.content)
        else:
            while amount>=0:
                ans.append(random.randint(min, max))

    def Dice ():
        ans=get_random(1, 6, 2)
        return ans[0], ans[1]
    
    def Flip():
        if random.randint(0, 1000) <= 453:
            ans = 'Орёл'
        else:
            ans = 'Решка'
        return ans
    
    def Roll(start, end, amount)
        return self.get_random(start, end, amount)
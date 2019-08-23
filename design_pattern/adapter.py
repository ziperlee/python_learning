"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

class Dog:
    def __init__(self):
        self.name = 'dog'

    def wang(self):
        return('wang')

class Cat:
    def __init__(self):
        self.name = 'cat'

    def miao(self):
        return('miao')

class Adapter:
    def __init__(self, obj, **adaptermethods):
        self.obj = obj
        self.__dict__.update(adaptermethods)

    def __getattr__(self, item):
        return getattr(self.obj, item)

objs = []
dog = Dog()
objs.append(Adapter(dog, make_noise=dog.wang))

cat = Cat()
objs.append(Adapter(cat, make_noise=cat.miao))

for obj in objs:
    print(f'a {obj.name} goes {obj.make_noise()}')

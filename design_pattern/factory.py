"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

class DogToy:
    def speak(self):
        print('wang wang')

class CatToy:
    def speak(self):
        print('miao miao')

def toy_factory(toy_type):
    if toy_type == 'dog':
        return DogToy()
    if toy_type == 'cat':
        return CatToy()

toy = toy_factory('dog')
toy.speak()

toy_cat = toy_factory('cat')
toy_cat.speak()
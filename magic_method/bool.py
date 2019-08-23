"""
 Create by zipee on 2019/4/5.
"""
__author__ = 'zipee'

class C:
    def __init__(self, x):
        self.x = x

    def __bool__(self):
        if self.x:
            return True
        return False

if __name__ == '__main__':
    c = C(None)
    if c:
        print('if')
    else:
        print('else')
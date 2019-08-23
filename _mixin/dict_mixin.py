"""
 Create by zipee on 2019/3/25.
"""
__author__ = 'zipee'

class DictMixin:
    def setdefault(self, key, default=None):
        print('this is DictMixin setdefault')
    def msetdefault(self, key, default=None):
        print('this is DictMixin msetdefault')

    pass
class DictMixin2:
    def setdefault(self, key, default=None):
        print('this is DictMixin setdefault2')
    def msetdefault(self, key, default=None):
        print('this is DictMixin msetdefault2')
    def msetdefault2(self, key, default=None):
        print('this is DictMixin msetdefault2')

    pass


class C(dict, DictMixin):
    pass

class CC(C, DictMixin2):
    pass

c = C()
print(dir(c))
c.msetdefault('a', 'haha')
c.setdefault('a', 'haha')
print(c)

cc = CC()
cc.msetdefault('a', 'haha')
cc.msetdefault2('a', 'haha')
cc.setdefault('a', 'haha')
print(c)

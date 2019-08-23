"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

from functools import wraps

# __new__
class C:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_singleton'):
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

# decorator
def singleton(cls):
    _singleton = {}

    @wraps(cls)
    def warpper(*args, **kwargs):
        if cls not in _singleton:
            _singleton[cls] = cls(*args, **kwargs)
        return _singleton[cls]
    return warpper

    # _singleton = None
    # @wraps(cls)
    # def warpper(*args, **kwargs):
    #     nonlocal _singleton
    #     if _singleton is not None:
    #         _singleton = cls(*args, **kwargs)
    #     return _singleton
    # return warpper

@singleton
class C2:
    pass

# class decorator
class class_singleton:
    _singleton = {}
    def __call__(self, cls, *args, **kwargs):
        def wapper():
            if cls not in self._singleton:
                self._singleton[cls] = cls(*args, **kwargs)
            return self._singleton[cls]
        return  wapper

@class_singleton()
class C3:
    pass

# metaclass
class C_meta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_singleton'):
            # 元类的__call__创建类实例， __new__创建类
            cls._singleton = super(C_meta, cls).__call__(*args, **kwargs)
            # cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton
class C4(metaclass=C_meta):
    pass


if __name__ == '__main__':

    # __new__
    c1 = C()
    c2 = C()
    print(c1 is c2)

    # module
    from design_pattern.singleton.module1 import c as c3
    from design_pattern.singleton.module2 import c as c4
    print(c3 is c4)

    # decorator
    c1 = C2()
    c2 = C2()
    print(c1 is c2)
    print(C2.__name__)

    # class decorator
    c1 = C3()
    c2 = C3()
    print(c1 is c2)
    print(C2.__name__)


    # __closure__
    class C3:
        pass
    c3 = singleton(C3)
    print(c3.__closure__)

    # metaclass
    c1 = C4()
    c2 = C4()
    print(c1 is c2)
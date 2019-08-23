"""
 Create by zipee on 2019/2/17.
"""
import typing

__author__ = 'zipee'

import attr

@attr.s
class Product:
    product_id = attr.ib()
    product_name = attr.ib()

    @product_id.validator
    def _product_id(self, attribute, value):
        if value < 0:
            raise ValueError("x must be positive")
    @product_name.default
    def name_does_not_matter(self):
        return self.product_id + 1

User = attr.make_class('User', ['uid', 'uname'])
User2 = attr.make_class('User', {
    'uid': attr.ib(default=22),
    'name': attr.ib(default=attr.Factory(list))
})

@attr.s
class C(object):
    x = attr.ib(default=attr.Factory(list))
    y = attr.ib(default=attr.Factory(
        lambda self: set(self.x),
        takes_self=True)
    )
@attr.s
class C2(object):
    x: int
    y: typing.List[int] = attr.Factory(list)

@attr.s(auto_attribs=True)
class C3:
    x: int = attr.ib(init=False)
    y: int = attr.ib(init=False)
    z: int = attr.ib(init=False)
    def __attrs_post_init__(self):
        self.x = 2
        self.y = 3
        self.z = 4



if __name__ == '__main__':
    p = Product(1)
    print(p)
    print(attr.fields(Product))
    print(attr.fields(Product).product_id)
    d = attr.asdict(p, filter=lambda p, v: p.name in ('product_id'))
    print(d)

    user = User(1, 2)
    print(user)

    user2 = User2(name=[])
    print(user2)

    print(C())
    print(C2())
    print(C3())

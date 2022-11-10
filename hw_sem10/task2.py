

class Singleton(type):

    res = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.res:
            cls.res[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.res[cls]


class TestObject(metaclass=Singleton):
    pass


a = TestObject()
print(a)
b = TestObject()
print(a is b)
c = TestObject()
print(c)
print(a is c)

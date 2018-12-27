# coding: utf-8

#http://blog.csdn.net/ghostfromheaven/article/details/7671853

# 方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
# 同一个类的所有实例天然拥有相同的行为(方法),
# 只需要保证同一个类的所有实例具有相同的状态(属性)即可
# 所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
# 可参看:http://code.activestate.com/recipes/66531/
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


one = MyClass2()
two = MyClass2()

# one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print one.a
# 3
print "two.a:",two.a                    #这两个实例共享了数据成员
#3
print id(one)
# 28873680
print id(two)
# 28873712
print one == two
# False
print one is two
# False
# 但是one和two具有相同的（同一个__dict__属性）,见:
print id(one.__dict__)
# 30104000
print id(two.__dict__)
# 30104000
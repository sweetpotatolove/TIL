O = object

class D(O):
    pass
class E(O): pass
class F(O): pass
class B(D, E): pass
class C(F, D): pass
class A(B, C): pass

# A클래스 상속 담색 순서 출력
print(A.__mro__)

# <class '__main__.A'>
# <class '__main__.B'>
# <class '__main__.C'>
# <class '__main__.D'>
# <class '__main__.E'>
# <class '__main__.F'>
# <class 'object'>

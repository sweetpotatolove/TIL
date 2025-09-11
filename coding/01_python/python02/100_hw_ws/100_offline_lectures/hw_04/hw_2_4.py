'''
문제
Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
    Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
    Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.

코드를 실행하고, 출력 결과를 확인한다.
'''
# Animal 클래스를 정의한다.
class Animal:
    # Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    # name: 각 동물 인스턴스의 이름을 기록할 변수
    def __init__(self, name):
        self.name = name
    
    # Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
    def speak(self):
        '''
            Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.

            아무 기능도 하지 않을 speak 메서드를 왜 Animal 클래스에 정의 한걸까?
            나중에 만들 Dog, Cat 클래스가 Animal 클래스를 상속 받아서
            각각 speak 메서드를 따로 가지게 될 건데, 왜 굳이 Animal 클래스에 정의할까?

            Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.
            즉, 하위 클래스들이 모두 공통적으로 speak 메서드를 가지고 있을 것이다라는 사실을 명시
        '''
        # 특별한 동작이 정의되어 있지 않네?
        pass    # 문법적으로 문제가 되지 않도록 pass 입력한다.

class Dog(Animal):
    # 본인이 사용할 모양으로 오버라이딩 해서 사용하고 있다.
    def speak(self):
        return 'Woof!'
    
class Cat(Animal):
    def speak(self):
        return 'Mewo!'
    
# Flyer와 Swimmer 클래스를 정의한다.
class Flyer:
    # Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
    def fly(self):
        return "Flying"

class Swimmer:
    # Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
    def swim(self):
        return "Swimming"
    
# Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
# Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
class Duck(Flyer, Swimmer, Animal):
    # Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
    def speak(self):
        return "Quack!"
    
# make_animal_speak 함수를 정의한다.
#     이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
def make_animal_speak(instance):
    print(instance.speak())

dog1 = Dog('치와와')
cat1 = Cat('페르시안 블루')
duck1 = Duck('거위')

make_animal_speak(dog1)
make_animal_speak(cat1)
make_animal_speak(duck1)



from abc import ABC, abstractmethod


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    @abstractmethod
    def say_hi(self):
        raise NotImplementedError

class Mother(AbstractParent):
    def __init__(self,age = 0):
        print('mother constructor')
        self.age = age

    def hello_friend(self):
        print("hi friend from mom")

    def do_work(self):
        print("i'm working")

    def say_hi(self):
        print(' hi from mom')

    def do_house_work(self):
        print('screaming on father')

class Father(AbstractParent):
    def __init__(self):
        print('father constructor')

    def play_guitar(self):
        print('playin guitar')

    def hello_friend(self):
        print("hi friend from dad")

    def do_house_work(self):
        print('sitting on the sofa and scrolling facebook ')

class Daughter(Mother, Father):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    def do_work(self):
        print("i'm working like a horse")

    def hello_friend(self):
        print('hello to friend from daughter')

class Friend:
    pass

def greet_mother(mother : Mother):
    print('hello mother')
    mother.do_work()

def greet_father(father : Father):
    print('hello father')
    father.play_guitar()

if __name__ == '__main__':
    daughter = Daughter()
    daughter.do_work()
    greet_mother(daughter)
    greet_father(daughter)
    daughter.play_guitar()

    #change object class
    daughter.__class__ = Friend

for i in [daughter]:
    i.do_house_work()

my_tuple = ('string', 10, daughter )
my_set ={ 1 ,2 ,5, 'a'}
frozen_set = frozenset(['w','a','o'])
my_dict = {1 : 'me',
           2 : 'him',
           3 : 'us'}
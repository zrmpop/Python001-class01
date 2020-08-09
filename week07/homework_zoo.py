from abc import ABCMeta, abstractmethod


class Zoo(object):
    def __init__(self, name):
        self.animals = []
        self.zoo_name = name

    def add_animal(self, animal):
        if animal in self.animals:
            return self.animals[animal]
        else:
            self.animals.append(animal)
            self.__dict__[type(animal).__name__] = animal


class Animal(metaclass=ABCMeta):
    size = {
        '小型': 1,
        '中型': 2,
        '大型': 3
    }
    is_meat = {
        '食肉': True,
        '食草': False,
        '杂食': False
    }
    is_fierce = {
        '凶猛': True,
        '温顺': False
    }

    @abstractmethod
    def __init__(self, is_meat, size, is_fierce):
        self.size = size
        self.is_meat = is_meat
        self.is_fierce = is_fierce

        if self.size != '1' and self.is_meat == True and self.is_fierce == True:
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False


class Cat(Animal):
    sound = '喵喵喵'

    def __init__(self, name, is_meat, size, is_fierce):
        super().__init__(is_meat, size, is_fierce)
        self.name = name
        self.suitbale_for_pet = True


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(f'zoo has cat: {bool(have_cat)}')

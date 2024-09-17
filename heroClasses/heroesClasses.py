class Hero:
    """Добавлен базовый класс Hero"""
    __mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name, character_class):
        """Написан конструктор для класса"""
        self.__name = name
        self.__charter_class = character_class
        self.__my_hero_skills = []
        self.__level = 0
        self.__exp = 0

    def name(self):
        return self.__name

    def character_class(self):
        return self.__charter_class

    def my_hero_skills(self):
        return self.__my_hero_skills

    def level(self):
        return self.__level

    def exp(self):
        return self.__exp

    def get_skills(self, character_class):
        """Добавлен геттер для навыков, результат зависит от выбранного класса"""
        if character_class == 'воин':
            return self.__warrior_skills
        elif character_class == 'маг':
            return self.__mage_skills
        elif character_class == 'рейнджер':
            return self.__ranger_skills
        else:
            exit("Ошибка перезапустите программу!")

    def get_new_level(self):
        if self.__exp >= 1000:
            self.__level = 3
            self.add_skill()
        elif self.__exp >= 500:
            self.__level = 2
            self.add_skill()
        elif self.__exp >= 200:
            self.__level = 1
            self.add_skill()
        else:
            self.__level = 0
        return f"Герой {self.name}, теперь {self.level} уровня, навыки: {', '.join(self.my_hero_skills)}"

    def add_exp(self, exp):
        self.exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        pass


class MyHero(Hero):
    pass

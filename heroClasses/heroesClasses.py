class Hero:
    """Добавлен базовый класс Hero"""
    __mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name, character_class):
        """Написан конструктор для класса"""
        self.__name = name
        self.__character_class = character_class
        self.__my_hero_skills = []
        self.__level = 0
        self.__exp = 0

    def name(self):
        """"геттер для имени"""
        return self.__name

    def character_class(self):
        """"геттер для класса"""
        return self.__character_class

    def my_hero_skills(self):
        """"геттер для навыков"""
        return self.__my_hero_skills

    def level(self):
        """"геттер для уровня"""
        return self.__level

    def exp(self):
        """"геттер для опыта"""
        return self.__exp

    def get_skills(self):
        """Добавлен геттер для навыков, результат зависит от выбранного класса"""
        if self.__character_class == 'воин':
            return self.__warrior_skills
        elif self.__character_class == 'маг':
            return self.__mage_skills
        elif self.__character_class == 'рейнджер':
            return self.__ranger_skills
        else:
            exit("Ошибка перезапустите программу!")

    def get_new_level(self):
        """"метод для проверки получения нового уровня"""
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
        return f"Герой {self.name}, теперь {self.level} уровня, навыки: {', '.join(self.__my_hero_skills)}"

    def add_exp(self, exp):
        """метод для добавления опыта"""
        self.__exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        pass


class MyHero(Hero):

 """"класс наследник"""

def __init__(self, name, character_class):
    """"метод инициализации"""
    super().__init__(name, character_class)
    self.skill_list = self.skill_list()


def add_skill(self):
    """"метод для добавления навыка"""
    for _ in range(self.get_new_level()):
        while True:
            print(f"доступные навыки: {", ".join(self.skill_list)}")
            new_skill = input("выберите навык: ")
            if new_skill in self.skill_list:
                self.__my_hero_skills.append(new_skill)
                self.skill_list.remove(new_skill)
                break
            else:
                print("такого нет навыка в списке данных попробуйте снова")
        if self.get_level() == len(self.__my_hero_skills):
            break
    return f"добавлены навыки: {", ".join(self.get_my_hero_skills())}"


























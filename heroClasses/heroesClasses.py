class Hero:
    """Добавлен базовый класс Hero"""
    mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name, character_class):
        """Написан конструктор для класса"""
        self.__name = name
        self.__character_class = character_class
        self.__my_hero_skills = []
        self.__level = 0
        self.__exp = 0

    def get_name(self):
        return self.__name

    def get_character_class(self):
        return self.__character_class

    def get_my_hero_skills(self):
        return self.__my_hero_skills

    def get_level(self):
        return self.__level

    def get_exp(self):
        return self.__exp

    def get_skills(self):
        """Добавлен геттер для навыков, результат зависит от выбранного класса"""
        if self.__character_class == 'воин':
            return self.__warrior_skills
        elif self.__character_class == 'маг':
            return self.mage_skills
        elif self.__character_class == 'рейнджер':
            return self.__ranger_skills
        else:
            exit("Ошибка, перезапустите программу!")

    def get_new_level(self):
        """Метод для проверки получения нового уровня"""
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
        return f"Герой {self.get_name()}, теперь {self.get_level()} уровня, навыки: {', '.join(self.get_my_hero_skills())}"

    def add_exp(self, exp):
        """Метод для добавления опыта"""
        self.__exp += exp
        return self.get_new_level()

    def add_skill(self):
        """Метод для добавления навыка"""
        skills = self.get_skills()
        for _ in range(self.get_level()):
            while True:
                print(f"{self.get_name()}, выберите навык: {', '.join(skills)}")
                new_skill = input("Введите навык: ")
                if new_skill in skills:
                    self.__my_hero_skills.append(new_skill)
                    skills.remove(new_skill)
                    break
                else:
                    print("НЕВЕРНЫЙ ВЫБОР!! попробуйте снова.")
            if self.get_level() == len(self.__my_hero_skills):
                break
        return f"Добавлены навыки: {', '.join(self.get_my_hero_skills())}"


class MyHero(Hero):
    """Класс наследник"""

    def __init__(self, name, character_class):
        """Метод инициализации"""
        super().__init__(name, character_class)

    def add_skill(self):
        super().add_skill()
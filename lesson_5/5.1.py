class AnimeCharacter:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.__is_main_character = False

    def get_is_main_character(self):
        return self.__is_main_character

    def set_is_main_character(self, is_main_character):
        self.__is_main_character = is_main_character

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I am a {self.gender} character."


class AnimeSeries:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def get_main_characters(self):
        return [character for character in self.characters if character.get_is_main_character()]


naruto = AnimeCharacter("Naruto Uzumaki", 17, "male")
sakura = AnimeCharacter("Sakura Haruno", 17, "female")
sasuke = AnimeCharacter("Sasuke Uchiha", 17, "male")

naruto.set_is_main_character(True)
sasuke.set_is_main_character(True)
sakura.set_is_main_character(True)

shippuden = AnimeSeries("Naruto: Shippuden", "Action, Adventure", 2007)
shippuden.add_character(naruto)
shippuden.add_character(sakura)
shippuden.add_character(sasuke)


# Вывод информации о серии и её основных персонажах
print(f"Anime Series: {shippuden.title} ({shippuden.release_year})")
print(f"Genre: {shippuden.genre}")
print("Main Characters:")
for character in shippuden.get_main_characters():
    print(character.introduce())
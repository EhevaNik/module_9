# Домашнее задание по теме "Создание функций на лету"
# Задача "Функциональное разнообразие":
from  random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)), где
# ? - место написания lambda-функции
print(list(map(lambda x, y: x == y, first, second)))

# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи:
def get_advanced_writer(file_name):
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
# неограниченное количество данных любого типа.
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf8') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
class MysticBall:
    def __init__(self, *words):
        self.words = words

# В этом классе также определите метод __call__, который будет случайным образом выбирать слово из words
# и возвращать его
    def __call__(self):
        word = choice(self.words)
        return word

# Вывод результата
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
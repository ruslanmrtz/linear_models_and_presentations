import requests
import time
import re

from random import randint


BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        result = func(*args, **kwargs)

        print(f'Функция была вызвана: {count} раз\n')
        return result
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        print(f'Функция вызвана с параметрами: {args}, {kwargs}\n')

        return result
    return wrapper


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        st_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f'Время выполнения функции word_count: {end_time - st_time}\n')

        return result
    return wrapper


@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    """
    Функция для посчета указанного слова на html-странице
    """

    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+' , ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


print(word_count('whole'))

import requests
import json

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def get_catigories(self):
        """Получаем список категорий"""

        response_categories = requests.get('https://api.chucknorris.io/jokes/categories')

        if response_categories.ok:
            categories_list = response_categories.json()
            for one_categories in categories_list:
                yield one_categories
        else:
            print('Ошибка!')

    def get_joke(self):
        """Получаем шутки по категориям"""

        counter_max = 16
        counter_min = 0

        categories_generator = self.get_catigories()

        while counter_min <= counter_max:
            category = next(categories_generator, None)
            if category is None:
                break
            print('Данная категоря - ' + str(category))

            get_joke_cotegories = requests.get('https://api.chucknorris.io/jokes/random?category=' + str(category))
            if get_joke_cotegories.ok:
                result_text_joke = get_joke_cotegories.json()
                result_text_joke_info = result_text_joke.get("value")
                print(result_text_joke_info)
            else:
                print('Ошибка!')
                break

            counter_min += 1




base_calss = Test_new_joke()
base_calss.get_catigories()
base_calss.get_joke()




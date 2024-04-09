import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        self.categories = self.get_catigories()

    def get_catigories(self):
        """Получаем список категорий по одной"""

        response_categories = requests.get('https://api.chucknorris.io/jokes/categories')
        categories_list = []

        if response_categories.ok:
            categories_list = response_categories.json()
        else:
            print('Ошибка!')

        return categories_list

    def get_joke_catigories(self):
        for category in self.categories:
            get_joke_cotegories = requests.get('https://api.chucknorris.io/jokes/random?category=' + str(category))
            print('Данная категоря - ' + str(category))
            if get_joke_cotegories.ok:
                result_text_joke = get_joke_cotegories.json()
                result_text_joke_info = result_text_joke.get("value")
                print(result_text_joke_info)
            else:
                print('Ошибка!')
                break

base_class = Test_new_joke()
base_class.get_catigories()
base_class.get_joke_catigories()

import requests
import json

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.resource_post = '/maps/api/place/add/json'
        self.resource_get = '/maps/api/place/get/json'
        self.param = '?key=qaclick123'
        self.path_file_plase_id = 'C:\\Users\\avas\\Desktop\\auto_test\\exStepikApi\\place_id'

    def new_location(self):
        post_url = self.base_url + self.resource_post + self.param
        print(post_url)

        body_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }


        attempt_min = 1
        attempt_max = 5

        while attempt_min <= attempt_max:
            creating_new_location = requests.post(post_url, json = body_post)
            if creating_new_location.ok:
                result_text_new_location = creating_new_location.json()
                result_text_new_location_info = result_text_new_location.get("place_id")
                print(result_text_new_location_info)
            else:
                print('Ошибка!')
                break

            with open(self.path_file_plase_id, 'a') as file:  # 'a' для добавления в файл (если файл уже существует)
                file.write(result_text_new_location_info + '\n')

            attempt_min += 1

    def get_check_new_place(self):
        string_on_file = 1

        attempt_min = 1
        attempt_max = 5

        while attempt_min <= attempt_max:
            with open(self.path_file_plase_id, 'r') as file:  # Открываем файл для чтения
                lines = file.readlines()  # Читаем все строки файла в список
                specific_line = lines[attempt_min - 1]  # Получаем нужную строку из списка

            get_url = self.base_url + self.resource_get + self.param + '&' + specific_line
            print(get_url)

            attempt_min += 1

test = Test_new_joke()
test.new_location()
test.get_check_new_place()
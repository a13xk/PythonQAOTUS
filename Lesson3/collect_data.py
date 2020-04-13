import csv
import json


# Читаем данные по книгам
books = list()
with open('books.csv', newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)
    for i, h in enumerate(header):
        header[i] = h.lower()

    # Итерируемся по данным делая из них словари
    for row in reader:
        books.append(dict(zip(header, row)))

# Читаем данные по юзерам
with open("users.json", "r") as f:
    users = json.loads(f.read())

# Список с словарями по шаблону из файла example.json
users_data = list()

# Если книг больше чем пользователей, то все раздавать не обязательно,
# если меньше, то тем кому нехватило - присвоить пустой массив.
for i, user in enumerate(users):
    user_data = dict()
    user_data["name"] = user.get("name")
    user_data["gender"] = user.get("gender")
    user_data["address"] = user.get("address")

    user_data["books"] = list()
    try:
        book = dict()
        book["title"] = books[i].get("title")
        book["author"] = books[i].get("author")
        book["height"] = books[i].get("height")
        user_data["books"].append(book)
    except IndexError:
        pass
    users_data.append(user_data)

# Записываем список объектов в файл
with open("users_data.json", "w") as f:
    s = json.dumps(users_data, indent=4)
    f.write(s)
#

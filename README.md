# api_final_yatube
_Учебный проект_

### Описание
>API сервис для социальной сети [Yatube](http://127.0.0.1:8000/)

### Технологии
- Python 3.9
- Django 3.2.16
- Django REST Framework 3.12
- JWT + Djoser
- Postman

### Запуск проекта в dev-режиме

✔Клонируйте репозиторий с сайта Github:

```sh
>git clone https://github.com/Irin-Baro/api_final_yatube.git
```

✔ Установите и активируйте виртуальное окружение

```sh
Для пользователей Windows:
python -m venv venv
source venv/Scripts/activate
```

✔ Установите зависимости из файла requirements.txt

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

✔ Выполните миграции:

```sh
python manage.py migrate
```

✔ Запуск проекта - в папке с файлом manage.py выполните команду:

```sh
python manage.py runserver
```

### Пример запроса
#####GET /api/v1/posts/

>http://127.0.0.1:8000/api/v1/posts/

Response samples:
>200

Content type:
>_application/json_

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Автор

| Автор | Учебная платформа |
| ------ | ------ |
| Irin-Baro | Yandex-Practicum |
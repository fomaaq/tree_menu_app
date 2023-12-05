# Tree menu app
Тестовое задание на Django - древовидное меню с использованием custom template tag.

## Содержание

- [Используемые технологии](#Используемые-технологии)
- [Установка и запуск](#Установка-и-запуск)


## Используемые технологии

- [Django ver. 4.2.7](https://docs.djangoproject.com/en/4.2/) - фреймворк для создания веб-приложения
- [SQLite ver. 3.4.4](https://www.sqlite.org/index.html) - БД, используемая в приложении
- [Docker ver. 24.0.6](https://www.docker.com/) - ПО для разворачивания и запуска приложения


## Установка и запуск

Приложение упаковано в docker-контейнер.

Для установки и запуска приложения необходимо выполнить команду:

```
docker-compose up
```
Приложение запускается по следующему адресу: http://localhost:8000/menu/

При необходимости можно заменить SECURITY_KEY, используемый в приложении: необходимо в файле [env_settings.env](https://github.com/fomaaq/tree_menu_app/blob/main/env_settings.env) указать свой ключ в переменной "my_security_key":

- Вы можете сгенерировать новый ключ, например, на сайте [Djecrety.ir](https://djecrety.ir/)

- либо использовать следующую команду для генерации:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Также в файле [env_settings.env](https://github.com/fomaaq/tree_menu_app/blob/main/env_settings.env) можно изменить параметр "DEBUG", который изначально установлен как "False". Для этого необходимо присвоить переменной "my_debug" значение "True".

# Lab 2

## Хід роботи
1. За допомогою пакетного менеджера *PIP* встановив *pipenv* та створив ізольоване середовище для Python:
```
pip install pipenv
pipenv --python 3.7
pipenv shell
```
2. Встановив бібліотеки (*requests, ntplib*):
```
pipenv install requests
pipenv install ntplib
```
3. Створив файл *app.py*, протестував та запустив, програма працює правильно.
4. Для тестування встановив бібліотеку *pytest*, запустив тести, всі тести виконались успішно:
```
pipenv install pytest
pytest tests/tests.py
```
5. Дописав у програмі (*app.py*) функцію, яка буде перевіряти час доби AM/PM та відповідно друкувати "Доброго дня/ночі". Також у файлі (*tests.py*) написав тест який перевіряє правильність роботи функції.
6. Виконання функції та тестів перенаправив у файл *results.txt*:
```
pipenv run python app.py append >> results.txt
pipenv run pytest tests/tests.py >> results.txt
```
7. Написав make-файл для сховища. Додав правила налаштування середовища та встановив залежності ( make install), запустив модульні тести ( make test), запустив додаток ( make run) та розгорнув ( make deploy).


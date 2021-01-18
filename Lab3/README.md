# Lab 3
## Хід роботи
1. Створив віртуальне середовище у папці Lab3 та встановив на неї усі необхідні пакети
            
       (Lab3) user@Pc:~/GitRepos/DevopsLabs/Lab3$ pipenv install django
       Installing django...
       Adding django to Pipfile's [packages]...
       ✔ Installation Succeeded 
       Pipfile.lock not found, creating...
       Locking [dev-packages] dependencies...
       Locking [packages] dependencies...
       Building requirements...
       Resolving dependencies...
       ✔ Success! 
       Updated Pipfile.lock (85c883)!
       Installing dependencies from Pipfile.lock (85c883)...
         🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
       (Lab3) user@Pc:~/GitRepos/DevopsLabs/Lab3$ 
2. Створив заготовку сайту за допомогою Django Framework та виніс файли на рівень вище
        
       (Lab3) user@Pc:~/GitRepos/DevopsLabs/Lab3$ pipenv run django-admin startproject my_site
3. Запустив Django сервер за допомогою команди ```pipenv run python manage.py runserver```<br/>
![](photos/1.jpg)
4. Все запустилось успішно і стартова сторінка Django відображається коректно. Зупинив сервер через Ctrl-C та зробив коміт.
5. Створив темплейт свого додатку (app) у якому та закомітив ці файли до свого репозиторію.
6. Створив директорію ```templates``` де створив файл ```main.html``` а також в папці ```main``` створив файл ```urls.py```. Закомітив усе до репозиторію
7. Відредагував файли ```my_site/urls.py``` та ```main/urls.py```.
8. Перейшов до свого додатку та зайнявся WEB сторінками. Для цього:
       
       - створив сторінки двох типів - перша буде зчитуватись з .html темплейта. друга сторінка буде просто повертати відповідь у форматі JSON;
       - відкрив та ознайомився із вмістом файла main/views.py.       
9. Щоб поєднати функції із реальними URL шляхами за якими будуть доступні наші веб сторінки, заповнив файл main/urls.py згідно зразка.Буде два URL посилання:
       
       - головна сторінка яка буде опрацьовуватись функцією main;
       - сторінка health/ яка буде опрацьована функцією health;
   Результати виконання попередніх кроків:
![](photos/2.jpg)
![](photos/3.jpg)
10. Зробив коміт з цими змінами до  свого репозиторію.
11. Встановив бібліотеку ```requests``` та запустив файл ```monitoring.py```
      #####Результат - створений файл ```server.log``` з наступним вмістом:
           
        INFO 2020-11-22 17:09:33,877 root : Сервер доступний. Час на сервері: test1
        INFO 2020-11-22 17:09:33,878 root : Запитувана сторінка: : test2
        INFO 2020-11-22 17:09:33,878 root : Відповідь сервера місти наступні поля:
        INFO 2020-11-22 17:09:33,878 root : Ключ: date, Значення: test1
        INFO 2020-11-22 17:09:33,878 root : Ключ: current_page, Значення: test2
        INFO 2020-11-22 17:09:33,878 root : Ключ: server_info, Значення: test3
        INFO 2020-11-22 17:09:33,878 root : Ключ: client_info, Значення: test4
12. Відкрив сторінку ```health``` в браузері:<br/>
![](photos/4.jpg)
13. * модифікував функцію ```health``` щоб генерувався перерік заданих даних:
        
          def health(request):
              response = {'date': get_current_time(), 'current_page': request.build_absolute_uri(), 'server_info': request.META['SERVER_NAME'] + " " + sys.platform, 'client_info': request.META['HTTP_USER_AGENT'] + "    IP:" + request.META['REMOTE_ADDR']}
              return JsonResponse(response)
    * дописав функціонал програми моніторингу сайту:
          
          def main(url):
              try:
                  r = requests.get(url)
              except requests.exceptions.RequestException as e:
                  logging.error(e)
                  logging.error("Немає зв'язку з сервером")
                  raise ConnectionError
          
              if r:
                  data = json.loads(r.content)
                  logging.info("Сервер доступний. Час на сервері: %s", data['date'])
                  logging.info("Запитувана сторінка: : %s", data['current_page'])
                  logging.info("Відповідь сервера містить наступні поля:")
                  for key in data.keys():
                      logging.info("Ключ: %s, Значення: %s", key, data[key])
    * добавив цикл з затримкою оновлення 60 секунд та запустив програму у бекграунді:
            
            python3 monitoring.py &
    * додав скрипт для запуску моніторингу:
            
            [scripts]
            server = "python manage.py runserver 0.0.0.0:8000"
            monitoring = "python monitoring.py"
14. Запустив сервер та переконався що головна сторінка відображається. Запустив моніторинг. Зробив коміт з усіма змінами.
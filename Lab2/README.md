# Lab 2
## Хід роботи
1. Створив папку Lab2 з README.md файлом.
2. Інсталював ```pipenv``` та створив ізольоване середовще

        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ pipenv --python 3
        Creating a virtualenv for this project...
        Pipfile: /home/user/Pipfile
        Using /usr/bin/python3.6m (3.6.9) to create virtualenv...
        ⠸ Creating virtual environment...created virtual environment CPython3.6.9.final.0-64 in 867ms
          creator CPython3Posix(dest=/home/user/.local/share/virtualenvs/user-5PivF_Od, clear=False, global=False)
          seeder FromAppData(download=False, pip=bundle, wheel=bundle, setuptools=bundle, via=copy, app_data_dir=/home/user/.local/share/virtualenv)
            added seed packages: pip==20.2.4, setuptools==50.3.2, wheel==0.35.1
          activators PythonActivator,FishActivator,XonshActivator,CShellActivator,PowerShellActivator,BashActivator
        
        ✔ Successfully created virtual environment! 
        Virtualenv location: /home/user/.local/share/virtualenvs/user-5PivF_Od
        Creating a Pipfile for this project...
        user@Pc:~$ pipenv shell
        Launching subshell in virtual environment...
        user@Pc:~$  . /home/user/.local/share/virtualenvs/user-5PivF_Od/bin/activate
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ 
3. Встановив бібліотеку requests у віртуальному середовищі.

        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ pipenv install requests
        Installing requests...
        Adding requests to Pipfile's [packages]...
        ✔ Installation Succeeded 
        Pipfile.lock not found, creating...
        Locking [dev-packages] dependencies...
        Locking [packages] dependencies...
        Building requirements...
        Resolving dependencies...
        ✔ Success! 
        Updated Pipfile.lock (b14837)!
        Installing dependencies from Pipfile.lock (b14837)...
          🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ 
4. Встановив бібліотеку ```ntplib``` 
        
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ pipenv install ntplib
        Installing ntplib...
        Adding ntplib to Pipfile's [packages]...
        ✔ Installation Succeeded 
        Pipfile.lock (b14837) out of date, updating to (a293ad)...
        Locking [dev-packages] dependencies...
        Locking [packages] dependencies...
        Building requirements...
        Resolving dependencies...
        ✔ Success! 
        Updated Pipfile.lock (a293ad)!
        Installing dependencies from Pipfile.lock (a293ad)...
          🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$
5. Створив файл ```app.py```, скопіював до нього код з репозиторію та запустив у віртуальному середовищі
        
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ python3 app.py
        ========================================
        Результат без параметрів: 
        No URL passed to function
        ========================================
        Результат з правильною URL: 
        Time is:  02:37:35 PM
        Date is:  11-02-2020
        success
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ 
6. Встановив бібліотеку ```pytest```
        
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ pipenv install pytest
        Installing pytest...
        Adding pytest to Pipfile's [packages]...
        ✔ Installation Succeeded 
        Pipfile.lock (a293ad) out of date, updating to (35af5c)...
        Locking [dev-packages] dependencies...
        Locking [packages] dependencies...
        Building requirements...
        Resolving dependencies...
        ✔ Success! 
        Updated Pipfile.lock (35af5c)!
        Installing dependencies from Pipfile.lock (35af5c)...
          🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ 
7. Запустив ```pytest tests/tests.py```
        
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ pytest tests/tests.py
        ======================================== test session starts =========================================
        platform linux -- Python 3.6.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
        rootdir: /home/user/GitRepos/DevopsLabs/Lab2
        collected 4 items                                                                                    
        
        tests/tests.py ....                                                                            [100%]
        
        ========================================= 4 passed in 0.60s ==========================================
        (Lab2) user@Pc:~/GitRepos/DevopsLabs/Lab2$ 
8. Дописав функцію що повертає стрінг привітання та функцію, що повертає нинішній час.
        
        def get_current_time(url=''):
            try:
                r = requests.get(url=url)
            except requests.exceptions.RequestException as e:
                raise ConnectionError
            d = r.json()
            str_time = d['time']
            return str_time
        
        def home_work(check_t):
            tm_in = int(check_t[1]) + int(check_t[0])*10
            print(tm_in)
            if check_t[9] == "P" and tm_in < 6 or check_t[9] == "P" and tm_in == 12:
                print("Доброго дня")
                daytime = "day"
            elif check_t[9] == "P" and tm_in > 6 and tm_in < 12:
                print("Доброго вечора")
                daytime = "evening"
            elif (check_t[9] == "A" and tm_in == 12) or (check_t[9] == "A" and tm_in < 6):
                print("Доброї ночі")
                daytime = "night"
            else:
                print("Доброго ранку")
                daytime = "morning"
            return daytime
9. Написав функцію для тестування своєї попередньої функції.
        
        def test_home_work(self):
            # Ваш захист
            self.assertTrue(home_work("03:07:45 AM") == "night")
            self.assertTrue(home_work("09:07:45 AM") == "morning")
            self.assertTrue(home_work("02:07:45 PM") == "day")
            self.assertTrue(home_work("10:07:45 PM") == "evening")
10. Перенаправив вивід виконання тестів у файл ```results.txt``` за допомогою команд ```>``` (перезапис) та ```>>``` (допис в кінці)
    ##### Результат виконання тесту, записаний у файл ```results.txt```
        ============================= test session starts ==============================
        platform linux -- Python 3.6.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
        rootdir: /home/user/GitRepos/DevopsLabs/Lab2
        collected 4 items
        
        tests/tests.py ....                                                      [100%]
        
        ============================== 4 passed in 0.64s ===============================  
11. Зробив коміт до свого репозиторію.
12.




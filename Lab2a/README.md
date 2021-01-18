# Lab 2a
## Хід роботи
1. <strong>Створив файл trial.py. В даному файлі буду виконувати наступні підпункти.</strong> <br/>
    * Вивів на екран константи мови Python
        ##### Код програми:
            print("First constant", False)
            print("Second constant", True)
            print("Third constant", None)
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py
            First constant False
            Second constant True
            Third constant None
    * Вивів на екран результат виконання вбудованих функцій <br/> (Взяв функції, що починаються з букви мого прізвища)
        ##### Код програми:
            print("1", f"in bool function is {bool(1)}")
            print("0", f"in bool function is {bool(0)}")
            print("Number 21", f"in binary is {bin(21)}")
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py 
            1 in bool function is True
            0 in bool function is False
            Number 21 in binary is 0b10101
    * Вивів на екран роботу циклу та розгалужень в ньому
        ##### Код програми:
            Flip_flop = True
            for counter in range(4):
                if(Flip_flop):
                    print("Hello")
                    Flip_flop = False
                else:
                    print("there")
                    Flip_flop = True
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py 
            Hello
            there
            Hello
            there
    * Вивів на екран роботу конструкції try -> except -> finally
        ##### Код програми:
            x = 1
            try:
                num = input("Please enter a number: ")
                x = int(num)
            except ValueError as e:
                print("Oops!", num,"was no valid number.Try again...")
            finally:
                print("Problem finally found!")
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py 
            Please enter a number: f
            Oops! f was no valid number.Try again...
            Problem finally found!
    * Вивів на екран інфо з файлу через контекст-менеджер
        ##### Код програми:
            with open("text.txt", "r") as text:
                for line in text:
                    print(line)
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py 
            This text here is to test the "with" function
    * Ознайомився з Python lambdas
        ##### Код програми:
            test_lambda = lambda item: item+2
            var_number = 8
            print(test_lambda(var_number))
        ##### Результат виконання:
            user@Pc:~/Python$ python3 trial.py 
            10
2. <strong>Скопіював файли з репозиторію devops_course/tree/master/lab2a до власного</strong>
    * Перейшов до папки з цими файлами та запустив командою ```python3 .```
        ##### Результат виконання:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 .
            We are in the __main__
            2020-10-22 17:24:33.328137
            linux
        Перша стрічка виводить назву виконуваного файлу.<br/>
        Друга стрічка виводить дату та час за гринвічем..<br/>
        Третя стрічка виводить назву ОС на якій було запущено програму.
    * Запустив програму через команду ```python . -h```
        ##### Результат виконання:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . -h
            usage: . [-h] [-o OPT] [-l]
            
            Приклад передачі аргументів у Python програму.
            
            optional arguments:
              -h, --help            show this help message and exit
              -o OPT, --optional OPT
                                    Цей параметр є вибірковим.
              -l, --logs            Якщо виконати команду з цим параметром будуть
                                    виводитись логи.
        У даному випадку ```-h``` виконує роль команди ```help```, яка описує які аргументи можна ввести.
    * Запустив програму через команду ```python3 . -o "Цей текст також має вивестись"```
        ##### Результат виконання:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . -o "Цей текст також має вивестись"
            We are in the __main__
            2020-10-23 11:33:36.415245
            linux
            З консолі було передано аргумент
             ========== >> Цей текст також має вивестись << ==========
    * Запустив програму з логуванням
        ##### Результат виконання:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . --logs
            2020-10-23 11:36:00,082 root INFO: Тут буде просто інформативне повідомлення
            2020-10-23 11:36:00,083 root WARNING: Це Warning повідомлення
            2020-10-23 11:36:00,083 root ERROR: Це повідомлення про помилку
    * Сворив власну функцію у файлі ```common.py```:

            def odd_even_parity(flag):
                if(flag == "True"):
                    var_list = list(range(0,101,2))
                elif(flag == "False"):
                    var_list = list(range(1,101,2))
                else:
                    print("Error: bad input arg")
                    var_list = None
                return var_list
    * Додав новий аргумет до файлу ```__main__``` та функцію ```do_parity()```
    
            parser.add_argument('-f', '--func', dest='parity', type=str, help='Цей параметр використовується в пошуку парних/непарних чисел.')
            
            def do_parity(num):
                print(common.odd_even_parity(num))
        ##### Результат виконання:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . -f True
            [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
            
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . -f False
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
            
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 . -f Not
            Error: bad input arg
    * Створив функцію ```erroneous_func()```,яка буде видавати помилку
        ##### Результат виконання:
            Без помилки:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 .
            We are in the __main__
            2020-10-23 13:41:53.188203
            linux
            Please enter a number: 1
            2020-10-23 13:41:56,551 root INFO: String was successfully converted into Int. All is good!
            Here is the result!
            
            З помилкою:
            user@Pc:~/GitRepos/DevopsLabs/Lab2a$ python3 .
            We are in the __main__
            2020-10-23 13:44:26.464174
            linux
            Please enter a number: f
            2020-10-23 13:44:29,475 root ERROR: Oops! f was no valid number.Try again...
            Here is the result!


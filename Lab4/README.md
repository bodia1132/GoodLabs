# Lab 4
## Хід роботи
1. Ознайомився що таке Docker та документацією до нього;
2. Для перевірки, чи ```docker``` встановлено на моїй поточній машині, запустив почергово наступні команди та перенаправив їх у файл ```my_work.log```:
        
       docker -v >> my_work.log
       docker -h >> my_work.log
       docker run docker/whalesay cowsay Docker is fun >> my_work.log
   Зробив коміт з усіма змінами до репозиторію
3. Ознайомився з базовими принципами роботи ```docker``` та перейшов до виконання наступних пунктів.
4. Створив імедж із Django сайтом зробленим у попередній роботі:
    * Використав команду щоб завантажити базовий імедж з репозиторію:
            
          docker pull python:3.6-slim
          docker images
          docker inspect python:3.6-slim
          
          user@Pc:~/GitRepos/DevopsLabs/Lab4$ docker images
          REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
          python              3.6-slim            7fcd5f355774        22 hours ago        111MB
          docker/whalesay     latest              6b362a9f73eb        5 years ago         247MB
    * Створив файл з іменем Dockerfile скопіював туди вміст файлу з основного репозиторію;
    * Ознайомився із коментарями та зрозумів структуру написання Dockerfile;
    * Замінив посилання на власний Git репозиторій із моїм веб-сайтом та закомітив даний Dockerfile
5. Створив власний [репозиторій](https://hub.docker.com/repository/docker/vyacheslavbeltyukov/lab4) на Docker Hub
6. Виконав білд (build) Docker імеджа та завантажив його до репозиторію.
        
       docker build -t vyacheslavbeltyukov/lab4:django .
       docker images
       dokcer push vyacheslavbeltyukov/lab4:django
       
       user@Pc:~/GitRepos/DevopsLabs/Lab4$ docker images
       REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
       vyacheslavbeltyukov/lab4   django              50fc18426637        19 minutes ago      319MB
       python                     3.6-slim            7fcd5f355774        23 hours ago        111MB
       docker/whalesay            latest              6b362a9f73eb        5 years ago         247MB
    [Посилання на скачування імеджа](https://hub.docker.com/layers/vyacheslavbeltyukov/lab4/django/images/sha256-f5524543325ecac35cc595889a0e04892f5d4cac1d28bd2666d6364365c3bc5e?context=repo)  
    Команда для скачування: ```docker pull vyacheslavbeltyukov/lab4:django```
7. Запустив щойностворений імедж:
        
       user@Pc:~/GitRepos/DevopsLabs/Lab4$ docker run -it --name=django --rm -p 8000:8000 vyacheslavbeltyukov/lab4:django
       Watching for file changes with StatReloader
       Performing system checks...
       
       System check identified no issues (0 silenced).
       
       You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
       Run 'python manage.py migrate' to apply them.
       December 12, 2020 - 14:37:16
       Django version 3.1.3, using settings 'my_site.settings'
       Starting development server at http://0.0.0.0:8000/
       Quit the server with CONTROL-C.
       
      Усе запустилось та веб-сайт за адресою 127.0.0.1:8000 успішно відобразився.
8. Створив файл ```Dockerfile.site``` та збілдив новий імедж для моніторингу серверу:
        
       docker build -t vyacheslavbeltyukov/lab4:monitoring --file Dockerfile.site .
       docker images
       docker push vyacheslavbeltyukov/lab4:monitoring
       
       user@Pc:~/GitRepos/DevopsLabs/Lab4$ docker images
       REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
       vyacheslavbeltyukov/lab4   monitoring          b2f95073b265        6 minutes ago       319MB
       vyacheslavbeltyukov/lab4   django              50fc18426637        53 minutes ago      319MB
       python                     3.6-slim            7fcd5f355774        24 hours ago        111MB
       docker/whalesay            latest              6b362a9f73eb        5 years ago         247MB
    Запустив обидва імеджі одночасно:
       
       docker run -it --name=django --rm -p 8000:8000 vyacheslavbeltyukov/lab4:django
       docker run --net=host --rm -it --volume /home/user/GitRepos/DevopsLabs/Lab4:/app vyacheslavbeltyukov/lab4:monitoring
9. Закомітив усі зміни до репозиторію та створив пулл реквест.

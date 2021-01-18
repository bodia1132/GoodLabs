# Lab4

+ Ознайомився з документацією Docker.
+ Виконав команди для перевірки встановленного Docker:
```
        "sudo docker -v"
        "sudo docker -h"
        "sudo docker run docker/whalesay cowsay Docker is fun"
```
+ Перенаправив вивід в my_work.log:
+ Виконав команди:
```
        "sudo docker pull python:3.8-slim"
        "sudo docker images"
        "sudo docker inspect python:3.8-slim"
```
+ Створив файл з іменем Dockerfile;
+ Замінив посилання на власний Git репозиторій із веб-сайтом та закомітив даний Dockerfile*
+ Створив власний репозиторій на Docker Hub
+ Виконав команди:
```
        "sudo docker build -t flox6375/lab_4:django ."
        "sudo docker images"
        "sudo docker push flox6375/lab_4:django"
```
+ [DockerRepo](https://hub.docker.com/repository/docker/flox6375/lab_4/);
+ Виконав команду:
```
        "sudo docker run -it --rm -p 8000:8000 flox6375/lab_4:django"
```
+ Веб-сайт працює

+ Додав логування при помилці
+ Домашня робота:
  1. Cтворив Dockerfile для моніторингу
  2. Виконав команди:
```
    "sudo docker build -t flox6375/lab_4:monitoring --file Dockerfile.monitor ."
    "sudo docker images"
    "sudo docker push flox6375/lab_4:monitoring"
```
  3. Виконав команди:
```
    "sudo docker run -it --rm -p 8000:8000 flox6375/lab_4:django"
    "sudo docker run --net=host -v $(pwd)/server.log:/main/server.log --rm -it monitoring"
```
  4. Оримав файл server.log з контейнеру

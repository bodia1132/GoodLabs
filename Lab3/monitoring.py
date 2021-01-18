import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    while(True):
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
        time.sleep(60)
    return 0

if __name__ == '__main__':
    main("http://localhost:8000/health")

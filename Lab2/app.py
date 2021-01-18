import requests
import ntplib
from datetime import datetime


def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
    else:
        check_time(get_time_if_url_not_work())
    return True

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

if __name__ == "__main__":
    a = "=" * 40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
    home_work(get_current_time('http://date.jsontest.com/'))
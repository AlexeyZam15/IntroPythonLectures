from random import randint
from datetime import datetime as dt


def get_time():
    return dt.now().strftime('%H:%M')


def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)


def get_pressure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(751, 770)


def get_wind_speed(sensor):
    if sensor:
        return randint(0, 30)
    else:
        return randint(31, 50)


def data_collection(sensor=1):
    return get_time(), get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor)

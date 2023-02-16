def time_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('time;{}'
                   .format(data))


def temperature_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(';temperature;{}'
                   .format(data))


def pressure_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(';pressure;{}'
                   .format(data))


def wind_speed_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(';wind_speed;{}\n'
                   .format(data))

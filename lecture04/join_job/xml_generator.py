from user_interface import time_view
from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view


def create(device=1):
    xml = \
        f'''<xml>
                 <time units = "">{time_view()}</time>
                 <temperature units = "c">{temperature_view(device)}</temperature>
                 <pressure units = "mmHg">{pressure_view(device)}</pressure>
                 <wind_speed units = "m/s">{wind_speed_view(device)}</wind_speed>
</xml>'''

    with open('data.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return xml


def new_create(data, device=1):
    time, temperature, pressure, wind_speed = data
    temperature = temperature * 1.8 + 32
    xml = \
        f'''<xml>
                 <time units = "">{time}</time>
                 <temperature units = "f">{temperature}</temperature>
                 <pressure units = "mmHg">{pressure}</pressure>
                 <wind_speed units = "m/s">{wind_speed}</wind_speed>
</xml>'''

    with open('new_data.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return data

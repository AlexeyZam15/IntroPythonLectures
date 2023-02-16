from user_interface import time_view
from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view


def create(device=1):
    style = 'style="font-size:22px"'
    html = \
        f'''<html>
        <head> </head>
        <body>
        <p {style}>Time: {time_view()}</p>
        <p {style}>Temperature: {temperature_view(device)} c</p>
        <p {style}>Pressure: {pressure_view(device)} mmHg</p>
        <p {style}>Wind speed: {wind_speed_view(device)} m/s</p>
        </body>
</html>'''

    with open('index.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return html


def new_create(data, device=1):
    time, temperature, pressure, wind_speed = data
    style = 'style="font-size:22px"'
    html = \
        f'''<html>
        <head> </head>
        <body>
        <p {style}>Time: {time}</p>
        <p {style}>Temperature: {temperature} c</p>
        <p {style}>Pressure: {pressure} mmHg</p>
        <p {style}>Wind speed: {wind_speed} m/s</p>
        </body>
</html>'''

    with open('new_ index.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return data

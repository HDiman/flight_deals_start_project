class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

'''
Цены
Запрос

Метод: GET.

URL: http://map.aviasales.ru/prices.json?origin_iata=LED&period=2017-02-01:season&direct=true&one_way=false&no_visa=true&schengen=true&need_visa=true&locale=ru&min_trip_duration_in_days=13&max_trip_duration_in_days=15

Параметры запроса

origin_iata — IATA-код пункта отправления. IATA-код указывается буквами верхнего регистра, например, MOW.
period — период дат для поиска:
month — отображать только перелёты в указанном месяце (необходимо указывать дату начала месяца, например, 2017-01-01);
season — отображать перелёты, входящие в сезон, указанного месяца (зима, весна, лето, осень);
year — весь год (дату можно не указывать).
direct — указывает на наличие перелётов без пересадок.
one_way — «true» для перелетов в одну сторону, «false» для туда-обратно.
no_visa — виза для русских не нужна.
schengen — нужна виза в шенген.
need_visa — нужна виза для русских.
locale — язык поиска.
min_trip_duration_in_days — минимальная продолжительность поездки (дней).
max_trip_duration_in_days — максимальная продолжительность поездки (дней).
'''
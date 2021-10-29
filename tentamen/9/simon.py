#!/usr/bin/env python3

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

# My code
def get_country(city):
    try:
        return next(filter(lambda x: city in x[1], countries.items()))[0]
    except StopIteration:
        return

print('.: CITYFINDER :-')
print('----------------')
while True:
    city = input('city > ')
    country = get_country(city)
    if country:
        print('INFO:', city, 'is a city in', country)
    else:
        print('ERROR: Country for', city, 'not found')

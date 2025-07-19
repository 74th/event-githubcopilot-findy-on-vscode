data = {
    "001": {
        "name": "Tokyo",
        "population": 13929286,
        "area": 2194.07,
        "country": "Japan"
    },
    "002": {
        "name": "New York City",
        "population": 8419600,
        "area": 789.43,
        "country": "USA"
    },
    "003": {
        "name": "London",
        "population": 8982000,
        "area": 1572,
        "country": "UK"
    },
}

def main():
    for city_id, city_info in data:
        print(f"City ID: {city_id}")
        print(f"Name: {city_info['name']}")
        print(f"Population: {city_info['population']}")
        print(f"Area: {city_info['area']} km²")
        print(f"Country: {city_info['country']}")
        print()
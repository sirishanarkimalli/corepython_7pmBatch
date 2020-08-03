import requests

def get_area(a):
    return 0 if a is None else a


resp = requests.get(f"https://restcountries.eu/rest/v2/all")

if resp.status_code != 200:
    print("No information from the url")
    exit(1)

countries= resp.json()

for c in countries:
    print(f"{c['name']:50} {c['population']:13} {get_area(c['area']):10}")

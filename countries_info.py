import requests

code =input("Enter the country code: ")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")

if resp.status_code != 200:
    print("No information from the url")
    exit(1)

country= resp.json()

print("Name=       ", country["name"])
print("Capital=    ", country["capital"])
print("Population= ", country["population"])
print("Size=       ", country["area"])


cities = {
    "Paris": {
        "country": "France",
        "population": 2_100_000,
        "fact": "Paris is home to the Eiffel Tower."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14_000_000,
        "fact": "Tokyo is the world's most populous metropolitan area."
    },
    "Cairo": {
        "country": "Egypt",
        "population": 10_000_000,
        "fact": "Cairo is located on the Nile River."
    }
}

for city, information in cities.items():
    print(f"{city}: {information}")

# difficulty rating of 5/10
# only hard part was formatting the dictionary, but getting the information was easy
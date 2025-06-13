capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}

print(travel_log["France"][1])

travel_log2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 15,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}
print(travel_log2["Germany"]["cities_visited"][2])
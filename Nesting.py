# dictionary = {
#   "Key1": "Value1",
#   "Key2": "Value2",
#   "Key3":[list],
#   "Key4":{dictionary1},
# }


############### Nesting ###############

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

############### Nesting a list in a dictionary ###############

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# ["A", "B", ["C", "D"]]

############### Nesting a dictionary in a dictionary ###############

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 11},
# }
#
# print(travel_log)

############### Nesting a dictionary inside a list ###############

travel_log = [
  {
     "Country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
  },

  {
     "Country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 11
  },

]

# Accessing information from the first dictionary in travel_log
print("1. Country:", travel_log[0]["Country"])
print("2. Cities Visited:", travel_log[0]["cities_visited"])
print("3. Total Visits:", travel_log[0]["total_visits"])
# Replace 0 with 1 if you want to access information from the second dictionary in travel_log.


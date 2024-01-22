
# {"Key": "Value"}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# # Retrieve from a dictionary
# print(programming_dictionary["Bug"])

###########################################################################################
###########################################################################################

# # Add a piece of data to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

###########################################################################################
###########################################################################################

# # Create an empty dictionary
# empty_dictionary = {}

###########################################################################################
###########################################################################################

# # Wipe an existing dictionary
# # Used to clear a users progress or if a game restarts
# programming_dictionary = {}
# print(programming_dictionary)

###########################################################################################
###########################################################################################

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "I am editing this Key. If this Key is not found, it will create a new dictionary entry"
# print(programming_dictionary)

###########################################################################################
###########################################################################################

# Loop through a dictionary
for key in programming_dictionary:
    print(f"{key}: ")
    print(programming_dictionary[key])

###########################################################################################
###########################################################################################


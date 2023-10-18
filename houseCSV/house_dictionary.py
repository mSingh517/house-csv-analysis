"""This script returns the name and number of a member of the house of representatives

This script reads the header in the traditional way then uses list and dictionary
comprehensions to make dictionaries of each representative in the file, with a tuple
of the state name and district number as the key and a mini dictionary as the value.
then it closes the file, takes user input, converts that into a tuple then compares the
user tuple with all the keys in dictionary and reports accordingly.
"""


def capitalize(state_input):
    """This function takes a user input and capitalizes the first letter of each word
    of the input and makes the rest of the word lowercase by using string slicing
    to present the input back to the user with proper grammar.

    :param state_input: user inputted string
    :return: list of words with first letter of each word uppercase and the rest lowercase
    """
    capitalized = [word[0].upper() + word[1:].lower() for word in state_input.split(' ')]
    return capitalized


# House_of_representatives_117_F22.csv
filename = input('Which file contains the information about the representatives? ')
reps_file = open(filename, encoding='latin1')
header = reps_file.readline()
labels = header.strip().split(',')

# uses list comprehension to strip/split data in rows, and dictionary comprehension to zip labels and rowdata
# (inner dictionary) to be the value linked to the key: state name and district tuple (outer dictionary)
rep_data = [line.strip().split(',') for line in reps_file]
reps_dict = {(rep[0].lower(), rep[1].lower()): dict(zip(labels, rep)) for rep in rep_data}

reps_file.close()

while True:
    state_search = input("For which state would you like information? ")
    if not state_search:
        break

    state_string = capitalize(state_search)
    district_search = input(f"For which district in {' '.join(state_string)} would you like to obtain information? ")
    district_string = capitalize(district_search)

    # converts user input into a lowercase tuple to compare with keys in reps_dict
    search_query = (state_search.lower(), district_search.lower())

    if search_query in reps_dict:
        print(f"The representative for district {reps_dict[search_query]['District or Representation Type']}"
              f" in the state of {reps_dict[search_query]['State or Territory']} is"
              f" {reps_dict[search_query]['Given name']} {reps_dict[search_query]['Family name']}.\n"
              f"The phone number is {reps_dict[search_query]['Phone']}."
              f" The office number is {reps_dict[search_query]['Office Room '].strip()}.")
    else:
        print(f"No representative was found for district {' '.join(district_string)} in the state of"
              f" {' '.join(state_string)}. ")

    print()

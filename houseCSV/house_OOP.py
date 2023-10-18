"""Creates a directory of representatives using OOP

The same problem handled before but using object-oriented programming.
In particular, constructors, get-methods and set-methods are used.
Two classes are defined: Seat, which contains the information for the seat
and Person, which contains the information for the representative.
"""

import csv


def capitalize(state_input):
    """This function takes a user input and capitalizes the first letter of each word
    of the input and makes the rest of the word lowercase by using string slicing
    to present the input back to the user with proper grammar.

    :param state_input: user inputted string
    :return: list of words with first letter of each word uppercase and the rest lowercase
    """
    capitalized = [word[0].upper() + word[1:].lower() for word in state_input.split(' ')]
    return capitalized


class Seat:
    """Contains seat info (state, district, phone and room numbers)


    attributes: state, district, phone and room number of each seat in house
    methods: initializer for state and district, setter/getter for phone and office number,
    setter/getter for representative to be passed to class Seat, getter for representative full name,
    str method to display output of attributes to user
    """

    def __init__(self, state, district):
        # initializes state and district as attributes, other elements are empty strings for now
        self.state = state
        self.district = district
        self.rep = ''
        self.phone_number = ''
        self.office_number = ''

    def set_phone(self, phone_number):
        # sets phone number
        self.phone_number = phone_number

    def set_office(self, office_number):
        # sets office number
        self.office_number = office_number

    def get_phone(self):
        # gets phone number
        return self.phone_number

    def get_office(self):
        # gets office number
        return self.office_number

    def set_rep(self, rep):
        # sets representative to be passed to class Seat
        self.rep = rep

    def get_rep(self):
        # gets representative
        return self.rep

    def get_rep_full_name(self):
        # gets representative full name
        if self.rep:
            return self.rep.__str__()

    def __str__(self):
        # returns proper output for user
        if self.district == 'At Large':
            return f'At large seat for the state of {self.state}.\n' \
                   f'Phone number: {self.phone_number}\n' \
                   f'Office: {self.office_number}\n' \
                   f'{self.rep}'
        else:
            return f'Seat for district {self.district} in the state of {self.state}.\n' \
                   f'Phone number: {self.phone_number}\n' \
                   f'Office: {self.office_number}\n' \
                   f'{self.rep}'


class Person:
    """Contains person info (given and family name and party)


    attributes: given and family name of representative, political party of representative
    methods: getters for given, family, and full name, setter/getter for party, str method for
    output to user
    """

    def __init__(self, given_name, family_name):
        # initializes given and family name, full name is generated from them, party is empty for now
        self.given_name = given_name
        self.family_name = family_name
        self.party = ''
        self.full_name = f'{self.given_name} {self.family_name}'

    def get_given(self):
        # gets given name
        return self.given_name

    def get_family(self):
        # gets family name
        return self.family_name

    def get_full_name(self):
        # gets full name
        return self.full_name

    def set_party(self, party):
        # sets party
        self.party = party

    def get_party(self):
        # gets party
        return self.party

    def __str__(self):
        # returns proper output of representative name and party (if it exists)
        if self.party:
            return f'Representative: {self.full_name} ({self.party})'
        else:
            return f'Representative: {self.full_name}'


# Main script
while True:
    # House_of_representatives_117_F22.csv
    dir_filename = input("Which file contains the information about the "
                         "representatives? (Enter to exit.) ")
    if not dir_filename:
        quit()

    try:
        directory = open(dir_filename, "r", encoding="latin-1")
    except FileNotFoundError:
        print(f"The file {dir_filename} could not be opened.\n\n\n")
    else:
        break

house_seats = csv.DictReader(directory)

state_label = "State or Territory"
district_label = "District or Representation Type"
phone_label = "Phone "
office_label = "Office Room "
given_name_label = "Given name"
family_name_label = "Family name"
party_label = "Party "

house = {}
for row in house_seats:
    if row[district_label] == 'At Large' or row[district_label].isnumeric():
        # creates instance for each person
        person = Person(row[given_name_label].strip(), row[family_name_label].strip())
        if row[party_label]:  # in case party is empty
            person.set_party(row[party_label].strip())

        rep_seat = Seat(row[state_label].strip(), row[district_label].strip())  # creates instance for each seat

        # sets all other information for Seat object, including person passed to Seat object
        rep_seat.set_phone(row[phone_label].strip())
        rep_seat.set_office(row[office_label].strip())
        rep_seat.set_rep(person)
        # adds Seat object to dictionary, key tuple is lowercase for easy comparison
        house.update({(row[state_label].lower(), row[district_label].lower()): rep_seat})

while True:
    state_search = input("For which state would you like information? ")
    if not state_search:
        break

    state_string = capitalize(state_search)  # capitalized for grammatically correct output, same for district
    district_search = input(f"For which district in {' '.join(state_string)} would you like to obtain information? ")
    district_string = capitalize(district_search)
    search_query = (state_search.lower(), district_search.lower())  # lowercase for easy comparison
    print()

    if search_query in house:
        print(house[search_query])
    else:
        print(f"No representative was found for district {' '.join(district_string)} in the state of"
              f" {' '.join(state_string)}. ")
    print()

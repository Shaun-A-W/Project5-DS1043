"""

This module and library was created by Shaun W. as part of
a project assignment in DS-1043. The objective of the project
is to create a library of unique and useful functions.

Current function list:
- Prime factorization (p_factor)
- Flatten lists (no_nest)
- Wikipedia Citation Scraper (wiki_refs)
-
-

"""


### --------------- ###
### Functionality 1 ###
### --------------- ###

def is_prime(value: int) -> bool:
    """Determine if a number is prime.
    Returns false for values < 2."""

    # Edge cases
    if value < 2:
        return False
    if value == 2:
        return True

    # Runs through each necessary integer in
    # range to determine if value is divisible
    for k in range(2, value//2 + 1):
        if value % k == 0:
            return False
    else: return True

def p_factor(value: int) -> list[int]:
    """Finds the prime factorization of integer value.
    If value is already prime, returns a list [1, value].
    Otherwise, returns list of prime factorization."""

    # Handle incorrect inputs
    if value < 1:
        raise ValueError("Value must be greater than or equal to 1.")
    # Check if initial value is already prime
    if is_prime(value):
        return [1, value]
    factors = []
    pf = 2

    # Run while value is still divisible by primes
    while value > 1:

        # Check if current factor is prime
        if not is_prime(pf):
            pf += 1
            continue

        # While current factor is prime,
        # Divide the value and append the factor
        while is_prime(pf):
            if value % pf == 0:
                factors.append(pf)
                value = value / pf
            else:
                pf += 1
                break

    return factors



### --------------- ###
### Functionality 2 ###
### --------------- ###

def no_nest(nest: list) -> list:
    """Flattens nested lists of items into a single list.
    Does not accept dictionaries."""
    simple = [] # Establish new list
    for item in nest:
        if isinstance(item, dict): # Ensure item is not a dictionary
            raise TypeError("Dictionaries are not compatible with no_nest()")
        if isinstance(item, list): # Flatten nested list if it appears
            for element in item:
                simple.append(element)
        else:
            simple.append(item) # Other items may be appended normally
    return simple



### --------------- ###
### Functionality 3 ###
### --------------- ###

import os
import io
import string
import shutil

# str left bool middle num right

def create_table(header: list[str, ...], data: list):
    """Create a list of strings containing a formatted table
    for printing or writing to a file"""

    # initialize final list
    table_list = []
    columns = []

    # max_widths will find the longest data in characters
    # max_widths will also round all floats to 2 decimals along the way
    columns = max_widths(header, data)

    # goes through and ensure individual lists match header length
    for storage in data:

        if isinstance(storage, list):
            if len(storage) == len(header):
                continue
            elif len(storage) != len(header):
                raise ValueError('Length of lists must be equal to length of header')

    # create heading and bar format, add to table_list
    # since all str type, one space on left, rest at end per
    temp_header = []
    for i in range(len(header)):
        spacing = columns[i] - len(header[i])
        temp_header.append(f"| {header[i]} " + " " * spacing)
    table_list.append(temp_header)

    temp_header = []
    for i in range(len(header)):
        temp_header.append("|-" + "-" * columns[i] + "-")
    table_list.append(temp_header)

    # goes through lists/dicts and adds formatted lists into final result
    for storage in data:

        temp_list = []

        # checks if the set in data is a dict
        if isinstance(storage, dict):
            key_list = list(storage.keys())
            value_list = list(storage.values())

            for i in range(len(header)):

                # checks if dict key matches header
                if key_list[i] == header[i]:

                    # each if deals with corresponding value types and their formatting
                    if isinstance(value_list[i], bool):

                        if value_list[i] is False:
                            spacing = columns[i] - 5
                            temp_list.append(f"| {value_list[i]}" + " " * spacing + " ")
                            continue
                        if value_list[i] is True:
                            spacing = columns[i] - 4
                            temp_list.append(f"| {value_list[i]}" + " " * spacing + " ")
                            continue

                    if isinstance(value_list[i], int):
                        copy = str(value_list[i])
                        if len(copy) > 8:
                            spacing = columns[i] - 8
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        else:
                            spacing = columns[i] - len(copy)
                            temp_list.append("| " + " " * spacing + f"{value_list[i]} ")
                        continue

                    if isinstance(value_list[i], float):
                        copy = str(round(value_list[i], 2))
                        if len(copy) > 8:
                            spacing = columns[i] - 8
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        else:
                            spacing = columns[i] - len(copy)
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        continue

                    if isinstance(value_list[i], str):
                        spacing = columns[i] - len(value_list[i])
                        temp_list.append(f"| {value_list[i]} " + " " * spacing)
                        continue

                elif key_list[i] != header[i]:
                    temp_list.append("| " + " " * columns[i] + " ")

            table_list.append(temp_list)

        # checks if set in data is a list
        if isinstance(storage, list):

            # goes through range for num of columns
            for i in range(len(header)):

                # each if deals with corresponding value types and their formatting
                if isinstance(storage[i], bool):

                    if storage[i] is False:
                        spacing = columns[i] - 5
                        temp_list.append(f"| {storage[i]}" + " " * spacing + " ")
                        continue
                    if storage[i] is True:
                        spacing = columns[i] - 4
                        temp_list.append(f"| {storage[i]}" + " " * spacing + " ")
                        continue

                if isinstance(storage[i], int):
                    copy = str(storage[i])
                    if len(copy) > 8:
                        spacing = columns[i] - 8
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    else:
                        spacing = columns[i] - len(copy)
                        temp_list.append("| " + " " * spacing + f"{storage[i]} ")
                    continue

                if isinstance(storage[i], float):
                    copy = str(round(storage[i], 2))
                    if len(copy) > 8:
                        spacing = columns[i] - 8
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    else:
                        spacing = columns[i] - len(copy)
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    continue

                if isinstance(storage[i], str):
                    spacing = columns[i] - len(storage[i])
                    temp_list.append(f"| {storage[i]} " + " " * spacing)
                    continue

            # adds appropriately formatted data to final table
            table_list.append(temp_list)

    return table_list


def view_table(header: list[str, ...], data: list, max_width=(shutil.get_terminal_size()).columns, file=None):
    """Prints the table to the console.
    Header is expected to be a list of strings.
    Data is expected to be a list of any items.
    Note the following:
    - this function should call `create_table`
    - pass the file keyword parameter to the print function
    - this will allow writing to a stream for testing"""

    # grab formatted table from create_table() function
    viewing = create_table(header, data)
    # grab count of columns
    num_columns = len(header)
    # grab list of column widths
    data_widths = max_widths(header, data)
    table_width = 0
    for item in data_widths:
        # add three due to create_table() formatting
        # from "| " (2) and " " (1) characters per item
        table_width += (3 + item)

    # final table_width will be the character count width of the entire table
    if max_width >= table_width + 1: # "+ 1" to account for adding "|"
        for i in range(len(viewing)):
            viewing[i].append("|")

    else:
        while True:
            if max_width < table_width + 1: # "+ 1" to account for adding "…"
                # remove last item/column from table
                for i in range(len(viewing)):
                    viewing[i].pop(-1)
                # recheck/re-assign width values for next while iteration
                table_width = 0
                # simply check length of header for width
                for j in viewing[0]:
                    table_width += len(j)
            else:
                break
        for i in range(len(viewing)):
            viewing[i].append("…")

    for v in range(len(viewing)):
        line = ''
        for t in viewing[v]:
            line += t
        print(line, file=None)

def max_widths(header, data) -> list:
    """Utilized by view_table() and create_table().
    Finds the max width for each column required."""

    widths = []
    widest = None
    copy = ''

    # beginning column max widths grabbed from header lengths
    for word in header:
        widths.append(len(word))

    # goes through data lists/dicts in the range of num of header columns
    for i in range(len(header)):

        widest = None

        # checks each list/dict
        for item in data:

            # checking widths in lists
            if isinstance(item, list):

                # each if deals with finding widths of the data as appropriate
                if isinstance(item[i], bool):
                    if widest is None or widest < 5:
                        widest = 5

                if isinstance(item[i], int):
                    copy = str(item[i])
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(item[i], float):
                    item[i] = round(item[i], 2)
                    copy = str(round(item[i], 2))
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(item[i], str):
                    if widest is None or len(item[i]) > widest:
                        widest = len(item[i])

                if widest > widths[i]:
                    widths[i] = widest

            # checking widths in dicts
            if isinstance(item, dict):

                # each if deals with finding widths of the data as appropriate
                key_list = list(item.keys())
                value_list = list(item.values())
                if isinstance(value_list[i], bool):
                    if widest is None or widest < 5:
                        widest = 5

                if isinstance(value_list[i], int):
                    copy = str(value_list[i])
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(value_list[i], float):
                    value_list[i] = round(value_list[i], 2)
                    copy = str(round(value_list[i], 2))
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(value_list[i], str):
                    if widest is None or len(value_list[i]) > widest:
                        widest = len(value_list[i])

                if widest > widths[i]:
                    widths[i] = widest

    return widths



### --------------- ###
### Functionality 4 ###
### --------------- ###

def file_wordcount(filename: str) -> int:
    """Takes a file string name as an input. Most common text
    files should be expected to work (such as .md or .txt).
    Encoding is UTF-8.
    Returns an integer representing the word count."""
    with open(filename, mode='r', encoding='utf-8') as file:
        text = file.read()
        text = text.split()
        print(text)
        counter = -1
        for word in text:
            counter += 1
            for letter in word:
                if letter.isalnum():
                    continue
                else: text[counter] = word.replace(letter, '')
        while "" in text:
            text.remove('')
        print(text)
        return len(text)



### --------------- ###
### Functionality 5 ###
### --------------- ###

def file_search(filename: str, query: list[str], case_sensitive: bool) -> dict[str, int]:
    """Searches in a text file for the number of occurrences
    of each word contained in the query list of strings. Utilizes
    a case_sensitive boolean argument. Returns a dict with key, value
    pairs as words and integers."""

    # Goes through query if case_sensitive = False
    # Alters query to casefold
    if not case_sensitive:
        counter = -1
        for word in query:
            counter += 1
            query[counter] = word.casefold()

    counts = {} # Establish dictionary
    with open(filename, mode='r', encoding='utf-8') as file:
        # Read and split text for list comprehension
        text = file.read()
        text = text.split()

        # Cleans text from list for alphanumeric
        counter = -1
        for item in text:
            cleaned = "".join(char for char in item if char.isalnum())
            counter += 1
            text[counter] = cleaned
            while "" in text:
                text.remove('')

        # Loops through each entry in text and checks
        # if the entry appears in the query
        # If in query, add to dictionary or add 1 to count
        for item in text:
            if case_sensitive:
                if item in query:
                    if item not in counts:
                        counts[item] = 1
                    else: counts[item] += 1
            if not case_sensitive:
                if item.casefold() in query:
                    if item not in counts:
                        counts[item.casefold()] = 1
                    else: counts[item.casefold()] += 1
    return counts



# comments below for future library implementation ideas

###################
#
# from bs4 import BeautifulSoup as Soup
# import requests
#
# def wikipedia_refs(url: str) -> dict[int, dict]:
#     references = {}
#     count = 1
#
#     wiki = requests.get(url)
#     pedia = Soup(wiki.text, 'html.parser')
#     citations = pedia.find('ol', class_='references')
#
#     for li in citations.find_all('li'):
#         ref = li.find_all('a')
#         print(ref)
#         print('')
#         tags = []
#         for tag in ref:
#             tags.append(tag.text.strip())
#
#         # references[count] =
#         for link in ref:
#             print(link)
#         count += 1
#         print(len(tags))
#
#
#
#     return references
#
# print(wikipedia_refs('https://en.wikipedia.org/wiki/Python_(programming_language)'))
#
###########################
#
# _limit = 2**20 # Subject to change based on user need
#
#
# def gen_prime(_limit: int) -> int:
#     """Generate a random prime number.
#     Uses _limit variable to determine a ceiling.
#     _limit must be an integer >= 2 for function to run."""
#     if _limit < 2:
#         raise ValueError("Prime limit must be greater than or equal to 2")
#     while True:
#         if is_prime(p:=random.randint(2, _limit)):
#             return p
#
# def gen_generator(_limit: int) -> int:
#     pass
#
###########################
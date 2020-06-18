# -*- codign: utf-8 -*-
import random

# Binary Search
def run():
    random_list = [random.randint(0, 100) for i in range(10)]
    print(random_list)
    search_number = int(_get_client_field("number to search"))
    # Sorted the list
    sorted_list = sorted(random_list)
    # index
    index_init = 0
    index_last = len(sorted_list)
    # Complements
    steps = 0
    response = "The value {} is not found".format(search_number)
    for i in sorted_list:
        steps += 1
        # ecuaion
        index_new = (index_init + index_last) // 2
        value = sorted_list[index_new]
        if(search_number > value):
            index_init = index_new
        elif search_number < value:
            index_last = index_new
        else:
            response = "The index is {} and the value is {}".format(
                index_new, value)
            break
    print("{}\n{}\nTotal Steps: {}".format(sorted_list, response, steps))


# Complements
def _get_client_field(message, option=True):
    field = None
    while __empty(field):
        title = ''
        if option:
            title = "What is the {message}? ".format(message=message)
        else:
            title = message
        field = input(f'\n{title}')
    return field


# Complements
def __empty(value):
    response = True
    if value and value != None:
        if len(value) >= 0:
            response = False
    return response


if __name__ == "__main__":
    run()

# -*- codign: utf-8 -*-

import sys
import os
import csv

# Const
CLIENT_TABLE_FILE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']

# Variables & Const
global clients
global options


clients = []
options = [
    'List Client',
    'Create Client',
    'Update Client',
    'Delete Client',
    'Search Client',
    'Exit'
]


def run():
    """Start the software"""
    _init_clients_from_storage()
    show_title()
    read_element()


def show_title():
    """Show custom title of 'Platzi Seller'"""
    complement = title = (
        '██████╗ ██╗      █████╗ ████████╗███████╗██╗    ███████╗███████╗██╗     ██╗     ███████╗██████╗')
    title += ('\n██╔══██╗██║     ██╔══██╗╚══██╔══╝╚══███╔╝██║    ██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗')
    title += ('\n██████╔╝██║     ███████║   ██║     ███╔╝ ██║    ███████╗█████╗  ██║     ██║     █████╗  ██████╔╝')
    title += ('\n██╔═══╝ ██║     ██╔══██║   ██║    ███╔╝  ██║    ╚════██║██╔══╝  ██║     ██║     ██╔══╝  ██╔══██╗')
    title += ('\n██║     ███████╗██║  ██║   ██║   ███████╗██║    ███████║███████╗███████╗███████╗███████╗██║  ██║')
    title += ('\n╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝    ╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝')
    # Add Styles
    break_line = ('-' * len(complement) + "\n") * 2
    print("{}\n{}\n{}\n".format(break_line, title, break_line))
    show_menu()


def show_menu():
    """Show the menu of 'Platzi Seller'"""
    print("Write a number of the next options:")
    for key, value in enumerate(options):
        print("{}. {}".format(key, value))


def read_element():
    """Execute and make the process of the actions specifics"""
    response = 'No action allowed'
    option = 0
    while option != len(options) - 1:
        input_data = _get_client_field('Options: ', False)
        if not __empty(input_data) and (input_data.isdigit() == True):
            option = int(input_data)
            response = switch(option)
        print(response)


def switch(option):
    return {
        0: show_all_clients,
        1: create_client,
        2: update_client,
        3: delete_client,
        4: search_client,
        (len(options) - 1): exit_software
    }[option]()


def exit_software():
    sys.exit(0)
    return "Good Bye!"


def show_all_clients():
    """Print all Clients"""
    elements = 'This is your list:\n#'
    for element in CLIENT_SCHEMA:
        elements += " | {}".format(element)
    response = "{}\n".format(elements)
    for key, value in enumerate(clients):
        response += "{index} | {client}".format(
            index=key, client=print_client(value))
    return response


def print_client(client):
    if len(client) <= 0:
        return 'No exist data for this client'
    return "{name} | {company} | {email} | {position}\n".format(
        name=client['name'],
        company=client['company'],
        email=client['email'],
        position=client['position'],
    )


def create_client():
    """Create a Client"""
    name = _get_client_field('name')
    company = _get_client_field('company')
    email = _get_client_field('email')
    position = _get_client_field('position')
    if not __empty(name) and not __empty(company) and not __empty(email) and not __empty(position):
        clients.append({'name': name, 'company': company,
                        'email': email, 'position': position})
        _save_client_to_storage()
        return show_all_clients()
    else:
        return "The client have values empty"


def update_client():
    """Update a Client"""
    response = 'Any Change'
    show_all_clients()
    index = _get_client_field('index')
    if _search_client(index):
        index = int(index)
        name = _get_client_field('name')
        company = _get_client_field('company')
        email = _get_client_field('email')
        position = _get_client_field('position')
        if not __empty(name) and not __empty(company) and not __empty(email) and not __empty(position):
            client = {'name': name, 'company': company,
                      'email': email, 'position': position}
            clients[index] = client
            response = "Client #{} is updated\n\n{}".format(
                index, show_all_clients())
            _save_client_to_storage()
    return response


def delete_client():
    """Delete a Client"""
    response = 'Any Change'
    show_all_clients()
    index = _get_client_field('index')
    if _search_client(index):
        index = int(index)
        del clients[index]
        response = "Client #{} is deleted\n\n{}".format(
            index, show_all_clients())
        _save_client_to_storage()
    return response


def _search_client(index, get_object=False):
    response = False
    if get_object:
        response = "Client not found"
    if not __empty(index):
        index = int(index)
        if __checkRangeArray(index, clients):
            response = True
            if get_object:
                response = clients[index]
    return response


def search_client():
    show_all_clients()
    index = _get_client_field('index')
    return print_client(_search_client(index, True))


# Complements
def __empty(value):
    response = True
    if value and value != None:
        if len(value) >= 0:
            response = False
    return response


def __checkRangeArray(index, array):
    return index >= 0 and index <= len(array) - 1


def _get_client_field(message, option=True):
    field = None
    while __empty(field):
        title = ''
        if option:
            title = "What is the client {message}? ".format(message=message)
        else:
            title = message
        field = input(f'\n{title}')
    return field


# Files
def _init_clients_from_storage():
    if not os.path.isfile(CLIENT_TABLE_FILE) or not os.access(CLIENT_TABLE_FILE, os.R_OK):
        open(CLIENT_TABLE_FILE, 'a').close()
    with open(CLIENT_TABLE_FILE, mode="r") as file:
        reader = csv.DictReader(file, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_client_to_storage():
    tmp_table = '{}.tmp'.format(CLIENT_TABLE_FILE)
    with open(tmp_table, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        # Modify Files
        os.remove(CLIENT_TABLE_FILE)
        os.rename(tmp_table, CLIENT_TABLE_FILE)


if __name__ == '__main__':
    run()

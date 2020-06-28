# -*- codign: uft-8 -*-
import click

# modulo
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()  # Decorador
@click.pass_context  # Decorador
def cli(context):  # Function
    context.obj = {}  # Diccionarios
    context.obj['clients_table'] = CLIENTS_TABLE

# With the alias call all functions of this module
cli.add_command(clients_commands.all)

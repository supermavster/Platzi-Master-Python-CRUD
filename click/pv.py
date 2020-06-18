# -*- codign: uft-8 -*-
import click

# modulo
from clients import commands as clients_commands


@click.group()  # Decorador
@click.pass_context  # Decorador
def cli(context):  # Function
    context.obj = {}  # Diccionarios


# With the alias call all functions of this module
cli.add_command(clients_commands.all)

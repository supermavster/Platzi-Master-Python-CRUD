# -*- codign: uft-8 -*-
import click


@click.group()  # Decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(context, name, company, email, position):
    """Creates a new Client"""  # Show instruction in console
    pass


@clients.command()
@click.pass_context
def update(context, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(context, client_uid):
    """Deletes a client"""
    pass


@clients.command()
@click.pass_context
def list(context):
    """List all clients"""
    pass


all = clients

# -*- codign: uft-8 -*-
import click

# Add Libraries
from clients.services import ClientService
from clients.models import Client


@click.group()  # Decorador
def clients():
    """Manages the clients lifecycle"""
    # client_service = ClientService(context.obj['clients_table'])


@clients.command()
@click.option(
    '-n', '--name',
    type=str,
    prompt=True,
    help='The client name'
)
@click.option(
    '-c', '--company',
    type=str,
    prompt=True,
    help='The client company'
)
@click.option(
    '-e', '--email',
    type=str,
    prompt=True,
    help='The client email'
)
@click.option(
    '-p', '--position',
    type=str,
    prompt=True,
    help='The client position'
)
@click.pass_context
def create(context, name, company, email, position):
    """Creates a new Client"""  # Show instruction in console
    client = Client(name, company, email, position)
    client_service = ClientService(context.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.option(
    '-uid', '--client_uid',
    type=str,
    prompt=True,
    help='The client uid'
)
@click.option(
    '-n', '--name',
    type=str,
    prompt=True,
    help='The client name'
)
@click.option(
    '-c', '--company',
    type=str,
    prompt=True,
    help='The client company'
)
@click.option(
    '-e', '--email',
    type=str,
    prompt=True,
    help='The client email'
)
@click.option(
    '-p', '--position',
    type=str,
    prompt=True,
    help='The client position'
)
@click.pass_context
def update(context, client_uid, name, company, email, position):
    """Updates a client"""
    client_service = ClientService(context.obj['clients_table'])
    find_client = client_service.find_client(client_uid)
    if find_client:
        client = Client(name, company, email, position, client_uid)
        client_service.update_client(find_client, client)


@clients.command()
@click.option(
    '-uid', '--client_uid',
    type=str,
    prompt=True,
    help='The client uid'
)
@click.pass_context
def delete(context, client_uid):
    """Delete a client"""
    client_service = ClientService(context.obj['clients_table'])
    find_client = client_service.find_client(client_uid)
    if find_client:
        client_service.delete_client(find_client)


@clients.command()
@click.pass_context
def list(context):
    """List all clients"""
    client_service = ClientService(context.obj['clients_table'])
    print(client_service.list_clients())


all = clients

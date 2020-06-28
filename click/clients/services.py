import csv

# Modulo
from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())
            return list(reader)

    def find_client(self, uid):
        with open(self.table_name, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())
            for value in reader:
                if value['uid'] == uid:
                    return value
            return None

    def delete_client(self, client):
        clients = self.list_clients()
        with open(self.table_name, 'w'), open(self.table_name, mode='a') as file:
            for data in clients:
                if client != data:
                    writer = csv.DictWriter(file, fieldnames=Client.schema())
                    writer.writerow(data)

    def update_client(self, find_client, client):
        clients = self.list_clients()
        with open(self.table_name, 'w'), open(self.table_name, mode='a') as file:
            for data in clients:
                if find_client == data:
                    data = client.to_dict()
                writer = csv.DictWriter(file, fieldnames=Client.schema())
                writer.writerow(data)

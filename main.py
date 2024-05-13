from server.server import SocketServer
import click

@click.command()
@click.option('--server', help='start the server')
def server():
    server = SocketServer()
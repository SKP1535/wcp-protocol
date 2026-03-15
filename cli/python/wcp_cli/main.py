import click
from .commands import create_work, list_work, register_agent


@click.group()
def cli():
    """WCP Command Line Interface"""
    pass


cli.add_command(create_work)
cli.add_command(list_work)
cli.add_command(register_agent)


if __name__ == "__main__":
    cli()
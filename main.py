import click
from control import control

controller = control.PasswordManagerController("./db/database.db")


@click.command(name="new", help="Add new password")
def add():
    controller.add_password()


@click.command(name="get", help="Get password")
@click.argument("username", required=True)
@click.argument("source", required=True)
def get(username, source):
    controller.get_password(username, source)


# @click.command()
# @click.argument("username", required=True)
# @click.argument("source", required=True)
# def update(username, source):
#     controller.update_password(username=username, source=source)


@click.command(name="del", help="Delete exist password")
@click.argument("username", required=True)
@click.argument("source", required=True)
def delete(username, source):
    controller.delete_password(username=username, source=source)


@click.command(name="all", help="Get all password")
def get_all():
    controller.get_all_password()


@click.group
def cli():
    pass


def main():
    cli.add_command(get_all)
    cli.add_command(add)
    cli.add_command(get)
    # cli.add_command(update)
    cli.add_command(delete)

    cli()


if __name__ == "__main__":
    main()

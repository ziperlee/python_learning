"""
 Created by liwei on 2019/12/16.
"""

import click

# https://www.jianshu.com/p/488750ca69f0
# https://click.palletsprojects.com/en/7.x/options/#name-your-options


@click.group()
def cli():
    pass


@cli.command()
@click.option("--count", default=1, help="打印次数", type=int)
@click.option("--name", prompt="请输入名字", help="姓名")
def hello(count, name):
    for _ in range(count):
        click.echo(f"hello {name}")


@cli.command()
@click.option("--count", default=1, help="打印次数", type=int)
@click.option("--name", prompt="请输入名字", help="姓名")
@click.option("--test", "-t")
@click.option("--test2", "-t2", "tt")
def world(count, name, test, tt):
    for _ in range(count):
        click.echo(f"world {name} {test} {tt}")


# cli.add_command(hello)
# cli.add_command(world)

if __name__ == "__main__":
    cli()

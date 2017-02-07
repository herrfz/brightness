import click
import subprocess as sp


class Config:
    def __init__(self):
        self.device = None
        self.brightness = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@pass_config
def cli(config):
    config.device = sp.check_output("xrandr --verbose | grep -w connected | cut -d' ' -f1", shell=True).decode().strip().split('\n')
    config.brightness = float(sp.check_output("xrandr --verbose | awk '/Brightness/ { print $2; exit }'", shell=True))


@cli.command()
@pass_config
def inc(config):
    'Increment brightness by 10%'
    if config.brightness < 1:
        for dev in config.device:
            sp.check_call('xrandr --output {} --brightness {}'.format(dev, config.brightness + .1), shell=True)


@cli.command()
@pass_config
def dec(config):
    'Decrement brightness by 10%'
    if config.brightness > 0:
        for dev in config.device:
            sp.check_call('xrandr --output {} --brightness {}'.format(dev, config.brightness - .1), shell=True)

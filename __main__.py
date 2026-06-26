
import click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Linux Assistant CLI"""
    if ctx.invoked_subcommand is None:
        ctx.invoke(run)


@cli.command()
def run():
    from core.runtime.checks import require_llama
    require_llama()
    
    from core.app import run_app
    run_app()


@cli.command()
def setup():
    from core.setup import setup_cmd
    setup_cmd()


def main():
    cli()


if __name__ == "__main__":
    main()
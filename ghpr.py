import click

@click.command()
@click.option('-t','--token', type=str, help='Github access token')
@click.option('-l','--pr-link', type=str, help='Full pull request link')
@click.option('--copy/--no-copy', type=bool, default=True, help='Copy output as markdown')
@click.option('--copy-csv', type=bool, default=False, help='Copy output as CSV')
def cli(token, pr_link, copy, copy_csv):
    click.echo('Token2 = {}'.format(token))
    click.echo('PR Link = {}'.format(pr_link))
    click.echo('Copy = {}'.format(copy))
    click.echo('Copy-CSV = {}'.format(copy_csv))


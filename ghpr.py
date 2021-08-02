import click

from src.helpers.githubHelper import parseGithubUrl
from src.github.github import Github

@click.command()
@click.option('-t','--token', type=str, help='Github access token')
@click.option('-l','--pr-link', type=str, help='Full pull request link')
@click.option('--copy/--no-copy', type=bool, default=True, help='Copy output as markdown')
@click.option('--copy-csv', type=bool, default=False, help='Copy output as CSV')
def cli(token, pr_link, copy, copy_csv):
    hostname, org, repo, prOrIssueNumber = parseGithubUrl(pr_link)
    github = Github(hostname=hostname, token=token)
    paginatedList = github.get_comments(org, repo, int(prOrIssueNumber))

    for comment in paginatedList:
        click.echo(comment.body)
        click.echo(comment.in_reply_to_id)


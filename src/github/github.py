import click
from github import Github as GithubSdk
from tabulate import tabulate

class Github:
    def __init__(self, hostname, token):
        base_url = "https://{}/api/v3".format(hostname)
        self.gh = GithubSdk(base_url=base_url, login_or_token=token)

    def get_repo(self, org, repo):
        click.echo("loading repo")
        return self.gh.get_repo(org + "/" + repo)
    
    def get_pull_request(self, repo, pr_number):
        click.echo("loading pr")
        pr = repo.get_pull(pr_number)

        return pr

    def get_user(self, user_or_org_name):
        click.echo("loading user")
        user = self.gh.get_user(user_or_org_name)
        
        return user
        
    def get_comments(self, pr):
        click.echo("loading review comments")
        comments = pr.get_review_comments()
        
        return comments
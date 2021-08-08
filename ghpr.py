import click
from click.utils import echo
import pyperclip
from tabulate import tabulate


from src.helpers.githubHelper import parse_github_url, parse_github_user
from src.helpers.formatHelper import format_comment, format_list_to_csv
from src.github.github import Github

@click.command()
@click.option('-t','--token', type=str, help='Github access token')
@click.option('-l','--pr-link', type=str, help='Full pull request link')
@click.option('--copy/--no-copy', type=bool, default=True, help='Copy output as markdown')
@click.option('--copy-csv', type=bool, default=False, help='Copy output as CSV')
def cli(token, pr_link, copy, copy_csv):
    hostname, org, repo_name, pr_or_issue_number = parse_github_url(pr_link)
    
    github = Github(hostname=hostname, token=token)
    repo = github.get_repo(org,repo_name)
    pr = github.get_pull_request(repo, int(pr_or_issue_number))
    user_or_org_name = parse_github_user(pr.user.url)
    user = github.get_user(user_or_org_name)
    paginated_list = github.get_comments(pr)
    
    formatted_comment_list = [["Track", "Sprint", "US","Developer","Reviwed By","ReviewedDate","Category","PR Link", "Comment", "Severity","Remark","Mitigation Plan","Target Date"]]
    
    click.echo("Formatting comments")
    
    for comment in paginated_list:
        # Avoid reply comments
        if comment.in_reply_to_id is None:
            click.echo("Processing comment: {}".format(comment.id))
            formatted_comment_list.append(format_comment(user, pr, comment))
        
    # Print comments
    click.echo(tabulate(formatted_comment_list, headers="firstrow", tablefmt="github"))

    # Copy to CSV
    if copy_csv:
        pyperclip.copy(format_list_to_csv(formatted_comment_list))
        click.echo("#################################")
        click.echo("\nContent copied in CSV format\n")
        click.echo("#################################")
    # Copy to clipboard
    elif copy:
        pyperclip.copy(tabulate(formatted_comment_list, headers="firstrow", tablefmt="github"))
        click.echo("#################################")
        click.echo("\nContent copied in Markdown format\n")
        click.echo("#################################")
    
    

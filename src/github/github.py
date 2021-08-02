from github import Github as GithubSdk

class Github:
    def __init__(self, hostname, token):
        base_url = "https://{}/api/v3".format(hostname)
        self.gh = GithubSdk(base_url=base_url, login_or_token=token)

    def get_comments(self, org, repo, pr_number):
        repo = self.gh.get_repo(org + "/" + repo)        
        pr = repo.get_pull(pr_number)
        comments = pr.get_review_comments()
        
        return comments
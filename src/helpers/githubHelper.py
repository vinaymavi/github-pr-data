from urllib.parse import urlparse

def parse_github_url(url):
    """ Parse a github url and return hostname, Org, repo, PR or isue id"""
    
    if url is None or len(url.strip()) == 0:
        return None, None, None, None
    
    url = url.strip()
    parsed_url = urlparse(url)
    path_list = parsed_url.path.split('/')
    
    hostname = parsed_url.netloc
    org = path_list[1]
    repo = path_list[2]
    
    if len(path_list) == 5:
        pr_or_issue_number = path_list[4]

    return hostname, org, repo, pr_or_issue_number

def parse_ticket_id(pr_title):
    """ Parse JIRA, Rally and other platfroms ticket id """

    if pr_title is None or len(pr_title.strip()) == 0:
        return None

    pr_title = pr_title.strip()
    ticket_id = pr_title.split(':')[0]

    return ticket_id.strip()

def parse_github_user(user_or_org_url):
    """ Parse github user or orgnization for provided github url"""
    
    if user_or_org_url is None or len(user_or_org_url.strip()) == 0:
        return None
    
    user_or_org_url = user_or_org_url.strip()
    parsed_url = urlparse(user_or_org_url)
    path_list = parsed_url.path.split('/')
    
    user_or_org = path_list[len(path_list) - 1]
    
    return user_or_org

    
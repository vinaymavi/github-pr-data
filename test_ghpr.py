from src.helpers.githubHelper import  parse_github_url, parse_ticket_id, parse_github_user

def test_githubHelper():
    invalid_url = None
    valid_ernterprise_url = 'https://github.comcast.com/BSD-Digital/business-voice-ui-assets/pull/376'
    valid_github_url = 'https://github.com/PyGithub/PyGithub/pull/1890'
    
    hostname, org, repo, pr_or_issue_number = parse_github_url(invalid_url)
    
    assert hostname == None
    assert org == None
    assert repo == None
    assert pr_or_issue_number == None
    
    hostname, org, repo, pr_or_issue_number = parse_github_url(valid_ernterprise_url)
    
    assert hostname == 'github.comcast.com'
    assert org == 'BSD-Digital'
    assert repo == 'business-voice-ui-assets'
    assert pr_or_issue_number == '376'
    
    hostname, org, repo, pr_or_issue_number = parse_github_url(valid_github_url)
    
    assert hostname == 'github.com'
    assert org == 'PyGithub'
    assert repo == 'PyGithub'
    assert pr_or_issue_number == '1890'

def test_parseTicketId():
    valid_ticket_id = 'ABC123'
    assert parse_ticket_id('ABC123 : changes related to resend invite version2') == valid_ticket_id

def test_parseGithubUser():
    valid_user = 'octocat'
    assert parse_github_user('https://api.github.com/users/octocat') == valid_user

    
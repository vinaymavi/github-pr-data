from src.helpers.githubHelper import  parseGithubUrl

def test_githubHelper():
    invalieUrl = None
    validEnterpriseUrl = 'https://github.comcast.com/BSD-Digital/business-voice-ui-assets/pull/376'
    validGithubUrl = 'https://github.com/PyGithub/PyGithub/pull/1890'
    
    hostname, org, repo, prOrIssueNumber = parseGithubUrl(invalieUrl)
    
    assert hostname == None
    assert org == None
    assert repo == None
    assert prOrIssueNumber == None
    
    hostname, org, repo, prOrIssueNumber = parseGithubUrl(validEnterpriseUrl)
    
    assert hostname == 'github.comcast.com'
    assert org == 'BSD-Digital'
    assert repo == 'business-voice-ui-assets'
    assert prOrIssueNumber == '376'
    
    hostname, org, repo, prOrIssueNumber = parseGithubUrl(validGithubUrl)
    
    assert hostname == 'github.com'
    assert org == 'PyGithub'
    assert repo == 'PyGithub'
    assert prOrIssueNumber == '1890'

    
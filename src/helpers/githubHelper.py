from urllib.parse import urlparse

def parseGithubUrl(url):
    """ Parse a github url and return hostname, Org, repo, PR or isue id"""
    
    if url is None or len(url.strip()) == 0:
        return None, None, None, None
    
    url = url.strip()
    parsedUrl = urlparse(url)
    pathList = parsedUrl.path.split('/')
    
    hostname = parsedUrl.netloc
    org = pathList[1]
    repo = pathList[2]
    
    if len(pathList) == 5:
        prOrIssueNumber = pathList[4]

    return hostname, org, repo, prOrIssueNumber
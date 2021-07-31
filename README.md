# Github-pr-data
Project to get data from github pull requests and transfrom it to a format that can be used for 

* Bookeeping of the comments 
* Analysis of the comments
* AI analysis of the comments
* AI Categorization of the comments

### Development setup 

* Create a virtualenv with python3.6 (suggested location: `./virtualEnv`)
* Activate the virtualenv ```source ./virtualEnv/bin/activate```
* Install requirements ```pip install -r requirements.txt```

### Reference

* Github API - https://docs.github.com/en/rest

## CLI `ghpr`
`ghpr` is the command line interface for the project.
### set 
This command set multiple configurations.

**Supported parameters:**

| Parameter | Description | Default value |  Required |
| --- | --- | --- | --- |
| --token | The token to use for authentication. |  | Yes |
| --hostname  | Github enterpise account hostname | Github.com | No  |
| --org | This is the organization name. |  | No |
| --repo | This is the repository name. | | No |

Example: 

Set Github token ```ghprd set --token```
Set Enterprise hostname ```ghprd set --hostname```
Set Githut orgnization ```ghprd set --org```

### Supported parameters:

This CLI supports the following parameters:

| Parameter | Description | Default value | Supported Values |  Required |
| --- | --- | --- | --- | --- |
| --token | The token to use for authentication.  |  |  | Yes, Can be ignored if already set |
| --hostname  | Github enterpise account hostname | Github.com |  | No |
| --org | This is the organization name. |  |  | Yes, Can be ignored if already set |
| --repo | This is the repository name. | |  | Yes |
| --pr | This is the pull request number. | | * PR number, PR link, PR link with org/repo/pr, PR link with repo/pr  | yes |
| --copy | Copy output in markdown format | true | `true`/`false`  | No |
| --copy-csv | Copy output in csv format | false | `true`/`false`  | No |


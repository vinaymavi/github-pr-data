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
* Setup module in editable mode ``` pip install --editable .```. Meaning no need to install the module every time when you want to change the code.

### Reference

* Github API - https://docs.github.com/en/rest
* Github python SDK - https://pygithub.readthedocs.io/en/latest/
* Click command line interface - https://click.palletsprojects.com/en/8.0.x/documentation/
## CLI `ghpr`
`ghpr` is the command line interface for the project.

### Supported parameters:

This CLI supports the following parameters:

| Option | Description | Default value | Supported Values |  Required |
| --- | --- | --- | --- | --- |
| --token | The token to use for authentication.  |  |  | Yes|
| --pr-link | This is the pull request number. | | PR link  | yes |
| --copy | Copy output in markdown format | true | `true`/`false`  | No |
| --copy-csv | Copy output in csv format | false | `true`/`false`  | No |


# Create installer
To create a standalone installer of this package, we are using [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/). 

Steps to create installer 

- Install pyinstaller `pip install pyinstaller`
- Run command `pyinstaller ghpr.py --hidden-import=_cffi_backend`. This command will create a `dist/ghpr` folder that contains the installer/executable file. 
- Add `dist/ghpr` folder to PATH variable 
- Run `ghpr` command from terminal

## How to use installer

- [Create github personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Unzip `ghpr` folder at your prefered location
- [Add this unzip folder path to PATH variable](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)
- Run `ghpr -t <your github access token> -l <pull request link> --copy-csv True`

For more information please check this https://github.com/vinaymavi/github-pr-data Github project
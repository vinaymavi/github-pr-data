from setuptools import setup,find_packages
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='VinayMavi',
    author_email = 'vinaymavi@gmail.com',
    description="Project to get data from github pull requests",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license='MIT',
    name='ghpr',
    url="https://github.com/vinaymavi/github-pr-data",
    project_urls={
        "Bug Tracker": "https://github.com/vinaymavi/github-pr-data/issues",
    },
    version='1.0.0',
    py_modules=['ghpr','src'],
    packages = find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'click==8.0.1',        
        'PyGithub==1.55',
        'pyperclip==1.8.2',
        'tabulate==0.8.9'
    ],
    entry_points={
        'console_scripts': [
            'ghpr = ghpr:cli',
        ],
    },
)
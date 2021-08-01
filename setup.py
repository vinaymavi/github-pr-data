from setuptools import setup

setup(
    name='ghpr',
    version='0.1.0',
    py_modules=['ghpr'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ghpr = ghpr:cli',
        ],
    },
)
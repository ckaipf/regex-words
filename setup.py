from setuptools import setup, find_packages

setup(
    name                           = 'regex_words',
    packages                       = find_packages(),
    include_package_data           = True,
    entry_points={
        "console_scripts": [
            "regex-words=regex_words.__main__:app",
        ]
    },
    install_requires=[
        'typer',
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov'
        ],
    },
)